import os
# lê os arquivos diretório edcomp_tarefa1_out
current_path = os.path.dirname(__file__)
output_path = os.path.join(current_path, 'edcomp_tarefa1_out')

def pega_solucao(letra):
    h = ['0.1', '0.01', '0.001', '0.0001', '1e-05', '1e-06']
    solutions = ''
    for hhh in h:
        letter_template = f'{letra}_h_{hhh}'
        # abre o txt equivalente
        with open(os.path.join(output_path, f'{letter_template}.txt'), 'r') as file:
            # lê o conteúdo
            content = file.read()
            # add \resizebox{\textwidth}{!}{ before content
            content = '\\resizebox{\\textwidth}{!}{\n' + content + '}'
        solution_template = f'\includegraphics{{{letter_template}.png}}\n\\\\ \n\n{content}'
        solutions += solution_template + '\n\n'
    # save to sol/sol_a.txt
    with open(os.path.join(current_path, f'sol/sol_{letra}.txt'), 'w') as file:
        file.write(solutions)

letras = ['a', 'b', 'c', 'd', 'e']

for letra in letras:
    pega_solucao(letra)