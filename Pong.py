import pygame
from paddle import Paddle
from ball import Ball

# Initializing the window
pygame.init()

# Creating the paddles
paddleA = Paddle((255, 255, 255), 10 , 100)
paddleA.rect.x = 0
paddleA.rect.y = 200

paddleB = Paddle((255, 255, 255), 10 , 100)
paddleB.rect.x = 690
paddleB.rect.y = 200

ball = Ball((255, 255, 255), 10 ,10)
ball.rect.x = 345
ball.rect.y = 195

#This will be a list that will contain all the sprites we intend to use in the game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# To define the game window
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pong")
icon = pygame.image.load("table-tennis.png")
pygame.display.set_icon(icon)

# To check how the screen gets updated over the time in the game
clock = pygame.time.Clock()

# Score initialisation
scoreA = 0
scoreB = 0

running = True
while running:
	screen.fill((0, 0, 0)) # Making the background black

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				running = False

	# Paddle Movement
	keys = pygame.key.get_pressed()
	# Paddle A movement
	if keys[pygame.K_w]:
		paddleA.moveUp(5)
	if keys[pygame.K_s]:
		paddleA.moveDown(5)
	# Paddle B movement
	if keys[pygame.K_UP]:
		paddleB.moveUp(5)
	if keys[pygame.K_DOWN]:
		paddleB.moveDown(5)

	# Collision of the ball
	if ball.rect.x > 690:
		scoreA += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x < 0:
		scoreB += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.y > 490:
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y < 75:
		ball.velocity[1] = -ball.velocity[1]

	#Detect collisions between the ball and the paddles
	if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
		ball.bounce()

	# Updating the sprite lists
	all_sprites_list.update()

	# Drawing the score bar
	pygame.draw.line(screen, (255, 255, 255), [0, 75], [700, 75], 5)

	# Drawing the net
	pygame.draw.line(screen, (255, 255, 255), [345, 0], [345, 500], 5)

	# Drawing all the sprites
	all_sprites_list.draw(screen)

	# Displaying the score
	font = pygame.font.Font(None, 64)
	text = font.render(str(scoreA), 1, (255, 255, 255))
	screen.blit(text, (175, 10))
	text = font.render(str(scoreB), 1, (255, 255, 255))
	screen.blit(text, (500, 10))

	# Limit the game to 60 fps
	clock.tick(60)

	# Updating the screen
	pygame.display.update()
