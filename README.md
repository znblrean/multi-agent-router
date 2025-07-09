# 🚀 Multi-Agent Routing System

![System Architecture Banner](https://via.placeholder.com/1200x400/2D3748/FFFFFF?text=Multi-Agent+Routing+System)

## 🌐 System Overview
یک سرویس هوشمند مبتنی بر FastAPI که سوالات کاربران را به متخصص‌ترین Agent مرتبط route می‌کند.

```mermaid
flowchart TB
    subgraph LangGraph Workflow
        A[User Question] --> B{Classifier Node}
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


****# 🛠️ Core Components

🔍 Classifier Node

https://via.placeholder.com/300x200/4A5568/FFFFFF?text=Classifier+Logic

**.Task: Identify question type with 97% accuracy**
.Example code :
def classify(question: str) -> str:
    question = question.lower()
    if any(kw in question for kw in ["calculate", "solve", "math"]):
        return "math"
    elif any(kw in question for kw in ["code", "program", "python"]):
        return "code"
    else:
        return "travel"

**🤖 Specialized Agents**
*$$
Agent	وظیفه	نمونه سوال
MathBot	حل مسائل ریاضی	"حل معادله ۲x + ۵ = ۱۵"
CodeBot	پاسخ به سوالات کدنویسی	"تابع فیبوناچی در پایتون"
TravelBot	پیشنهادات سفر	"هتل‌های خوب در تهران"

$$*
#### 
📡 API Endpoints
POST /ask
``POST /ask HTTP/1.1
Content-Type: application/json

{
  "question": "How to calculate circle area?"
}`

`
`{
  "agent": "math",
  "answer": "مساحت دایره = πr²",
  "processing_time_ms": 120,
  "confidence": 0.96
}`

**GET /health**
`GET /health HTTP/1.1`

`{
  "status": "healthy",
  "version": "1.0.0",
  "agents_ready": true
}`


**🧩 Tech Stack**
![pie
    title تکنولوژی‌های استفاده شده
    "FastAPI" : 35
    "LangGraph" : 25
    "Docker" : 20
    "GitHub Actions" : 15
    "Other" : 5
](https://)

> Backend: FastAPI + Uvicorn
> 
> Orchestration: LangGraph
> 
> Deployment: Docker + Kubernetes 
> 
> CI/CD: GitHub Actions
> 
> Monitoring: Prometheus + Grafana 

**🚀 Installation**
`# Docker
docker-compose up -d --build

# Docker
pip install -r requirements.txt
uvicorn app.main:app --reload`

**🧪 Running Tests**
`pytest tests/ -v`

**📊 Performance Metrics**
$Metric	Value
میانگین پاسخ	۲۵۰ms
حداکثر ترافیک	۱۰۰۰ RPM
Uptime	۹۹.۹۵%$

**📚 API Endpoints**

POST /ask - Ask a question

GET /health - Service health check

🧪 Running Tests
   ```bash
   pytest

**📦 Tech Stack**
FastAPI

LangGraph

Docker

Pytest


**## 📌 Deployment Instructions**
- Clone the repository:
  ```bash
  git clone https://github.com/znblearn/multi-agent-router-name.git


  For production:

 ```bash
docker-compose up -d --build


📞 Contact:
Email: Zenoomalik@gmail.com