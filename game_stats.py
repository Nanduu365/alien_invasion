import pygame.font
from pygame.sprite import Group

from ship import Ship

class GameStats:
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai):
        '''Initialize the statistics'''
        self.settings = ai.settings
        self.reset_stats()

        #Start the game in an inactive state
        self.game_active = False

        #High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        '''Initialize statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1



class Scoreboard :
    '''A class to represent scoring information'''

    def __init__(self, ai):
        '''Initialize score keeping attributes'''
        pygame.font.init()

        self.ai = ai
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai.settings
        self.stats = ai.stats

        #Font settings for scoring information.
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self) :
        '''Turn the score into a rendered image'''

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)  # a string formatting directive that tells python to inisert comas into numbers when converting a numerical value to string.
        self.score_image = self.font.render(score_str, True, 
                            self.text_color, self.settings.bg_color)
        
        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        

    def show_score(self):
        '''draw score, high score, ships and level to the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image , self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        '''Check to see if there is a new highscore'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_high_score(self):
        '''Turn the high score into a rendered image'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = str(high_score)

        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, self.settings.bg_color)
        
        #Center the highscore at the top of the screen
        self.high_score_rect= self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        '''Turn the level into a rendered image'''
        level_str = f"LEVEL {str(self.stats.level)}"
        font = pygame.font.SysFont(None, 24)
        self.level_image = font.render(level_str, True, 
                            self.text_color, self.settings.bg_color)
        
        #Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.topright= self.score_rect.bottomright


    def prep_ships(self):
        '''Show how many ships are left'''
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)




