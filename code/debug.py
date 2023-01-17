import  pygame
pygame.init()
font= pygame.font.Font(None,30)

def Debug(info, y=10, x=10):
    displaye_surface= pygame.display.get_surface()
    debug_surf=font.render(str(info),True,'White')
    debug_rect= debug_surf.get_rect(topleft=(x,y))
    pygame.draw.rect(displaye_surface, 'Black', debug_rect)
    displaye_surface.blit(debug_surf,debug_rect)

