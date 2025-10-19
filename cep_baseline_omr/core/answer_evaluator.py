def evaluate_responses(responses, answer_key, grading="standard", weights=None):
    """
    Compares responses to answer key and computes score.
    Supports weighted scoring.
    """
    weights = weights or {}
    score = 0
    correct = {}
    incorrect = {}
    subject_scores = {}

    for q_no, selected in responses.items():
        correct_ans = answer_key.get("flat", {}).get(q_no)
        subject = answer_key.get("subject_map", {}).get(q_no, "General")
        weight = weights.get(subject, 1.0) if grading == "weighted" else 1.0

        if selected == correct_ans:
            score += weight
            correct[q_no] = selected
            subject_scores[subject] = subject_scores.get(subject, 0) + weight
        else:
            incorrect[q_no] = selected

    return {
        "score": round(score, 2),
        "correct": correct,
        "incorrect": incorrect,
        "subject_scores": subject_scores
    }
