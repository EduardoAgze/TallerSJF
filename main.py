from logic.chef import Chef
from logic.cliente import Cliente
from logic.min_heap import MinHeap
import pygame 

pygame.init()
pygame.font.init()
 
# --- Configuración de la ventana ---
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PixelChef-SJFgame")
reloj = pygame.time.Clock()
 
# --- Colores ---
NEGRO = (30, 30, 30)
ROJO = (200, 60, 60)
VERDE = (60, 180, 90)
AMARILLO = (220, 190, 60)
BLANCO = (255, 255, 255)
 
# --- Fuente para texto ---
fuente = pygame.font.Font(None, 28)
 
# --- Botones del menú (simulados con Rect) ---
boton_hamburguesa = pygame.Rect(50, 500, 180, 60)
boton_cafe = pygame.Rect(260, 500, 180, 60)
boton_pizza = pygame.Rect(470, 500, 180, 60)
 
corriendo = True
 
while corriendo:
    # 1. EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
 
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_hamburguesa.collidepoint(evento.pos):
                print("Clic: Hamburguesa (5s)")
            elif boton_cafe.collidepoint(evento.pos):
                print("Clic: Café (2s)")
            elif boton_pizza.collidepoint(evento.pos):
                print("Clic: Pizza (8s)")
 
    # 2. LÓGICA
    # (vacío por ahora — aquí no va nada de logic/ todavía)
 
    # 3. DIBUJO
    pantalla.fill(NEGRO)
 
    pygame.draw.rect(pantalla, ROJO, boton_hamburguesa)
    pygame.draw.rect(pantalla, AMARILLO, boton_cafe)
    pygame.draw.rect(pantalla, VERDE, boton_pizza)
 
    texto_h = fuente.render("Hamburguesa", True, BLANCO)
    texto_c = fuente.render("Café", True, BLANCO)
    texto_p = fuente.render("Pizza", True, BLANCO)
 
    pantalla.blit(texto_h, (boton_hamburguesa.x + 15, boton_hamburguesa.y + 20))
    pantalla.blit(texto_c, (boton_cafe.x + 50, boton_cafe.y + 20))
    pantalla.blit(texto_p, (boton_pizza.x + 50, boton_pizza.y + 20))
 
    pygame.display.flip()
    reloj.tick(60)
 
pygame.quit()
 
