from main_screen import *
import levels.level_1


def loose_screen(paused):
    try:
        while paused:
            draw_text("You Lost", main_font, "black", screen, 1550 // 2, 840 // 4)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(1550 // 2 - 100, 840 // 2 - 50, 200, 50)
            pygame.draw.rect(screen, "black", button_1)
            draw_text("Restart", font, "white", screen, 1550 // 2, 840 // 2 - 25)
            button_3 = pygame.Rect(1550 // 2 - 100, 840 // 2 + 37.5, 200, 50)
            pygame.draw.rect(screen, "black", button_3)
            draw_text("Main screen", font, "white", screen, 1550 // 2, 840 // 2 + 62.5)
            button_2 = pygame.Rect(1550 // 2 - 100, 840 // 2 + 125, 200, 50)
            pygame.draw.rect(screen, "black", button_2)
            draw_text("Quit", font, "white", screen, 1550 // 2, 840 // 2 + 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_1.collidepoint((mx, my)):
                        levels.level_1.bg_sound.play()
                        paused = False
                        return True, 90, 700, 584
                    if button_2.collidepoint((mx, my)):
                        pygame.quit()
                        sys.exit()
                    if button_3.collidepoint((mx, my)):
                        main_menu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Changed event.type to event.key
                        levels.level_1.bg_sound.play()
                        paused = False

            pygame.display.update()
    except AttributeError as e:
        print("Attribute error occurred:", e)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    loose_screen(False)
