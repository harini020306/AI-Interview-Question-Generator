# 🤖 AI Interview Coach

An AI-powered interview preparation platform built with **Python, Streamlit, and Google Gemini**.

AI Interview Coach generates personalized interview questions based on the candidate's **job role, skills, interview type, and difficulty level**, then evaluates their answers using Gemini and provides meaningful feedback.

## 🚀 Features

* 🎯 Personalized interview questions
* 💼 Job-role based questions
* 🛠️ Skill-based question generation
* 📊 Easy, Medium, and Hard difficulty levels
* 🎤 Technical, Coding, HR, and Aptitude interview modes
* 🔢 Generate 10–20 questions per interview
* 🤖 AI-powered answer evaluation
* ⭐ Candidate scoring
* 💡 Strengths and improvement suggestions
* 📝 AI-generated better answers
* 🔐 Secure Gemini API key handling
* 🖥️ Interactive Streamlit interface

## 🧠 How It Works

```text
                ┌──────────────────────┐
                │      User Input      │
                │                      │
                │ Job Role             │
                │ Skills               │
                │ Interview Type       │
                │ Difficulty           │
                │ Number of Questions  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Google Gemini     │
                │   Question Generator │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Interview Questions  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Candidate Answer   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Google Gemini     │
                │    AI Evaluator      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    AI Feedback       │
                │                      │
                │ Score                │
                │ Strengths            │
                │ Improvements         │
                │ Better Answer        │
                └──────────────────────┘
```

## 🛠️ Tech Stack

| Technology    | Purpose                               |
| ------------- | ------------------------------------- |
| Python        | Core programming language             |
| Streamlit     | Web application interface             |
| Google Gemini | AI question generation and evaluation |
| python-dotenv | Environment variable management       |
| JSON          | Structured data handling              |
| Git & GitHub  | Version control and project hosting   |

## 📂 Project Structure

```text
AI-Interview-Question-Generator/
│
├── app.py
├── gemini_generator.py
├── gemini_evaluator.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── data/
│   └── questions.json
│
└── screenshots/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/harini020306/AI-Interview-Question-Generator.git
```

```bash
cd AI-Interview-Question-Generator
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

Never upload your real API key to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔐 Environment Variables

The project uses an environment variable for the Gemini API key.

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

The actual `.env` file is intentionally excluded from GitHub using `.gitignore`.

## 🎯 Example Workflow

```text
Enter Job Role
      ↓
Enter Skills
      ↓
Select Interview Type
      ↓
Select Difficulty
      ↓
Select Number of Questions
      ↓
Generate Questions
      ↓
Answer Questions
      ↓
AI Evaluation
      ↓
Score + Feedback + Better Answer
```

## 📊 AI Evaluation

The evaluator provides:

* **Score** – evaluates the quality of the candidate's answer
* **Strengths** – identifies what was done well
* **Improvements** – highlights missing concepts
* **Better Answer** – provides an improved interview-ready response

## 🔮 Future Enhancements

* 🎙️ Voice-based interviews
* 🗣️ Speech-to-text answers
* 📈 Interview performance dashboard
* 📊 Progress tracking
* 🧑‍💼 Resume-based question generation
* ⏱️ Timed interview mode
* 🏆 Interview history and analytics
* 🌐 Online deployment
* 📄 Automatic interview report generation

## 👩‍💻 Author

**Harini K.**

B.E. Electronics and Communication Engineering

Interested in **Artificial Intelligence, Machine Learning, Python, IoT, and Embedded Systems**.

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
