[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/F62_0SL3)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10907776&assignment_repo_type=AssignmentRepo)
# 


# **Desolation**
## Introdução
Este é um jogo desenvolvido por Luige Orlandi Quinze e Gustavo Ribolla, alunos de CComp do Insper
com o auxilio momentanêo de outros colegas, como Matheus, Sarti, Ian e outros. Tambem foram utilizadas multiplas ferramentas de auxilio, como chatGPT, Github-CoPilot e guias na internet.

O jogo nasce de um mundo inspirado em um universo estilo soulsborne, atmosfera e dinâmica que inspirou a arte do jogo.
Ao longo do desenvolvimento, por muitas vezes acabamos mirando em mais do que podiamos fazer em tão pouco tempo, então no jogo existem muitas mecanicas ainda incompletas para o que poderia um dia evoluir para um verdadeiro indie. Porem, como este não é o caso atualmente, irei seguir com breves explicações de o que cada parte do código faz, pois este pode por vezes parecer confuos.

Antes de entrar em detalhes do código, é importante mencionar que juntamente do Pygame, neste projeto tambem estamos pela primeira vez aplicando classes em python, logo este é um elemento muito frequente nos códigos.

===========================================================================================================

## Explicação do código
Damos inicio no código pelo main.py, que é o executor do nosso jogo. Este arquivo serve apenas para iniciar a tela "loops", que em seguida ativa outras telas. Podemos dizer que este é o pavil do jogo, a primeira parte a ser ativada que desencadeia todo o resto.

Após falarmos do main.py, vamos intuitivamente para o loops.py, que é o nosso gerenciador de loops para este pygame, nele o loop do jogo é iniciado com o apertar da tecla espaço, e após o jogador morrer tambem direcionado para a tela final de morte. A tela de morte por sua vez é apenas uma tela de despedida, localizada no final.py.

Agora no jogo.py temos o maior desenvolvimento de código, pois nele todos os outros arquivos e classes são utilizados e canalizados em um ponto. Os principais arquivos utilizados no jogo.py são o hunter.py, monstros.py e dungeon.py, cada um responsavel por um dos elementos chaves do game, jogador, inimigos e mapa respectivamente. Todos estes códigos são então suportados por outros arquivos auxiliares, tal como o constantes.py e config.py, que servem para reunir configs e constantes para serem utilizadas pelos principais arquivos.

===========================================================================================================

## Processo de desenvolvimento
O processo de desenvolvimento deste jogo começou com o objetivo de mirarmos por um jogo de alto nivel indie apresentando conceitos interessantes, sendo assim demos no inicio de nosso código foco em desenvolvimento de imagens e sprites. Porem conforme fomos iniciando o projeto em python, notamos que o que almejavamos era muito mais complicado do que parecia, principalmente para nosso primeiro pygame, assim gerando uma situação onde tivemos pouco tempo para conseguirmos implementarmos tudo o que almejavamos.

===========================================================================================================

## Créditos

imagem de funde de morte: https://br.pinterest.com/pin/459578336955918929/

musica de fundo: https://www.youtube.com/watch?v=bLbf3ulQsp8