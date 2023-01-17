import os
import openai
def chat_gpt(text_input):
    openai.api_key = "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"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=text_input,
      temperature=0.3,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return(response['choices'][0]['text'])

def html_str(txt):
    txt = txt.replace('\n', '')
    txt = txt.replace('.jpg','')
    return(txt)

from googletrans import Translator
def Bengali_translator(sentence):
    translator = Translator()
    return(translator.translate(sentence).text)

from googletrans import Translator
def Bengali_output(sentence):
    translator = Translator()
    return(translator.translate(sentence, dest='bn').text)

import urllib.request, json 
import requests
dfl=[0,0,0]
link = "https://api.telegram.org/bot[Token]]/"
while True:
    with urllib.request.urlopen(link + "getUpdates") as url:
        data = json.loads(url.read().decode())
        l = len(data['result'])
        dfl.append(l)
        #print(dfl)
        if dfl[-1]>dfl[-2]:
            recive_smg = Bengali_translator(data['result'][-1]['message']['text'])
            recive_id = data['result'][-1]['message']['from']['id']
            #print('text :'+recive_smg+' id :'+str(recive_id))
            if 'hello' in recive_smg:
                requests.get(link + "sendMessage?chat_id="+ str(recive_id) + "&text=how can i help you?")
            elif recive_smg == 'stop':
                break
            else:
                print("get")
                gpt_txt = chat_gpt(recive_smg)
                f_gpt_txt = html_str(gpt_txt)
                #f_text = Bengali_output(f_gpt_txt)
                requests.get(link + "sendMessage?chat_id="+ str(recive_id) + "&text="+f_gpt_txt)
                print("sent")