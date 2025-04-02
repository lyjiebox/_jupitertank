import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏窗口尺寸
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 600

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 坦克尺寸
TANK_WIDTH = 50
TANK_HEIGHT = 50

# 炮弹尺寸
BULLET_WIDTH = 10
BULLET_HEIGHT = 20

# 初始化窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("坦克大战")

# 加载字体
font = pygame.font.Font("simhei.ttf", 24)

# 游戏难度设置
DIFFICULTY = {
    "易": {"enemy_speed": 1, "bullet_speed": 2, "enemy_spawn_rate": 100},
    "中": {"enemy_speed": 2, "bullet_speed": 3, "enemy_spawn_rate": 75},
    "难": {"enemy_speed": 3, "bullet_speed": 4, "enemy_spawn_rate": 50}
}

# 在pygame初始化后，加载图片
try:
    # 加载坦克图片
    red_tank_img = pygame.image.load("tank_redtank.png")
    blue_tank_img = pygame.image.load("tank_bluetank.png")
    
    # 调整图片大小以匹配坦克尺寸
    red_tank_img = pygame.transform.scale(red_tank_img, (TANK_WIDTH, TANK_HEIGHT))
    blue_tank_img = pygame.transform.scale(blue_tank_img, (TANK_WIDTH, TANK_HEIGHT))
    print("坦克图片加载成功！")
except Exception as e:
    print(f"图片加载失败: {e}")
    pygame.quit()
    sys.exit()

class Tank:
    """坦克类"""
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.speed = 5
        self.bullets = []
        # 根据颜色选择对应的坦克图片
        self.image = red_tank_img if color == RED else blue_tank_img

    def draw(self):
        """绘制坦克"""
        # 使用图片替代矩形
        screen.blit(self.image, (self.x, self.y))
        if self.name:  # 只有玩家坦克显示名字
            text = font.render(self.name, True, WHITE)
            screen.blit(text, (self.x + 10, self.y + 10))

    def move(self, direction):
        """移动坦克"""
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WINDOW_WIDTH - TANK_WIDTH:
            self.x += self.speed

    def shoot(self):
        """发射炮弹"""
        bullet = Bullet(self.x + TANK_WIDTH // 2 - BULLET_WIDTH // 2, self.y, -5)
        self.bullets.append(bullet)

class Bullet:
    """炮弹类"""
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        """绘制炮弹"""
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT))

    def move(self):
        """移动炮弹"""
        self.y += self.speed

def draw_menu():
    """绘制难度选择菜单"""
    screen.fill(BLACK)
    title_text = font.render("选择难度", True, WHITE)
    easy_text = font.render("1. 易", True, WHITE)
    medium_text = font.render("2. 中", True, WHITE)
    hard_text = font.render("3. 难", True, WHITE)
    
    screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(easy_text, (WINDOW_WIDTH // 2 - easy_text.get_width() // 2, 200))
    screen.blit(medium_text, (WINDOW_WIDTH // 2 - medium_text.get_width() // 2, 250))
    screen.blit(hard_text, (WINDOW_WIDTH // 2 - hard_text.get_width() // 2, 300))
    
    pygame.display.flip()

def select_difficulty():
    """选择难度"""
    draw_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "易"
                elif event.key == pygame.K_2:
                    return "中"
                elif event.key == pygame.K_3:
                    return "难"

def show_score_screen(score, win):
    """显示成绩单"""
    screen.fill(BLACK)
    title_text = font.render("游戏结束", True, WHITE)
    score_text = font.render(f"你的分数: {score}", True, WHITE)
    if win:
        result_text = font.render("你赢了！", True, WHITE)
    else:
        result_text = font.render("你输了！", True, WHITE)
    
    screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 200))
    screen.blit(result_text, (WINDOW_WIDTH // 2 - result_text.get_width() // 2, 250))
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

def draw_start_screen():
    """绘制开机画面"""
    screen.fill(BLACK)
    start_text = font.render("按空格开始游戏...", True, WHITE)
    screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, WINDOW_HEIGHT - 50))
    pygame.display.flip()

def start_screen_animation():
    """显示开机画面图片，按下任意键继续"""
    screen.fill(BLACK)  # 清空屏幕，设置背景颜色
    # 加载开机画面图片
    start_screen_img = pygame.image.load("tank_startscreen.png")
    
    # 获取图片尺寸
    img_width = start_screen_img.get_width()
    img_height = start_screen_img.get_height()
    
    # 计算图片居中位置
    img_x = (WINDOW_WIDTH - img_width) // 2
    img_y = (WINDOW_HEIGHT - img_height) // 2
    
    # 绘制图片
    screen.blit(start_screen_img, (img_x, img_y))
    pygame.display.flip()

    # 等待按键
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 检测键盘按键
                return  # 按下任意键后退出函数

def main():
    """主游戏函数"""
    # 显示开机画面
    start_screen_animation()

    while True:
        # 选择难度
        difficulty = select_difficulty()

        # 初始化我方坦克
        player = Tank(WINDOW_WIDTH // 2 - TANK_WIDTH // 2, WINDOW_HEIGHT - TANK_HEIGHT - 10, RED, "Jupiter")

        # 敌方坦克和炮弹
        enemies = []
        enemy_bullets = []

        # 游戏状态
        running = True
        clock = pygame.time.Clock()
        enemy_spawn_counter = 0
        score = 0

        while running:
            screen.fill(BLACK)

            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        player.shoot()

            # 处理键盘输入
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move("left")
            if keys[pygame.K_RIGHT]:
                player.move("right")

            # 生成敌方坦克
            enemy_spawn_counter += 1
            if enemy_spawn_counter >= DIFFICULTY[difficulty]["enemy_spawn_rate"]:
                enemy = Tank(random.randint(0, WINDOW_WIDTH - TANK_WIDTH), 0, BLUE, "")
                enemies.append(enemy)
                enemy_spawn_counter = 0

            # 更新敌方坦克和炮弹
            for enemy in enemies:
                enemy.y += DIFFICULTY[difficulty]["enemy_speed"]
                enemy.draw()

                # 敌方坦克发射炮弹
                if random.randint(0, 100) < 5:
                    bullet = Bullet(enemy.x + TANK_WIDTH // 2 - BULLET_WIDTH // 2, enemy.y + TANK_HEIGHT, DIFFICULTY[difficulty]["bullet_speed"])
                    enemy_bullets.append(bullet)

            # 更新我方炮弹
            for bullet in player.bullets:
                bullet.move()
                bullet.draw()

            # 更新敌方炮弹
            for bullet in enemy_bullets:
                bullet.move()
                bullet.draw()

            # 绘制我方坦克
            player.draw()

            # 碰撞检测
            for bullet in player.bullets:
                for enemy in enemies:
                    if (bullet.x < enemy.x + TANK_WIDTH and
                        bullet.x + BULLET_WIDTH > enemy.x and
                        bullet.y < enemy.y + TANK_HEIGHT and
                        bullet.y + BULLET_HEIGHT > enemy.y):
                        player.bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 1
                        if score >= 10:
                            running = False
                            win = True

            for bullet in enemy_bullets:
                if (bullet.x < player.x + TANK_WIDTH and
                    bullet.x + BULLET_WIDTH > player.x and
                    bullet.y < player.y + TANK_HEIGHT and
                    bullet.y + BULLET_HEIGHT > player.y):
                    running = False
                    win = False

            # 绘制分数
            score_text = font.render(f"分数: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            # 更新显示
            pygame.display.flip()
            clock.tick(60)

        # 显示成绩单
        if not show_score_screen(score, win):
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 