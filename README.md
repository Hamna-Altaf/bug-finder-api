AI-Powered Bug Identifier for Code Snippets
A FastAPI-based REST API that accepts code snippets and returns possible bug descriptions and fix suggestions using Gemini-1.5-Pro. Designed to help junior developers and security researchers understand what’s wrong in a piece of code.

Features
POST /find-bug: Send a code snippet, get a bug report (logical, syntax, runtime).
GET /sample-cases: Retrieve example buggy code snippets with explanations.
Tone Mode: Choose between developer and casual explanation styles.
Rate Limiting: Max 5 requests per minute per IP.
Language Support: Python, JavaScript, C, etc.
Gemini Pro API Integration for smart analysis.

Tech Stack
FastAPI – Web framework
Google Generative AI – Bug analysis
SlowAPI – Rate limiting
Pydantic – Request validation
Uvicorn – ASGI server

Installation & Running Locally
1. clone the repo
  git clone https://github.com/hamna-altaf/bug-finder-api.git
  cd bug-finder-api

2. install dependencies
   pip install -r requirements.txt
   
3. run the app
   uvicorn app.main:app --reload

4. Access Swagger Docs:
   Open http://127.0.0.1:8000/docs in your browser


Rate Limiting
Max 5 requests per minute per IP
Returns 429 if limit is exceeded

