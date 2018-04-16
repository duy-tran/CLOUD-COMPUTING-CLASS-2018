# Lab session #4: Creating a web application using cloud PaaS

### Universitat Politècnica de Catalunya

Course link: [ccbda-upc.github.io](https://ccbda-upc.github.io/).

Group 1207

-   Quang Duy Tran - duy9968\@gmail.com

-   Marc Garnica Caparros - marcgarnicacaparros\@gmail.com

Assignment link: [Lab 6 Assignment](https://github.com/CCBDA-UPC/Assignments-2018/blob/master/Lab06.md)
Webapp repository: [Django express webapp](https://github.com/marcgarnica13/eb-django-express-singup-base)

## Objectives

The following README summarizes the tasks done during the sixth lab session of the Cloud Computing for Big Data Analytics course in Universitat Politècnica de Catalunya. For project delivery and recovery of information during the course evolution.

This session continues the deployment of a basic web app with Django framework accessible in this [repository](https://github.com/marcgarnica13/eb-django-express-singup-base). During the following sessions this repository will keep track of the modifications and updates of the webapp.

This session works on how to provide oour services with a REST API and use third party services to enrich our features. Finally it connects the app with Google Cloud Platform for advanced analytics.

## Pre-lab homeworks

No pre-lab tasks needed

## Lab tasks

### Task 6.1: How to provide your services through a REST API

On our product development is always wise to decouple as much as possible our architecture and one great strategy for achieving independence between our components is to separate the creation of results with the visualization of them.

In this section we want to provide a web-based API providing the needed results to the interface for plotting a chart. On top of gaining flexibility this also makes the results reusable for other purposes (p.e other pages of other web app where the data is needed as well)

- [x] We added a new mapped URL to our application */chart*.
- [x] For plotting the chart we used the Python library [Vincent](https://github.com/wrobstory/vincent) connecting with the front-end javascript library [D3.js](https://d3js.org/).
- [x] The initial code for plotting the chart was the following:

```python
import vincent
from django.conf import settings

BASE_DIR = getattr(settings, "BASE_DIR", None)


def chart(request):
    domain = request.GET.get('domain')
    preview = request.GET.get('preview')
    leads = Leads()
    items = leads.get_leads(domain, preview)
    domain_count = Counter()
    domain_count.update([item['email'].split('@')[1] for item in items])
    domain_freq = domain_count.most_common(15)
    if len(domain_freq) == 0:
        return HttpResponse('No items to show', status=200)
    labels, freq = zip(*domain_freq)
    data = {'data': freq, 'x': labels}
    bar = vincent.Bar(data, iter_idx='x')
    bar.to_json(os.path.join(BASE_DIR, 'static', 'domain_freq.json'))
    return render(request, 'chart.html', {'items': items})
```

And consequently our interface *chart.html* was as follows:

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Vega Scaffold</title>
    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <script src="http://d3js.org/topojson.v1.min.js"></script>
    <script src="http://d3js.org/d3.geo.projection.v0.min.js" charset="utf-8"></script>
    <script src="http://trifacta.github.com/vega/vega.js"></script>
</head>
<body>
<div id="vis"></div>
</body>
<script type="text/javascript">
    // parse a spec and create a visualization view
    function parse(spec) {
        vg.parse.spec(spec, function (chart) {
            chart({el: "#vis"}).update();
        });
    }
    parse('{% static 'domain_freq.json' %}');
</script>
</html>
```
- [x] Following the setup configuration the data gathered was dumped to a the *domain_freq.json* inside the *static* folder. As seen in previous sessions, this static folder is linked to an AWS S3 bucket and served as static content by AWS CloudFront. In other words, the data of this file it is not updated eventhough changing the query which causes errors in the content of the chart.

  This is our solution on how to solve this problem:

   - We created a new S3 bucket responsible of serving to the web app the dynamic content. Called eb-dynamic.

   ![New s3](img/creating_new_s3.png)

   - On each request served by the application, the data is stored in a file and updated in the eb-dynamic s3 bucket. The following code was modified.

   On *views.py*

   ```python
   def chart(request):
    domain = request.GET.get('domain')
    preview = request.GET.get('preview')
    # if both domain and preview are provided the file name is the concatenation of both
    if domain and preview:
        requestFileName = str(domain) + str(preview) + '.json'
    # if only the domain is provided the file name is the domain
    elif domain:
        requestFileName = str(domain) + '.json'
    # if only the preview is provided the file name is the preview
    elif preview:
            requestFileName = str(preview) + '.json'
    # finally if nothing is provided the file name is all.json
    else:
        requestFileName = 'all.json'

    leads = Leads()
    items = leads.get_leads(domain, preview)
    domain_count = Counter()
    domain_count.update([item['email'].split('@')[1] for item in items])
    domain_freq = domain_count.most_common(15)

    if len(domain_freq) == 0:
        return HttpResponse('No items to show', status=200)

    labels, freq = zip(*domain_freq)
    # data for the chart
    data = {'data': freq, 'x': labels}
    bar = vincent.Bar(data, iter_idx='x')

    # updating/creating the file in the S3 dynamic bucket
    leads.push_chart_definition(bar.to_json(), requestFileName)

    # building the URL for accessing the file
    requestFileName = 'https://s3-eu-west-1.amazonaws.com/eb-dynamic/' + str(requestFileName)
    return render(request, 'chart.html', {'requestFileName': requestFileName})
   ```

   And on the file *models.py*

    ```python
    def push_chart_definition(self, chart, name):
        try:
            s3 = boto3.resource('s3', region_name=AWS_REGION)
            obj = s3.Object('eb-dynamic', name)
            obj.put(Body=chart)
        except Exception as e:
            logger.error(
                'Error connecting to the s3 bucket: ' + (e.fmt if hasattr(e, 'fmt') else '') + ','.join(e.args)
            )
            return None

    ```

    Notice that in order to provide a correct answer in any request we are not just using one file in the S3 bucket. This are the possible combinations for creating a file depending on the query:

    | Domain | Preview | Filename |
    | :---: | :---: | :---: |
    | catalunya.cat | Yes  | catalunya.cat.Yes.json |
    | -  | No  | No.json |
    | gmail.com | - | gmail.com.json |
    | - | - | all.json |

    Aligned with that the *chart.html* file is now using the sent variable requestFileName to GET the file to parse for the chart plot:

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vega Scaffold</title>
        <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
        <script src="http://d3js.org/topojson.v1.min.js"></script>
        <script src="http://d3js.org/d3.geo.projection.v0.min.js" charset="utf-8"></script>
        <script src="http://trifacta.github.com/vega/vega.js"></script>
    </head>
    <body>
    <div id="vis"></div>
    </body>
    <script type="text/javascript">
        // parse a spec and create a visualization view
        function parse(spec) {
            vg.parse.spec(spec, function (chart) {
                chart({el: "#vis"}).update();
            });
        }
        parse('{{ requestFileName }}')
    </script>
    </html>
    ```

    When running in localhost, we experienced some problems receivng a *403 Forbidden* code when GETTING the desired file from our S3 bucket. At first, we tried to solve to the CORS configurations but what really solved the problem was adding a policy to the bucket. Both policy and CORS can be seen in the following images.

    ![CORS configuration](img/CORS.png)

    ![Bucket policy](img/policy_s3.png)

    After this the application was running correctly in local.

 - [x] When deploying we needed to run again the ```pip freeze > requirements.txt``` in order to ensure the Elasticbeanstalk environment install all the packaged needed for the app. Finally the chart feature was working well in the EB. The application can be accessed through this [link](http://gsgsignup-j4mtn-env.eu-west-1.elasticbeanstalk.com)

  ![Eb query all](img/eb_chart_all.png)

  ![Eb query domain and preview](img/eb_chart_domainPreview.png)


### Task 6.2: How to provide our service combined with third-party services
