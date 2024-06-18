<!-- >Hello! This is a fruit sorting game I made using graphics. The pixel art is partly sourced and partly my own work. 
Use the right and left arrow keys to put the fruits in the correct boxes, all the while avoiding rotten or bug-infested fruits.
That's all, have fun! :> 
-->

```python
from graphics import Canvas
import random
    
CANVAS_WIDTH = 350
CANVAS_HEIGHT = 460
OFFSET = 10

SIZE = 80
DELAY = 0.004
OTHER_DELAY = 0.003
COUNT = 4

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
fruit_list = ["apple", "orange", "banana", "badapple", "badbanana"]
good_fruits = ["apple", "orange", "banana"]

def main():
    #setup start
    size = SIZE
    fruit_count = 20
    player_score = 0

    left_x = CANVAS_WIDTH/2 - size/2 + 5
    left_y = CANVAS_HEIGHT/2 - size/2 - 20
    
    #setup end


    #game start
    start()

    fruits_num = canvas.create_text(
        300, 10,
        text = str(fruit_count),
        font = 'Lucida Console',
        #font = 'Consolas'
        font_size = 20,
        color = 'black'
    )

    score_num = canvas.create_text(
        90, 10,
        text = str(player_score),
        font = 'Lucida Console',
        font_size = 20,
        color = 'black'
    )

    delay = DELAY

    while fruit_count > 0 :
        score = send_fruit(left_x, left_y, size, 0, 0, delay)
        #baskets(curr_fruit)
        fruit_count -= 1
        fruits_num = update_fruits(fruit_count, fruits_num)
        
        player_score += score
        if player_score<0 :
            player_score = 0
        score_num = update_score(player_score, score_num)
    
    end_screen(player_score)


def start():
    loader()

    start = canvas.create_image_with_size(
        0, 0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        "start.png"
    )

    time.sleep(6)

    start_screen()
    canvas.clear()
    
    canvas.create_rectangle( 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT/2, color='#ADD8E6')
    canvas.create_rectangle( 0, CANVAS_HEIGHT/2+40, CANVAS_WIDTH, CANVAS_HEIGHT, color='#808080')
    canvas.create_rectangle( 0, CANVAS_HEIGHT/2 - 10, CANVAS_WIDTH, CANVAS_HEIGHT/2+40, color='#4a6fc5')
    
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

def send_fruit(left_x, left_y, size, distance, num, delay) :
    while True :
        fruit = random.choice(fruit_list)
        count = 0
        temp_score = 0

        fruit_text = baskets(fruit)
        fruit_label = canvas.create_text(
            15, 235,
            text = fruit_text,
            color = 'white',
            font_size = 18
        )

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
            if key == "ArrowRight" and left_y < CANVAS_HEIGHT-150:
                canvas.get_last_key_press()
                move_right(left_x, left_y, size, distance, fruit)
                if fruit_text.endswith(str(fruit)) :
                    temp_score = 10
                else :
                    temp_score = -10
                break
            elif key == "ArrowLeft" and left_y < CANVAS_HEIGHT-150 :
                canvas.get_last_key_press()
                move_left(left_x, left_y, size, distance, fruit)
                if fruit_text.startswith(str(fruit)) :
                    temp_score = 10
                else :
                    temp_score = -10
                break
            elif fruit.startswith("bad"):
                temp_score = 10
            else :
                temp_score = -10

            canvas.get_last_key_press()
            canvas.delete(ramp)

        canvas.delete(fruit_label)
          
        return temp_score
        break

def move_right(left_x, left_y, size, distance, fruit) :
    canvas.get_last_key_press()
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

def move_left(left_x, left_y, size, distance, fruit) :
    canvas.get_last_key_press()
    while left_x + size > 0 :
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

def update_score(curr_score, score_num):
    canvas.delete(score_num)
    score_num = canvas.create_text(
        90, 10,
        text = str(curr_score),
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

def baskets(fruit):
    left = random.choice(good_fruits)
    if good_fruits.count(fruit)==0 :  #bad fruit
        temp = good_fruits.pop(good_fruits.index(left))
        right = random.choice(good_fruits)
        good_fruits.append(temp)
    else :  #good fruit
        if(left == fruit) :
            temp = good_fruits.pop(good_fruits.index(left))
            right = random.choice(good_fruits)
            good_fruits.append(temp)
        else :
            right = fruit
    
    space = "                                         "

    if left=="apple":
        left+="  "

    return left+space+right

def end_screen(player_score):
    canvas.clear()
    border = canvas.create_rectangle(
        0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color='black'
    )

    if player_score>0 :
        canvas.create_text(
            30, 110,
            text = "CONGRATULATIONS!",
            font = 'Lucida Console',
            font_size = 32,
            color = 'green'
        )
    else :
        canvas.create_text(
            40, 80,
            text = "GAME OVER",
            font = 'Lucida Console',
            font_size = 50,
            color = 'red'
        )
    
    temp = "YOUR SCORE: "+str(player_score)
    canvas.create_text(
        35, 200,
        text = temp,
        font = 'Lucida Console',
        font_size = 30,
        color = 'white'
    )

    canvas.create_text(
        30, 280,
        text = "Thanks for playing!",
        font = 'Lucida Console',
        font_size = 25,
        color = 'white'
    )

def start_screen():
    border = canvas.create_rectangle(
        0, 0,
        CANVAS_WIDTH, CANVAS_HEIGHT,
        'black'
    )

    back = canvas.create_rectangle(
        OFFSET, OFFSET, CANVAS_WIDTH-OFFSET, CANVAS_HEIGHT-OFFSET, 'pink'
    )


def loader():
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "orange.png")
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "banana.png")
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "apple.png")
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "badbanana.png")
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "badapple.png")
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "background1.png")
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "background2.png")
    canvas.create_image(CANVAS_HEIGHT, CANVAS_WIDTH, "background3.png")


if __name__ == '__main__':
    main()
```