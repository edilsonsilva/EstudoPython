# import subprocess

# data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8')
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#         results = subprocess.check_output(['netsh','wlan','show','profile',i,"key"])
#         results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#         try:
#                 print("{:<30}| {:<}".format(i, results[0]))
#         except IndexError:
#                 print("{:<30}| {:<}".format(i,""))
# input("")

import subprocess

try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')
    profiles = [i.split(":")[1][1:-1] for i in data.split('\n') if "All User Profile" in i]
    
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            print("{:<30}| {:<}".format(i, results[0]))
        except (IndexError, subprocess.CalledProcessError):
            print("{:<30}| {:<}".format(i, "Senha não encontrada ou erro ao acessar"))
except subprocess.CalledProcessError:
    print("Erro ao executar o comando netsh")

input("Pressione Enter para sair...")