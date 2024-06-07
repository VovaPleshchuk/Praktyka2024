#Імпорт бібліотек
import pygame
import random

pygame.init()

# Визначення кольорів
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
snake_color = (0, 0, 0)

# Параметри дисплея
dis_width = 1000
dis_height = 700

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змійка')

#Налаштування годинника для контрою частоти кадрів, та шрифтів
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

#Ця функція малює змійку на дисплеї
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])

#Ця функція відображає повідомлення
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2))
    dis.blit(mesg, mesg_rect)

#Ця функція відображає рахунок у верхньому лівому куті екрану
def your_score(score):
    value = score_font.render("Твій рахунок: " + str(score), True, black)
    dis.blit(value, [0, 0])

#Дальше сама гра
#Встановлюються початкові умови гри, координати змійки, напрямок її руху, її початкова довжина, та координати їжі
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    #Це головний цикл гри який триває поки game over не стане True
    while not game_over:
        #Обробка стану (гра закінчена), виводиться відповідне повідомлення, після чого дається вибір
        while game_close == True:
            dis.fill(red)
            message("Ти програв! Натисни Q-Вийти або C-Грати знову", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #Тут обробляються події такі як вихід зз гри, та натискання клавіш для зміни напрямку змії
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #Перевірка зіткнень, якщо змійка виходить за межі дисплея, то гра закінчується
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            #Оновлення координат зміїки, Коли змійка рухається, дисплей очищається білим кольором, а їжа малюється на новій позиції
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        #Сегменти змійки додаються до списку, а якщо довжина списку перевищує довжину змійки, найстаріший сегмент видаляється
        # Перевіряється чи не зіткнулась змійка сама з собою
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #Малюється змійка та оновлюється рахунок на диспелї
        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        #Якщо змійка з'їла їжу, генеруються нові координати їжі, та збільшується довжина змійки
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        #Оновлення частоти кадрів, швидкість змійки збільшується зі збільшенням її довжини
        clock.tick(snake_speed + (Length_of_snake // 1))

    #Завершення гри
    pygame.quit()
    quit()

gameLoop()
