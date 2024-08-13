## Cloud Resume API with Azure

This project demonstrates a serverless Cloud Resume API built using Azure Functions and Azure Cosmos DB for NoSQL storage.

## Detailed Blog

My first blog on hashnode: [Cloud Resume API with Azure](https://sushantbagul.hashnode.dev/cloud-resume-api-with-azure)

## Project Overview

**My Resume API**

Access my resume data in JSON format by making a GET request to the following endpoint:

```
https://sushantresumeapi.azurewebsites.net/resumeapi?id=1
```


**Video Demonstration**
<p align="center">
  <a href="https://youtu.be/C7DFHk4nvXI">
    <img src="https://img.youtube.com/vi/C7DFHk4nvXI/0.jpg" alt="Video Demo">
  </a>
</p>

**Tech Stack**

- **Azure Functions:** Serverless compute platform for building and running code without managing servers.
- **Azure Cosmos DB for NoSQL:** Highly scalable NoSQL database service for storing your resume data.

**Feature Added**

- Whenever someone visits my API, the view count increases. This allows us to track the reach of our Resume API.

## Project Details

**Description:**
Developed and deployed a serverless API using Azure Functions and CosmosDB, integrated with GitHub Actions for automated CI/CD. The API serves resume data in JSON format and ensures seamless updates with every code push.

**Key Achievements:**

- **Cloud Infrastructure:**
  - Set up Azure resources, including Resource Groups and Azure CosmosDB.
  - Designed and implemented a CosmosDB database and container to store structured JSON resume data.

- **Serverless API Development:**
  - Created a Python-based Azure Function to fetch and return resume data from CosmosDB.
  - Configured local settings and environment variables to securely manage API keys and connection strings.

- **Automation and Deployment:**
  - Integrated GitHub Actions for continuous integration and deployment.
  - Automated deployment process, ensuring each code change triggers a build and deploy pipeline to Azure Functions.
  - Implemented a CI/CD pipeline using GitHub Actions to streamline the deployment process.

- **Technologies Used:**
  - **Languages:** Python
  - **Cloud Services:** Azure Functions, Azure CosmosDB
  - **Automation Tools:** GitHub Actions
  - **Development Tools:** Visual Studio Code, Azure Functions Core Tools

**Impact:**
- Enabled real-time updates to the resume API with minimal manual intervention.
- Leveraged serverless architecture to reduce infrastructure management overhead.
- Improved reliability and scalability of the API by using cloud-native services.

**Project URL:**
[GitHub Repository](https://github.com/Sushant1209/Azure-Resume-API-Challenge)

## Author

- Twitter: [@tw_sushant18](https://x.com/tw_sushant18)
- LinkedIn: [@sushant-bagul](https://www.linkedin.com/in/sushant-bagul/)

