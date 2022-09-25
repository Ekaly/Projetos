from vglobais import *
from time import sleep


def titulo():
    global databr
    a = 'AUTOESCOLA CESMAC'
    a2 = ('=' * 10 + a + '=' * 10)
    a3 = len(a2)
    a5 = ('=' * a3)
    mtitulo = f'{a5}\n{a2}\n{a5}'
    print(mtitulo)
    print(f'\n{databr}\n')


def tela_registro():
    global cadastro
    r = ''
    while r != 2:
        print('')
        r = input('Digite [1] para validar um novo candidato ou [2] para retornar ao menu. \nSua resposta: ')
        print('')
        if r.isnumeric() == True:
            r = int(r)
            if r == 1:
                ajuste = len('Digite o nome do candidato e sua data de nascimento:')
                ajuste = ajuste - (ajuste//2) - (len('[NOVA VALIDAÇÃO]') // 2)
                print('>' * ajuste, '[NOVA VALIDAÇÃO]', '<' * ajuste)
                print('Digite o nome do candidato e sua data de nascimento: \n')
                nome, nascimento = input('Nome: '), input('Ano de Nascimento [AAAA]: ')
                if nascimento.isnumeric() == True:
                    nascimento = int(nascimento)
                    idade = ano_atual - nascimento
                    candidato = nome, nascimento
                    cadastro.append(candidato)
                    if idade >= 18:
                        print('')
                        print(f'O candidato {nome} está aprovado para dar entrada em sua CNH, pois já atingiu a maioridade penal'
                              f' tendo {idade} anos de idade.')
                        sleep(2)
                    else:
                        print('')
                        print(f'Com a idade de {idade} anos, o candidato {nome} foi reprovado para a solicitação de CNH, pois ainda'
                              f' não atingiu a maioridade penal.')
                        sleep(2)
                else:
                    print('Valor digitado para nascimento é inválido! Tente novamente.')
            elif r == 2:
                print('Candidatos registrados nesta sessão: ')
                for i in cadastro:
                    print(cadastro.index(i)+1,i)
                print('')
                print('Retornando ao menu.')
                print('')
            if r != 1 and r != 2:
                print('Resposta inválida! Tente novamente.')
                sleep(2)
                break
        else:
            print('A opção digitada é inválida; tente novamente.\n')
            sleep(1.5)
            break


class Iniciar():
    def listagem(self):
        if len(cadastro) >= 1:
            print('')
            for i in cadastro:
                print(cadastro.index(i) + 1, i)
            input(f'\nPressione "Enter" para continuar.\n')
        else:
            input('\nAinda não há candidatos registrados nesta sessão.\n\nPressione "Enter" para continuar. \n')

    def exclusao(self):
        if len(cadastro) > 0:
            for i in cadastro:
                print(cadastro.index(i) + 1, 'º', i)
            print('')
            cadastropop = input('Escolha um registro a ser excluído digitando seu número correspondente: ')
            if cadastropop.isnumeric() == True:
                cadastropop = int(cadastropop) - 1
                if cadastropop > len(cadastro) or cadastropop < 0:
                    print('\nO número digitado não corresponde com os existentes no registro. Tente novamente.\n')
                else:
                    cadastro.pop(cadastropop)
                    print('\nLista atualizada:\n')
                    for i in cadastro:
                        print(cadastro.index(i) + 1, i)
                    input('Pressione "Enter" para continuar.')
            print('')
        else:
            input('\nAinda não há candidatos registrados nesta sessão.\n\nPressione "Enter" para continuar. \n')