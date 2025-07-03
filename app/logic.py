import google.generativeai as genai
import json



genai.configure(api_key="AIzaSyBAGZQmc438MahNVV8g2RIsU7NpT7Xvchs")

model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_code(language: str, code: str, mode: str = "developer") -> dict:
    tone_instruction = "Explain clearly for a developer." if mode == "developer" else "Use a casual and simple explanation for anyone to understand."
    
    prompt = f"""{tone_instruction}

    You are a senior software bug analyst. Carefully review the following {language} code snippet and identify any bugs.

    Return your answer in valid JSON with the following fields:
    - bug_type (e.g. "Logical Bug", "Runtime Error", "Syntax Error", "Off-by-One Error", etc)
    - description (what is wrong and why)
    - suggestion (how to fix it, if possible)

    Code to analyze:
    {code}
    """
    try:
        response = model.generate_content(prompt)
        reply_text = response.text.strip()


        #This will replace the backticks if the reply includes them
        if reply_text.startswith("```json"):
            reply_text = reply_text.replace("```json", "").replace("```", "").strip()

        return json.loads(reply_text)

    except Exception as e:
        return {
            "bug_type": "Error",
            "description": "Something went wrong while analyzing the code.",
            "suggestion": str(e) if "quota" not in str(e) else "Gemini API quota exceeded. Try again later"
        }
