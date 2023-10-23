import random

import pygame

import functions
import mob
import pistol
import player
import projectile
import shotgun
import wave
import background
import camera
import border
from ReprTraceback import ReprTraceback

ReprTraceback.init()

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BG = (150, 150, 255)
BackGround = background.Background('assets\\background.png', [0, 0])
pygame.transform.scale(BackGround.image, screen.get_size())
directions: list = ["up", "right", "down", "left"]
weapon_specific_projectiles: dict = {"shotgun": {"up": ("shotgun_up_1", "shotgun_up_2"),
                                                 "right": ("shotgun_right_1", "shotgun_right_2"),
                                                 "down": ("shotgun_down_1", "shotgun_down_2"),
                                                 "left": ("shotgun_left_1", "shotgun_left_2")}}
SPAWNENEMY = pygame.USEREVENT
SPAWNWEAPON = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, 3000)
pygame.time.set_timer(SPAWNWEAPON, 5000)
player = player.Player(50, 50, 500, 500, .5, direction="down", health=10,
                       weapon="pistol", weapon_index=0, color="red")
players = pygame.sprite.Group()
player.add(players)
camera = camera.Camera(player)
border = border.Border(camera, player)
camera.setmethod(border)
projectiles = pygame.sprite.Group()
mobs = pygame.sprite.Group()
weapons = pygame.sprite.Group()
default_ammo_count: dict = {"pistol": 50, "shotgun": 50}

text_font = pygame.font.SysFont("Arial", 30)
wave_map: dict = {1: 3, 2: 20, 3: 30}
current_wave = 1
# can potentially create a group for waves in the future. Considering some stages to split players up into their own
new_wave = wave.Wave(current_wave, wave_map[current_wave], 0, wave_map[current_wave], [], False, False)

run = True
while run:
    screen.fill(BG)
    screen.blit(BackGround.image, (0 - camera.offset.x, 0 - camera.offset.y))
    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed, True)
    screen.blit(player.image, (player.pos_x-25, player.pos_y-25))
    # in order to actually have the character in the correct position, I need to adjust the actual player position
    # rather than just the image that appears
    print(player.pos_x, player.pos_y, "single")
    functions.draw_text(player.current_weapon + " bullets remaining: " + str(player.weapon_ammo[player.weapon_index]),
                        text_font, (0, 0, 0), 1150, 25, screen)
    functions.draw_text("Current Health:" + str(player.health), text_font, (0, 0, 0), 1150, 60, screen)
    functions.draw_text("Wave: " + str(new_wave.wave_number), text_font, (0, 0, 0), 700, 25, screen)
    functions.draw_text("Mobs Remaining: " + str(new_wave.mobs_remaining), text_font, (0, 0, 0), 650, 60, screen)
    functions.draw_text("Mobs Spawned: " + str(new_wave.mobs_spawned), text_font, (0, 0, 0), 650, 95, screen)
    players.draw(screen)
    for stuff in players:
        print(stuff.pos_x, stuff.pos_y, "group")
    mobs.update(player)
    mobs.draw(screen)
    projectiles.update()
    projectiles.draw(screen)
    weapons.update()
    weapons.draw(screen)
    new_wave.update()
    camera.scroll()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if keys_pressed[pygame.K_SPACE]:
            char_pos_x, char_pos_y = player.get_position()
            char_direction = player.get_direction()
            if player.weapon_ammo[player.weapon_index] == 0:
                continue
            if player.current_weapon == "pistol":
                proj = projectile.Projectile(char_pos_x, char_pos_y, 10, char_direction, 5, 2, "blue")
                proj.add(projectiles)
            elif player.current_weapon == "shotgun":
                proj1 = projectile.Projectile(char_pos_x, char_pos_y, 10,
                                              weapon_specific_projectiles[player.current_weapon][char_direction][0],
                                              5, 2,
                                              "blue")
                proj2 = projectile.Projectile(char_pos_x, char_pos_y, 10, char_direction, 5, 2, "blue")
                proj3 = projectile.Projectile(char_pos_x, char_pos_y, 10,
                                              weapon_specific_projectiles[player.current_weapon][char_direction][1],
                                              5, 2,
                                              "blue")

                proj1.add(projectiles)
                proj2.add(projectiles)
                proj3.add(projectiles)
            player.weapon_ammo[player.weapon_index] -= 1

        if event.type == pygame.KEYDOWN:
            player.update(event.key, False)

        if event.type == SPAWNENEMY and not new_wave.spawn_complete:
            mob_pos_x, mob_pos_y = random.randint(50, 1450), random.randint(50, 950)
            new_mob = mob.Mob(5, .2, 2, mob_pos_x, mob_pos_y, "white")
            new_mob.add(mobs)
            new_wave.mobs_spawned += 1

        if event.type == SPAWNWEAPON:
            wep_pos_x, wep_pos_y = random.randint(50, 1450), random.randint(50, 950)
            weapon_random_index = random.randint(0, 1)
            if weapon_random_index == 0:
                new_weapon = pistol.Pistol("pistol", 1, 1, 1, 1, 1,
                                           "yellow", wep_pos_x, wep_pos_y)
            elif weapon_random_index == 1:
                new_weapon = shotgun.Shotgun("shotgun", 1, 1, 1, 1, 1,
                                             "pink", wep_pos_x, wep_pos_y)
            new_weapon.add(weapons)

    if new_wave.wave_end:
        current_wave += 1
        print(current_wave, wave_map[current_wave])
        new_wave = wave.Wave(current_wave, wave_map[current_wave], 0, wave_map[current_wave], [], False, False)
    # This will tell me which mob has collided with a bullet
    # make hit_mob go first so mobs aren't appended to a list (causing update errors)
    mob_proj_collision = pygame.sprite.groupcollide(mobs, projectiles, False, True)
    mob_player_collision = pygame.sprite.groupcollide(players, mobs, False, False)
    weapon_player_collision = pygame.sprite.groupcollide(players, weapons, False, False)
    if mob_proj_collision:
        for hit_mob, hit_projectiles in mob_proj_collision.items():
            for hit_projectile in hit_projectiles:
                hit_mob.health -= hit_projectile.damage
            if not hit_mob.alive:
                new_wave.mobs_remaining -= 1
                hit_mob.kill()

    # collision seems to take into account masking, while vectorization doesn't, thus we are "colliding" more than
    # once prior to the rectangle resetting to a farther position. Need to use masking.

    if mob_player_collision:
        for hit_player, hit_mobs in mob_player_collision.items():
            for hit_mob in hit_mobs:
                hit_player.health -= hit_mob.damage
                hit_mob.pos_x += 200
                hit_mob.pos_y += 200
    if not players:
        break

    if weapon_player_collision:
        for cur_player, cur_weapon in weapon_player_collision.items():

            for weapon in cur_weapon:
                weapon_name = weapon.name
                if weapon_name not in cur_player.weapon_map:
                    cur_player.weapon_arsenal.append(weapon_name)
                    cur_player.weapon_ammo.append(default_ammo_count[weapon_name])
                    cur_player.weapon_map[weapon_name] = len(cur_player.weapon_arsenal) - 1
                cur_player.weapon_index = cur_player.weapon_map[weapon_name]
                cur_player.current_weapon = cur_player.weapon_arsenal[cur_player.weapon_index]
                cur_player.weapon_ammo[cur_player.weapon_index] = default_ammo_count[cur_player.current_weapon]
                print(cur_player.current_weapon, cur_player.weapon_arsenal, cur_player.weapon_index)
                weapon.kill()

    pygame.display.flip()

pygame.quit()
