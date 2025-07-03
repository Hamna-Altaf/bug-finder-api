# bug-finder-api
AI-Powered Bug Identifier for Code Snippets: A FastAPI-based REST API that accepts code snippets and returns possible bug descriptions and fix suggestions using Gemini-1.5-Pro LLM. Designed to help developers understand what’s wrong in a piece of code.

Features
POST /find-bug: Send a code snippet, get a bug report (logic, runtime, syntax, etc).

GET /sample-cases: Retrieve example buggy code snippets with explanations.

Rate Limiter: Prevents abuse (max 5 requests/minute per IP).

Tone Mode: Choose between developer and casual explanation styles.

Multi-language support: Python, JavaScript, C, etc.

Gemini Pro API integration.

Tech Stack
FastAPI for API framework

Google Generative AI for bug analysis

SlowAPI for rate limiting

Pydantic for request validation

Uvicorn as ASGI server


Installation & Running Locally
1. clone the repo:

    git clone https://github.com/hamna-altaf/bug-finder-api.git
    cd bug-finder-api

2. install dependencies:
    pip install -r requirements.txt

3. Enter your Gemini API key:
    genai.configure(api_key="your-gemini-api-key")

4. run the app:
    uvicorn app.main:app --reload

5. Visit docs / swagger UI:
    http://127.0.0.1:8000/docs
    # by adding /docs 

Rate Limiting:
    Max 5 requests per minute per IP
    Returns 429 if limit is exceeded

