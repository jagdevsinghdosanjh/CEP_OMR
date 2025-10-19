def generate_poetic_feedback(student_name, responses, expected=108):
    """
    Returns poetic feedback based on missing responses.
    """
    actual = len(responses)
    missing = expected - actual

    if missing == 0:
        return f"""
🌟 *All bubbles sang in harmony —  
{student_name} marked each one with clarity.*  
✅ No responses missing. A complete scan!
"""
    elif missing <= 5:
        return f"""
✨ *A few bubbles wandered, some stayed shy —  
But {student_name}'s scan still reached the sky.*  
🕳️ Missing responses: {missing}
"""
    else:
        return f"""
🌧️ *Some bubbles slept, some skipped the dance —  
Let’s guide them gently for another chance.*  
🕳️ Missing responses: {missing}
"""

def recommend_badge(score, subject_scores):
    """
    Maps score to poetic badge themes.
    """
    if score >= 100:
        return "🌌 Constellation — mastery across subjects"
    elif score >= 75:
        return "🌊 Ripple — strong impact, growing reach"
    elif score >= 50:
        return "🌱 Seedling — emerging clarity, keep growing"
    else:
        return "🪞 Reflection — revisit, refine, rise again"

def display_badge(student_name, score, subject_scores):
    badge = recommend_badge(score, subject_scores)
    return f"""
🎖️ **Badge for {student_name}**  
Score: {score}  
Theme: {badge}
"""
