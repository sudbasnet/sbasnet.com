import re


def parse_yarn(jfile):
    conversation = {}
    for conv in jfile:
        body = conv["body"].split("\n")
        strings = [b.strip() for b in body if len(b) > 0 and b[0] != "["]
        q_text = [re.sub(r"[\[\]]", "", b).strip() for b in body
                  if len(b) >= 4 and b[:2] == "[[" and b[-2:] == "]]"]
        print()
        questions = []
        for i in range(len(q_text)):
            questions.append(
                {"id": i + 1,
                 "question": q_text[i].split("|")[0].strip(),
                 "goto": q_text[i].split("|")[1].strip()}
            )
            conversation[conv["title"]] = {
                "tags": "", "strings": strings, "questions": questions
            }
    return conversation
