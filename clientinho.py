import socket
import threading

host = 'localhost'
port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def send_messages():
    """Função para enviar mensagens para o servidor."""
    while True:
        message = input("Digite a mensagem (ou 'exit' para sair): ")
        if message.lower() == 'exit':
            client.close()
            print("Desconectado do servidor.")
            break
        try:
            client.send(message.encode('utf-8'))
        except:
            print("Erro ao enviar mensagem. Encerrando...")
            break

def receive_messages():
    """Função para receber mensagens do servidor."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("Conexão com o servidor foi perdida.")
                break
            print(f"\nMensagem recebida: {message}")
        except:
            print("Erro ao receber mensagem. Encerrando...")
            break
    client.close()

send_thread = threading.Thread(target=send_messages)
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True

receive_thread.start()
send_thread.start()

send_thread.join()
