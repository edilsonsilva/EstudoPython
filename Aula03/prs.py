import subprocess

def get_wifi_networks():
    # Executa o comando 'netsh wlan show profile' no prompt de comando
    process = subprocess.run(["netsh", "wlan", "show", "profile"], capture_output=True, text=True)

    # Obtém a saída do comando
    output = process.stdout

    # Separa cada linha da saída
    lines = output.split("\n")

    # Cria uma lista de redes wifi
    networks = []

    # Itera sobre cada linha da saída
    for line in lines:
        # Remove os espaços em branco da linha
        line = line.strip()

        # Se a linha não estiver vazia
        if line:
            # Encontra a posição da senha na linha
            index = line.find(":")

            # Obtém a senha da linha
            network = line[:index]
            password = line[index + 1:]

            # Adiciona a rede à lista
            networks.append((network, password))

    return networks


if __name__ == "__main__":
    # Obtém as redes wifi disponíveis
    networks = get_wifi_networks()

    # Exibe as redes wifi
    for network, password in networks:
        print("Rede:", network)
        print("Senha:", password)