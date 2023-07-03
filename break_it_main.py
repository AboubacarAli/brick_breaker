import tkinter as tk
from main_features import *

# Creation of the root window
root = tk.Tk()
root.title("BREAK IT")

# Creating the canva
canvas = tk.Canvas(root, width=root_width, height=root_height, bg="black")
canvas.pack()

# Creating the paddle
paddle = canvas.create_rectangle(
    PADDLE_X, PADDLE_Y, PADDLE_X + PADDLE_WIDTH, PADDLE_Y + PADDLE_HEIGHT, fill="white"
)

# Creating the ball
ball = canvas.create_oval(
    BALL_X - BALL_RADIUS, BALL_Y - BALL_RADIUS, BALL_X + BALL_RADIUS, BALL_Y + BALL_RADIUS, fill="white"
)

# Creating the bricks
bricks = []
for row in range(BRICKS_ROWS):
    for col in range(BRICKS_COLS):
        x1 = col * BRICK_WIDTH
        y1 = row * BRICK_HEIGHT
        x2 = x1 + BRICK_WIDTH
        y2 = y1 + BRICK_HEIGHT
        color = BRICK_COLORS[row]
        brick = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        bricks.append(brick)

# Moving the paddle
def move_paddle(event):
    if event.keysym == "Left":
        canvas.move(paddle, -10, 0)
    elif event.keysym == "Right":
        canvas.move(paddle, 10, 0)

# Assigning the left and right button to the function that moves the paddle
canvas.bind_all("<KeyPress-Left>", move_paddle)
canvas.bind_all("<KeyPress-Right>", move_paddle)

# Updating the ball's position
def update_ball_position():
    global BALL_SPEED_X, BALL_SPEED_Y
    canvas.move(ball, BALL_SPEED_X, BALL_SPEED_Y)
    ball_pos = canvas.coords(ball)

    # Bouncing the ball on the canva sides
    if ball_pos[0] <= 0 or ball_pos[2] >= root_width:
        BALL_SPEED_X = -BALL_SPEED_X
    if ball_pos[1] <= 0 or ball_pos[3] >= root_height:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Bouncing the ball on the paddle
    if canvas.coords(ball)[3] >= canvas.coords(paddle)[1] and canvas.coords(ball)[2] >= canvas.coords(paddle)[0] and canvas.coords(ball)[0] <= canvas.coords(paddle)[2]:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Collision between the ball and the bricks
    for brick in bricks:
        brick_pos = canvas.coords(brick)
        if (
            ball_pos[2] >= brick_pos[0]
            and ball_pos[0] <= brick_pos[2]
            and ball_pos[3] >= brick_pos[1]
            and ball_pos[1] <= brick_pos[3]
        ):
            canvas.delete(brick)
            bricks.remove(brick)
            BALL_SPEED_Y = -BALL_SPEED_Y
            break

    # Victory message when all the bricks are destroyed
    if len(bricks) == 0:
        canvas.create_text(
            root_width // 2,
            root_height // 2,
            text="You won the game!!!",
            font=("Purple", 24),
            fill="white",
        )


# Calling recursively the function after a certain time
    canvas.after(20, update_ball_position)

# Initializing the ball position updating
update_ball_position()

# Running the main loop
root.mainloop()