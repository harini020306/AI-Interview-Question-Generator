import streamlit as st

from gemini_generator import generate_ai_questions
from gemini_evaluator import evaluate_answer


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    layout="centered"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .score-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        border: 1px solid #ddd;
    }

    .score-number {
        font-size: 45px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# TITLE
# ==================================================

st.markdown(
    '<div class="main-title">🤖 AI Interview Coach</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Practice interviews and receive instant AI-powered feedback using Google Gemini.'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# SESSION STATE
# ==================================================

if "started" not in st.session_state:
    st.session_state.started = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "evaluations" not in st.session_state:
    st.session_state.evaluations = []

if "current_evaluation" not in st.session_state:
    st.session_state.current_evaluation = None


# ==================================================
# INTERVIEW SETUP
# ==================================================

if not st.session_state.started:

    st.header("🎯 Interview Setup")

    job_role = st.text_input(
        "💼 Job Role",
        placeholder="Example: Python Developer"
    )

    skills_input = st.text_input(
        "🛠️ Skills",
        placeholder="Example: Python, SQL, Machine Learning"
    )

    interview_type = st.selectbox(
        "🎯 Interview Type",
        [
            "Technical",
            "Coding",
            "HR",
            "Aptitude"
        ]
    )

    difficulty = st.selectbox(
        "📊 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    number_of_questions = st.number_input(
        "🔢 Number of Questions",
        min_value=10,
        max_value=20,
        value=10,
        step=1
    )

    st.divider()

    if st.button(
        "🚀 Start Interview",
        use_container_width=True
    ):

        if not job_role.strip():

            st.warning(
                "⚠️ Please enter your job role."
            )

        elif not skills_input.strip():

            st.warning(
                "⚠️ Please enter at least one skill."
            )

        else:

            skills = [
                skill.strip()
                for skill in skills_input.split(",")
                if skill.strip()
            ]

            with st.spinner(
                "🤖 Gemini is preparing your interview..."
            ):

                try:

                    generated_questions = generate_ai_questions(
                        job_role,
                        skills,
                        interview_type,
                        difficulty,
                        int(number_of_questions)
                    )

                    st.session_state.questions = (
                        generated_questions
                    )

                    st.session_state.current_question = 0
                    st.session_state.evaluations = []
                    st.session_state.current_evaluation = None

                    st.session_state.job_role = job_role
                    st.session_state.skills = skills
                    st.session_state.interview_type = interview_type
                    st.session_state.difficulty = difficulty

                    st.session_state.started = True

                    st.rerun()

                except Exception as e:

                    st.error(
                        f"❌ Error generating questions: {e}"
                    )


# ==================================================
# INTERVIEW MODE
# ==================================================

elif (
    st.session_state.current_question
    < len(st.session_state.questions)
):

    current = st.session_state.current_question

    total = len(st.session_state.questions)

    question = st.session_state.questions[current]


    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    st.header("🎤 Interview in Progress")

    st.progress(
        (current + 1) / total
    )

    st.write(
        f"### Question {current + 1} of {total}"
    )

    st.divider()


    # --------------------------------------------------
    # Question
    # --------------------------------------------------

    st.subheader(
        question
    )


    # --------------------------------------------------
    # Answer
    # --------------------------------------------------

    answer = st.text_area(
        "✍️ Your Answer",
        height=180,
        placeholder="Type your answer here..."
    )


    # --------------------------------------------------
    # Evaluate
    # --------------------------------------------------

    if st.button(
        "🤖 Evaluate My Answer",
        use_container_width=True
    ):

        if not answer.strip():

            st.warning(
                "⚠️ Please enter your answer first."
            )

        else:

            with st.spinner(
                "🧠 Gemini is evaluating your answer..."
            ):

                try:

                    evaluation = evaluate_answer(
                        question,
                        answer,
                        st.session_state.job_role,
                        st.session_state.skills
                    )

                    st.session_state.current_evaluation = (
                        evaluation
                    )

                    st.session_state.evaluations.append(
                        evaluation
                    )

                    st.rerun()

                except Exception as e:

                    st.error(
                        f"❌ Evaluation error: {e}"
                    )


    # --------------------------------------------------
    # Show Evaluation
    # --------------------------------------------------

    if st.session_state.current_evaluation:

        evaluation = (
            st.session_state.current_evaluation
        )

        st.divider()

        st.subheader("🧠 AI Evaluation")


        # Score
        st.metric(
            "⭐ Score",
            f"{evaluation['score']:.1f} / 10"
        )


        # Strengths
        st.markdown("### ✅ Strengths")

        for strength in evaluation["strengths"]:

            st.write(
                f"• {strength}"
            )


        # Improvements
        st.markdown(
            "### ⚠️ Areas for Improvement"
        )

        for improvement in evaluation["improvements"]:

            st.write(
                f"• {improvement}"
            )


        # Better Answer
        st.markdown(
            "### 💡 Better Answer"
        )

        st.info(
            evaluation["better_answer"]
        )


        st.divider()


        # Next Question
        if st.button(
            "➡️ Next Question",
            use_container_width=True
        ):

            if current < total - 1:

                st.session_state.current_question += 1

                st.session_state.current_evaluation = None

                st.rerun()

            else:

                st.session_state.current_question = total

                st.session_state.current_evaluation = None

                st.rerun()


# ==================================================
# INTERVIEW COMPLETED
# ==================================================

else:

    st.header("🏆 Interview Completed!")

    st.success(
        "🎉 Congratulations! You completed the interview."
    )


    evaluations = (
        st.session_state.evaluations
    )


    # ==================================================
    # FINAL SCORE
    # ==================================================

    if evaluations:

        scores = [
            evaluation["score"]
            for evaluation in evaluations
        ]

        average_score = (
            sum(scores) / len(scores)
        )


        st.markdown(
            f"""
            <div class="score-box">

            <div>🏆 Overall Interview Score</div>

            <div class="score-number">
            {average_score:.1f} / 10
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        # ==================================================
        # PERFORMANCE
        # ==================================================

        if average_score >= 8.5:

            performance = "🌟 Excellent"

            message = (
                "Outstanding performance! "
                "You are interview ready."
            )

        elif average_score >= 7:

            performance = "🔥 Very Good"

            message = (
                "Great performance! "
                "A little more practice can make you stronger."
            )

        elif average_score >= 5:

            performance = "👍 Good"

            message = (
                "Good start. Focus on the improvement areas."
            )

        else:

            performance = "📚 Needs Improvement"

            message = (
                "Keep practicing. "
                "Review the concepts and try again."
            )


        st.subheader(
            f"Performance: {performance}"
        )

        st.write(
            message
        )


        # ==================================================
        # INTERVIEW DETAILS
        # ==================================================

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Questions",
                len(evaluations)
            )

        with col2:

            st.metric(
                "Average Score",
                f"{average_score:.1f}"
            )


        # ==================================================
        # SCORE BREAKDOWN
        # ==================================================

        st.subheader(
            "📈 Score Breakdown"
        )

        for index, evaluation in enumerate(
            evaluations,
            start=1
        ):

            score = evaluation["score"]

            st.write(
                f"Question {index}"
            )

            st.progress(
                score / 10
            )

            st.caption(
                f"Score: {score:.1f}/10"
            )


        # ==================================================
        # DETAILED FEEDBACK
        # ==================================================

        st.subheader(
            "📝 Detailed Feedback"
        )

        for index, evaluation in enumerate(
            evaluations,
            start=1
        ):

            with st.expander(
                f"Question {index} — "
                f"{evaluation['score']:.1f}/10"
            ):

                st.markdown(
                    "### ✅ Strengths"
                )

                for strength in evaluation["strengths"]:

                    st.write(
                        f"• {strength}"
                    )


                st.markdown(
                    "### ⚠️ Improvements"
                )

                for improvement in evaluation["improvements"]:

                    st.write(
                        f"• {improvement}"
                    )


                st.markdown(
                    "### 💡 Better Answer"
                )

                st.info(
                    evaluation["better_answer"]
                )


    else:

        st.warning(
            "No evaluations were recorded."
        )


    # ==================================================
    # NEW INTERVIEW
    # ==================================================

    st.divider()

    if st.button(
        "🔄 Start New Interview",
        use_container_width=True
    ):

        st.session_state.clear()

        st.rerun()
