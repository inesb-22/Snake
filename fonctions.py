def affichage(snake, pastille, score, antipastille, TAILLE):

    fill(0, 100, 0)
    
    if len(snake) > 1:
        qx = snake[0][0]
        qy = snake[0][1]
        #direction to the next segment to orient the tail
        dx_q = (snake[1][0] - snake[0][0]) / TAILLE
        dy_q = (snake[1][1] - snake[0][1]) / TAILLE
        
        if dx_q == 1: #moving right
            triangle(qx + TAILLE, qy, qx + TAILLE, qy + TAILLE, qx, qy + TAILLE/2)
        elif dx_q == -1: #moving left
            triangle(qx, qy, qx, qy + TAILLE, qx + TAILLE, qy + TAILLE/2)
        elif dy_q == 1: #moving down
            triangle(qx, qy + TAILLE, qx + TAILLE, qy + TAILLE, qx + TAILLE/2, qy)
        else: #moving up
            triangle(qx, qy, qx + TAILLE, qy, qx + TAILLE/2, qy + TAILLE)
            
    #body (from 2nd segment to the second to last)
    for c in snake[1:-1]:
        rect(c[0], c[1], TAILLE, TAILLE, 4)

    #head (snake[-1])
    fill(34, 139, 34)
    hx = snake[-1][0]
    hy = snake[-1][1]
    cx = hx + TAILLE / 2
    cy = hy + TAILLE / 2
    
    #head base
    ellipse(cx, cy, TAILLE, TAILLE)
    
    #head direction
    if len(snake) > 1:
        dx_t = (snake[-1][0] - snake[-2][0]) / TAILLE
        dy_t = (snake[-1][1] - snake[-2][1]) / TAILLE
    else:
        dx_t = 1
        dy_t = 0

    #eyes
    fill(0)
    if dx_t != 0: #if moving horizontally
        ellipse(cx + dx_t * TAILLE*0.1, cy - TAILLE*0.25, TAILLE*0.15, TAILLE*0.15)
        ellipse(cx + dx_t * TAILLE*0.1, cy + TAILLE*0.25, TAILLE*0.15, TAILLE*0.15)
    else: #if moving vertically
        ellipse(cx - TAILLE*0.25, cy + dy_t * TAILLE*0.1, TAILLE*0.15, TAILLE*0.15)
        ellipse(cx + TAILLE*0.25, cy + dy_t * TAILLE*0.1, TAILLE*0.15, TAILLE*0.15)

    #snake tongue
    stroke(220, 20, 20)
    strokeWeight(2)
    bout_x = cx + dx_t * TAILLE * 0.9
    bout_y = cy + dy_t * TAILLE * 0.9
    
    #tongue base
    line(cx + dx_t * TAILLE * 0.5, cy + dy_t * TAILLE * 0.5, bout_x, bout_y)
    
    # Tongue fork
    if dx_t != 0:
        line(bout_x, bout_y, bout_x + dx_t * TAILLE * 0.2, bout_y - TAILLE * 0.15)
        line(bout_x, bout_y, bout_x + dx_t * TAILLE * 0.2, bout_y + TAILLE * 0.15)
    else:
        line(bout_x, bout_y, bout_x - TAILLE * 0.15, bout_y + dy_t * TAILLE * 0.2)
        line(bout_x, bout_y, bout_x + TAILLE * 0.15, bout_y + dy_t * TAILLE * 0.2)
        
    stroke(0) # Reset default stroke (black, 1px) for the rest of the game
    strokeWeight(1)

    # apple
    fill(220, 20, 20)
    ellipse(pastille[0] + TAILLE / 2, pastille[1] + TAILLE / 2 + 1, TAILLE * 0.85, TAILLE * 0.85)

    # Little leaf
    fill(30, 180, 30)
    ellipse(pastille[0] + TAILLE / 2 + 2, pastille[1] + 3, TAILLE * 0.35, TAILLE * 0.2)


    fill(245)
    ellipse(antipastille[0] + TAILLE / 2, antipastille[1] + TAILLE / 2 - 1, TAILLE * 0.75, TAILLE * 0.75)

    fill(245)
    rect(antipastille[0] + TAILLE * 0.35, antipastille[1] + TAILLE * 0.5, TAILLE * 0.3, TAILLE * 0.3)

    fill(0)
    ellipse(antipastille[0] + TAILLE * 0.38, antipastille[1] + TAILLE * 0.4, TAILLE * 0.2, TAILLE * 0.2)
    ellipse(antipastille[0] + TAILLE * 0.62, antipastille[1] + TAILLE * 0.4, TAILLE * 0.2, TAILLE * 0.2)

    #score
    fill(0)
    textSize(14)
    textAlign(LEFT, TOP)
    text("Score: " + str(score), 5, 2)


def deplacement(snake, dx, dy):
    snake.pop(0)
    snake.append([snake[-1][0] + dx, snake[-1][1] + dy])


def collision(snake, TAILLE, antipastille, score):
    #wall collision
    if (snake[-1][0] > width - 2 * TAILLE
        or snake[-1][0] < TAILLE
        or snake[-1][1] > height - 2 * TAILLE
        or snake[-1][1] < TAILLE ):
        finjeu(TAILLE, score)

    #body collision
    for c in snake[:-1]:
        if snake[-1][0] == c[0] and snake[-1][1] == c[1]:
            finjeu(TAILLE, score)

    # skull collision
    if (snake[-1][0] == antipastille[0] and snake[-1][1] == antipastille[1]):
        finjeu(TAILLE, score)


def finjeu(TAILLE, score):
    # Dark overlay for game over
    fill(0, 0, 0, 160)
    rect(0, 0, width, height)

    fill(250, 50, 150)
    textSize(TAILLE * 1.8)
    textAlign(CENTER, CENTER)
    text("Game Over", width / 2, height / 2 - 20)

    fill(255)
    textSize(TAILLE)
    text(
        "Final score: " + str(score),
        width / 2,
        height / 2 + 20
    )

    if score <= 2:
        fill(255, 80, 80)
        text("Looser !", width / 2, height / 2 + 50)
    elif 2 < score <= 4:
        fill(255, 162, 0)
        text("You can do better", width / 2, height / 2 + 50)
    elif score >= 5:
        fill(148, 255, 166)
        text("Good job !", width / 2, height / 2 + 50)

    noLoop()
