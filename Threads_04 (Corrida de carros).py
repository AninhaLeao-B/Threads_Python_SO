import threading
import random
import time
import os

DISTANCIA = 30  # tamanho da barra de progresso

def barra_progresso(valor, total):
    percentual = valor / total
    preenchido = int(percentual * total)
    vazio = total - preenchido
    return f"[{'█' * preenchido}{'▒' * vazio}] {valor}/{total}"

def corredor(nome, estado, ranking, lock):
    distancia = 0

    while distancia < DISTANCIA:
        distancia += random.randint(1, 3)
        distancia = min(distancia, DISTANCIA)

        estado[nome] = distancia
        time.sleep(random.uniform(0.1, 0.3))

    # Quando chegar ao final, registra a posição no ranking
    with lock:
        ranking.append(nome)

def imprimir_estado(estado):
    os.system("cls" if os.name == "nt" else "clear")

    print("🏁 CORRIDA DE THREADS 🏁\n")
    for nome, dist in estado.items():
        print(f"{nome:<10} {barra_progresso(dist, DISTANCIA)}")
    print()

def main():
    corredores = ["Carlo", "Rápidex", "Turbo", "Foguetão"]
    estado = {nome: 0 for nome in corredores}

    ranking = []         # ordem de chegada
    lock = threading.Lock()

    threads = []

    for nome in corredores:
        t = threading.Thread(target=corredor,
                             args=(nome, estado, ranking, lock))
        threads.append(t)
        t.start()

    # Atualiza a tela enquanto a corrida acontece
    while any(t.is_alive() for t in threads):
        imprimir_estado(estado)
        time.sleep(0.1)

    imprimir_estado(estado)

    # Finalização
    print("🏆 Corrida finalizada!")
    print("\nRANKING FINAL:\n")

    for pos, nome in enumerate(ranking, start=1):
        medalha = {1:"🥇", 2:"🥈", 3:"🥉"}.get(pos, "🏅")
        print(f"{pos}º lugar: {nome} {medalha}")

    print()

if __name__ == "__main__":
    main()



"""Criação de múltiplas threads
Execução concorrente (as mensagens saem embaralhadas)
Uso de threading.Thread
Uso de join() pra esperar todas finalizarem
Não depende de CPU — é 100% I/O bound (impressões + sleeps)
Comportamento não determinístico (cada corrida é diferente)
Esse tipo de exemplo deixa SUPER claro como threads funcionam."""