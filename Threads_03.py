import threading
import time

stop_event = threading.Event()

def tarefa(nome, intervalo):
    """Cada thread executa até o stop_event ser acionado."""
    while not stop_event.is_set():
        print(f"[{nome}] executando...")
        time.sleep(intervalo)
    print(f"[{nome}] finalizada.")

def esperar_resposta():
    """Fica perguntando continuamente até o usuário digitar 'sim'."""
    while not stop_event.is_set():
        resposta = input("Deseja parar as tarefas? (sim/não): ").strip().lower()

        if resposta == "Sim" or resposta == "sim" or resposta == "S" or resposta == "s":
            print("Encerrando todas as threads...")
            stop_event.set()
        elif resposta == "não" or resposta == "nao" or resposta == "n" or resposta == "N":
            print("Ok! As threads continuarão executando.")
            time.sleep(1)  # só pra não spammar o terminal
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.")
            time.sleep(0.5)

# --- Criar threads de tarefa ---
threads = [
    threading.Thread(target=tarefa, args=("Tarefa A", 1)),
    threading.Thread(target=tarefa, args=("Tarefa B", 1.5)),
    threading.Thread(target=tarefa, args=("Tarefa C", 2)),
]

# Thread que fica fazendo a pergunta até o final
thread_input = threading.Thread(target=esperar_resposta)

# Iniciar as threads
for t in threads:
    t.start()

thread_input.start()

# Esperar todas terminarem
for t in threads:
    t.join()

thread_input.join()

print("Programa encerrado!")
