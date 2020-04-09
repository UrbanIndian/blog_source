Title: Cloud Workload Placement Strategy
Author: Janit Vora
Date: 2020-04-07 11:29
Category: cloud
Tags: cloud, technology, strategy, enterprise architecture
Slug: cloud-workload-placement

Several factors go into determining the optimal workload placement strategy. Determining the best workload placement strategy is easy for greenfield projects or for start-ups. For mature enterprises who decide to move to the cloud, the workload placement strategy is based on the [cloud adoption strategy](https://www.janitvora.com/articles/2020/02/25/enterprise-cloud-adoption-strategy/ "cloud adoption strategy"). Based on the cloud adoption strategy, the enterprise architect needs to conduct application profiling for all applications and determine their cloud migration strategy based on the models like [Gartner's 5R model](https://www.computerweekly.com/tip/Cloud-applications-Five-migration-tips-from-Gartner "Gartner's 5R model") or [AWS' 6R model](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/ "AWS' 6R model").

## Attributes for Application Profiling:
------------
An enterprise architect should focus on their organization's current portfolio to understand its technical landscape, challenges, and dependencies in order to determine the workload placement strategy. Criteria can vary from one organization to another, but the criteria should cover the following attributes:
#### Architecture
Understand your application architecture in the context of its multiple components. This type of focus might result in you categorizing applications as monolithic with technical debt to be resolved. Levels of distribution and standardization might also drive the need to decompose and group workloads into manageable chunks of effort for cloud adoption.

Other important factors are stateful applications, applications that run on traditional systems, and determining the components to be replaced as applications are re-architected for cloud migration.

On the other hand, some workloads require less effort and can be moved as-is. Those workloads are usually stateless, standardized and have a microservices architecture.

While determining the final outcome the enterprise architect should consider the full lifecycle of applications: from development to production support. Understanding and assessing all the environments of a workload and support structures is essential before determining the migration path of a workload.

#### Security and compliance
The enterprise architect should be cognizant of all compliance requirements(PCI, GDPR etc.) related to the enterprise as they analyse the as-is landscape and prepare to vet cloud target options. It is important to establish plans which satisfy each compliance requirement associated with all workloads.

#### Data
Another important consideration is data. Based on the criticality of the application and its data, it needs to be determined if the data wil be hosted on-premise, inside the UK, inside EU or global, what will be the data access mechanism and at what speeds.

#### Technology
Technical factors also help prioritize workloads for applications. An application which uses web containers to encapsulate business logic will require less effort to transform into a cloud solution as compared to a monolithic COBOL software. Hence the effort required to migrate to the cloud vis-a-vis the benefits it might bring needs to be considered.

#### Dependencies
All enterprise workloads are tightly knit in to the application landscape. Hence upstream and downstream dependencies need to be considered for each workload. Very few stand-alone workloads exist in an enterprise. All workloads are tightly or loosely coupled with key business and technical functions in an enterprise. It is important to analyze the impact of replacing or changing each workload to avoid unsuccessful cloud adoption attempts.

#### Scalability
Cloud based applications should be inherently scalable. However, scalability requires a level of abstraction between application state, particular IP addresses, particular system calls and their underlying platforms. Some applications should be positioned to scale and take advantage of cloud capabilities like cloud bursting. To leverage the benefits of cloud computing, workloads which need scalability should be duly prioritized. 

## Output of Application Profiling
------------
Based on the attributes mentioned above, we can take a decision of what to do with a workload and do some Application Profiling for each workload. Workloads could be:

#### Repurchased: Drop and Shop
Effectively, this is just a licensing change. Drop the on-premise application and shop a SaaS application on the cloud. This strategy is useful for legacy applications which need upgrade (Eg. Hosted CRM)  or legacy applications which are incompatible to the cloud(Eg. Telco Billing Software).

#### Rehosted: Lift and Shift:
This involves moving applications from on-premise hosting to cloud hosting without any changes being made to the application. Eg: Moving a website from on-premise hosting to AWS. To leverage this strategy, it is important to identify the right applications that can benefit from the cloud in their current form. 

#### Replatformed: Lift, Tinker and Shift:
This strategy involves moving applications from on premise to the cloud by making some changes to these application to ensure cloud compatibility. The crucial factors while executing this strategy are to identify the right workloads for migration and extensive post migration testing and monitoring.

#### Re-factored/Re-Architected:
The decision to rearchitect an application is cost intensive and hence should be taken after proper cost benefit analysis. Critical applications which need to leverage cloud-native features such as development agility, scalability or performance are perfect candidates for rearchitecture usually to a microservices based architecture. 

#### Retired:
Applications which are identified as redundant or candidates for consolidation with other applications are retired. 

#### Retained: 
Applications which could not be easily migrated to the cloud, but are critical from a strategic perspective will be retained. 

https://cloud.netapp.com/blog/aws-migration-strategy-the-6-rs-in-depth

##Workload Placement Strategy
------------
Once enterprise architecture determines that a workload needs to be moved to the cloud, the next step is to:

- Determine the appropriate Cloud Service Model for that workload and 

- Determine the appropriate Cloud Deployment Model for that workload
<p align = "center">
![Cloud Workloads Model]({static}/img/CloudWorkloadModels.png)
</p>
#### How to determine Cloud Service Model?
<p align = "center">
![Cloud Service Model]({static}/img/CloudServiceModel.png)
</p>
#### How to determine Cloud Deployment Model?
Deployment model will also need to be assessed and determined for workloads. 
Deployment model assessment framework has the following attributes:

- Cloud Service Providers: There are three major cloud providers: AWS: Amazon Web Services, Microsoft Azure and Google Cloud Portal. As discussed above in the [enterprise cloud adoption strategy blog](https://www.janitvora.com/articles/2020/02/25/enterprise-cloud-adoption-strategy/ "enterprise cloud adoption strategy blog") these three are the frontrunners for cloud computing since they have the scale, resilience and maturity to be able to host large enterprise workloads.  

- Geography: There are three tiers within which all data stored for an enterprise across its cloud platforms should fit: Local (Within the UK), Across Europe and Global. This could be implemented across private, public or hybrid cloud as per the size and scale of an enterprise.

- Data Classification: Data is usually classified as 


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Secret: Available only to specific individuals,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Confidential: Available to selected groups,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Internal: Available to everyone within the organization and

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Public: Available to everyone including the general public
<p align = "center">
![Data Classification]({static}/img/DataClassification.jpg)
</p>
Irrespective of the classification and geography of where the data is stored, PCI and GDPR as well as any other applicable regulations should be strictly adhered to while designing the workload deployment architecture. 

- Service Tier:
<p align = "center">
![Service Tier]({static}/img/ServiceTier.jpg)
</p>
##Important Architectural Principles
------------
While deploying workloads on the cloud, some important architectural principles should be adhered to:

- Data Workload Availability: Authentication mechanisms, access channels and systems should help provide access in-line with data criticality.
	
- Data Workload Confidentiality: Should be implemented across the cloud workloads by ensuring that access is 'Least Privilege' so that right people have access to the data. Data should be encrypted at rest, in transit and in use. 
	
- Data Workload Integrity: Should be achieved by protecting data from deletion or modification and ensuring that important lost data could also be recovered. 
	
- The level of abstraction provided across multiple clouds will depend on the cloud portability strategy of the enterprise.
	
- Securing the network and minimizing attack surface
	
- Securing application workloads and workload integrations through appropriate authentication and authorization mechanisms

##Conclusion:
------------
The first step of workload placement is to conduct application profiling of existing applications in an enterprise and determine whether to repurchase, rehost, replatform, rearchitect, retain or retire existing applications. Based on the application profiling, an appropriate cloud service model and cloud deployment model is determined for each workload. The workload placement strategy of each workload is thus determined with due consideration to important architectural principles. 

##References:
------------
https://www.ibm.com/garage/method/practices/discover/cloud-workload-assessment

https://www.ibm.com/developerworks/library/mw-1609-fernandes-trs/index.html

https://cloud.netapp.com/blog/aws-migration-strategy-the-6-rs-in-depth

https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

https://www.computerweekly.com/tip/Cloud-applications-Five-migration-tips-from-Gartner
