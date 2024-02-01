import pygame
import sys
import Card

GREEN = (200, 255, 200)
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((1500, 1000))
sc.fill(GREEN)

img_empty = pygame.image.load("images/empty.png")

W = 400 - 50 - img_empty.get_width() // 1.3
H = 100


def adW():
    global W
    W += 50 + img_empty.get_width() // 1.3
    return W


row1: list = list()
row2: list = list()
row3: list = list()
row_humon: list = list()

row1_cord: list = list()
row2_cord: list = list()
row3_cord: list = list()
row_humon_cord: list = list()

for i in range(4):
    row1.append(pygame.transform.scale(img_empty, (img_empty.get_width() // 1.3, img_empty.get_height() // 1.3)))
    row1[i].set_alpha(128)
    row2.append(pygame.transform.scale(img_empty, (img_empty.get_width() // 1.3, img_empty.get_height() // 1.3)))
    row3.append(pygame.transform.scale(img_empty, (img_empty.get_width() // 1.3, img_empty.get_height() // 1.3)))

for i in range(6):
    row_humon.append(pygame.transform.scale(img_empty, (img_empty.get_width() // 1.3, img_empty.get_height() // 1.3)))

for i in range(4):
    row1_cord.append(row1[i].get_rect(topleft=(adW(), H)))

W = 400 - 50 - img_empty.get_width() // 1.3
H += 20 + img_empty.get_height() // 1.3

for i in range(4):
    row2_cord.append(row2[i].get_rect(topleft=(adW(), H)))

W = 400 - 50 - img_empty.get_width() // 1.3
H += 20 + img_empty.get_height() // 1.3

for i in range(4):
    row3_cord.append(row3[i].get_rect(topleft=(adW(), H)))

W = 400 - (50 + img_empty.get_width() // 1.3) * 2
H += 20 + img_empty.get_height() // 1.3

for i in range(6):
    row_humon_cord.append(row_humon[i].get_rect(topleft=(adW(), H)))

for i in range(6):
    if i < 4:
        sc.blit(row1[i], row1_cord[i])
        sc.blit(row2[i], row2_cord[i])
        sc.blit(row3[i], row3_cord[i])
    sc.blit(row_humon[i], row_humon_cord[i])


eat = Card.Card("images/CardEat1.png")
# img_1 = pygame.image.load("images/CardEat1.png")
# img1 = pygame.transform.scale(img_1, (img_1.get_width() // 1.3, img_1.get_height() // 1.3))
row1[0].blit(eat.sca(), ((row1[0].get_width() - eat.sca().get_width()) // 2, (row1[0].get_height() - eat.sca().get_height())//2))
print()
sc.blit(row1[0], row1_cord[0])

print(row3[0])


pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         for i in range(4):
        #             if ()
    # -- Ход игрока
    # использование карт
    # обработка урона и убитых карт
    # отрисовка
    # -- ход бота
    # использование намеченых карт и показать след. атвку
    # обработка урона и убитых карт
    # отрисовка
    pygame.time.delay(20)
