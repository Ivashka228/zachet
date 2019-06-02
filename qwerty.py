import requests, json

domain = 'kinopoisk'
count = 10
token = '2713db032713db032713db039e27793307227132713db037be042163e422bf1f7564190'

url = "https://api.vk.com/method/wall.get?domain={}&count={}&access_token={}&v=5.74".format(domain, count, token)

response = requests.get(url)
answer = json.loads(response.text)
print(answer)
print(answer['response']['items'][1]['likes'])




for post in answer['response']['items']:
    print(post['text'] + '\n')
    print('лайки:', post['likes']['count'])
    print('коментарии:', post['comments']['count'])