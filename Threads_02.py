import threading
import time

# Variável compartilhada
continuar = True

def tarefa():
    """Simula uma tarefa executada em paralelo."""
    while continuar:
        print("Executando tarefa em background...")
        time.sleep(1)
    print("Tarefa encerrada.")

def esperar_resposta():
    """Espera o usuário escrever sim ou não."""
    global continuar
    resposta = input("Deseja continuar? (sim/não): ").strip().lower()

    if resposta == "n":
        print("Encerrando pela escolha do usuário...")
        continuar = False
    else:
        print("Continuando execução normalmente!")

# Criando as threads
thread_tarefa = threading.Thread(target=tarefa)
thread_input = threading.Thread(target=esperar_resposta)

# Iniciando as threads
thread_tarefa.start()
thread_input.start()

# Espera as threads terminarem
thread_tarefa.join()
thread_input.join()

print("Programa finalizado.")
