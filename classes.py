import pygame
pygame.init()

font = pygame.font.SysFont('arialblack', 75)
little_font = pygame.font.SysFont('arialblack', 30)

#écriture de texte dans la fenêtre
def write_text(text: str, font, color, x, y, fenetre):
    img = font.render(text, True, color)
    fenetre.blit(img, (x, y))




class Restart:
	def __init__(self,fenetre):
		self.fenetre = fenetre

	def restart_button(self):
		self.img_restart = pygame.image.load('assets/restart.png')
		self.restart_button = pygame.transform.scale(self.img_restart,(100,100))
		self.hit_restart_button = self.restart_button.get_rect(center=(700,100))

	def show_restart_button(self):
		self.fenetre.blit(self.restart_button,self.hit_restart_button)

	def get_rect_restart(self):
		return self.hit_restart_button


class Casa:
	def __init__(self, fenetre):
		self.fenetre = fenetre
	def casa_button(self):
		self.img_home = pygame.image.load('assets/home.png')
		self.home_button = pygame.transform.scale(self.img_home, (100,100))
		self.hit_home_button = self.home_button.get_rect(center=(600,100))
	def show_home_button(self):
		self.fenetre.blit(self.home_button, self.hit_home_button)
	def get_rect_home(self):
		return self.hit_home_button
	