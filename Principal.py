from modulos import *


def principal():
    global cadastro
    titulo()
    while True:
        resp = input('Digite o número correspondente à opção desejada:\n'
                 '[1] Validar um novo candidato\n'
                 '[2] Consultar a lista de candidatos registrados nesta sessão\n'
                 '[3] Excluir um candidato\n'
                 '[4] Sair do programa\n'
                 '\n'
                 'Digite sua opção: ')
        if resp == '1':
            tela_registro()
        if resp == '2':
            Iniciar().listagem()
        if resp == '3':
            Iniciar().exclusao()
        if resp == '4':
            print('\nEncerrando o programa.')
            sleep(1.5)
            break
        if resp < '1' or resp > '4':
            print('\nA opção digitada não é válida. Tente novamente.\n')
            sleep(1.5)


principal()
