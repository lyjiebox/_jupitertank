import pygame
import time
import random

# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# 定义屏幕大小
DIS_WIDTH = 800
DIS_HEIGHT = 600

# 创建游戏窗口
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('贪吃蛇游戏')

# 定义时钟
clock = pygame.time.Clock()

# 定义蛇的大小和速度
snake_block = 20
snake_speed = 10

# 定义字体样式
# 使用支持中文的字体文件，例如 "simhei.ttf"
font_style = pygame.font.Font("simhei.ttf", 25)
score_font = pygame.font.Font("simhei.ttf", 35)

def our_snake(snake_block, snake_list):
    """
    绘制蛇
    :param snake_block: 蛇的块大小
    :param snake_list: 蛇的坐标列表
    """
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """
    显示消息
    :param msg: 消息内容
    :param color: 消息颜色
    """
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def gameLoop():
    """
    游戏主循环
    """
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(BLUE)
            message("你输了! 按Q退出或C重新开始", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLUE)
        pygame.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 启动游戏
gameLoop() 