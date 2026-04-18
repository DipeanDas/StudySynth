import streamlit as st
import re


def render_quiz(questions):
    st.subheader("Quiz")

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    with st.form("quiz_form"):
        user_answers = []

        for i, q in enumerate(questions):
            st.write(f"**Q{i+1}. {q['question']}**")

            choice = st.radio(
                f"Select answer for Q{i+1}",
                q["options"],
                key=f"q_{i}"
            )

            user_answers.append(choice)

        submit = st.form_submit_button("Submit Quiz")

    # Process ONLY after clicking submit
    if submit:
        st.session_state.quiz_submitted = True
        st.session_state.user_answers = user_answers

    # Show results AFTER submit
    if st.session_state.quiz_submitted:
        score = 0

        st.divider()
        st.subheader("Results")

        for i, q in enumerate(questions):
            user_ans = st.session_state.user_answers[i]

            # 🔧 Normalize correct answer (handles a, A, a), etc.)
            correct_letter = re.sub(r"[^a-zA-Z]", "", q["answer"]).lower()

            # 🔧 Extract option letter safely
            def get_option_letter(option):
                return option.strip()[0].lower()

            correct_option = next(
                (opt for opt in q["options"] if get_option_letter(opt) == correct_letter),
                None
            )

            if user_ans == correct_option:
                score += 1
                st.success(f"Q{i+1}: Correct")
            else:
                st.error(f"Q{i+1}: Wrong")
                if correct_option:
                    st.write(f"Correct Answer: **{correct_option}**")
                else:
                    st.write("Correct Answer: Not detected (format issue)")

        st.divider()
        st.success(f"Final Score: {score}/{len(questions)}")