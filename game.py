import pygame

class Game():

  WIDTH = 600
  HEIGHT = 600
  BG_COLOR = 'black'
  RESET_GAME_KEY = pygame.K_SPACE
  
  def __init__(self):
    pygame.init()
    self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    self._clock = pygame.time.Clock()
    
    # Flags
    self._running = True
    self._init = True

    # Variables

    # run
    self._run()
  
  def _run(self):
    
    while self._running:
      
      self._screen.fill(self.BG_COLOR)
      
      self._event_poll()
      
      self._update()
      
      self._draw()
      
      pygame.display.flip()
    
    pygame.quit()
    
  def _update(self):
    if self._init:
      # set variables to default value
      pass
  
  def _draw(self):
    pass
  
  def _event_poll(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self._running = False
      if event.type == pygame.KEYDOWN and event.dict['key'] == self.RESET_GAME_KEY:
        self._init = True 
      
      

if __name__ == '__main__':
  app = Game()
