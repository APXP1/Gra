import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))


class Player:
    def __init__(self):
        self.x_cord = 550
        self.y_cord = 550
        self.width = 0
        self.height = 0
        self.image = pygame.image.load("postać.png")
        self.speed = 3

    def tick(self, keys):
        if keys[pygame.K_a]:
            self.x_cord -= self.speed
        if keys[pygame.K_d]:
            self.x_cord += self.speed

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


def main():
    run = True
    player = Player()
    background = pygame.image.load("tło.webp")
    while run:
        pygame.time.Clock().tick(1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        player.tick(keys)

        window.blit(background, (0, 0))
        player.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()