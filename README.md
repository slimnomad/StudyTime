# Study Time - AI Study Planner

A simple Flask app I built to organize my study schedule. Lets you create subjects, add tasks with deadlines, track exams, and get AI-generated weekly study plans based on your workload.

## Why I built this
I was juggling multiple courses and kept missing deadlines or cramming last minute. Existing study apps were either too complicated or didn't adapt to my changing workload. So I made something simple that focuses on what I actually need: seeing everything in one place and getting smart suggestions for what to study each week.

## Features
- Create and manage subjects (like "Calculus II" or "Organic Chem")
- Add tasks with difficulty ratings and due dates
- Track exams and important deadlines
- Mark tasks as complete when done
- Get AI-powered weekly study plans that prioritize based on urgency and difficulty
- Basic stats to see your progress

## Tech Stack
- Backend: Flask (Python 3.9+)
- Database: SQLite (for simplicity, easy to switch to PostgreSQL later)
- ORM: SQLAlchemy
- AI: Groq's Llama3-70b-8192 (lightning fast inference)
- Frontend: Basic HTML/CSS with a touch of Bootstrap for responsiveness
- Nothing fancy - tried to keep it clean and understandable

## Setup
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Set up your API key:
   - Get a Groq key from console.groq.com (free tier available)
   - Create a `.env` file with: `GROQ_API_KEY=your_key_here`
6. Initialize the database: `flask init-db`
7. Run the app: `flask run`
8. Visit http://localhost:5000

## How it works (briefly)
The AI study plan feature looks at:
- Upcoming deadlines (tasks/exams)
- Estimated difficulty of each item
- Your current workload
- Then generates a balanced weekly plan suggesting what to focus on each day

It's not perfect - sometimes the suggestions need tweaking - but it's helped me avoid those 3am panic sessions before exams.

## Notes
- This was built as a learning project to practice Flask, SQLAlchemy, and integrating APIs
- Code isn't production-perfect but it works for personal use
- Feel free to fork and adapt it for your own workflow
- If you find bugs or have suggestions, issues are welcome!
- The Groq API is incredibly fast - responses come back in milliseconds, making the study plan generation feel instantaneous

---
Built with ☕ during late-night study sessions