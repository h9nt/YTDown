import requests
from random import randint
from time import sleep

link = input("\n Enter link >>> ")

url = "https://flvto.pro/convert"

payload = {
    "video": link,
    "formats": "MP3",
    "convert": "Convert"
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "flvto.pro",
    "Origin": "https://flvto.pro",
    "Referer": "https://flvto.pro/de1/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

request = requests.post(url, headers=headers, data=payload)

url = "https://alpha.matevid.com/api/json"

payload = {
    "ftype": "mp3",
    "url": link
}

headers = {
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "alpha.matevid.com",
    "Origin": "https://flvto.pro",
    "Referer": "https://flvto.pro/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.post(url, headers=headers, json=payload).json()

hash14 = response['tasks'][0]['hash']
print(hash14)

url = "https://alpha.matevid.com/api/json"

payload = {
    "hash": hash14
}

headers = {
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "alpha.matevid.com",
    "Origin": "https://flvto.pro",
    "Referer": "https://flvto.pro/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.post(url, headers=headers, json=payload).json()

taskId = response['taskId']

url = "https://alpha.matevid.com/api/json/task"

payload = {
    "taskId": taskId
}

headers = {
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "alpha.matevid.com",
    "Origin": "https://flvto.pro",
    "Referer": "https://flvto.pro/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.post(url, headers=headers, json=payload)

try:
    while response.json()['download_progress'] <= 100 and not response.json()['status'] == "finished":
        print("Converting..")
        sleep(1)
        if response.json()['download'] and response.json()['download_progress'] == 100:
            try:
                with open(response.json()['title'], 'wb') as file:
                    down = requests.get(response.json()['download'])
                    file.write(down.content)
                print("Saved Video!")
            except FileNotFoundError as e:
                print(str(e))
        else:
            break
except Exception as e:
    print(str(e))
