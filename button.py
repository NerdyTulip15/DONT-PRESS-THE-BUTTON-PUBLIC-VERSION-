import pygame

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["button.png", "button_pressed.png"]
        self.image_num = 0
        self.image = pygame.image.load(self.image_list[self.image_num])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def button_pressed(self):
        self.image_num = 1
        self.image = pygame.image.load(self.image_list[self.image_num])
        self.rescale_image(self.image)

    def button_unpressed(self):
        self.image_num = 0
        self.image = pygame.image.load(self.image_list[self.image_num])
        self.rescale_image(self.image)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
