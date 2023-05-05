import json

CHAT_GPT_LOG_FILE = "./chat_gpt.log"
IN_STR = "\n\n=== INPUT ================================================\n\n"
OUT_STR = "\n\n=== OUTPUT ===============================================\n\n"


def append_gpt_input(message):
    with open(CHAT_GPT_LOG_FILE, "a") as f:
        f.write(IN_STR)
        f.write(json.dumps(message, indent=2))


def append_gpt_output(message):
    with open(CHAT_GPT_LOG_FILE, "a") as f:
        f.write(OUT_STR)
        f.write(json.dumps(message, indent=2))
