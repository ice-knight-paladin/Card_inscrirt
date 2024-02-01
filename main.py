import pygame
import sys
import Card
import resources

GREEN = (200, 255, 200)
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((1500, 1000))
sc.fill(GREEN)

img_empty = Card.Card("images/empty.png")

W = 400 - 50 - img_empty.img.get_width() // 1.3
H = 100


def adW():
    global W
    W += 50 + img_empty.img.get_width() // 1.3
    return W


row1: list = list()
row2: list = list()
row3: list = list()
row_humon: list = list()

row1_cord: list = list()
row2_cord: list = list()
row3_cord: list = list()
row_humon_cord: list = list()


for i in range(6):
    if i < 4:
        row1.append(Card.Card("images/empty.png"))
        row1[i].csle.set_alpha(128)
        row2.append(Card.Card("images/empty.png"))
        row3.append(Card.Card("images/empty.png"))
    row_humon.append(Card.Card("images/empty.png"))

for i in range(4):
    row1_cord.append(row1[i].csle.get_rect(topleft=(adW(), H)))

W = 400 - 50 - img_empty.img.get_width() // 1.3
H += 20 + img_empty.img.get_height() // 1.3

for i in range(4):
    row2_cord.append(row2[i].csle.get_rect(topleft=(adW(), H)))

W = 400 - 50 - img_empty.img.get_width() // 1.3
H += 20 + img_empty.img.get_height() // 1.3

for i in range(4):
    row3_cord.append(row3[i].csle.get_rect(topleft=(adW(), H)))

W = 400 - (50 + img_empty.img.get_width() // 1.3) * 2
H += 20 + img_empty.img.get_height() // 1.3

for i in range(6):
    row_humon_cord.append(row_humon[i].csle.get_rect(topleft=(adW(), H)))

for i in range(6):
    if i < 4:
        sc.blit(row1[i].csle, row1_cord[i])
        sc.blit(row2[i].csle, row2_cord[i])
        sc.blit(row3[i].csle, row3_cord[i])
    sc.blit(row_humon[i].csle, row_humon_cord[i])


# eat = Card.Card("images/CardEat1.png")
# eat.csle.set_alpha(128)
row1[0] = Card.Card("images/CardEat1.png")
row1[0].csle.set_alpha(128)
# row1[0].csle.blit(row1[0].csle, ((img_empty.csle.get_width() - row1[0].csle.get_width()) // 2, (img_empty.csle.get_height() - row1[0].csle.get_height())//2))
sc.blit(row1[0].csle, (row1_cord[0][0] + 6, row1_cord[0][1] + 7))

print(row1[0].dm, row1[0].hp)
print(row2[0].dm, row2[0].hp)

pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(4):
                    if row2[i].hpe() == False:
                        if row1[i].hpe() != False:
                            row2[i] = row1[i]
                            row1[i] = Card.Card("images/empty.png")
                            row1[i].csle.set_alpha(128)
                            pygame.display.update()
                    print(111, row2[i].hpe(), row1[i].hpe())


    # -- Ход игрока
    # использование карт
    # обработка урона и убитых карт
    # отрисовка
    # -- ход бота
    # использование намеченых карт и показать след. атвку
    # обработка урона и убитых карт
    # отрисовка
    pygame.time.delay(20)
