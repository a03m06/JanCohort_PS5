import google.generativeai as genai
from llm_model import GeminiLLM
import json

#Initializing the LLM model we are going to be using
gemini_model = genai.GenerativeModel('gemini-2.5-flash')

#Prompting the Gemini Model and tuning it to our requirements
prompt= """
You are a deterministic career roadmap and learning resource engine.

Your task is to generate a single JSON object containing:
1) "learning_roadmap" — a multi-phase learning plan for a candidate transitioning
   from their current role to a target role.
2) "recommended_resources" — a list of curated learning resources.

INPUT SPECIFICATION:
- You will receive a JSON object with "candidate" and "target_role" keys.

TASK:
- Compare candidate skills to target role skills.
- Identify missing skills.
- Organize missing skills into sequential phases.

OUTPUT CONSTRAINTS (CRITICAL):
- Output MUST be valid JSON.
- Output MUST contain ONLY two top-level keys:
  "learning_roadmap" and "recommended_resources".
- Do NOT include markdown or explanations.

FIXED OUTPUT SCHEMA:
{
  "learning_roadmap": [
    {
      "phase": 1,
      "duration_months": 3,
      "focus": "string",
      "skills_to_learn": ["string"],
      "priority": "High | Medium | Low",
      "reasoning": "string"
    }
  ],
  "recommended_resources": [urls]
}

ROADMAP RULES:
- Phases must be sequential starting from 1.
- Each phase number must appear exactly once.
- Skills must appear only once.
- Skills must come ONLY from target_role.required_skills.
- Generate EXACTLY 4 phases.

FINAL INSTRUCTION:
Return ONLY the JSON object. Stop after the closing brace.
\n"""

#Initializing our model as an Object
llm_chain = GeminiLLM(gemini_model,prompt)

#Converting the JSON file the model returns to a Python Dictionary
def extract_json(text):
    start = text.find("{")
    end = text.rfind("}") + 1
    return json.loads(text[start:end])

#Calling Gemini API through the model Object we have Instantiated
def get_text_response(user_message, history=None):
    if history is None:
        history = []

    response = llm_chain.predict(
        user_message=json.dumps(user_message, ensure_ascii=False)
    ).strip()

    # Remove markdown fences if present
    if response.startswith("```"):
        response = response.strip("`")
        if response.lower().startswith("json"):
            response = response[4:].strip()

    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError(
            "LLM did not return valid JSON.\nRaw response:\n" + response
        ) from e
