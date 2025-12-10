import threading
import time
import random
import os

# Representa 5 pontos da cozinha
# 0 = seguro
# 1 = fumaça
# 2 = fogo pequeno
# 3 = incêndio grande (quase perdido!)
cozinha = [0, 0, 0, 0, 0]

# Controle sincronizado
lock = threading.Lock()

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def imprimir():
    limpar()
    print("🔥 COZINHA CAÓTICA — MONITORAMENTO 🔥\n")
    nomes = ["Fogão", "Pia", "Balcão", "Despensa", "Chaminé"]

    simbolos = {
        0: "✔ Seguro",
        1: "💨 Fumaça",
        2: "🔥 Fogo pequeno",
        3: "🔥🔥 INCÊNDIO!!!"
    }

    for i, nivel in enumerate(cozinha):
        print(f"{nomes[i]:<10} → {simbolos[nivel]}")
    print("\n(Pressione CTRL+C para sair)\n")

def sabotador():
    """Causa problemas constantemente."""
    while True:
        time.sleep(random.uniform(0.5, 2))
        with lock:
            idx = random.randint(0, 4)
            if cozinha[idx] < 3:
                cozinha[idx] += 1
                print(f"\n😈 SABOTADOR: aumentou problema em {idx}!\n")
            else:
                print("\n😈 SABOTADOR: riu vendo o fogo crescer!\n")

def bombeiro():
    """Tenta apagar os incêndios e controlar os danos."""
    while True:
        time.sleep(random.uniform(0.7, 2.5))
        with lock:
            idx = random.randint(0, 4)
            if cozinha[idx] > 0:
                cozinha[idx] -= 1
                print(f"\n👨‍🚒 BOMBEIRO: reduziu fogo em {idx}.\n")
            else:
                print("\n👨‍🚒 BOMBEIRO: verificou e estava tudo ok.\n")

def monitor():
    """Atualiza a tela sempre."""
    while True:
        imprimir()
        time.sleep(0.4)

def main():
    print("Iniciando simulação da cozinha caótica...\n")

    t1 = threading.Thread(target=sabotador, daemon=True)
    t2 = threading.Thread(target=bombeiro, daemon=True)
    t3 = threading.Thread(target=monitor, daemon=True)

    t1.start()
    t2.start()
    t3.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando simulação...")

if __name__ == "__main__":
    main()
