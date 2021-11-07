file = open('C:\\Riot Games\\League of Legends\\lockfile')

LocalClientData = 0

for line in file:
    LocalClientData = line.split(":")

LOCAL_PORT = LocalClientData[2]
LOCAL_KEY = LocalClientData[3]

file.close()

print(LOCAL_PORT)
print(LOCAL_KEY)
