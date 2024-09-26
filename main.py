import pygame
import sys
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	asteroid_field = AsteroidField()

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for item in updatable:
			item.update(dt)
		
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()

			if asteroid.collision(player):
				print("Game over!")
				sys.exit()

		screen.fill((0,0,0))

		for item in drawable:
			item.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000
	
if __name__ == "__main__":
    main()