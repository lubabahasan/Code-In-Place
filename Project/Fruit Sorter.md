<!-- >Hello! This is a fruit sorting game I made using graphics. The pixel art is partly sourced and partly my own work. 
Use the right and left arrow keys to put the fruits in the correct boxes, all the while avoiding rotten or bug-infested fruits.
That's all, have fun! :> 
-->

```python
from graphics import Canvas
import random
    
CANVAS_WIDTH = 350
CANVAS_HEIGHT = 460

SIZE = 80
DELAY = 0.004
OTHER_DELAY = 0.003
COUNT = 4

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
fruit_list = ["apple", "orange", "banana", "badapple", "badbanana"]

def main():
    #setup start
    size = SIZE
    fruit_count = 20

    left_x = CANVAS_WIDTH/2 - size/2 + 5
    left_y = CANVAS_HEIGHT/2 - size/2 - 20

    canvas.create_rectangle( 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT/2, color = '#ADD8E6' )
    #setup end

    #game start
    start_menu()

    fruits_num = canvas.create_text(
        300, 10,
        text = "20",
        font = 'Lucida Console',
        #font = 'Consolas'
        font_size = 20,
        color = 'black'
    )

    delay = DELAY
    while fruit_count > 0 :
        send_fruit(canvas, left_x, left_y, size, 0, 0, delay)
        fruit_count -= 1
        fruits_num = update_fruits(fruit_count, fruits_num)

def start_menu():
    ramp = ramp_start(1)
    start_texts()

def ramp_start(num):
    ramp = canvas.create_image_with_size(
        0, 0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        "background"+str(num)+".png"
    )
    return ramp

def start_texts():

    top = canvas.create_text(
            70, 30,
            text = "Game starts in...",
            #font = 'Lucida Console',
            font = 'Consolas',
            font_size = 25,
            color = 'black'
        )

    for i in range (3) :
        seconds = 3-i
        text = canvas.create_text(
            160, 70,
            text = str(seconds),
            #font = 'Lucida Console',
            font = 'Consolas',
            font_size = 30,
            color = 'black'
        )
        time.sleep(1)
        canvas.delete(text)

    canvas.delete(top)
    text = canvas.create_text(
        103, 50,
        text = "Start!",
        font = 'Lucida Console',
        #font = 'Consolas'
        font_size = 35,
        color = 'black'
    )

    time.sleep(0.7)
    canvas.delete(text)

    score = canvas.create_text(
        10, 10,
        text = "Score: ",
        font = 'Lucida Console',
        #font = 'Consolas'
        font_size = 20,
        color = 'black'
    )

    fruit_left = canvas.create_text(
        210, 10,
        text = "Fruits: ",
        font = 'Lucida Console',
        #font = 'Consolas'
        font_size = 20,
        color = 'black'
    )

    update_score(0)

def send_fruit(canvas, left_x, left_y, size, distance, num, delay) :
    while True :
        fruit = random.choice(fruit_list)
        count = 0
        while left_y < CANVAS_HEIGHT :
            ramp = ramp_start(num)
            
            image = canvas.create_image_with_size(
                left_x,
                left_y,
                size,
                size,
                fruit+".png"
            )
            size += 1
            left_x = CANVAS_WIDTH/2 - size/2 + 5
            left_y += distance
            distance += 0.1
            
            if num==1 and count==COUNT :
                num=2
                count=0
            elif num==2 and count==COUNT :
                num=3
                count=0
            elif count==COUNT :
                num=1
                count=0

            count += 1
            
            time.sleep(delay)
            canvas.delete(image)
            
            key = canvas.get_last_key_press()
            if key == "ArrowRight" :
                move_right(left_x, left_y, size, distance, fruit, num)
                key = "None"
                break
            elif key == "ArrowLeft" :
                move_left(left_x, left_y, size, distance, fruit, num)
                key = "None"
                break
            
            canvas.delete(ramp)
            
        break

def move_right(left_x, left_y, size, distance, fruit, num) :

    while left_x < CANVAS_WIDTH :
            image = canvas.create_image_with_size(
                left_x,
                left_y,
                size,
                size,
                fruit+".png"
            )

            left_x = CANVAS_WIDTH/2 - size/2 + distance
            distance += 10

            time.sleep(OTHER_DELAY)
            canvas.delete(image)

def move_left(left_x, left_y, size, distance, fruit, num) :

    while left_x + size > 0 :
            ramp = ramp_start(num)
            image = canvas.create_image_with_size(
                left_x,
                left_y,
                size,
                size,
                fruit+".png"
            )
            left_x = CANVAS_WIDTH/2 - size/2 - distance
            distance += 10

            time.sleep(OTHER_DELAY)
            canvas.delete(image)
            canvas.delete(ramp)

def update_score(score):
    score_num = canvas.create_text(
        90, 10,
        text = str(score),
        font = 'Lucida Console',
        font_size = 20,
        color = 'black'
    )
    return score_num

def update_fruits(fruits_left, prev_fruit):
    canvas.delete(prev_fruit)
    new_fruits = canvas.create_text(
        300, 10,
        text = str(fruits_left),
        font = 'Lucida Console',
        font_size = 20,
        color = 'black'
    )
    return new_fruits

if __name__ == '__main__':
    main()
```