from flask import Flask
from flask import render_template
from flask import request
import requests
import random
import json


app = Flask(__name__)
ipp = "127.0.0.1"

domain = ['bezumas', 'fckbrain', 'prukl', 'amfet1', 'memeque']
count = 100
token = '2713db032713db032713db039e27793307227132713db037be042163e422bf1f7564190'

def poisk(gtt, greeting):
    sppisok = []
    sch = []
    if gtt == 'pr':
        for i in domain:
            url = "https://api.vk.com/method/wall.search?owners_only=1&query={}&domain={}&count={}&access_token={}&v=5.74".format(greeting, i, count, token)

            response = requests.get(url)
            answer = json.loads(response.text)
            print(answer)
#            print(answer['response']['items'][1]['likes'])

            for post in answer['response']['items']:
#                print(post['post_type'])
                if post['post_type'] == 'post':
                    originalUrl = 'https://vk.com/wall' + str(post['owner_id']) + '_' + str(post['id'])
                    sppisok.append({'text':post['text'], 'likes':post['likes']['count'], 'pablik':i, 'post':originalUrl})
                    print(post['text'] + '\n')
#            print(sppisok)
    if gtt == 'rh':
        for i in domain:
            if ' ' in greeting:
                greeting = greeting.replace(',', '')
                greeting = greeting.split(' ')
#                print("KFGV", greeting)
            for p in greeting:
                url = "https://api.vk.com/method/wall.search?owners_only=1&query={}&domain={}&count={}&access_token={}&v=5.74".format(p, i, count, token)

                response = requests.get(url)
                answer = json.loads(response.text)
#                print(answer)
                #            print(answer['response']['items'][1]['likes'])

                for post in answer['response']['items']:
#                   print("KFGV", greeting)
#                   print(post['post_type'])
                    if post['post_type'] == 'post':
                        originalUrl = 'https://vk.com/wall' + str(post['owner_id']) + '_' + str(post['id'])
                        sppisok.append({'text': post['text'], 'likes': post['likes']['count'], 'pablik': i, 'post':originalUrl})
#                        print(post['text'] + '\n')
#                print(sppisok)
    sppisok = sorted(sppisok, key=lambda k: k['likes'], reverse=True)
    return(sppisok)

@app.route('/')
def index():
    gtt = ''
    greeting = ''
    if "ress" in request.args:
        greeting = request.args['ress']
    if "get" in request.args:
        gtt = request.args['get']
    if gtt == "rh":
        resultt = poisk(gtt, greeting)
    elif gtt == "pr":
        resultt = poisk(gtt, greeting)
    else:
        resultt = ''
    return render_template('index.html', result=resultt)

app.run(debug=True, port=8080)