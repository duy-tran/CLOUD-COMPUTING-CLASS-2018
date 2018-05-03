# Breaking down the **Internet of Things** infrastructure

### Universitat Politècnica de Catalunya

-   Quang Duy Tran - duy9968\@gmail.com

-   Marc Garnica Caparros - marcgarnicacaparros\@gmail.com

## Abstract

The most common concepts related to Internet of Things and IoT innovation projects are sensors, biometrics, connected assets or any other machine smartly connected to a network. The general idea uses to forget the network configurations and technologies, cloud databases and stream managing systems with a key role to make an IoT ecosystem work. This project tries to expalin in detail the needed backend behind any IoT deployment with the focus on the cloud infrastructure needed for such a system.

## Table of contents

* [1. Internet of Things: Overview](#Overview)
* [2. Architecture deployment](#Architecture)
  * [2.1. Device - Gateway - Cloud](#Architecture_triplet)
  * [2.2. Pipelining and Dataflow](#Architecture_pipelining)
* [3. Device](#Device)
  * [3.1. Type of information](#DeviceInformation)
  * [3.2. Metadata](#DeviceMetadata)
  * [3.3. Management](#DeviceManagement)
* [4. Gateway](#Gateway)
* [5. Cloud](#Content6)
  * [5.1. Architecture](#Cloud_architecture)
  * [5.2. Ingestion](#Cloud_ingestion)
  * [5.3. Data storage](#Cloud_storage)
  * [5.4. Rule processing and stream analytics](#Cloud_stream)
  * [5.5. Analytics](#Cloud_analytics)
  * [5.6. Archival Storage (A.P.I)](#Cloud_api)
* [6. Providers](#Providers)
* [7. Use cases](#UseCases)

<a name="Overview"/>

## 1. Internet of Things: Overview

Through the years there has not been any agreement on the IoT system definition. The term Internet of Things is usually referring to use cases and scenarios where network connectivity and computing capability extends to objects such as sensors or any other day to day item not normally considered computers. All this new devices are connected to the Internet which enables them generate, exchange and consume data with minimal human intervention.

[OASIS](https://www.oasis-open.org/) defined in 2014 the Internet of Things as a "System where the Internet is connected to the physical world via ubiquitous sensors".

**Which is the impact of Internet of Things?** Numerous companies and organizations are investing a lot of money on improving and facilitating IoT ecosystem, going from the smart connected devices to communication protocols or stream analysis systems. The impact of IoT in our processes and business has still not being able to be measure because as it is shown in the following image, it is potentially present in every sector of our life.

<p align="center"><img src="../img/iot_market.png "/></p>


Iot systems could be connected versions of common objects familiar in a daily word or also purpose-built devices for functions not yet realized. Including all the specific use cases and opportunities in the same standards and definitions is an impossible task, with the extra complexity of having to deal with *diverse hardware, diverse OS and softwares and different network requirements*.

All in all, building and end-to-end IoT solution is more than connecting devices through the network and requires a powerful and well designed infrastructure behind.

<a name="Architecture"/>

## 2. Architecture deployment

In order to build a strong and sustainable IoT system, the architecture design needs to be robust, integrated and strongly connected in order to carry the data from the devices to the very end where the insights and analytics will be the core of any data-driven decisions systems.

In a first abstract level, the system can be divided in three basic components or stages: Device - Gateway - Cloud.

<a name="Architecture_triplet"/>

### 2.1. Device - Gateway - Cloud
<table width="100%">
  <tr>
  <td width="33%">
    <strong>Device</strong>
  </td>
  <td width="33%">
    <strong>Gateway</strong>
  </td>
  <td width="33%">
    <strong>Cloud</strong>
  </td>  
  </tr>

  <tr>
  <td width="33%">
    <p align="center"><img src="../img/device.jpg "/></p>
  </td>
  <td width="33%">
   <p align="center"><img src="../img/gateway.jpg "/></p>
  </td>
  <td width="33%">
  <p align="center"><img src="../img/cloud_2.png "/></p>
  </td>  
  </tr>

  <tr>
  <td width="33%">
    First level of interaction with the real word by hardware and software tools. Devices might be directly or indirectly connected with each other through Internet. Devices includes anything from legacy industrial devices to robotic camera systems, water-level detectors, air quality sensors, accelerometers, and heart rate monitors. They can be dedicated machines or applications in computers or smart-phones.
  </td>
  <td width="33%">
    Gateways enables devices directly or indirectly connected to reach cloud services and storage. They can also add some functionalities and early processing of data.
  </td>
  <td width="33%">
    Cloud services is the most used and most efficient solution in order to consume the huge amount of data your IoT ecosystem will be producing. Without any limitation, IoT Cloud component includes any sort of Cloud system applications: Static content, autoscaling groups, Big Data Management Systems, SQL and NoSQL distributed databases and Streaming analytics and rule processing workflows.
  </td>  
  </tr>
</table>

<a name="Architecture_pipelining"/>

### 2.2. Pipelining and dataflow

The architecture of *Device-Gateway-Cloud* can also be analaysed from a very equivalent paradigm where the IoT systems are seen as a **Pipeline of Data and components** or usually called a **Dataflow**.

<p align="center"><img src="../img/dataflow.png "/></p>

On **stage 1** the system is basically collecting data form the environment or the object of measurement and transforming it into useful raw data. Some new technologies enable some initial data processing in stage 1. Systems always needs to balance between having all the possible data with a late processing or interact with the insights directly with early as possible processing of the data. This stage is completely done in the Device components.

**Stage 2** is in charge of gathering the data collected in stage 1. Gateway component is the main actor in this stage. The raw and analog data from the devices needs to be aggregated and converted into digital streams in order to be processed further in the analytics systems. This conversion and aggregation is usually performed in the Data Acquisitions Systems. The data is transferred by wire, WI-FI or the Internet. Intelligent gateways can also enrich the data received by means of malware protection, analytics and data management services.

After the two first stages and having the data digitalized and aggregated, it is time to cross the IT Edge and start performing analytics and building on top of the data. **Stage 3** and **Stage 4** are mainly located in the Cloud component.

As a first reasoning, one can fall into the error of directly pipe the data coming from stage 2 to the data center in stage 4. Having one large data pipe it requires an enormous capacity, in terms of storage and data processing. Stage 3 is focused on preprocessing and early managing the data, this is extremely useful to first, move on only on the meaningful data and second filter and divide the data for a better management later. Real time dashboards and emergency systems can also benefit of this intermediate stage 3.

The final stage of the data flow is where the powerful utilities of an IoT ecosystem can really be raised up. Data centers and data management services in this stage have three main objectives:

 - Data management purposes in order to store the data and the insights in the most efficient way.
 - In-depth processing and analytics on the data. Providing data visualizaiton, commanding and interpretation tools for the decision systems.
 - Managing a exhaustive archive of the system data and opening the data to the required stakeholders. It is as important as achieving results as having the ability to go back through the data to identify errors or further analysis. For example creating an API to consume the data filtered by date or type.

<a name="Device"/>

## 3. Device

As presented in the previous section of this document, device components involves any resource (hardware or software) able to capture data frames and measurements from the environment. It is a crucial component in any IoT ecosystem. Without really going into detail about the mechanisms and functionalities of the devices and machines, the main features to understand in order to design a robust ecosystem are **Type of Information**, **Device Metadata and Commands** and **Device management**.

<a name="DeviceInformation"/>

### 3. Type of information

Each resource has the capability to consume or produce various type of information. The system needs to be aware of these types and manage and process it accordingly. Along with the measurements and telemetry data recorded in the devices they also keep information about their state.

<a name="DeviceMetadata"/>

### 3.1. Metadata and Commands

The amount of metadata that a device can include highly depends on each device manufacturers. Some resources only include the minimum metadata which is the properties of the device and the telemetry definitions. Some other enriched devices can even keep further information about the device metadata and even emit tags related to their environment for further analysis or commands to interact with them. This is a very simple example of device metadata:

```json
{
  "DeviceProperties": {
    "DeviceID": "deviceid1",
    "HubEnabledState": null,
    "CreatedTime": "2016-04-25T23:54:01.313802Z",
    "DeviceState": "normal",
    "UpdatedTime": null
    },
  "SystemProperties": {
    "ICCID": null
  },
  "Commands": [],
  "CommandHistory": [],
  "IsSimulatedDevice": false,
  "id": "fe81a81c-bcbc-4970-81f4-7f12f2d8bda8"
}
```

Device commands are defined as actions that operate directly in the device. Depending on the type of device and infrastructure this can be very useful for the system to interact with the environment and the choices of implementation. Being able to operate on the devices it is a very powerful tool but it also implies some drawbacks such as ambiguity in the device state, semantics development for the commands and command expiration management (commands should not live forever).

<a name="DeviceManagement"/>

### 3.2. Management

As any other IT asset management, devices (and gateways) require a rigorous management involving provisioning, operating and updating the devices. The majority of the devices in the market offer fully integrated managing systems including registration, authentication and authorization of the resources. Moreover a Logging system sampling the events generated by the devices and their state it is also useful to track the system back for checkpoints.

In some deployments, updating the devices can be a very time-consuming task and not practical at all. A very intuitive solution is to use the already deployed connection between devices and the network to propagate the commands and updates. This is the idea of som over-the-air updates and IoT management technologies such as [Android Things](https://developer.android.com/things/) or Debian package repositories (APT) in Cloud Platforms or [Resin.io](https://resin.io/).

The following image shows an example of a IoT sensors management system implement by Ajuntament de Barcelona with mainly sound sensors in Barcelona

<p align="center"><img src="../img/device_management.png "/></p>


<a name="Gateway"/>

## 4. Gateway
The gateway component is sometimes underrated in how big is his impact in the ecosystem. When managing huge networks of devices it is important to deploy the correct and accurate gateway installation to transfer and propagate the operations in an efficient, controlled and fast manner.

Huge data networks are usually working with different data transfer protocols depending on the environment and the devices connected, gateways are in charge of translate and encapsulate the data transfer protocols and make all the nodes interconnected semantically. Usually it is correct to claim that a gateway works as proxy, receiving data and packaging if for transmission. Several levels of hierarchy in the gateway deployment are used to distribute the effort and organized the data transfer.
