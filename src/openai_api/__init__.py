#!/usr/bin/env python3
"""
Script para testar os diferentes sons do piezo buzzer
"""

import RPi.GPIO as GPIO
import time

# Configuração dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definição do pino do buzzer
PINO_BUZZER = 18  # Buzzer no pino GPIO 18

# Configurar pino como saída
GPIO.setup(PINO_BUZZER, GPIO.OUT)

# Configuração do PWM para o buzzer
buzzer = GPIO.PWM(PINO_BUZZER, 440)  # Inicializa em 440 Hz

def tocar_nota(frequencia, duracao, pausa=0.1):
    """Toca uma nota no buzzer."""
    buzzer.start(50)  # 50% duty cycle
    buzzer.ChangeFrequency(frequencia)
    time.sleep(duracao)
    buzzer.stop()
    time.sleep(pausa)

def som_acesso_autorizado():
    """Som para acesso autorizado - Duas notas ascendentes."""
    print("Tocando: Som de acesso autorizado")
    tocar_nota(880, 0.2, 0)  # Nota A5
    tocar_nota(1760, 0.2)    # Nota A6

def som_acesso_negado():
    """Som para acesso negado - Duas notas descendentes graves."""
    print("Tocando: Som de acesso negado")
    tocar_nota(220, 0.5, 0)  # Nota A3 (mais grave)
    tocar_nota(110, 0.5)     # Nota A2 (ainda mais grave)

def som_invasao():
    """Som para invasão - Alarme com frequência variável."""
    print("Tocando: Som de alarme de invasão")
    buzzer.start(50)
    # Som de alarme com frequência variável
    for i in range(3):  # Repetir 3 vezes
        for freq in range(880, 1760, 100):
            buzzer.ChangeFrequency(freq)
            time.sleep(0.05)
        for freq in range(1760, 880, -100):
            buzzer.ChangeFrequency(freq)
            time.sleep(0.05)
    buzzer.stop()
    time.sleep(0.5)

def som_melodia_teste():
    """Melodia para testar o funcionamento do buzzer."""
    print("Tocando: Melodia de teste")
    # Notas da escala C maior
    notas = [262, 294, 330, 349, 392, 440, 494, 523]
    # Tocar escala ascendente
    for nota in notas:
        tocar_nota(nota, 0.2, 0.05)
    # Tocar escala descendente
    for nota in reversed(notas):
        tocar_nota(nota, 0.2, 0.05)

def main():
    """Função principal que testa todos os sons."""
    try:
        print("Teste dos sons do piezo buzzer")
        print("------------------------------")
        
        while True:
            print("\nEscolha um tipo de som para testar:")
            print("1. Som de acesso autorizado")
            print("2. Som de acesso negado")
            print("3. Som de alarme de invasão")
            print("4. Melodia de teste")
            print("0. Sair")
            
            opcao = input("Digite sua escolha (0-4): ")
            
            if opcao == "1":
                som_acesso_autorizado()
            elif opcao == "2":
                som_acesso_negado()
            elif opcao == "3":
                som_invasao()
            elif opcao == "4":
                som_melodia_teste()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    except KeyboardInterrupt:
        print("\nTeste interrompido pelo usuário.")
    finally:
        # Limpar configurações GPIO
        GPIO.cleanup()
        print("Teste finalizado.")

if __name__ == "__main__":
    main()