from fonctions import *

TAILLE = 20

# Initial snake body with 5 segments
snake = [[i * TAILLE, 10 * TAILLE] for i in range(1, 6)]

# Initial movement direction (moving right)
dx = TAILLE
dy = 0

# Random apple (bonus) position aligned with grid coordinates
pastille = [(int(random(18)) + 1) * TAILLE, (int(random(18)) + 1) * TAILLE]

speed = 40

# Random skull (malus) position aligned with grid coordinates
antipastille = [(int(random(18)) + 1) * TAILLE, (int(random(18)) + 1) * TAILLE]

score = 0


def setup():
    size(20 * TAILLE, 20 * TAILLE)


def draw():
    global snake, pastille, speed, antipastille, score

    #draw sky blue background and field
    background(135, 206, 235)
    fill(173, 216, 230)
    rect(TAILLE, TAILLE, width - 2 * TAILLE, height - 2 * TAILLE)

    #game elements (snake, apple, skull, score)
    affichage(snake, pastille, score, antipastille, TAILLE)

    #game update tick based on speed setting
    if frameCount % speed == 0:
        deplacement(snake, dx, dy)
        collision(snake, TAILLE, antipastille, score)

        # When the snake eats the apple
        if snake[-1] == pastille:
            # Increase game speed up to maximum threshold
            if speed > 4:
                speed -= 4

            # Generate new position for apple
            pastille = [(int(random(18)) + 1) * TAILLE, (int(random(18)) + 1) * TAILLE]
            score += 1

            antipastille = [ (int(random(18)) + 1) * TAILLE, (int(random(18)) + 1) * TAILLE]

            #extend snake length
            snake.append([snake[-1][0] + dx, snake[-1][1] + dy])

        if pastille == antipastille:
            pastille = [(int(random(18)) + 1) * TAILLE, (int(random(18)) + 1) * TAILLE]


def keyPressed():
    global dx, dy

    #prevent direct 180 degree reverse turns
    if keyCode == UP and dy == 0:
        dx = 0
        dy = -TAILLE

    elif keyCode == DOWN and dy == 0:
        dx = 0
        dy = TAILLE

    elif keyCode == LEFT and dx == 0:
        dx = -TAILLE
        dy = 0

    elif keyCode == RIGHT and dx == 0:
        dx = TAILLE
        dy = 0
