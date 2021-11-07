import requests

file = open('C:\\Riot Games\\League of Legends\\lockfile')

LocalClientData = 0

for line in file:
    LocalClientData = line.split(":")

LOCAL_PORT = LocalClientData[2]
LOCAL_KEY = LocalClientData[3]

file.close()

print(LOCAL_PORT)
print(LOCAL_KEY)

request = requests.get('https://127.0.0.1:53019/lol-summoner/v1/current-summoner', auth=('riot', LOCAL_KEY), verify=False)


print(request.json())

