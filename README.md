\# 🚀 Serverless Event Processing System



A fully functional, production-ready serverless architecture built on AWS from scratch.

Designed to demonstrate real-world cloud engineering skills using event-driven design patterns.



!\[Architecture](./architecture/serverless-event-processing-api.png)



\---



\## 📌 Project Overview



This project implements a complete serverless pipeline that:

\- Accepts HTTP requests from any client (Postman, Web, Mobile)

\- Validates incoming data using AWS Step Functions

\- Stores valid data in DynamoDB with a unique ID

\- Handles errors gracefully with retry logic and catch states

\- Logs everything to CloudWatch for full observability



\---



\## 🏗️ Architecture

Client (Postman / Web / Mobile)

↓

Amazon API Gateway (POST /submit)

↓

AWS Lambda (event-entry-handler)

↓

AWS Step Functions (my-validator-workflow)

├── ✅ name exists → Lambda → DynamoDB → Success

└── ❌ name missing → Fail / Reject



\---



\## 🧩 Components



| Component | AWS Service | Description |

|---|---|---|

| API Layer | Amazon API Gateway | Exposes REST endpoint POST /submit |

| Processing | AWS Lambda (Python) | Parses and routes the request |

| Orchestration | AWS Step Functions | Manages workflow and validation logic |

| Database | Amazon DynamoDB | Stores validated events with unique ID |

| Monitoring | Amazon CloudWatch | Centralized logs and execution history |



\---



\## ⚙️ Workflow Logic



\### Valid Flow (name present)

API → Lambda → Step Functions → CheckName ✅ → SaveToDynamoDB → DynamoDB → Success



\### Invalid Flow (name missing)

API → Lambda → Step Functions → CheckName ❌ → RejectRequest → Fail



\### Failure Flow (Lambda error)

SaveToDynamoDB → Error → Retry (3x) → Catch → HandleError → End



\---



\## 🔁 Reliability Features



\### Retry Policy

\- Error: States.ALL

\- Interval: 2 seconds

\- Max Attempts: 3

\- Backoff Rate: 2.0 (Exponential Backoff)



\### Error Handling (Catch)

\- Catches all errors (States.ALL)

\- Redirects to HandleError state

\- Prevents full workflow failure



\---



\## 📊 Observability



\- ✅ Step Functions execution logs → CloudWatch

\- ✅ Lambda logs → CloudWatch

\- ✅ Log level: ALL

\- ✅ Execution input/output logged

\- ✅ Error tracing enabled



\---



\## 🧪 How to Test



\### 1. Valid Request

```json

POST /submit

{

&#x20; "name": "Khalid"

}

```

Expected: 200 OK — data saved to DynamoDB



\### 2. Invalid Request

```json

POST /submit

{

&#x20; "age": 25

}

```

Expected: Execution Failed — MissingName error



\---



\## 📁 Project Structure

serverless-event-processing/

├── architecture/

│   └── serverless-event-processing-api.png

├── lambdas/

│   └── lambda\_function.py

├── step-functions/

│   └── state-machine.json

├── screenshots/

│   └── step-functions-workflow-success.png

├── docs/

└── README.md



\---



\## 🛠️ Tech Stack



\- \*\*Runtime\*\*: Python 3.x

\- \*\*API\*\*: Amazon API Gateway (HTTP API)

\- \*\*Compute\*\*: AWS Lambda

\- \*\*Orchestration\*\*: AWS Step Functions (Standard Workflow)

\- \*\*Database\*\*: Amazon DynamoDB (On-demand)

\- \*\*Monitoring\*\*: Amazon CloudWatch Logs

\- \*\*IAM\*\*: Custom execution roles with least privilege



\---



\## 📸 Screenshots



All execution screenshots are available in the `/screenshots` folder showing:

\- Successful execution with name present

\- Failed execution with missing name

\- DynamoDB saved records

\- CloudWatch logs



\---



\## 👨‍💻 Author



\*\*Khalid Korena\*\*

Cloud \& Backend Engineer

Building real-world serverless systems on AWS



\---



\## 📄 License



MIT License — feel free to use and modify.

