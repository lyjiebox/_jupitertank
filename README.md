# 🚀 Jupiter Tank - 父子编程游戏集

> Use Cursor to code some small games for my son.

用 Cursor (AI 辅助编程) 为儿子做的几个 Python + Pygame 小游戏。寓教于乐 🦐

## 🎮 游戏列表

### 1. 🚜 坦克大战 (`tank_game.py`)

经典坦克对战游戏，红方坦克 vs 多个 AI 蓝方坦克。

**特性**：
- 🎚️ **三档难度**（易 / 中 / 难），影响敌方移动速度、子弹速度、刷新频率
- 🛡️ **随机障碍物**（4 个不重叠的灰色障碍，玩家和敌方都会被挡）
- 🔫 **炮弹数量限制**（每辆坦克最多同时存在 3 发，避免无脑乱射）
- 💥 **完善碰撞检测**：子弹击中坦克 / 障碍物，坦克之间碰撞，坦克撞障碍物
- 🖼️ **图片素材**：使用真实坦克 / 子弹 / 开屏画面图片
- 🎯 **胜负判定**：击毁 10 辆敌方坦克获胜

**操作**：
- `↑ ↓ ← →` 移动
- `空格` 发射炮弹

### 2. 🐍 贪吃蛇 (`snake_game.py`)

经典贪吃蛇，吃食物长身体，撞墙或撞自己结束。

**特性**：
- 中文界面（使用 `simhei.ttf` 字体）
- 实时分数显示
- 游戏结束后可按键重开

**操作**：
- `↑ ↓ ← →` 控制方向
- 游戏结束后：`Q` 退出 / `C` 重开

## 🧱 技术栈

- Python 3.x
- Pygame
- 中文字体支持（SimHei）

## 🚀 快速开始

```bash
# 1. 安装 pygame
pip install pygame

# 2. 启动坦克大战
python tank_game.py

# 3. 启动贪吃蛇
python snake_game.py
```

## 📂 项目结构

```
_jupitertank/
├── tank_game.py             # 坦克大战主程序
├── snake_game.py            # 贪吃蛇主程序
├── simhei.ttf               # 中文字体
├── tank_startscreen.png     # 坦克游戏开屏画面
├── tank_redtank.png         # 玩家坦克（红）
├── tank_bluetank.png        # 敌方坦克（蓝）
└── tank_bullet.png          # 子弹素材
```

## 🌟 项目背景

`Jupiter` 是儿子的英文名。这个仓库是父亲利用 Cursor 等 AI 编程工具，为儿子量身定制小游戏的实验场。每个功能迭代都伴随着一次"调试 + 玩游戏"的亲子时光 👨‍👦

后续可能继续添加：
- 🎯 打砖块
- 🏓 双人对战乒乓
- 🦖 跳跳龙

## 📜 更新日志

- **v3 (2026-05-24)**：坦克大战重大更新 —— 障碍物系统、炮弹限制、完善碰撞检测、难度调整
- **v2**：坦克改为图片素材，贪吃蛇添加注释
- **v1**：初始版本（基础坦克 + 贪吃蛇）

---

**Made with ❤️ by [lyjiebox](https://github.com/lyjiebox) for Jupiter**
