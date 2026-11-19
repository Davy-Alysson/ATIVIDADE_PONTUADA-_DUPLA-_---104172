#Davy Alysson de Sousa Gomes
#Rayan dos Santos Ezequiel 

import os
import sys
import time

os.system('cls' if os.name == 'nt' else 'clear')

senha_acesso_certa = '123'

depositos = []
saques = []


def senha_acesso():
    for i in range(3):
        print('=== SENHA DE ACESSO ===')
        senha = input('Digite sua senha: ')

        if senha == senha_acesso_certa:
            print('ACESSO AUTORIZADO!')
            time.sleep(1)
            return True
        else:
            print('SENHA INCORRETA!\n')

    print('ACESSO BLOQUEADO.')
    return False


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=== BANCO COFRINHO · CAIXA ===')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver extrato')
    print('0 - Sair')


def mostrar_saldo(saldo):
    print(f'\nSaldo atual: R$ {saldo:.2f}')


def mostrar_extrato(saldo):
    print('\n=== EXTRATO BANCÁRIO ===')
    print(f'\nDepósitos realizados ({len(depositos)}):')
    if len(depositos) == 0:
        print('  Nenhum depósito.')
    else:
        for d in depositos:
            print(f'  + R$ {d:.2f}')
    print(f'\nSaques realizados ({len(saques)}):')
    if len(saques) == 0:
        print('  Nenhum saque.')
    else:
        for s in saques:
            print(f'  - R$ {s:.2f}')
    print(f'\nSaldo atual: R$ {saldo:.2f}')


def deposito(saldo):
    print('\n=== DEPÓSITO ===')
    try:
        valor = float(input('Quanto deseja depositar? R$ '))
    except ValueError:
        print('Valor inválido.')
        return saldo
    if valor <= 0:
        print('Operação recusada: valor inválido. O saldo não mudou.')
        return saldo

    saldo += valor
    depositos.append(valor)
    print(f'Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}')
    return saldo


def saque(saldo):
    print('\n=== SAQUE ===')
    try:
        valor = float(input('Quanto deseja sacar? R$ '))
    except ValueError:
        print('Valor inválido.')
        return saldo
    if valor <= 0:
        print('Operação recusada: valor inválido.')
        return saldo
    elif valor > 1000:
        print('Operação recusada: limite máximo de R$ 1000.00 por saque.')
        return saldo
    elif valor > saldo:
        print('Operação recusada: saldo insuficiente.')
        return saldo
    saldo -= valor
    saques.append(valor)
    print(f'Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}')
    return saldo


def pausar():
    input('\nPressione ENTER para voltar ao menu...')


def sair():
    print('Obrigado por usar o Banco Cofrinho!')
    time.sleep(1.5)
    sys.exit()

saldo = 500.00

if not senha_acesso():
    sys.exit()

while True:
    menu()
    try:
        escolher = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida.')
        time.sleep(1.5)
        continue
    match escolher:
        case 1:
            mostrar_saldo(saldo)
            pausar()
        case 2:
            saldo = deposito(saldo)
            pausar()
        case 3:
            saldo = saque(saldo)
            pausar()
        case 4:
            mostrar_extrato(saldo)
            pausar()
        case 0:
            sair()
        case _:
            print('Opção inválida')
            time.sleep(1.5)