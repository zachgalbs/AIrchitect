import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)