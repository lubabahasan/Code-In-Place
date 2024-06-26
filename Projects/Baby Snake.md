
```python

from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.15 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    food = canvas.create_image_with_size(
        random.randrange(0, CANVAS_WIDTH, SIZE),
        random.randrange(0, CANVAS_HEIGHT, SIZE),
        SIZE, SIZE,
        "apple_2.png"
    )

    snake = canvas.create_rectangle(
        0, 0, SIZE, SIZE, 'green'
    )

    x = canvas.get_left_x(snake)
    y = canvas.get_top_y(snake)
    direction = 'right'

    while x+20 < CANVAS_WIDTH and y+20 <CANVAS_HEIGHT and x>=0 and y>=0:

        food_x = canvas.get_left_x(food)
        food_y = canvas.get_top_y(food)
        
        if (food_x == x and food_y == y):
            canvas.moveto(food, 
                random.randrange(0, CANVAS_WIDTH, SIZE),
                random.randrange(0, CANVAS_HEIGHT, SIZE)
            )

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
        
        if (x+20 < CANVAS_WIDTH and y+20 <CANVAS_HEIGHT) and ( x>=0 and y>=0 ):
            if direction == 'right':
                canvas.move(snake, 20, 0)
            elif direction == 'left':
                if x==0 : return
                canvas.move(snake, -20, 0)
            elif direction == 'up':
                if y==0 : return
                canvas.move(snake, 0, -20)
            elif direction == 'down':
                canvas.move(snake, 0, 20)

        time.sleep(DELAY)
        
if __name__ == '__main__':
    main()

```