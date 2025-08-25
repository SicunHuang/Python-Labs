'''
Play "piper game" where the user controls a sand piper to collect as many clams on the beach without getting wet

CS 150 Lab 10

Name: Sicun Huang

Creativity:

'''
import pygame
from random import randint
import math

# Constants to determine the size of the screen
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 500

# Number of clams to draw at the beginning of the game (or when regenerating)
NUM_CLAMS = 10

# Amount the player should move with each key press
STEP = 50

# Frames-per-second for the game
FPS = 60

class Entity():
    '''Base class for all game entities

    The game will create instances of the child classes of Entity

    Attributes:
        rect: A pygame.Rect that describes the location and size of the entity
    '''
    def __init__(self, x, y, width, height):
        '''Initialize an Entity

        Args:
            x, y: Initial x,y position for entity
            width: Width of entity's rectangle
            height: Height of entity's rectangle
        '''
        self.rect = pygame.Rect(x, y, width, height)
    
    def get_x(self):
        '''Return the current x-coordinate'''
        return self.rect.x
    
    def set_x(self, value):
        '''Set the x-coordinate to value'''
        self.rect.x = value
    
    def shift_x(self, shift):
        '''Shift the x-coordinate by shift (positively or negatively)'''
        self.rect.x += shift
    
    def get_y(self):
        '''Return the current y-coordinate'''
        return self.rect.y
    
    def set_y(self, value):
        '''Set the y-coordinate to value'''
        self.rect.y = value
    
    def shift_y(self, shift):
        '''Shift the y-coordinate by shift (positively or negatively)'''
        self.rect.y += shift
    
    def collide(self, other):
        """Check if the two entities overlap"""
        return self.rect.colliderect(other.rect)


class Player(Entity):
    """Child class derived from class Entity and describes attributes of the piper"""
    def __init__(self):
        """Initialize the player's rectangle in the top-left corner of the screen"""
        super().__init__(0,0,50,50)
        
    def render(self, display):
        """
        Load the image of the piper and render it on the display
        
        Args:
            display: The surface on which player is shown
        """
        self.image = pygame.transform.scale(pygame.image.load('piper.png'),self.rect.size)
        pygame.Surface.blit(display,self.image,self.rect)
        
        
class Clam(Entity):
    """Child class derived from class Entity and describes attributes of the clams"""
    def __init__(self):
        """Initialize the clam's rectangle randomly in the right-half of the screen and make them collectable to the piper"""
        super().__init__(randint(0.5*SCREEN_WIDTH, SCREEN_WIDTH-30),randint(0, SCREEN_WIDTH-30),30,30)
        self.visible = True #clam can be collected
    
    def render(self, display):
        """
        Load the image of the clam and render it on the display
        
        Args:
            display: The surface on which clam is shown
        """
        self.image = pygame.transform.scale(pygame.image.load('clam.png'),self.rect.size)
        pygame.Surface.blit(display,self.image,self.rect)
        
    
class Wave(Entity):
    """Child class derived from class Entity and describes attributes of the wave"""
    def __init__(self):
        """Initialize the wave so that it starts at the 3/4 of the screen"""
        super().__init__(0.75*SCREEN_WIDTH, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    def render(self, display):
        """
        Render the wave on the display with blue color
        
        Args:
            display: The surface on which wave is shown
        """
        pygame.draw.rect(display, (0, 0, 255), self.rect)

def play_game(max_time):
    '''Main game function for Piper's adventure

    Args:
        max_time: Number of seconds to play for
    '''
    
    # Initialize the pygame engine
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial',14)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Piper's adventures")

    # Initialize Player, Wave and Clams
    player = Player()
    clams = []
    for i in range(NUM_CLAMS):
        clams.append(Clam())
    wave = Wave()

    time  = 0
    score = 0

    # Main game loop
    while time < max_time:

        # Obtain any user inputs
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
          break

        # Screen origin (0, 0) is the upper-left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.shift_x(STEP)
            elif event.key == pygame.K_LEFT:
                player.shift_x(-STEP)
            elif event.key == pygame.K_UP:
                player.shift_y(-STEP)
            elif event.key == pygame.K_DOWN:
                player.shift_y(STEP)
        
        # Determine if Piper gathered more clams
        for clam in clams:
            if player.collide(clam) and clam.visible == True:
                clam.visible = False
                score += 1 
       
        # Update the position of the wave
        wave.set_x(0.75 * SCREEN_WIDTH - 0.25 * SCREEN_WIDTH * math.sin(time))
        # When the wave has reached its peak create new clams
        if wave.rect.left < 0.51*SCREEN_WIDTH:
            for clam in range(NUM_CLAMS):
                clams[clam] = Clam() 
            
        # If the piper touched the wave the game is over...
        if player.collide(wave):
            break
        # Draw all of the game elements
        screen.fill([255,255,255])
        
        # Draw clams
        for clam in clams:
            if clam.visible == True:
                clam.render(screen)
        
        # Draw piper
        player.render(screen)
        # Draw wave
        wave.render(screen)
        # Render the current time and score
        text = font.render('Time = ' + str(round(max_time-time, 1)), True, (0, 0, 0))
        screen.blit(text, (10, 0.95*SCREEN_HEIGHT))
    
        text = font.render('Score = ' + str(score), True, (0, 0, 0))
        screen.blit(text, (10, 0.90*SCREEN_HEIGHT))

        # Render next frame
        pygame.display.update()
        clock.tick(FPS)

        # Update game time by advancing time for each frame
        time += 1.0/FPS

    print('Game over!')
    print('Score =', score)

    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    play_game(30)
