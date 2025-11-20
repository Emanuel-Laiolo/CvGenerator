This project is a Python-based tool that generates my Curriculum Vitae programmatically. Instead of manually editing documents, I treat my professional experience as a dataset (`JSON`) and render it into a styled format (`HTML/PDF`) using Jinja2 templating.

## 🚀 Live Demo
Check out the web version of my CV here:
👉 https://the-anderson.github.io/CvGenerator/

## 🛠️ Tech Stack
* **Python:** Core logic and data processing.
* **Jinja2:** Templating engine to render HTML.
* **JSON:** Data storage for professional experience and skills.
* **HTML/CSS:** Semantic structure and print-friendly styling.

## 📂 Project Structure
* `cv_data.json`: Contains my profile, experience, and skills (The "Database").
* `template.html`: The structural design of the CV (The "View").
* `build_cv.py`: The script that merges data with the template (The "Controller").

## 💻 How to run locally
1. Clone the repo:
   ```bash
   git clone [https://github.com/The-Anderson/CvGenerator.git](https://github.com/The-Anderson/CvGenerator.git)
