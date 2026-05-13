\# Architecture Documentation



\## Overview



This document explains the technical decisions and architecture of the Serverless Event Processing System.



\---



\## Components In Detail



\### 1. Amazon API Gateway

\- Type: HTTP API

\- Endpoint: POST /submit

\- Accepts JSON body from any client

\- Passes request directly to Lambda



\---



\### 2. AWS Lambda (event-entry-handler)

\- Runtime: Python 3.x

\- Triggered by: API Gateway

\- Responsibilities:

&#x20; - Parse incoming request body

&#x20; - Pass data to Step Functions

&#x20; - Return response to client



\---



\### 3. AWS Step Functions (my-validator-workflow)

\- Type: Standard Workflow

\- States:

&#x20; - CheckName — validates if name field exists

&#x20; - SaveToDynamoDB — invokes Lambda to store data

&#x20; - HandleError — catches and logs any errors

&#x20; - RejectRequest — rejects invalid requests



\---



\### 4. Amazon DynamoDB (serverless-events)

\- Type: On-demand

\- Partition Key: id (String)

\- Stores:

&#x20; - id: unique UUID generated per request

&#x20; - data: the full request body



\---



\### 5. Amazon CloudWatch

\- Logs all Step Functions executions

\- Logs all Lambda invocations

\- Log level: ALL

\- Used for debugging and monitoring



\---



\## Data Flow

Client sends POST /submit with JSON body

API Gateway receives request

Lambda parses the body

Step Functions starts execution

CheckName validates the data

If valid → Lambda saves to DynamoDB

If invalid → Workflow fails with MissingName

All logs sent to CloudWatch





\---



\## Error Handling Strategy



| Scenario | Behavior |

|---|---|

| name missing | RejectRequest — Fail state |

| Lambda timeout | Retry 3 times with backoff |

| Unexpected error | Catch → HandleError state |



\---



\## Retry Policy



```json

{

&#x20; "ErrorEquals": \["Lambda.ServiceException"],

&#x20; "IntervalSeconds": 2,

&#x20; "MaxAttempts": 3,

&#x20; "BackoffRate": 2.0

}

```



\---



\## Security



\- IAM roles with least privilege

\- Lambda only invokable by Step Functions

\- API Gateway with HTTPS only

\- DynamoDB access limited to Lambda role

