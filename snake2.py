from random import randint
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        reset_game()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randint(-15, 15) * 10
        food.y = randint(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

def reset_game():
    "Reset the game to play again."
    answer = input("Game Over! Apakah Anda ingin bermain lagi? (y/n): ")
    if answer.lower() == 'y':
        clear()
        global snake, food, aim
        snake = [vector(10, 0)]
        food = vector(0, 0)
        aim = vector(0, -10)
        move()
    else:
        print("Terima kasih telah bermain!")
        bye()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
