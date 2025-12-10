import threading
import time
import random
import os

# Variáveis compartilhadas
evento_disparo = threading.Event()
fired_time = None  # será preenchido pelo thread que dispara
lock_time = threading.Lock()

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_disparo(min_delay=2, max_delay=6):
    """Thread que espera um tempo aleatório e então dispara o alvo."""
    global fired_time
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

    limpar()
    print("🎯🎯🎯   ALVO!!!   🎯🎯🎯")
    print("PRESSIONE ENTER AGORA!!!\n")

    with lock_time:
        fired_time = time.time()
    evento_disparo.set()

def main():
    global fired_time
    limpar()
    print("=== TESTE DE REFLEXO 3000 ===")
    print("Prepare-se...")
    print("Quando aparecer 'ALVO', pressione ENTER o mais rápido possível!")
    input("\nPressione ENTER para começar...")

    # 20% de chance de FALSO ALARME antes do real
    if random.random() < 0.2:
        limpar()
        print("🎭 FALSO ALARME!!!")
        print("Se apertou agora, será considerado 'antecipado'.")
        time.sleep(1.5)

    # inicia o thread que fará o disparo aleatório
    evento_disparo.clear()
    fired_time = None
    thread_disparo = threading.Thread(target=esperar_disparo, args=(2, 6))
    thread_disparo.daemon = True
    thread_disparo.start()

    # marca o instante em que começamos a esperar o ENTER do usuário
    press_start = time.time()
    input()  # espera o ENTER do usuário
    press_time = time.time()

    # analisando os casos
    if not evento_disparo.is_set():
        # usuário apertou antes do disparo real
        limpar()
        print("⚠️ VOCÊ ATIROU ANTES DO ALVO!!! (Prematuro)")
        print("Resultado: DESCLASSIFICADO — tente esperar o ALVO aparecer.")
    else:
        # cálculo seguro do tempo de reação
        with lock_time:
            if fired_time is None:
                # Caso improvável: disparo sinalizado mas tempo não registrado
                fired_time = press_start
        tempo_reacao = press_time - fired_time
        limpar()
        print("🎯 ALVO ACERTADO!")
        print(f"⏱ Seu tempo de reação foi: {tempo_reacao:.4f} segundos")

        # feedback divertido
        if tempo_reacao < 0.12:
            print("🚀 Reflexos de outro nível!")
        elif tempo_reacao < 0.25:
            print("😎 Excelente!")
        elif tempo_reacao < 0.45:
            print("🙂 Bom!")
        elif tempo_reacao < 0.8:
            print("😐 Pode melhorar.")
        else:
            print("🐢 Devagar demais — pratique!")

    print("\nObrigada por jogar! 🌟\n")

if __name__ == "__main__":
    main()
