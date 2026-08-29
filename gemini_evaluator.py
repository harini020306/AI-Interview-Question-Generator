from google import genai
from dotenv import load_dotenv
import os
import json


# --------------------------------------------------
# Load API Key
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please check your .env file."
    )


# --------------------------------------------------
# Evaluate Answer
# --------------------------------------------------

def evaluate_answer(
    question,
    answer,
    job_role,
    skills
):
    """Evaluate a candidate's answer using Gemini."""

    client = genai.Client(
        api_key=api_key
    )

    skills_text = ", ".join(skills)

    prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate's answer objectively.

Candidate Information:
Job Role: {job_role}
Skills: {skills_text}

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer based on:

1. Technical correctness
2. Relevance
3. Clarity
4. Depth
5. Interview suitability

Give a score from 0 to 10.

Return ONLY valid JSON.

Do NOT use Markdown.
Do NOT add ```json.
Do NOT add ```.

Return exactly this format:

{{
    "score": 7,
    "strengths": [
        "Strength 1",
        "Strength 2"
    ],
    "improvements": [
        "Improvement 1",
        "Improvement 2"
    ],
    "better_answer": "A better version of the answer."
}}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    response_text = response.text.strip()


    # --------------------------------------------------
    # Remove Markdown code fences if Gemini adds them
    # --------------------------------------------------

    if response_text.startswith("```json"):
        response_text = response_text[7:]

    elif response_text.startswith("```"):
        response_text = response_text[3:]

    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()


    # --------------------------------------------------
    # Convert JSON
    # --------------------------------------------------

    evaluation = json.loads(response_text)


    # --------------------------------------------------
    # Validate Score
    # --------------------------------------------------

    score = evaluation.get("score")

    if not isinstance(score, (int, float)):
        raise ValueError(
            "Invalid score returned by Gemini."
        )

    score = max(0, min(10, float(score)))

    evaluation["score"] = score


    return evaluation


# --------------------------------------------------
# Test Evaluator
# --------------------------------------------------

if __name__ == "__main__":

    question = (
        "What is the difference between a list "
        "and a tuple in Python?"
    )

    answer = (
        "A list is mutable while a tuple is immutable. "
        "Lists use square brackets and tuples use parentheses."
    )

    evaluation = evaluate_answer(
        question,
        answer,
        "Python Developer",
        ["Python", "SQL"]
    )

    print("\n🤖 AI Evaluation\n")

    print(
        json.dumps(
            evaluation,
            indent=4
        )
    )
