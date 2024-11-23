import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for updateable in updatable_group:
            updateable.update(dt)
        for asteroid in asteroids_group:
            if asteroid.check_collision(player):
                print("Game Over!")
                raise SystemExit
            for shot in shot_group:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60) / 1000) # convert miliseconds to seconds

if __name__ == "__main__":
    main()