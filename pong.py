# import pygame
# from Paddle import Paddle 
# from ball import ball


# pygame.init()

# BLACK = (0,0,0)
# WHITE = (255,255,255)  


# size = (700,500)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Pong")

# paddleA = Paddle(WHITE, 10, 100)
# paddleA.rect.x = 20
# paddleA.rect.y = 200

# paddleB = Paddle(WHITE, 10, 100)
# paddleB.rect.x = 670
# paddleB.rect.y = 200

# ball = ball(WHITE,10,10)
# ball.rect.x = 345
# ball.rect.y = 195


# all_sprite_list = pygame.sprite.Group()

# all_sprite_list.add(paddleA)
# all_sprite_list.add(paddleB)
# all_sprite_list.add(ball)

# carryOn = True


# clock = pygame.time.Clock()

# scoreA = 0
# scoreB = 0


# while carryOn:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             carryOn = False
#         elif event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_x:
#                 carryon=False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         paddleA.moveup(5)
#     if keys[pygame.K_s]:
#         paddleA.movedown(5)
#     if keys[pygame.K_UP]:
#         paddleB.moveup(5)
#     if keys[pygame.K_DOWN]:
#         paddleB.movedown(5)

                
#     all_sprite_list.update()

#     if ball.rect.x>=690:
#         scoreA+=1
#         ball.velocity[0] = -ball.velocity[0]
#     if ball.rect.x<=0:
#         scoreB+=1
#         ball.velocity[0] = -ball.velocity[0]
#     if ball.rect.y>490:
#         ball.velocity[1] = -ball.velocity[1]
#     if ball.rect.y<0:
#         ball.velocity[1] = -ball.velocity[1]

#     if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
#         ball.bounce()

#     screen.fill(BLACK)

#     pygame.draw.line(screen, WHITE, [349, 0], [349,500], 5)

#     all_sprite_list.draw(screen)

#     font = pygame.font.Font(None, 74)
#     text = font.render(str(scoreA), 1, WHITE)
#     screen.blit(text, (250,10))
#     text = font.render(str(scoreB), 1, WHITE)
#     screen.blit(text, (420,10))

#     pygame.display.flip()

#     clock.tick(60)

# pygame.quit()

# Import the pygame library and initialise the game engine
import pygame
from Paddle import Paddle
from ball import ball
 
pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
 
ball = ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the 2 paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
 
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
#Initialise player scores
scoreA = 0
scoreB = 0
 
effect = pygame.mixer.Sound('paddle_hit.wav')
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                    carryOn=False
        if scoreA == 10 or scoreB == 10:
            carryOn = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True: #Infinite loop that will be broken when the user press the space bar again
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break #Exit infinite loop
        
 
    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)  
 
    # --- Game logic should go here
    all_sprites_list.update()
    
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
      effect.play()
    
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen) 
 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()