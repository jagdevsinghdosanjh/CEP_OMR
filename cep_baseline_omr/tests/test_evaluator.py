import pytest
from core.answer_evaluator import evaluate_responses

# Sample answer key
answer_key = {
    "flat": {
        1: 2, 2: 1, 3: 0, 4: 3, 5: 2
    },
    "subject_map": {
        1: "Punjabi", 2: "Punjabi", 3: "Punjabi", 4: "Science", 5: "Science"
    }
}

def test_evaluate_standard_scoring():
    responses = {1: 2, 2: 1, 3: 1, 4: 3, 5: 0}
    result = evaluate_responses(responses, answer_key, grading="standard")

    assert result["score"] == 3.0
    assert len(result["correct"]) == 3
    assert len(result["incorrect"]) == 2
    assert result["subject_scores"]["Punjabi"] == 2.0
    assert result["subject_scores"]["Science"] == 1.0

def test_evaluate_weighted_scoring():
    responses = {1: 2, 2: 1, 3: 1, 4: 3, 5: 0}
    weights = {"Punjabi": 1.0, "Science": 2.0}
    result = evaluate_responses(responses, answer_key, grading="weighted", weights=weights)

    assert result["score"] == 4.0
    assert result["subject_scores"]["Punjabi"] == 2.0
    assert result["subject_scores"]["Science"] == 2.0
