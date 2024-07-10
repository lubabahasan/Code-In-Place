
```python

from graphics import Canvas
import time
import random
    
CANVAS_HEIGHT = 450
CANVAS_WIDTH = CANVAS_HEIGHT*1.7
SIZE = 30


# if you make this larger, the game will go slower
DELAY = 0.15

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    '''grass = canvas.create_rectangle(
        0, 0, CANVAS_HEIGHT, CANVAS_HEIGHT, "salmon"
    )'''

    grass = canvas.create_image_with_size(
        0, 0, CANVAS_HEIGHT, CANVAS_HEIGHT,
        "grass.png"
    )
    canvas.set_outline_color(grass,"black")

    food = canvas.create_image_with_size(
        random.randrange(SIZE, (CANVAS_HEIGHT-SIZE), SIZE),
        random.randrange(SIZE, (CANVAS_HEIGHT-SIZE), SIZE),
        SIZE, SIZE,
        "apple_2.png"
    )

    snake = canvas.create_rectangle(
        0, 0, SIZE, SIZE, 'green'
    )
    
    x = canvas.get_left_x(snake)
    y = canvas.get_top_y(snake)
    direction = 'right'

    while x+SIZE < CANVAS_HEIGHT and y+SIZE < CANVAS_HEIGHT and x>=0 and y>=0:

        food_x = canvas.get_left_x(food)
        food_y = canvas.get_top_y(food)
        
        print(str(food_x)+" "+str(food_y))
        print(str(x)+" "+str(y))

        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = 'left'
            #print('left arrow pressed!')
        if key == 'ArrowRight':
            direction = 'right'
            #print('right arrow pressed!')
        if key == 'ArrowUp':
            direction = 'up'
            #print('up arrow pressed!')
        if key == 'ArrowDown':
            direction = 'down'
            #print('down arrow pressed!')

        x = canvas.get_left_x(snake)
        y = canvas.get_top_y(snake)
        
        if (x+SIZE < CANVAS_HEIGHT and y+SIZE < CANVAS_HEIGHT) and ( x>=0 and y>=0 ):
            if direction == 'right':
                canvas.move(snake, SIZE, 0)
            elif direction == 'left':
                if x==0 : return
                canvas.move(snake, -SIZE, 0)
            elif direction == 'up':
                if y==0 : return
                canvas.move(snake, 0, -SIZE)
            elif direction == 'down':
                canvas.move(snake, 0, SIZE)

        if (food_x == x and food_y == y):
            canvas.moveto(food, 
                random.randrange(SIZE, (CANVAS_HEIGHT-SIZE), SIZE),
                random.randrange(SIZE, (CANVAS_HEIGHT-SIZE), SIZE),
            )

        time.sleep(DELAY)
        
if __name__ == '__main__':
    main()


```