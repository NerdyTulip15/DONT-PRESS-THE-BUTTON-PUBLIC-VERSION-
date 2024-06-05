import pygame

class Door:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.image = pygame.image.load(img)
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_left(self, amount):
        self.x = self.x - amount
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
