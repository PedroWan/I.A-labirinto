# I.A-labirinto
IA Simbólica para Resolução de Labirintos
# Sobre o Projeto

Este projeto implementa uma Inteligência Artificial simbólica capaz de resolver labirintos em uma matriz 10x10.
O objetivo é encontrar o caminho da posição inicial (1,1) até a final (10,10), desviando de obstáculos e gerenciando energia limitada.

A cada movimento:

O robô perde 1 ponto de energia.

Pode recuperar energia em posições especiais (Power-ups).

Caminhos inviáveis (energia ≤ 0) são descartados.

---------------------------------------------------------------------------------------------------------------------------------------

# Funcionalidades

Geração aleatória de labirintos com obstáculos (15 a 35).

Inclusão de pontos de energia:

5 posições que concedem +5 de energia

3 posições que concedem +10 de energia

Algoritmo de busca A* com heurística de distância euclidiana.

Visualização gráfica do labirinto, do caminho encontrado e dos power-ups.

Exibição de estatísticas finais:

Caminho percorrido

Energia restante

Power-ups coletados e evitados

---------------------------------------------------------------------------------------------------------------------------------------

# Tecnologias Utilizadas

Python 3

Bibliotecas:

random → geração aleatória de obstáculos e power-ups

math → cálculo da heurística (distância euclidiana)

matplotlib → visualização gráfica do labirinto e do caminho

---------------------------------------------------------------------------------------------------------------------------------------

# Conclusão

Este projeto demonstrou a aplicação da IA simbólica e algoritmos de busca em um problema clássico: a travessia de labirintos em ambientes parcialmente observáveis.
O uso do algoritmo A* com heurística de distância euclidiana mostrou-se eficaz na maioria dos cenários, conciliando a viabilidade do caminho com a limitação de energia do agente.
