Title: Enterprise Cloud Adoption Strategy
Author: Janit Vora
Date: 2020-02-25 9:00
Category: cloud
Tags: cloud, technology, strategy, enterprise architecture
Slug: enterprise-cloud-adoption-strategy

The objective of this post is to suggest activities required to be completed for Enterprise Architecture to help an organization embark on its cloud adoption journey.

I have used the long-form format since the intention is to inform and hence enable Enterprise Architecture. This encompasses the journey from determining the cloud strategy to creating a BAU cloud function within the enterprise.

The scope of this guide is to help an organization’s enterprise architecture function make decisions on how to move its technology estate to the cloud. This guide describes the activities required, related decisions, challenges, risks and success factors for a successful journey to cloud computing.

## How to define Enterprise Cloud Strategy?
<p align = "center">
![How to define an Enterprise Cloud Strategy?]({static}/img/HowToDefineEnterpriseCloudStrategy.jpg)
</p>
------------

### Inputs to Cloud Strategy
There are different factors which influence Enterprise Cloud Strategy. These factors serve as inputs to the process of defining the cloud strategy:

- Business Strategy, Vision and Mission: IT strategy is informed by business strategy and hence vision and mission related to cloud adoption strategy should also be derived from the same.
- Inputs from ‘Application Portfolio Rationalization: ’Vision, mission, approach should also dovetail with any application portfolio rationalization programmes undertaken and
- Inputs from ‘IT Strategy and Technology Roadmap’: The overall IT strategy and technology roadmap of the enterprise will also inform the cloud strategy
- Inputs from ‘Cloud Maturity assessment’ might help determine the cloud maturity of an enterprise and could be another input to determining cloud strategy
- Enlisting the major reasons for cloud adoption - reasons which help answer 'Why Cloud?' will help determine the approach to cloud adoption. Some of the usual reasons for cloud adoption could be:
<p align = "center">
![Reasons for using Cloud Strategy]({static}/img/cloud-adoption-reasons.png)
</p>
------------

### Defining the Enterprise Cloud Strategy
Based on the inputs, understanding of the technology stack and organizational priorities, decisions need to be made regarding various dimensions of the cloud strategy. There are multiple dimensions that need to be considered. I will try and discuss through an indicative list of all aspects which need to be considered to determine an enterprise cloud strategy.

#### 1. Cloud Migration Strategy
Based on organizational priorities, technology roadmap and portfolio rationalization recommendations, it needs to be determined as to what cloud strategy the organization should follow:

| Aggressive Cloud Strategy |Planned Cloud Strategy|Reactive Cloud Strategy|
| ------------ | ------------ | ------------ |
|Try to position all applications to cloud first|Conduct Cloud Suitability Assessment for the full application portfolio|Based on APR assessment and technology strategy, initiate cloud migration for select existing and new applications|

#### 2. Hosting Approach
The hosting strategy for cloud adoption depends on an organization’s priorities. The most common approaches to hosting with their characteristics are described below:
<p align = "center">
![Cloud Hosting Approach]({static}/img/Hybrid_cloud_hosting.png)
</p>
#### 3. Cloud Tiers: How to choose between IaaS, PaaS and SaaS

<p align = "center">
![Choosing between IaaS, PaaS and SaaS, Source: Microsoft]({static}/img/HowToChooseIaaSPaaSSaaS.png)
</p>
An IaaS model provides maximum control as the figure above illustrates. It allows you full control over the operating system, and allows you to introduce secure concepts such as isolated VMs, secure boot, just-in-time access, etc. 

PaaS increases this abstraction OS, middleware and runtime are also provided by the cloud vendor. PaaS components are architected to provide scalability and agility to support cloud applications. This is an evolution from IaaS which requires the architect or engineer to build the scalability and agility using traditional techniques at the infrastructure level, i.e. load balancers, traffic management, scale-sets, etc. 

SaaS completes the models, whereby the platform provider (i.e. Microsoft) manages the entire stack and provisions access to the "software" as required by the users of the organisation. In this model, the organisation has a lot less control within the infrastructure and the application tier and instead places more trust in the vendor. Ultimately this is the cloud nirvana, as typically SaaS products are 'born in the cloud' and can usually be considered truly 'cloud native'.

####4. How to choose the correct cloud implementation: Multi cloud, Hybrid Cloud or Private Cloud?

Multi cloud wins this hands down thanks to reasons ranging from vendor lock in, performance and latency, compliance across geographies and resilience. As seen below, multi cloud is the most popular approach to cloud globally. 
<p align = "center">
![Enterprise Cloud Strategy]({static}/img/MultiCloudAdoptionStats1.png)
</p>
There are different reasons and different ways to use multi cloud as described below:
<p align = "center">
![Multi cloud approach]({static}/img/MulticloudStrategyStats2.png)
</p>
Multi cloud is the dominant approach suggested for cloud services – especially for large enterprises which need to ensure compliance to various regulations. Single public cloud is useful for those looking to optimize costs whereas private cloud is a great option for those with especially stringent data security requirements.

Cloud management platforms such as Flexera (Rightscale), Scalr, Embotics, Morpheus Data etc. help manage multi cloud environments with ease. Here is [Gartner’s magic quadrant report for Cloud Management Platforms](https://www.gartner.com/en/documents/3897466/magic-quadrant-for-cloud-management-platforms "Gartner’s magic quadrant report for Cloud Management Platforms").

Another recent, noteworthy development is [Google’s Anthos](https://cloud.google.com/anthos "Google’s Anthos") – a Kubernetes based suite of GCP components that helps organisations to run applications on premises, on Google cloud and also to manage workloads on third-party clouds like AWS and Azure. This gives you ‘the freedom to deploy, run and manage your applications on the cloud of your choice, without requiring administrators and developers to learn different environments and APIs.’

#### 5. Which Public Cloud Provider?

After zeroing in on the multi-cloud approach, we need to decide which cloud providers should we choose to go with. While workload placement strategy might help determine the best fit cloud for each individual workload, AWS, Ms Azure and GCP are the usual suspects for most cloud implementations.

AWS had stolen a march over the competition, but Azure is catching up fast as the data from Rightscale's reports show below:
<p align = "center">
![Public Cloud Adoption]({static}/img/publiccloudadoption.png)
</p>
Here is another comparison chart from Spiceworks’[Public Cloud Trends in 2019 and Beyond](https://community.spiceworks.com/blog/3208-public-cloud-trends-in-2019-and-beyond "Public Cloud Trends in 2019 and Beyond") survey with responses from the users of AWS, Ms Azure and GCP.

<p align = "center">
![AWS vs Ms Azure vs Google Cloud]({static}/img/AWSvsAzurevsGCP.png)
</p>
AWS is the oldest, most well-known and feature rich of all public cloud providers. It also has the largest community of users. This usually makes it the first choice for most cloud adoption programmes. 

#### 6. Challenges, Risks, Controls implemented
The Cloud Controls Matrix created by the Cloud Security Alliance is the best and only meta-framework of cloud-specific security controls. These controls which span across the enterprise are mapped to leading standards, best practices and regulations. CCM provides organizations with the needed structure, detail and clarity relating to information security tailored to cloud computing. CCM is currently considered a de-facto standard for cloud security assurance and compliance. The current version of the CCM is v3.0.1.
<p align = "center">
![CCM V3.0.1 Domains]({static}/img/CCMv3.0.1Domains.png)
</p>
An architect can leverage the [CCM v3.0.1](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v3-0-1/ "CCM v3.0.1") and tailor it to their organization.

#### 7. Critical Enablers to define Enterprise Cloud Strategy
An Enterprise Cloud Strategy will need enablers listed below to be implemented successfully:

- Workload Placement Strategy: Define a framework using which the organization can place workloads quickly, securely and in line with relevant regulations. 
- Portability Strategy: Define guidelines to ensure that an application is portable between cloud providers. This is essential to ensure success of the multi-cloud strategy.
- Exit Strategy: Create a document which provides guidance and direction to the organization to identify contingencies and create an exit plan for every application placed on the cloud.
- Cloud Service Deployment Standards: Ensure that every application hosted on cloud infrastructure are evaluated for and adhere to service deployment standards.

#### 8. Target State
Determining the Target State for an organization's technology estate will help drive the cloud adoption strategy. Here is a sample target state. The target state will help manage lots of complex apps in a flexible manner at a low cost.
<p align = "center">
![Target State]({static}/img/TargetState_New.jpg)
</p>
#### 9. Goals, Benefits and Measuring Success
A good Enterprise Cloud Strategy should define the goals that it needs to achieve, the benefits it should accrue to the organization and the method to measure these benefits. The goals should be well defined, clearly articulated and time bound. Goals could be across different areas and should differ as cloud maturity increases in the organization. A few sample goals for the beginning of an Enterprise's cloud journey are:
<p align = "center">
![Goals]({static}/img/Goals.jpg)
</p>
#### 10. Cloud Governance Strategy
A cloud governance board should be established on the lines of EA governance boards. The cloud governance board should have representatives from all areas of the enterprise. 

The cloud governance board, as its name suggests will be responsible for governing cloud adoption in the enterprise. The board will have to convene regularly in the initial days of cloud adoption with their focus on functions such as:

- Cloud Advisory: Advising any business area(s) on cloud adoption
- Cloud Feasibility: Reviewing the feasibility and risks related to cloud migration proposals from each business area
- Cloud Approval: Approving the cloud adoption proposal(s)

The cloud governance board should be supported by the technical cloud advisory. The technical cloud advisory should be a sub-group of the cloud governance board with members who understand cloud technology and can advise the cloud governance board on complicated issues related to the cloud. 

------------
### A well defined Enterprise Cloud Strategy
As an end product of the exercise, the cloud strategy should communicate the following:

- Define an approach to cloud adoption and key decisions made regarding the same
- Define a Target State for Cloud Adoption
- List the Goals and related Key Success Factors for cloud adoption
- List activities, foreseeable risks, challenges and controls adopted for the cloud
- Define a Target Operating Model for the BAU cloud function