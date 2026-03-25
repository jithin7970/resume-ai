# ResumeMatch AI 🎯
> AI-powered resume vs job description analyzer — built with Python Flask + Claude API

## What it does
Paste your resume and any job description → get an honest match score, skill gaps, strengths, and suggestions powered by Claude AI.

## Tech Stack
- **Backend:** Python, Flask
- **AI:** Anthropic Claude API (claude-sonnet)
- **Frontend:** HTML5, CSS3, Vanilla JS
- **Deployment:** Render (free tier)

## Setup & Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/resumematch-ai
cd resumematch-ai
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your API key
```bash
# Mac/Linux
export ANTHROPIC_API_KEY=your_api_key_here

# Windows
set ANTHROPIC_API_KEY=your_api_key_here
```
Get your free API key at: https://console.anthropic.com

### 5. Run the app
```bash
python app.py
```
Visit: http://localhost:5000

## Deploy to Render (Free)
1. Push code to GitHub
2. Go to render.com → New Web Service
3. Connect your GitHub repo
4. Set environment variable: `ANTHROPIC_API_KEY`
5. Build command: `pip install -r requirements.txt`
6. Start command: `gunicorn app:app`
7. Done — your app is live!

## Project Structure
```
resumematch-ai/
├── app.py              # Flask routes
├── analyzer.py         # Claude API integration
├── requirements.txt    # Dependencies
├── templates/
│   └── index.html      # Frontend UI
└── README.md
```

## Author
Jithin Chidepudi — [LinkedIn](https://linkedin.com/in/jithinchidepudi) | [GitHub](https://github.com/jithinchidepudi)
