import threading
import time
import random
import os

PRATOS = {
    "Omelete": (5, 1),
    "Macarrão": (8, 2),
    "Sopa": (10, 2),
    "Hambúrguer": (7, 1)
}

def barra_progresso(valor, total):
    preenchido = int((valor / total) * 20)
    return "[" + "█" * preenchido + "▒" * (20 - preenchido) + f"] {valor}/{total}s"


# ==========================================================
#  FUNÇÃO PRINCIPAL DOS COZINHEIROS
# ==========================================================

def cozinheiro(nome, prato, estado, lock, fogo_evento,
               gas_evento, apagao_evento, briga_evento):
    tempo_total, variacao = PRATOS[prato]
    tempo = 0

    while tempo < tempo_total:
        # fogo = todo mundo morre e sai
        if fogo_evento.is_set():
            with lock:
                estado[nome] = "🔥 INCÊNDIO! PAROU!"
            return

        # apagão = trava geral
        while apagao_evento.is_set():
            with lock:
                estado[nome] = "⚡ Sem energia!"
            time.sleep(0.5)

        # gás acabou = cozinha para
        while not gas_evento.is_set():
            with lock:
                estado[nome] = "🛑 Sem gás!"
            time.sleep(0.5)

        # briga = todos congelam
        while briga_evento.is_set():
            with lock:
                estado[nome] = "🤼 Parado (briga!)"
            time.sleep(0.5)

        # preparo normal
        time.sleep(random.uniform(0.4, 1.0))
        tempo += random.randint(1, variacao + 1)
        tempo = min(tempo, tempo_total)

        # possível desastre: prato caiu
        if random.random() < 0.05:
            tempo = max(0, tempo - random.randint(2, 4))
            with lock:
                estado[nome] = "💥 Derrubou o prato!"
            time.sleep(1.2)

        with lock:
            estado[nome] = tempo

    with lock:
        estado[nome] = "PRONTO! 🎉"


# ==========================================================
#  EVENTOS DE BAGUNÇA
# ==========================================================

def chef_reclamando(fogo_evento, mensagens, lock):
    while not fogo_evento.is_set():
        time.sleep(random.uniform(2, 5))
        with lock:
            print("\n" + random.choice(mensagens) + "\n")


def incendio(fogo_evento, lock):
    time.sleep(random.randint(6, 15))
    if not fogo_evento.is_set():
        with lock:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n🔥🔥🔥 A COZINHA PEGOU FOGO!!! 🔥🔥🔥\n")
        fogo_evento.set()


def acabar_gas(gas_evento, lock):
    time.sleep(random.randint(5, 12))
    with lock:
        print("\n🛑 O gás acabou!! Esperando reposição...\n")
    gas_evento.clear()
    time.sleep(random.randint(3, 7))
    with lock:
        print("\n💨 Gás voltou! Continuem!\n")
    gas_evento.set()


def apagao(apagao_evento, lock):
    time.sleep(random.randint(10, 20))
    with lock:
        print("\n⚡ APAGÃO! Tudo parou!\n")
    apagao_evento.set()
    time.sleep(random.randint(3, 6))
    with lock:
        print("\n💡 Energia voltou!\n")
    apagao_evento.clear()


def briga(briga_evento, lock):
    time.sleep(random.randint(8, 18))
    with lock:
        print("\n🤼 Dois cozinheiros começaram a brigar!\n")
    briga_evento.set()
    time.sleep(random.randint(2, 5))
    with lock:
        print("\n🤝 Briga resolvida. Voltem ao trabalho!\n")
    briga_evento.clear()


# ==========================================================
#  IMPRESSÃO CONTÍNUA DO ESTADO
# ==========================================================

def imprimir_estado(estado, pratos):
    os.system("cls" if os.name == "nt" else "clear")
    print("🍳 COZINHA INFERNAL — ACOMPANHAMENTO DOS PRATOS 🍳\n")
    for cozinheiro, progresso in estado.items():
        prato = pratos[cozinheiro]
        if isinstance(progresso, str):
            status = progresso
        else:
            total = PRATOS[prato][0]
            status = barra_progresso(progresso, total)
        print(f"{cozinheiro:<12} ({prato:<12}) {status}")
    print()


# ==========================================================
#  MAIN
# ==========================================================

def main():
    pratos_alocados = {nome: nome for nome in PRATOS}
    estado = {nome: 0 for nome in PRATOS}

    lock = threading.Lock()

    # eventos de controle
    fogo_evento = threading.Event()     # mata tudo
    gas_evento = threading.Event()      # se desligar, pausa tudo
    apagao_evento = threading.Event()   # pausa total
    briga_evento = threading.Event()    # pausa geral

    gas_evento.set()  # começa com gás ON

    mensagens_chef = [
        "👨‍🍳 CHEFE: Quem queimou o alho de novo?!",
        "👨‍🍳 CHEFE: Isso é uma cozinha ou um circo?!",
        "👨‍🍳 CHEFE: SE APRESSEM, OS CLIENTES ESTÃO ESPERANDO!",
        "👨‍🍳 CHEFE: Se esse omelete demorar mais 1 minuto eu desisto!",
        "👨‍🍳 CHEFE: QUEM DEIXOU A PANELA SEM VIGIA?!",
        "👨‍🍳 CHEFE: EU NÃO AGUENTO MAIS ESSA COZINHA!!!"
    ]

    threads = []

    # cozinheiros
    for nome in PRATOS:
        t = threading.Thread(target=cozinheiro,
            args=(nome, nome, estado, lock, fogo_evento,
                  gas_evento, apagao_evento, briga_evento))
        t.daemon = True
        t.start()
        threads.append(t)

    # eventos caóticos
    threading.Thread(target=chef_reclamando, args=(fogo_evento, mensagens_chef, lock), daemon=True).start()
    threading.Thread(target=incendio, args=(fogo_evento, lock), daemon=True).start()
    threading.Thread(target=acabar_gas, args=(gas_evento, lock), daemon=True).start()
    threading.Thread(target=apagao, args=(apagao_evento, lock), daemon=True).start()
    threading.Thread(target=briga, args=(briga_evento, lock), daemon=True).start()

    # loop principal
    try:
        while any(t.is_alive() for t in threads) and not fogo_evento.is_set():
            imprimir_estado(estado, pratos_alocados)
            time.sleep(0.4)
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
        fogo_evento.set()

    imprimir_estado(estado, pratos_alocados)

    if fogo_evento.is_set():
        print("🚨 EMERGÊNCIA: Cozinha evacuada! Tudo perdido! 🚨")
    else:
        print("🥳 Todos os pratos prontos! Milagre na cozinha infernal!")

    print("\nFim do expediente.\n")


if __name__ == "__main__":
    main()
