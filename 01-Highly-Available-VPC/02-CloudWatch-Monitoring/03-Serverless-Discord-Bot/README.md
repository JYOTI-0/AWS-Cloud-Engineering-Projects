# 🤖 Event-Driven Serverless Notification Bot

Welcome to the **Serverless Automation** section of my Cloud Portfolio! ⚡

In modern cloud computing, managing servers for simple background tasks is inefficient. In this project, I built a completely serverless event-driven architecture that automatically triggers a Python script via an API endpoint to send real-time notifications to a third-party platform (Discord).

---

## 🏗️ Architecture Diagram

This sequence diagram outlines the entire flow of the HTTP request from the user's browser to the final Discord webhook delivery.

```mermaid
sequenceDiagram
    participant User as HTTP Client (Browser)
    participant API as Amazon API Gateway
    participant Lambda as AWS Lambda (Python)
    participant Discord as Discord Webhook
    
    User->>API: 1. Send HTTP Trigger Request
    API->>Lambda: 2. Invoke Serverless Function
    Note over Lambda: 3. Process Python Script &<br/>Create JSON Payload
    Lambda->>Discord: 4. POST Request with Payload
    Discord-->>Lambda: 5. 200 OK (Message Delivered)
    Lambda-->>API: 6. 200 OK (Success Status)
    API-->>User: 7. "Message sent to Discord!"
```
