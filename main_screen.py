import levels.level_1
import levels.level_2
import levels.level_3
import sys
import pygame
import os

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройка окна
WIDTH, HEIGHT = 1600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Main Menu")

# Настройка текста
font = pygame.font.Font("fonts/Micro5-Regular.ttf", 36)
main_font = pygame.font.Font("fonts/Micro5-Regular.ttf", 100)

# Функция для вывода текста на экран


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


# Функция главного меню
def main_menu():
    try:
        bg = pygame.image.load(os.path.join("images", "start_screen.jpg_large")).convert_alpha()
        person = pygame.image.load(os.path.join("images", "pixil-frame-0 (2).png")).convert_alpha()
        x = pygame.image.load(os.path.join("images", "5ce1ea638f5be16ad27b9503.png")).convert_alpha()
    except pygame.error as e:
        print("Error loading images:", e)
        pygame.quit()
        sys.exit()
    while True:
        screen.blit(bg, (0, -190))
        screen.blit(person, (-50, 300))
        draw_text("Woodcutter", main_font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
        screen.blit(x, (WIDTH // 2 - 190, HEIGHT // 2 - 250))
        draw_text("Head", main_font, BLACK, screen, WIDTH // 2 - 100, HEIGHT // 4 + 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 25, 200, 50)
        pygame.draw.rect(screen, BLACK, button_1)
        draw_text("Level 1", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50)

        button_2 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 125, 200, 50)
        pygame.draw.rect(screen, BLACK, button_2)
        draw_text("Level 2", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 150)

        button_3 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 225, 200, 50)
        pygame.draw.rect(screen, BLACK, button_3)
        draw_text("Level 3", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 250)

        button_4 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 325, 200, 50)
        pygame.draw.rect(screen, BLACK, button_4)
        draw_text("Quit", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint((mx, my)):
                    levels.level_1.level_1()
                if button_2.collidepoint((mx, my)):
                    levels.level_2.level_2()
                if button_3.collidepoint((mx, my)):
                    levels.level_3.level_3()
                if button_4.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
