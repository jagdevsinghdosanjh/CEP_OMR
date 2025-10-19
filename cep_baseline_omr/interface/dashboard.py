import pandas as pd
import streamlit as st

def display_class_dashboard(results):
    """
    Displays a class-wide dashboard of student scores and breakdowns.
    `results` is a list of dictionaries with keys: Name, Roll No, Score, subject_scores
    """
    st.markdown("## 🏫 School-Wide Dashboard")

    # Summary Table
    df = pd.DataFrame(results)
    st.dataframe(df[["Name", "Roll No", "Score"]], use_container_width=True)

    # Subject-Wise Aggregates
    st.markdown("### 📊 Subject-Wise Averages")
    subject_totals = {}
    subject_counts = {}

    for result in results:
        for subject, score in result["subject_scores"].items():
            subject_totals[subject] = subject_totals.get(subject, 0) + score
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    subject_averages = {
        subject: round(subject_totals[subject] / subject_counts[subject], 2)
        for subject in subject_totals
    }

    for subject, avg in subject_averages.items():
        st.write(f"• {subject}: {avg} average score")

def export_summary(results, output_path="class_summary.xlsx"):
    """
    Exports class summary to Excel.
    """
    df = pd.DataFrame(results)
    df.to_excel(output_path, index=False)
    print(f"📤 Exported class summary to {output_path}")
