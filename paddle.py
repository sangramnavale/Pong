import pygame
class Paddle(pygame.sprite.Sprite):

	def __init__(self, color, width, height):
		# Calling the parent class
		super().__init__()

		# Setting the background and the background color
		self.image = pygame.Surface([width, height])
		self.image.fill((0, 0, 0))
		self.image.set_colorkey((0, 0, 0)) # Making the background transparent

		# Drawing the paddle
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		# Fetch the rectangle object that has the dimensions of the image
		self.rect = self.image.get_rect()

	def moveUp(self, pixels):
		self.rect.y -= pixels
		# Defining the top border
		if self.rect.y < 75:
			self.rect.y = 75

	def moveDown(self, pixels):
		self.rect.y += pixels
		# Defining the bottom border
		if self.rect.y > 400:
			self.rect.y = 400

