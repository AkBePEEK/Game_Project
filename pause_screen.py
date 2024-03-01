import main_screen
import levels.level_1

def pause_screen(paused):
    while paused:
        main_screen.draw_text("Pause", main_screen.main_font, "black", main_screen.screen, 1550 // 2, 840 // 4)

        mx, my = main_screen.pygame.mouse.get_pos()

        button_1 = main_screen.pygame.Rect(1550 // 2 - 100, 840 // 2 - 50, 200, 50)
        main_screen.pygame.draw.rect(main_screen.screen, "black", button_1)
        main_screen.draw_text("Resume", main_screen.font, "white", main_screen.screen, 1550 // 2, 840 // 2 - 25)
        button_3 = main_screen.pygame.Rect(1550 // 2 - 100, 840 // 2 + 37.5, 200, 50)
        main_screen.pygame.draw.rect(main_screen.screen, "black", button_3)
        main_screen.draw_text("Main screen", main_screen.font, "white", main_screen.screen, 1550 // 2, 840 // 2 + 62.5)
        button_2 = main_screen.pygame.Rect(1550 // 2 - 100, 840 // 2 + 125, 200, 50)
        main_screen.pygame.draw.rect(main_screen.screen, "black", button_2)
        main_screen.draw_text("Quit", main_screen.font, "white", main_screen.screen, 1550 // 2, 840 // 2 + 150)

        for event in main_screen.pygame.event.get():
            if event.type == main_screen.pygame.QUIT:
                main_screen.pygame.quit()
                main_screen.sys.exit()
            if event.type == main_screen.pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint((mx, my)):
                    levels.level_1.bg_sound.play()
                    paused = False
                if button_2.collidepoint((mx, my)):
                    main_screen.pygame.quit()
                    main_screen.sys.exit()
                if button_3.collidepoint((mx, my)):
                    main_screen.main_menu()
            if event.type == main_screen.pygame.KEYDOWN:
                if event.type == main_screen.pygame.K_ESCAPE:
                    levels.level_1.bg_sound.play()
                    paused = False

        main_screen.pygame.display.update()


if __name__ == '__main__':
    pause_screen(True)