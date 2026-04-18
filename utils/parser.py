def parse_response(text):
    summary_part, quiz_part = text.split("QUIZ:")

    summary = summary_part.replace("SUMMARY:", "").strip()

    questions = []
    blocks = quiz_part.strip().split("Q")[1:]

    for block in blocks:
        lines = block.strip().split("\n")
        q_text = lines[0].split("|")[1]

        options, answer = [], ""

        for line in lines[1:]:
            if line.startswith(("a)", "b)", "c)")):
                options.append(line)
            elif "ANS:" in line:
                answer = line.split(":")[1].strip()

        questions.append({
            "question": q_text,
            "options": options,
            "answer": answer
        })

    return summary, questions