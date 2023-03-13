import openai
from decouple import config

openai.api_key = config('OPENAI_SECRET_KEY')

def get_text():
    with open('bot.txt') as bot:
        contents = bot.read()
        return contents

def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(engine=engine,
                                        prompt=prompt,
                                        temperature=temp,
                                        max_tokens=tokens,
                                        top_p=top_p,
                                        frequency_penalty=freq_pen,
                                        presence_penalty=pres_pen,
                                        stop=stop)
    
    text = response['choices'][0]['text'].strip()
    return text

if __name__=='__main__':
    # prompt = 'write a lsit of famous american actors'
    while True:
        conversation = list()
        user_input = input('USER: ')
        conversation.append('USER: %s' %user_input)
        text_block = get_text().replace('<<BLOCK>>',"\n".join(conversation))
        prompt = text_block+"\nFLOYD: "
        
        response = gpt3_completion(prompt)
        print('FLOYD',response)