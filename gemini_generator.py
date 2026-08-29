from google import genai
import json


def generate_ai_questions(
    job_role,
    skills,
    interview_type,
    difficulty,
    number_of_questions
):
    """Generate structured interview questions using Gemini."""

    client = genai.Client()

    skills_text = ", ".join(skills)

    prompt = f"""
You are an expert interviewer.

Generate exactly {number_of_questions} interview questions.

Candidate Information:
Job Role: {job_role}
Skills: {skills_text}
Interview Type: {interview_type}
Difficulty: {difficulty}

Rules:

1. Generate exactly {number_of_questions} questions.
2. Questions must match the job role.
3. Questions must use the candidate's skills.
4. Match the requested difficulty.
5. Technical → technical concepts.
6. Coding → programming problems.
7. HR → behavioral/situational questions.
8. Aptitude → quantitative/logical reasoning.
9. Do NOT provide answers.
10. Return ONLY valid JSON.
11. Do not use Markdown.
12. Do not add ```json or ```.

Return exactly this format:

[
    {{
        "question": "Question text"
    }},
    {{
        "question": "Question text"
    }}
]
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    response_text = interaction.output_text.strip()

    questions_data = json.loads(response_text)

    questions = [
        item["question"]
        for item in questions_data
    ]

    return questions


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    questions = generate_ai_questions(
        "Python Developer",
        ["Python", "SQL"],
        "Technical",
        "Medium",
        10
    )

    print("\n🤖 Generated Interview Questions:\n")

    for index, question in enumerate(
        questions,
        start=1
    ):
        print(f"{index}. {question}")