class Robot(pygame.sprite.Sprite):

    def __init__(self, pos, surface):
        super().__init__()
        self.direction = pygame.math.Vector2(0,0)
        self.image = pygame.image.load("robot.png")




    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.guarda_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.guarda_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            if self.direction.y == 0: #puo saltare solo se non sta saltando
                self.salta()