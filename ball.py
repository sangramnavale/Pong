import pygame
from random import randint

BLACK = (0 ,0 ,0)

class Ball (pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		# Call the parent class:
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		# Drawing the (rectangle) ball:
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		# Velocity component of the rectangular ball:
		self.velocity = [randint(4, 8), randint(-8, 8)]

		# Fetching the rectangle object which is having the dimensions of the image:
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8, 8)