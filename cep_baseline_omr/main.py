import cv2
import numpy as np
import os
import json

from core.bubble_scanner import detect_bubbles
from core.grid_mapper import generate_question_grid
from core.response_mapper import map_bubbles_to_responses
from core.metadata_extractor import extract_bubble_metadata
from core.answer_evaluator import evaluate_responses
from core.excel_writer import write_student_to_excel
from core.feedback_generator import generate_poetic_feedback, display_badge
from interface.dashboard import export_summary

# Load answer key
with open("data/answer_key.json", "r") as f:
    answer_key = json.load(f)

# Grid parameters
grid = generate_question_grid(start_x=80, start_y=180, dx=38, dy=28, rows=54, cols=2)

# Metadata bubble blocks (define if using bubble-based ID extraction)
metadata_blocks = {}  # Optional: fill with bubble positions

# Process all images in sample folder
results = []
scan_folder = "data/sample_omr_scans"
template_path = "data/CEP Baseline Recording Sheet 9th 10th.xlsx"
output_path = "data/exports/class10_results.xlsx"

for filename in os.listdir(scan_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(scan_folder, filename)
        img = cv2.imread(path)
        bubbles = detect_bubbles(img)
        responses = map_bubbles_to_responses(bubbles, grid)
        metadata = extract_bubble_metadata(bubbles, metadata_blocks)

        evaluation = evaluate_responses(responses, answer_key)
        print(generate_poetic_feedback(metadata["student_id"], responses))
        print(display_badge(metadata["student_id"], evaluation["score"], evaluation["subject_scores"]))

        student_data = {
            "name": metadata["student_id"],
            "student_id": metadata["student_id"],
            "section": "A",
            "responses": responses,
            "correct": evaluation["correct"],
            "answer_key": answer_key["flat"],
            "subject_scores": evaluation["subject_scores"]
        }

        write_student_to_excel(student_data, template_path, output_path)

        results.append({
            "Name": metadata["student_id"],
            "Roll No": metadata["student_id"],
            "Score": evaluation["score"],
            "subject_scores": evaluation["subject_scores"]
        })

# Export summary
export_summary(results)
