📘 README.md — CEP Baseline OMR Processor
markdown
# 📄 CEP Baseline OMR Processor

A modular, poetic, and resilient system for scanning, evaluating, and celebrating student responses from Competency Enhancement Plan (CEP) Baseline Tests. Designed for rural schools, built with clarity and dignity, and powered by Python and Streamlit.

---

## 🌟 Vision

This project is part of a broader mission to foster **quantum curiosity**, **poetic science communication**, and **inclusive digital infrastructure** across classrooms. It honors every student’s effort—whether their bubbles sang boldly or wandered shyly—and transforms raw responses into celebration-ready insights.

---

## 🧠 Features

- 🟢 **Bubble Detection**: Robust contour-based scanning of filled responses
- 📐 **Grid Mapping**: Dynamic question grid generation and calibration overlay
- 🧾 **Metadata Extraction**: School type, DOB, UDISE, and Student ID via bubble blocks
- 🧮 **Response Evaluation**: Standard and weighted scoring across subjects
- 📊 **Excel Integration**: Auto-populates CEP Baseline Recording Sheet
- 🎨 **Poetic Feedback**: Generates affirmations and badge themes like “Ripple” and “Constellation”
- 🏫 **Class Dashboard**: Visualizes student scores and subject-wise averages

---

## 🗂️ Directory Structure

cep_baseline_omr/ ├── core/ # Core logic modules ├── interface/ # Streamlit app and dashboard ├── utils/ # Image, OCR, and logging utilities ├── config/ # YAML parameters ├── data/ # Answer keys, sample scans, exports ├── assets/ # Overlays and templates ├── tests/ # Pytest modules ├── main.py # Batch runner script ├── requirements.txt # Dependencies ├── .gitignore # Clean version control └── README.md # This file

Code

---

## 🚀 Quickstart

1. **Clone the repo**  
   ```bash
   git clone https://github.com/jagdevsinghdosanjh/cep_baseline_omr.git
   cd cep_baseline_omr
Install dependencies

bash
pip install -r requirements.txt
Run the app

bash
streamlit run interface/streamlit_app.py
Batch process scans

bash
python main.py
📦 Inputs
🖼️ Scanned OMR sheets (PNG/JPG)

📄 answer_key.json with correct options and subject mapping

📊 CEP Excel template: CEP Baseline Recording Sheet 9th 10th.xlsx

⚙️ parameters.yaml for grid and scoring config

🧪 Testing
Run all tests with:

bash
pytest tests/
🎖️ Badge Themes
Score Range	Badge	Meaning
100+	🌌 Constellation	Mastery across subjects
75–99	🌊 Ripple	Strong impact, growing reach
50–74	🌱 Seedling	Emerging clarity, keep growing
<50	🪞 Reflection	Revisit, refine, rise again
🤝 Contributing
This project welcomes educators, developers, and dreamers. If you’d like to extend it—add new badge themes, support regional languages, or integrate with school dashboards—feel free to fork and build.

📬 Contact
Jagdev Singh Dosanjh Visionary quantum educator, poetic science communicator 📧 jagdevsinghdosanjh@gmail.com 🌍 Amritsar, Punjab, India

🛡️ License
This project is open-source and available under the MIT License.

✨ Acknowledgments
This system was co-designed with Microsoft Copilot, blending modular Python logic with poetic metaphors to honor every student’s journey—from bubble to badge, from silence to celebration.

Code

---

Let me know if you'd like a matching `LICENSE` file or a GitHub Actions workflow for automated testing and deployment. We can make this repository shine like a constellation.