import os
import json
import re
import urllib.request

# Reads GEMINI_API_KEY from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent?key=" + GEMINI_API_KEY
    if GEMINI_API_KEY else ""
)

def analyze_resume_vs_job(resume_text: str, job_description: str) -> dict:
    """
    Sends resume + job description to Gemini API.
    Returns a structured analysis with score, strengths, gaps, and suggestions.
    """

    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is not set. "
            "Run: set GEMINI_API_KEY=your-key-here  (Windows) "
            "or: export GEMINI_API_KEY=your-key-here  (Mac/Linux)"
        )

    prompt = f"""
You are an expert technical recruiter and career coach with 15+ years of experience in the IT industry, especially in India.

A candidate has shared their resume and a job description. Your job is to:
1. Carefully compare the resume against the job description
2. Give an honest match score out of 100
3. List what is strong in the resume for this role
4. List the skill/experience gaps
5. Give specific, actionable suggestions to improve chances

Respond ONLY in valid JSON format with this exact structure:
{{
  "score": <integer 0-100>,
  "verdict": "<one line honest summary of fit>",
  "strengths": ["<strength 1>", "<strength 2>", ...],
  "gaps": ["<gap 1>", "<gap 2>", ...],
  "suggestions": ["<suggestion 1>", "<suggestion 2>", ...],
  "keywords_matched": ["<keyword1>", "<keyword2>", ...],
  "keywords_missing": ["<keyword1>", "<keyword2>", ...]
}}

---
RESUME:
{resume_text}

---
JOB DESCRIPTION:
{job_description}
"""

    payload = json.dumps({
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }).encode("utf-8")

    req = urllib.request.Request(
        GEMINI_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode("utf-8"))

    raw = data["candidates"][0]["content"]["parts"][0]["text"].strip()

    # Strip markdown code fences if present
    raw = re.sub(r'^```json\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)

    result = json.loads(raw)
    return result