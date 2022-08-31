import urllib.request
print('\033[31m'+'MinecraftServerAutoConstruction by RuskLabo Running'+'\033[0m')
url='https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/135/downloads/paper-1.19.2-135.jar'
save_name='server.jar'
urllib.request.urlretrieve(url, save_name)

f = open('start(Windows).bat', 'w', encoding='utf-8', newline='\n')
f.write('java -Xmx2G -jar server.jar nogui\n')
f.write('pause\n')
f.close()

f = open('start(Mac,Linux).sh', 'w', encoding='utf-8', newline='\n')
f.write('#!/usr/bin/env bash\n')
f.write('java -Xmx2G -jar server.jar nogui\n')
f.close()

f = open('eula.txt', 'w', encoding='utf-8', newline='\n')
f.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n')
f.write('#2022\n')
f.write('eula=true\n')
f.close()