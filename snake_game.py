import pygame
import time
import random

# 初始化pygame
pygame.init()

# 定义颜色常量（RGB值）
WHITE = (255, 255, 255)    # 白色
YELLOW = (255, 255, 102)   # 黄色
BLACK = (0, 0, 0)          # 黑色
RED = (213, 50, 80)        # 红色
GREEN = (0, 255, 0)        # 绿色
BLUE = (50, 153, 213)      # 蓝色

# 定义游戏窗口尺寸
DIS_WIDTH = 800    # 窗口宽度
DIS_HEIGHT = 600   # 窗口高度

# 创建游戏窗口并设置标题
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('贪吃蛇游戏')

# 定义时钟对象，用于控制游戏帧率
clock = pygame.time.Clock()

# 定义蛇的属性
snake_block = 20    # 蛇身每一块的大小（像素）
snake_speed = 2    # 蛇的移动速度（每秒移动的次数）

# 加载字体
# 使用支持中文的字体文件 simhei.ttf
font_style = pygame.font.Font("simhei.ttf", 25)    # 普通文本字体
score_font = pygame.font.Font("simhei.ttf", 35)    # 分数显示字体

def our_snake(snake_block, snake_list):
    """
    绘制蛇身
    :param snake_block: 蛇身方块的大小
    :param snake_list: 包含蛇身所有部分坐标的列表
    """
    for x in snake_list:
        # 绘制蛇身的每一块，使用黑色方块表示
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """
    在屏幕上显示消息
    :param msg: 要显示的消息文本
    :param color: 消息的颜色
    """
    # 渲染文本
    mesg = font_style.render(msg, True, color)
    # 将文本显示在屏幕中间偏上的位置
    dis.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def gameLoop():
    """
    游戏主循环函数
    包含了游戏的主要逻辑：移动、吃食物、碰撞检测等
    """
    # 游戏状态标志
    game_over = False    # 游戏是否结束
    game_close = False   # 当前回合是否结束

    # 初始化蛇的位置（屏幕中心）
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    # 蛇的移动方向变化量
    x1_change = 0
    y1_change = 0

    # 蛇身列表和长度
    snake_List = []          # 存储蛇身体所有部分的坐标
    Length_of_snake = 1      # 蛇的初始长度

    # 随机生成食物的位置
    foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 10.0) * 10.0

    # 主游戏循环
    while not game_over:
        # 游戏结束处理循环
        while game_close == True:
            dis.fill(BLUE)   # 填充蓝色背景
            message("你输了! 按Q退出或C重新开始", RED)   # 显示游戏结束消息
            pygame.display.update()   # 更新显示

            # 处理游戏结束时的按键事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # 点击窗口关闭按钮
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:   # 按Q退出
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:   # 按C重新开始
                        gameLoop()

        # 处理游戏进行时的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 关闭窗口
                game_over = True
            if event.type == pygame.KEYDOWN:   # 按键事件
                # 处理方向键，改变蛇的移动方向
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

        # 检查是否撞墙
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True

        # 更新蛇的位置
        x1 += x1_change
        y1 += y1_change

        # 绘制游戏画面
        dis.fill(BLUE)   # 填充背景色
        pygame.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])   # 绘制食物

        # 更新蛇身
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]    # 删除多余的蛇身部分

        # 检查是否撞到自己
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # 绘制蛇
        our_snake(snake_block, snake_List)

        # 更新显示
        pygame.display.update()

        # 检查是否吃到食物
        if x1 == foodx and y1 == foody:
            # 生成新的食物位置
            foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1    # 蛇身长度加1

        # 控制游戏速度
        clock.tick(snake_speed)

    # 游戏结束，退出pygame
    pygame.quit()
    quit()

# 启动游戏
gameLoop() 