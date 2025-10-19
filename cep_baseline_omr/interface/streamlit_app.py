import streamlit as st
import cv2
import numpy as np
import json

from core.bubble_scanner import detect_bubbles
from core.grid_mapper import generate_question_grid, draw_grid_overlay
from core.metadata_extractor import extract_bubble_metadata
from core.response_mapper import map_bubbles_to_responses
from core.answer_evaluator import evaluate_responses
from core.excel_writer import write_student_to_excel
from core.feedback_generator import generate_poetic_feedback, display_badge
from interface.dashboard import display_class_dashboard

# Page setup
st.set_page_config(page_title="CEP Baseline OMR Processor", layout="wide")
st.title("📄 CEP Baseline OMR Processor")

# Sidebar
with st.sidebar:
    uploaded_file = st.file_uploader("Upload scanned OMR sheet", type=["jpg", "jpeg", "png"])
    answer_key_file = st.file_uploader("Upload answer_key.json", type=["json"])
    show_grid = st.checkbox("🔍 Show Grid Overlay")
    export_excel = st.checkbox("📤 Export to Excel")

# Load answer key
if answer_key_file:
    try:
        answer_key = json.load(answer_key_file)
    except Exception:
        st.error("❌ Failed to load answer_key.json. Please check the file format.")
        st.stop()
else:
    st.warning("Please upload answer_key.json")
    answer_key = {"flat": {}, "subject_map": {}}

# Process image
if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        st.error("❌ Failed to decode image. Please upload a valid PNG or JPG file.")
        st.stop()

    bubbles = detect_bubbles(img)

    # Grid parameters (adjust as needed)
    grid = generate_question_grid(start_x=80, start_y=180, dx=38, dy=28, rows=54, cols=2)

    if show_grid:
        grid_img = draw_grid_overlay(img.copy(), grid)
        st.image(grid_img, caption="🧭 Grid Overlay for Calibration")

    responses = map_bubbles_to_responses(bubbles, grid)
    metadata_blocks = {}  # Define expected bubble blocks for metadata
    metadata = extract_bubble_metadata(bubbles, metadata_blocks)

    st.markdown(f"### 🎓 Student: **{metadata['student_id']}** | School: **{metadata['school_mgmt']}**")
    st.markdown(generate_poetic_feedback(metadata["student_id"], responses))

    evaluation = evaluate_responses(responses, answer_key)
    st.markdown(display_badge(metadata["student_id"], evaluation["score"], evaluation["subject_scores"]))

    st.markdown("#### 📊 Subject-wise Scores")
    for subject, score in evaluation["subject_scores"].items():
        st.write(f"• {subject}: {round(score, 2)}")

    # Export to Excel
    if export_excel:
        student_data = {
            "name": metadata["student_id"],
            "student_id": metadata["student_id"],
            "section": "A",
            "responses": responses,
            "correct": evaluation["correct"],
            "answer_key": answer_key["flat"],
            "subject_scores": evaluation["subject_scores"]
        }
        write_student_to_excel(
            student_data,
            "data/CEP Baseline Recording Sheet 9th 10th.xlsx",
            "data/exports/class10_results.xlsx"
        )
        st.success("✅ Results written to Excel")

    # Dashboard
    display_class_dashboard([{
        "Name": metadata["student_id"],
        "Roll No": metadata["student_id"],
        "Score": evaluation["score"],
        "subject_scores": evaluation["subject_scores"]
    }])
else:
    st.info("📥 Please upload a scanned OMR sheet to begin.")
