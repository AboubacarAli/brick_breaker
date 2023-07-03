# Window sizing
root_width = 1525
root_height = 800

# Paddle sizing
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10

# Paddle's initial position
PADDLE_X = (root_width - PADDLE_WIDTH) // 2
PADDLE_Y = root_height - PADDLE_HEIGHT - 10

# Ball sizing
BALL_RADIUS = 10

# Ball's initial position
BALL_X = root_width // 2
BALL_Y = root_height // 2

# Ball's speed
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Bricks sizing
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICKS_ROWS = 4
BRICKS_COLS = root_width // BRICK_WIDTH

# Bricks color
BRICK_COLORS = ["red", "orange", "yellow", "green"]




"""def ask_player_pseudo():
            player_pseudo = input("Enter your name or pseudo : ")
            return player_pseudo



def store_player_pseudo(player_pseudo):
    file="players_pseudo.txt"
    try:
        with open(file, "r") as f:
            pseudos = f.readlines()
            pseudos = [name.strip() for name in names]
            if player_pseudo not in names:
                with open(file, "a") as f:
                    f.write(player_pseudo + "\n")
    except FileNotFoundError:
            with open(file, "w") as f:
                f.write(player_pseudo + "\n")"""