import pygame
from planet import Planet
from data import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_TITLE)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(SUN_DATA.distance, 0, SUN_DATA.radius, YELLOW, SUN_DATA.mass)
    sun.sun = True

    mercury = Planet(MERCURY_DATA.distance, 0, MERCURY_DATA.radius, DARK_GREY, MERCURY_DATA.mass)
    mercury.y_vel = MERCURY_DATA.orbital_velocity

    venus = Planet(VENUS_DATA.distance, 0, VENUS_DATA.radius, WHITE, VENUS_DATA.mass)
    venus.y_vel=VENUS_DATA.orbital_velocity

    earth = Planet(EARTH_DATA.distance, 0, EARTH_DATA.radius, LIGHT_BLUE, EARTH_DATA.mass)
    earth.y_vel=EARTH_DATA.orbital_velocity

    mars = Planet(MARS_DATA.distance, 0, MARS_DATA.radius, RED, MARS_DATA.mass)
    mars.y_vel=MARS_DATA.orbital_velocity
    
    jupiter = Planet(JUPITER_DATA.distance, 0, JUPITER_DATA.radius, ORANGE, JUPITER_DATA.mass)
    jupiter.y_vel=JUPITER_DATA.orbital_velocity
    
    saturn = Planet(SATURN_DATA.distance, 0, SATURN_DATA.radius, LIGHT_BROWN, SATURN_DATA.mass)
    saturn.y_vel=SATURN_DATA.orbital_velocity

    uranus = Planet(URANUS_DATA.distance, 0, URANUS_DATA.radius, GREY, URANUS_DATA.mass)
    uranus.y_vel=URANUS_DATA.orbital_velocity
    
    neptune = Planet(NEPTUNE_DATA.distance, 0, NEPTUNE_DATA.radius, DARK_BLUE, NEPTUNE_DATA.mass)
    neptune.y_vel=NEPTUNE_DATA.orbital_velocity

    planets = [
        sun, mercury, venus, earth, mars, 
        jupiter, saturn, uranus, neptune
    ]

    while run:
        clock.tick(CLOCK_TICK_FRAMERATE)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
