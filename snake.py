import pygame
import time
import random

pygame.init()

# Cores RGB utilizadas no jogo 
amarelo = (255, 255, 0)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (58, 139, 206)

# Tela
largura_tela = 600
altura_tela = 400

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Serpente by <br>batalha')

# Parâmetros iniciais
clock = pygame.time.Clock()
fonte = pygame.font.SysFont('calibri', 25)

bloco = 10
velocidade = 13

# Funções
def placar(pontos):
    valor = fonte.render('Pontuação: ' + str(pontos), True, amarelo)
    tela.blit(valor, [3, 3])

def desenha_cobra(bloco, cobra):
    for x in cobra:
        pygame.draw.rect(tela, preto, [x[0], x[1], bloco, bloco])

def fim_de_jogo(color):
    msg1 = 'Fim de jogo!'
    msg2 = 'Pressione "C" para continuar jogando ou "S" para sair.'
    comprimento_msg1 = len(msg1)
    comprimento_msg2 = len(msg2)
    texto1 = fonte.render(msg1, True, color)
    tela.blit(texto1, [3, 150])
    texto2 = fonte.render(msg2, True, color)
    tela.blit(texto2, [3, 180])

def jogo():
    game_over = False
    game_close = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2

    x1_change = 0
    y1_change = 0

    cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura_tela - bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - bloco) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            tela.fill(azul)
            fim_de_jogo(vermelho)
            placar(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -bloco
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = bloco
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -bloco
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = bloco
                    x1_change = 0

        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        tela.fill(azul)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, bloco, bloco])
        head = []
        head.append(x1)
        head.append(y1)
        cobra.append(head)
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for x in cobra[:-1]:
            if x == head:
                game_close = True

        desenha_cobra(bloco, cobra)
        placar(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_tela - bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - bloco) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.display.quit()
    pygame.quit()
    quit()

jogo()