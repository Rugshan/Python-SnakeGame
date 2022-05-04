from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

GAME_SPEED = 0.07
is_game_on = True

screen = None
snake = None
food = None
scoreboard = None


def pause_game():
    if is_game_on:
        snake.toggle_pause()
        scoreboard.toggle_pause_screen()


def restart_game():
    global is_game_on
    if not is_game_on:
        global screen, snake, food, scoreboard
        del snake, food, scoreboard
        screen.clearscreen()
        setup_game()
        is_game_on = True


def end_game():
    global is_game_on
    is_game_on = False
    scoreboard.game_over()


def eat_food():
    food.refresh()
    scoreboard.increment_score()


def setup_game():
    global screen, snake, food, scoreboard
    screen = Screen()
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(pause_game, "p")


setup_game()

while is_game_on:

    screen.update()
    time.sleep(GAME_SPEED)

    # Check if game is paused.
    if not snake.is_paused:
        snake.move()

    # Detect collision with wall or tail.
    if snake.detect_wall_collision() or snake.detect_tail_collision():
        end_game()

    # Detect collision with food.
    if snake.detect_food_collision(food):
        eat_food()

screen.exitonclick()
