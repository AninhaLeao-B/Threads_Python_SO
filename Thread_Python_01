import threading
import time

# Função que cada thread vai executar
def tarefa(nome, tempo):
    print(f"Iniciando {nome}...")
    time.sleep(tempo)              # simula uma operação demorada de I/O
    print(f"{nome} finalizada!")

# Criando duas threads
t1 = threading.Thread(target=tarefa, args=("Tarefa 1", 3))
t2 = threading.Thread(target=tarefa, args=("Tarefa 2", 5))

# Iniciando as threads
t1.start()
t2.start()

# Esperando as duas terminarem
t1.join()
t2.join()

print("Todas as tarefas foram concluídas!")
