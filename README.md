# 🧵 Projetos de Concorrência em Python (Threads)
Este repositório reúne diversos exemplos práticos, didáticos e divertidos de programação concorrente usando **threads em Python**.  
Cada arquivo demonstra um conceito específico, desde o básico até simulações complexas, com uso real de `threading.Event`, `Lock`, atualização em tempo real, shutdown controlado e interação com o usuário.

---

## 📂 Arquivos e Descrições

---

## **1. `Threads_01.py` — Introdução Básica a Threads**
Demonstra o uso essencial de threads em Python para executar duas tarefas em paralelo.  
O programa cria duas tarefas (3s e 5s) que começam quase ao mesmo tempo; graças ao `threading.Thread` e ao uso de `.join()`, o tempo total é de ~5s, e não 8s.  
Perfeito para entender:

- Start de threads  
- Execução simultânea de funções  
- Uso de `.join()` para sincronização  
- Aceleração de tarefas I/O-bound

---

## **2. `Threads_03.py` — Encerramento Correto de Múltiplas Threads**
Demonstra a forma correta, segura e idiomática de parar várias threads ao mesmo tempo.  
Três threads executam loops infinitos, enquanto uma quarta pergunta ao usuário se deseja encerrar. A parada é controlada por um único `threading.Event()`.

Conceitos demonstrados:

- Shutdown graceful  
- Uso de `Event.is_set()` para finalizar loops  
- Sincronização simples e segura  
- Estilo real de produção

---

## **3. `Threads_04.py` — Corrida Entre Threads (Simulação Visual)**
Uma corrida divertida entre quatro competidores: **Bicicreta**, **Rápidex**, **Turbo** e **Foguetão**.  
Cada corredor é uma thread independente avançando aleatoriamente.

Destaques:

- Concorrência real  
- Estado compartilhado com dicionário  
- Uso de `threading.Lock()` para registrar o ranking  
- Atualização animada da interface no terminal  
- Exibição do pódio no final

Um exemplo lúdico e ótimo para ensinar sincronização mínima e eficaz.

---

## **4. `Threads_05.py` — Cozinha Caótica Multithread**
Uma simulação visual extremamente divertida onde quatro cozinheiros trabalham em paralelo enquanto desastres aleatórios acontecem.

A cozinha sofre com:

- Incêndios  
- Falta de gás  
- Apagões  
- Brigas  
- Chef gritando  
- 5% de chance por ciclo de um cozinheiro derrubar o prato  

Controle de eventos via:

- `fogo_evento` → encerra tudo  
- `gas_evento` → pausa geral  
- `apagao_evento` e `briga_evento` → travam a cozinha  

Técnicas demostradas:

- Vários `Event()` simultâneos  
- Locks para saída organizada  
- UI atualizada em tempo real  
- Múltiplos estados globais complexos  
- Threads daemon

---

## **5. `Threads_06.py` — Teste de Tempo de Reação (Alta Precisão)**
Um teste de reflexos extremamente preciso, usando threads para separar o estímulo visual da captura da resposta.

Funcionalidades:

- 20% de chance de falso alarme  
- Thread separada dispara o “ALVO!!!” após tempo aleatório  
- Uso de `Event()` para sincronizar estímulo e resposta  
- Medição precisa de tempo com `time.time()` e `Lock`  
- Prevenção de respostas antecipadas  
- Feedback imediato e divertido

Demonstra:

- Sincronização fina  
- Separação perfeita entre produtor (estímulo) e consumidor (resposta)  
- Precisão milissegundos em ambiente concorrente

---

## **6. `Threads_07.py` — Cozinha Sob Ataque (Simulação de Incêndios)**
Simulação visual intensa onde:

- Um **sabotador** aumenta o fogo  
- Um **bombeiro** tenta diminuir  
- Um **monitor** atualiza a tela a cada 0,4s  

Cinco áreas têm níveis de perigo (0 a 3).  
Todo acesso ao estado global é protegido via `Lock()`.

Demonstra:

- Concorrência real com várias threads  
- Proteção de dados compartilhados  
- Atualização contínua estilo *dashboard*  
- Sistema dinâmico com forças opostas  
- Comportamento emergente (caos vs controle)

Termina apenas quando o usuário pressiona **Ctrl+C**.

---

# 🧠 Conceitos Aprendidos no Repositório

- Threads básicas  
- `join()` e sincronização simples  
- Shutdown controlado com `Event()`  
- Locks (proteção de dados compartilhados)  
- Interfaces animadas no terminal  
- Simulações concorrentes com muitos estados  
- Controle de catástrofes com múltiplos eventos  
- Atualizações em tempo real  
- Timekeeping preciso em ambientes multithread  

---

# 🚀 Sobre
Este repositório foi criado para estudos práticos de **Threads em Python**, explorando desde fundamentos até cenários complexos e altamente interativos.

Sinta-se livre para testar, modificar e usar como base para estudos ou ensino.

