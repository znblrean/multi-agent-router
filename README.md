<<<<<<< HEAD
=======
# Multi-Agent Routing System

![System Architecture Banner](https://via.placeholder.com/1200x400?text=Multi-Agent+System+Architecture)

## System Overview

این سیستم یک پلتفرم مسیریابی هوشمند برای توزیع درخواست‌ها بین عامل‌های تخصصی است.

## Architecture

```mermaid
flowchart TB
    subgraph LangGraph Workflow
        A[User Question] --> B(Classifier Node)
        B -->|Math| C[MathBot]
        B -->|Code| D[CodeBot]
        B -->|Travel| E[TravelBot]
        C --> F[Response Formatter]
        D --> F
        E --> F
        F --> G[API Response]
    end

    subgraph Infrastructure
        H[FastAPI] --> I[Docker]
        I --> J[GitHub Actions]
    end 
>>>>>>> 1a0121e74764e448d69fe25e468b571f043b3cc4
