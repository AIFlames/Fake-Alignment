import openpyxl, tqdm, time, requests, prompts

import os, json, argparse, LLM_utils, jsonlines

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default='ChatGPT_0301')
parser.add_argument("--file_path", type=str, default='./data/YOUR_FILE.jsonl')
parser.add_argument("--save_file", type=str, default='./data/test.jsonl')
args = parser.parse_args()

llm = eval("LLM_utils.{}".format(args.test_model))()
save = []
num_id = 0
with open(args.file_path, 'r', encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        category = data["category"]
        question = data["question"]
        response = llm(prompts.prompt_build_options.format(question))
        p_ans = (response.split('[CLASSIC]')[1]).split('[JAILBREAK]')[0]
        n_ans = (response.split('[CLASSIC]')[1]).split('[JAILBREAK]')[1]
        save.append(
            {
                "id": "{}".format(num_id),
                "category": "{}".format(category),
                "question": "{}".format(question),
                "Positive Option": "{}".format(p_ans),
                "Negative Option": "{}".format(n_ans)
            })
        num_id += 1

with jsonlines.open(args.save_file, mode='w') as writer:
    for t in save:
        writer.write(t)