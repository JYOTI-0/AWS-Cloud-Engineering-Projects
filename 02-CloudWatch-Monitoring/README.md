# 📈 Automated Server Monitoring & Alerting System

Welcome to the **Monitoring & Incident Response** section of my Cloud Portfolio! ☁️🔔

Building a server is only half the job; ensuring it stays healthy is where the real engineering happens. In this project, I implemented a proactive monitoring pipeline that automatically detects high resource usage and alerts the administrator before any system failure occurs.

---

## 🏗️ Architecture Diagram

This diagram illustrates the automated flow from resource consumption to real-time notification.

```mermaid
graph LR
    EC2[Ubuntu EC2 Instance] -- Sends Metrics<br>(Every 5 mins) --> CW[Amazon CloudWatch]
    subgraph "Proactive Monitoring"
        CW -- Evaluates --> Condition{"Is CPU >= 80%?"}
        Condition -- Yes --> Alarm((Trigger Alarm))
    end
    Alarm -- Triggers --> SNS[Amazon SNS Topic]
    SNS -- Publishes via Email --> Inbox([Admin Email Inbox])
    
    style Alarm fill:#ffcccc,stroke:#ff0000,stroke-width:2px
```


- *"Configured SNS to send email when EC2 CPU crosses 80%."*
