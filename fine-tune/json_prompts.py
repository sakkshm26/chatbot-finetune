from concurrent.futures import ThreadPoolExecutor
import openai

openai.api_key = "YOUR_API_KEY"

def call_openai_api(chunk):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content": 'I have the following text transcript that in need to put in JSONL prompt-completion pair format for fune tuning. Example format, "{\\"prompt\\": \\"Who are you?\\", \\"completion\\": \\"I am Donald Trump, a businessman, republican and former president of United States of America.\\"}" Please generate 10 to 15 appropriate questions which reflects the personality of Donald Trump for the following text and place the questions and text in JSONL format. The \'completion\' should come verbatim from the text. You must use the \'you\' form for all prompt questions, never say "the speaker". You must utilize the entire text in the completion. Always answer the completion from the first person:',
            },
            {"role": "user", "content": f"Transcript: {chunk}."},
        ],
        max_tokens = 1500,
        n = 1,
        stop = None,
        temperature = 0.8,
    )
    # print(response)
    return response.choices[0]['message']['content'].strip()

def generate_prompts(tokens):
    file = open('transcripts.txt', 'r')
    transcripts = file.read()
    splitted_transcripts = transcripts.split()
    chunks = [' '.join(splitted_transcripts[i:i + tokens]) for i in range(0, len(splitted_transcripts), tokens)]

    response = call_openai_api(chunks[19])
    file = open(f'prompt_completion_pairs{19}.jsonl', 'w')
    file.write(response)
    file.close()

    response = call_openai_api(chunks[20])
    file = open(f'prompt_completion_pairs{20}.jsonl', 'w')
    file.write(response)
    file.close()

    # for index, chunk in enumerate(chunks[2:7]):
    #         response = call_openai_api(chunk)
    #         print(response)
    #         file = open(f'prompt_completion_pairs{index+2}.jsonl', 'w')
    #         file.write(response)
    #         file.close()

    with ThreadPoolExecutor(max_workers=5) as executor:
        # responses = list(executor.map(call_openai_api, chunks)) # this can cause api rate limit error 
        for index, chunk in enumerate(chunks[0:1]):
            responses = list(executor.map(call_openai_api, chunk))
            print(responses)
            file = open(f'prompt_completion_pairs{index}.jsonl', 'w')
            for response in responses:
                file.write(response + '\n')

generate_prompts(tokens=1200)

# model_name = "ft-p1y15vuU0mOnMS5XP4IZmkRG"