import pygame
from core.events.event_handler import EventHandler
from core.game_controller import GameController
from gui.screen_manager import ScreenManager

class Game():

  WIDTH = 600
  HEIGHT = 600
  BG_COLOR = 'black'
  
  def __init__(self):
    pygame.init()
    self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    self._clock = pygame.time.Clock()
    
    # Flags
    self._running = True
    self._init = True
    self._space_clicked = False

    # Variables

  
  def start(self):
    self._run()
  
  def _run(self):
    
    while self._running:
      self._event_poll()
      self._update()
      self._draw()
    
    pygame.quit()
    
  def _update(self):
    if self._init:
      # set variables to default value
      pass
  
  def _draw(self):
    self._screen.fill(self.BG_COLOR)
    
    # Render the game

    # Display
    pygame.display.flip()
  
  def _event_poll(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self._running = False
      if event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_SPACE:
        self._space_clicked = True 
      
      

if __name__ == '__main__':
  app = Game()
  app.start()
