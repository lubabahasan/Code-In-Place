>>> Hello! This is a fruit sorting game I made using graphics. The pixel art is partly sourced and partly my own work. 
Use the right and left arrow keys to put the fruits in the correct boxes, all the while avoiding rotten or bug-infested fruits.
That's all, have fun! :> 


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
fruits = ["apple", "orange", "banana", "badapple"]

def main():
    #setup start
    size = SIZE
    fruit_count = 20

    left_x = CANVAS_WIDTH/2 - size/2 + 5
    left_y = CANVAS_HEIGHT/2 - size/2 - 20

    set_background()
    #setup end

    #game start
    start_menu(canvas)
    add_dustbin()

    delay = DELAY
    while fruit_count > 0 :
        fruit = send_fruit(canvas, left_x, left_y, size, 0, 0, delay)
        fruit_count -= 1

def send_fruit(canvas, left_x, left_y, size, distance, num, delay) :
    while True :
        fruit = random.choice(fruits)
        cnt = 0
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

            if num==1 and cnt==COUNT :
                num=2
                cnt=0
            elif num==2 and cnt==COUNT :
                num=3
                cnt=0
            elif cnt==COUNT :
                num=1
                cnt=0

            cnt += 1

            time.sleep(delay)
            canvas.delete(image)

            key = canvas.get_last_key_press()
            if key == "ArrowRight" :
                move_right(left_x, left_y, size, distance, fruit, num)
                break
            elif key == "ArrowLeft" :
                move_left(left_x, left_y, size, distance, fruit, num)
                
                break
            canvas.delete(ramp)

        break

def move_right(left_x, left_y, size, distance, fruit, num) :

    while left_x < CANVAS_WIDTH :
            #ramp = ramp_start(num)

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

def set_background():
    bg1 = canvas.create_rectangle(
        0, -20, CANVAS_WIDTH, CANVAS_HEIGHT/2, "#add8e6"
    )
    bg2 = canvas.create_rectangle(
        0, CANVAS_HEIGHT/2 - 20, CANVAS_WIDTH, CANVAS_HEIGHT, "#969898"
    )
    cartons1 = canvas.create_image_with_size(
        -300, -60, 460, 460, "carton.png"
    )
    cartons2 = canvas.create_image_with_size(
        190, -60, 460, 460, "carton.png"
    )

def ramp_start(num):
    ramp = canvas.create_image_with_size(
        -12, 40,
        350,
        350,
        "ramps"+str(num)+".png"
    )
    return ramp

def start_menu(canvas):
    ramp = ramp_start(1)
    add_dustbin()
    start_delay()

def start_delay():

    top = canvas.create_text(
            70, 30,
            text = "Game starts in...",
            #font = 'Lucida Console',
            font = 'Consolas',
            font_size = 25,
            color = 'black'
        )

    for i in range (3) :
        seconds = i+1
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
        font_size = 40,
        color = 'black'
    )

    time.sleep(0.7)
    canvas.delete(text)

def add_dustbin():
    canvas.create_image_with_size(
        10, 280, 330, 320, "dustbin.png"
    )
    

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
```