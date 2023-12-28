from planet import Planet

# App parameters
WIDTH, HEIGHT = 1200, 800
APP_TITLE = "Planet Simulation"
CLOCK_TICK_FRAMERATE = 60

# RGB Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
DARK_GREY = (80, 78, 81)
WHITE = (255, 255, 255)
LIGHT_BLUE = (100, 149, 237)
RED = (188, 39, 50)
ORANGE = (255, 165, 0)
LIGHT_BROWN = (210, 180, 140)
GREY = (173, 216, 230)
DARK_BLUE = (0, 0, 139)

# Planet Data using structurized using a class
class PlanetData:
    def __init__(self, mass, radius, distance, orbital_velocity):
        self.mass = mass
        self.radius = radius
        self.distance = distance
        self.orbital_velocity = orbital_velocity

SUN_DATA = PlanetData(1.98892 * 10**30, 10, 0, 0)
MERCURY_DATA = PlanetData(3.30 * 10**24, 6, 0.387 * Planet.AU, -47.4 * 1000)
VENUS_DATA = PlanetData(4.8685 * 10**24, 8, 0.723 * Planet.AU, -35.02 * 1000)
EARTH_DATA = PlanetData(5.9742 * 10**24, 10, -1 * Planet.AU, 29.783 * 1000)
MARS_DATA = PlanetData(6.39 * 10**23, 7, -1.524 * Planet.AU, 24.077 * 1000)
JUPITER_DATA = PlanetData(1.898 * 10**27, 24, 5.203 * Planet.AU, -13.07 * 1000)
SATURN_DATA = PlanetData(5.683 * 10**26, 19, 9.582 * Planet.AU, -9.69 * 1000)
URANUS_DATA = PlanetData(8.681 * 10**25, 14, 19.22 * Planet.AU, -6.81 * 1000)
NEPTUNE_DATA = PlanetData(1.024 * 10**26, 12, 30.05 * Planet.AU, -5.43 * 1000)
