import main_screen
import pause_screen

try:
    main_screen.pygame.init()

    def level_3():
        clock = main_screen.pygame.time.Clock()

        def loose_screen(paused):
            while paused:
                main_screen.draw_text("Pause", main_screen.main_font, "black", screen, 1550 // 2, 840 // 4)

                mx, my = main_screen.pygame.mouse.get_pos()

                button_1 = main_screen.pygame.Rect(1550 // 2 - 100, 840 // 2 - 50, 200, 50)
                main_screen.pygame.draw.rect(screen, "black", button_1)
                main_screen.draw_text("Restart", main_screen.font, "white", screen, 1550 // 2, 840 // 2 - 25)
                button_3 = main_screen.pygame.Rect(1550 // 2 - 100, 840 // 2 + 37.5, 200, 50)
                main_screen.pygame.draw.rect(screen, "black", button_3)
                main_screen.draw_text("Main screen", main_screen.font, "white", screen, 1550 // 2, 840 // 2 + 62.5)
                button_2 = main_screen.pygame.Rect(1550 // 2 - 100, 840 // 2 + 125, 200, 50)
                main_screen.pygame.draw.rect(screen, "black", button_2)
                main_screen.draw_text("Quit", main_screen.font, "white", screen, 1550 // 2, 840 // 2 + 150)

                for event in main_screen.pygame.event.get():
                    if event.type == main_screen.pygame.QUIT:
                        main_screen.pygame.quit()
                        main_screen.sys.exit()
                    if event.type == main_screen.pygame.MOUSEBUTTONDOWN:
                        if button_1.collidepoint((mx, my)):
                            bg_sound.play()
                            return True, 90, 700, 584
                        if button_2.collidepoint((mx, my)):
                            main_screen.pygame.quit()
                            main_screen.sys.exit()
                        if button_3.collidepoint((mx, my)):
                            main_screen.main_menu()
                    if event.type == main_screen.pygame.KEYDOWN:
                        if event.type == main_screen.pygame.K_ESCAPE:
                            bg_sound.play()
                            paused = False

                main_screen.pygame.display.update()


        screen = main_screen.pygame.display.set_mode((1550, 840), main_screen.pygame.FULLSCREEN) #flags=pygame.NOFRAME)
        main_screen.pygame.display.set_caption("ITP project")
        main_screen.pygame.display.set_icon(main_screen.pygame.image.load("../images/2730363_game_inkcontober_steal_sword_tools_icon.png"))

        font1 = main_screen.pygame.font.Font("../fonts/Micro5-Regular.ttf", 60)
        text_surface = font1.render("Game", True, 'red')

        #Player
        bg = main_screen.pygame.image.load("../images/back.jpg").convert_alpha()
        walk_right = [
            main_screen.pygame.image.load("../images/woodcutter/walk_right/Woodcutter_walk.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_right/Woodcutter_walk (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_right/Woodcutter_walk (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_right/Woodcutter_walk (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_right/Woodcutter_walk (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_right/Woodcutter_walk (5).png").convert_alpha(),
        ]
        walk_left = [
            main_screen.pygame.image.load("../images/woodcutter/walk_left/image.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_left/image (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_left/image (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_left/image (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_left/image (5).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/walk_left/image (6).png").convert_alpha()
        ]
        idle = [
            main_screen.pygame.image.load("../images/woodcutter/idle/Woodcutter_idle.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/idle/Woodcutter_idle (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/idle/Woodcutter_idle (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/idle/Woodcutter_idle (3).png").convert_alpha()
        ]
        climb = [
            main_screen.pygame.image.load("../images/woodcutter/climb/Woodcutter_climb.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/climb/Woodcutter_climb (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/climb/Woodcutter_climb (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/climb/Woodcutter_climb (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/climb/Woodcutter_climb (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/climb/Woodcutter_climb (5).png").convert_alpha()
        ]
        craft = [
            main_screen.pygame.image.load("../images/woodcutter/craft/Woodcutter_craft.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/craft/Woodcutter_craft (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/craft/Woodcutter_craft (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/craft/Woodcutter_craft (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/craft/Woodcutter_craft (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/craft/Woodcutter_craft (5).png").convert_alpha()
        ]
        death = [
            main_screen.pygame.image.load("../images/woodcutter/death/Woodcutter_death.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/death/Woodcutter_death (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/death/Woodcutter_death (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/death/Woodcutter_death (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/death/Woodcutter_death (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/death/Woodcutter_death (5).png").convert_alpha()
        ]
        hurt = [
            main_screen.pygame.image.load("../images/woodcutter/hurt/Woodcutter_hurt.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/hurt/Woodcutter_hurt (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/hurt/Woodcutter_hurt (2).png").convert_alpha()
        ]
        push = [
            main_screen.pygame.image.load("../images/woodcutter/push/Woodcutter_push.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/push/Woodcutter_push (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/push/Woodcutter_push (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/push/Woodcutter_push (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/push/Woodcutter_push (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/push/Woodcutter_push (5).png").convert_alpha()
        ]
        run = [
            main_screen.pygame.image.load("../images/woodcutter/run/Woodcutter_run.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/run/Woodcutter_run (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/run/Woodcutter_run (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/run/Woodcutter_run (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/run/Woodcutter_run (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/run/Woodcutter_run (5).png").convert_alpha()
        ]
        attack1 = [
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack1/image.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack1/Woodcutter_attack1.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (4).png").convert_alpha()

        ]
        attack2 = [
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack2/Woodcutter_attack2.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (5).png").convert_alpha()
        ]
        attack3 = [
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack3/Woodcutter_attack3_1.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack3/Woodcutter_attack3_2.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack3/Woodcutter_attack3_3.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack3/Woodcutter_attack3_4.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack3/Woodcutter_attack3_5.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/woodcutter_attack3/Woodcutter_attack3_6.png").convert_alpha()
        ]
        jump = [
            main_screen.pygame.image.load("../images/woodcutter/jump/Woodcutter_jump.png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/jump/Woodcutter_jump (1).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/jump/Woodcutter_jump (2).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/jump/Woodcutter_jump (3).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/jump/Woodcutter_jump (4).png").convert_alpha(),
            main_screen.pygame.image.load("../images/woodcutter/jump/Woodcutter_jump (5).png").convert_alpha(),
        ]

        #Sounds
        bg_sound = main_screen.pygame.mixer.Sound("../sounds/greenfield-birds-suburban-sounds-in-the-background-16683.mp3")
        bg_sound.play()

        #Enemy
        monster = main_screen.pygame.image.load("../images/woodcutter/Woodcutter.png").convert_alpha()
        monster_x = 584
        monster_y = 700

        bg_x = 0

        player_anim_count = 0
        player_speed = 6
        player_acceleration = 1.5
        player_x = 90
        player_y = 700


        jump_count = 3

        is_jump = False
        running = True
        gameplay = True
        motion = False

        while running:

            screen.blit(bg, (-10, 0))
            screen.blit(monster, (monster_x, monster_y))

            if gameplay:
                player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
                monster_rect = monster.get_rect(topleft=(monster_x, monster_y))

                if player_rect.colliderect(monster_rect):
                    gameplay = False

                keys = main_screen.pygame.key.get_pressed()
                motion_buttons = [
                    keys[main_screen.pygame.K_a], keys[main_screen.pygame.K_d], keys[main_screen.pygame.K_LEFT],
                    keys[main_screen.pygame.K_RIGHT], keys[main_screen.pygame.K_SPACE],
                    main_screen.pygame.mouse.get_pressed()
                ]
                if not is_jump:
                    if not (keys[main_screen.pygame.K_a] or keys[main_screen.pygame.K_d] or keys[main_screen.pygame.K_LEFT]
                            or keys[main_screen.pygame.K_RIGHT]):
                        screen.blit(idle[player_anim_count % 4], (player_x, player_y))
                    else:
                        if keys[main_screen.pygame.K_a] or keys[main_screen.pygame.K_LEFT]:
                            screen.blit(walk_left[player_anim_count % 6], (player_x, player_y))
                            bg_x += 2
                        elif keys[main_screen.pygame.K_d] or keys[main_screen.pygame.K_RIGHT]:
                            screen.blit(walk_right[player_anim_count % 6], (player_x, player_y))
                            bg_x -= 2
                    if keys[main_screen.pygame.K_SPACE]:
                        is_jump = True
                else:
                    if jump_count >= -3:
                        if jump_count > 0:
                            player_y -= (jump_count ** 4) // 2
                        else:
                            player_y += (jump_count ** 4) // 2

                        if jump_count != 3:
                            screen.blit(jump[jump_count % 6], (player_x, player_y))
                        else:
                            screen.blit(idle[0], (player_x, player_y))
                        jump_count -= 1
                    else:
                        is_jump = False
                        jump_count = 3

                if keys[main_screen.pygame.K_LEFT] or keys[main_screen.pygame.K_a] and player_x > 20:
                    player_x -= player_speed
                elif keys[main_screen.pygame.K_RIGHT] or keys[main_screen.pygame.K_d] and player_x < 1500:
                    player_x += player_speed

            else:
                gameplay, player_x, player_y, monster_x = loose_screen(True)

            main_screen.pygame.display.update()

            for event in main_screen.pygame.event.get():
                if event.type == main_screen.pygame.QUIT:
                    running = False
                    main_screen.pygame.quit()
                elif event.type == main_screen.pygame.KEYDOWN:
                    if event.key == main_screen.pygame.K_ESCAPE:
                        bg_sound.stop()
                        pause_screen.pause_screen(True)

            monster_x -= 8
            player_anim_count += 1
            clock.tick(15)
except AttributeError:
    pass

if __name__ == "__main__":
    level_3()
