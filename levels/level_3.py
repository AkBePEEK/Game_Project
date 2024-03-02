import pygame

pygame.init()

bg_sound = pygame.mixer.Sound("sounds/greenfield-birds-suburban-sounds-in-the-background-16683.mp3")


def level_3():
    clock = pygame.time.Clock()

    paused = True

    bg_sound.play()
    screen = pygame.display.set_mode((1550, 840), pygame.FULLSCREEN) #flags=pygame.NOFRAME)
    pygame.display.set_caption("ITP project")
    pygame.display.set_icon(pygame.image.load("images/2730363_game_inkcontober_steal_sword_tools_icon.png"))

    font1 = pygame.font.Font("fonts/Micro5-Regular.ttf", 60)
    text_surface = font1.render("Game", True, 'red')

    #Player
    bg = pygame.image.load("images/back.jpg").convert_alpha()
    walk_right = [
        pygame.image.load("images/woodcutter/walk_right/Woodcutter_walk.png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_right/Woodcutter_walk (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_right/Woodcutter_walk (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_right/Woodcutter_walk (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_right/Woodcutter_walk (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_right/Woodcutter_walk (5).png").convert_alpha(),
    ]
    walk_left = [
        pygame.image.load("images/woodcutter/walk_left/image.png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_left/image (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_left/image (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_left/image (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_left/image (5).png").convert_alpha(),
        pygame.image.load("images/woodcutter/walk_left/image (6).png").convert_alpha()
    ]
    idle = [
        pygame.image.load("images/woodcutter/idle/Woodcutter_idle.png").convert_alpha(),
        pygame.image.load("images/woodcutter/idle/Woodcutter_idle (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/idle/Woodcutter_idle (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/idle/Woodcutter_idle (3).png").convert_alpha()
    ]
    climb = [
        pygame.image.load("images/woodcutter/climb/Woodcutter_climb.png").convert_alpha(),
        pygame.image.load("images/woodcutter/climb/Woodcutter_climb (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/climb/Woodcutter_climb (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/climb/Woodcutter_climb (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/climb/Woodcutter_climb (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/climb/Woodcutter_climb (5).png").convert_alpha()
    ]
    craft = [
        pygame.image.load("images/woodcutter/craft/Woodcutter_craft.png").convert_alpha(),
        pygame.image.load("images/woodcutter/craft/Woodcutter_craft (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/craft/Woodcutter_craft (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/craft/Woodcutter_craft (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/craft/Woodcutter_craft (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/craft/Woodcutter_craft (5).png").convert_alpha()
    ]
    death = [
        pygame.image.load("images/woodcutter/death/Woodcutter_death.png").convert_alpha(),
        pygame.image.load("images/woodcutter/death/Woodcutter_death (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/death/Woodcutter_death (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/death/Woodcutter_death (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/death/Woodcutter_death (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/death/Woodcutter_death (5).png").convert_alpha()
    ]
    hurt = [
        pygame.image.load("images/woodcutter/hurt/Woodcutter_hurt.png").convert_alpha(),
        pygame.image.load("images/woodcutter/hurt/Woodcutter_hurt (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/hurt/Woodcutter_hurt (2).png").convert_alpha()
    ]
    push = [
        pygame.image.load("images/woodcutter/push/Woodcutter_push.png").convert_alpha(),
        pygame.image.load("images/woodcutter/push/Woodcutter_push (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/push/Woodcutter_push (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/push/Woodcutter_push (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/push/Woodcutter_push (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/push/Woodcutter_push (5).png").convert_alpha()
    ]
    run = [
        pygame.image.load("images/woodcutter/run/Woodcutter_run.png").convert_alpha(),
        pygame.image.load("images/woodcutter/run/Woodcutter_run (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/run/Woodcutter_run (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/run/Woodcutter_run (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/run/Woodcutter_run (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/run/Woodcutter_run (5).png").convert_alpha()
    ]
    attack1 = [
        pygame.image.load("images/woodcutter/woodcutter_attack1/image.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack1/Woodcutter_attack1.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack1/Woodcutter_attack1 (4).png").convert_alpha()
    ]
    attack2 = [
        pygame.image.load("images/woodcutter/woodcutter_attack2/Woodcutter_attack2.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack2/Woodcutter_attack2 (5).png").convert_alpha()
    ]
    attack3 = [
        pygame.image.load("images/woodcutter/woodcutter_attack3/Woodcutter_attack3_1.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack3/Woodcutter_attack3_2.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack3/Woodcutter_attack3_3.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack3/Woodcutter_attack3_4.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack3/Woodcutter_attack3_5.png").convert_alpha(),
        pygame.image.load("images/woodcutter/woodcutter_attack3/Woodcutter_attack3_6.png").convert_alpha()
    ]
    jump = [
        pygame.image.load("images/woodcutter/jump/Woodcutter_jump.png").convert_alpha(),
        pygame.image.load("images/woodcutter/jump/Woodcutter_jump (1).png").convert_alpha(),
        pygame.image.load("images/woodcutter/jump/Woodcutter_jump (2).png").convert_alpha(),
        pygame.image.load("images/woodcutter/jump/Woodcutter_jump (3).png").convert_alpha(),
        pygame.image.load("images/woodcutter/jump/Woodcutter_jump (4).png").convert_alpha(),
        pygame.image.load("images/woodcutter/jump/Woodcutter_jump (5).png").convert_alpha(),
    ]

    #Sounds

    #Enemy
    m_attack1 = [
        pygame.image.load("images/3 Big bloated/attack_1/Big_bloated_attack1.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_1/Big_bloated_attack1 (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_1/Big_bloated_attack1 (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_1/Big_bloated_attack1 (3).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_1/Big_bloated_attack1 (4).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_1/Big_bloated_attack1 (5).png").convert_alpha(),
    ]
    m_attack2 = [
        pygame.image.load("images/3 Big bloated/attack_2/Big_bloated_attack2.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_2/Big_bloated_attack2 (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_2/Big_bloated_attack2 (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_2/Big_bloated_attack2 (3).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_2/Big_bloated_attack2 (4).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_2/Big_bloated_attack2 (5).png").convert_alpha(),
    ]
    m_attack3 = [
        pygame.image.load("images/3 Big bloated/attack_3/Big_bloated_attack3.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_3/Big_bloated_attack3 (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_3/Big_bloated_attack3 (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_3/Big_bloated_attack3 (3).png").convert_alpha(),
    ]
    m_attack4 = [
        pygame.image.load("images/3 Big bloated/attack_4/Big_bloated_attack4.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_4/Big_bloated_attack4 (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_4/Big_bloated_attack4 (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_4/Big_bloated_attack4 (3).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_4/Big_bloated_attack4 (4).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/attack_4/Big_bloated_attack4 (5).png").convert_alpha(),
    ]
    m_death = [
        pygame.image.load("images/3 Big bloated/death/Big_bloated_death.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/death/Big_bloated_death (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/death/Big_bloated_death (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/death/Big_bloated_death (3).png").convert_alpha(),
    ]
    m_hurt = [
        pygame.image.load("images/3 Big bloated/hurt/Big_bloated_hurt (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/hurt/Big_bloated_hurt (1) (1).png").convert_alpha(),
    ]
    m_idle = [
        pygame.image.load("images/3 Big bloated/idle/Big_bloated_idle.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/idle/Big_bloated_idle (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/idle/Big_bloated_idle (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/idle/Big_bloated_idle (3).png").convert_alpha(),
    ]
    m_sneer = [
        pygame.image.load("images/3 Big bloated/sneer/Big_bloated_sneer.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/sneer/Big_bloated_sneer (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/sneer/Big_bloated_sneer (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/sneer/Big_bloated_sneer (3).png").convert_alpha(),
    ]
    m_walk = [
        pygame.image.load("images/3 Big bloated/walk/Big_bloated_walk.png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/walk/Big_bloated_walk (1).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/walk/Big_bloated_walk (2).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/walk/Big_bloated_walk (3).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/walk/Big_bloated_walk (4).png").convert_alpha(),
        pygame.image.load("images/3 Big bloated/walk/Big_bloated_walk (5).png").convert_alpha(),
    ]
    monster_x = 584
    monster_y = 660
    monster_health = 4

    bg_x = 0

    player_anim_count = 0
    player_speed = 10
    player_acceleration = 1.5
    player_x = 90
    player_y = 700

    jump_count = 3

    is_jump = False
    running = True
    gameplay = True
    motion = False
    player_lost = False
    while running:

        screen.blit(bg, (-10, 0))

        if gameplay:
            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
            monster_rect = m_walk[0].get_rect(topleft=(monster_x + 10, monster_y))
            if player_rect.colliderect(monster_rect):
                gameplay = False
                player_lost = True

            keys = pygame.key.get_pressed()
            motion_buttons = [
                keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_SPACE],
                pygame.mouse.get_pressed()
            ]
            screen.blit(m_walk[player_anim_count % 4], (monster_x, monster_y))
            if monster_health <= 0:
                screen.blit(m_death[player_anim_count % 4], (monster_x, monster_y))
                if player_anim_count % 4 == 0 and player_anim_count != 0:
                    screen.blit(m_death[3], (monster_x, monster_y))
                    gameplay = False
            else:
                monster_x -= 6

            if not is_jump:
                if not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or
                keys[pygame.K_1] or keys[pygame.K_2] or keys[pygame.K_3]):
                    screen.blit(idle[player_anim_count % 4], (player_x, player_y))
                else:
                    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                        screen.blit(walk_left[player_anim_count % 6], (player_x, player_y))
                        bg_x += 2
                    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                        screen.blit(walk_right[player_anim_count % 6], (player_x, player_y))
                        bg_x -= 2
                    elif keys[pygame.K_1]:
                        screen.blit(attack1[player_anim_count % 6], (player_x, player_y))
                    elif keys[pygame.K_2]:
                        screen.blit(attack2[player_anim_count % 6], (player_x, player_y))
                    elif keys[pygame.K_3]:
                        screen.blit(attack3[player_anim_count % 6], (player_x, player_y))
                if keys[pygame.K_SPACE]:
                    is_jump = True
                for i in range(4, 1):
                    if keys[exec(f"pygame.K_{i}")]:
                        screen.blit(exec(f"attack{i}")[player_anim_count % 6], (player_x, player_y))
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
            if monster_x <= player_x + 50:
                if monster_health == 4:
                    screen.blit(m_attack1[player_anim_count % 4], (monster_x, monster_y))
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 20:
                player_x -= player_speed
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x < 1500:
                player_x += player_speed

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        from pause_screen import pause_screen
                        bg_sound.stop()
                        pause_screen(True)
                    if event.key == pygame.K_1:
                        if monster_x - player_x <= 120:
                            monster_health -= 1
                            screen.blit(m_hurt[player_anim_count % 2], (monster_x, monster_y))
                    if event.key == pygame.K_2:
                        if monster_x - player_x <= 120:
                            monster_health -= 2
                            screen.blit(m_hurt[player_anim_count % 2], (monster_x, monster_y))
                    if event.key == pygame.K_3:
                        if monster_x - player_x <= 120:
                            monster_health -= 3
                            screen.blit(m_hurt[player_anim_count % 2], (monster_x, monster_y))

        else:
            from loose_screen import loose_screen
            from win_screen import win_screen
            bg_sound.stop()
            if player_lost:
                gameplay, player_x, player_y, monster_x = loose_screen(True)
                player_lost = False
            else:
                win_screen("level_2")
        pygame.display.update()

        player_anim_count += 1
        clock.tick(15)


if __name__ == "__main__":
    level_3()