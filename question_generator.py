import json
import random
import os


def load_questions():
    """Load questions from the JSON file."""

    file_path = os.path.join(
        os.path.dirname(__file__),
        "data",
        "questions.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_questions(
    skills,
    interview_type,
    difficulty,
    number_of_questions
):
    """Generate questions based on skills, interview type and difficulty."""

    questions_data = load_questions()

    available_questions = []

    # Clean the inputs
    interview_type = interview_type.strip()
    difficulty = difficulty.strip()

    for skill in skills:

        skill = skill.strip()

        # Check skill
        if skill not in questions_data:
            continue

        # Check interview type
        if interview_type not in questions_data[skill]:
            continue

        # Check difficulty
        if difficulty not in questions_data[skill][interview_type]:
            continue

        # Add questions
        available_questions.extend(
            questions_data[skill][interview_type][difficulty]
        )

    # No questions found
    if not available_questions:
        return []

    # Randomize questions
    random.shuffle(available_questions)

    # Return required number
    return available_questions[:number_of_questions]


# Test
if __name__ == "__main__":

    questions = generate_questions(
    ["Python"],
    "Technical",
    "Medium",
    10
)

    print("\n🤖 Generated Interview Questions:\n")

    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question}")