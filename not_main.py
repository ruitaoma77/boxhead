import random

import pygame

import mob
import pistol
import player
import projectile
import shotgun
from  ReprTraceback import ReprTraceback
ReprTraceback.init()

pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

BG = (100, 100, 255)
directions = ["up", "right", "down", "left"]
SPAWNENEMY = pygame.USEREVENT
SPAWNWEAPON = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, 3000)
pygame.time.set_timer(SPAWNWEAPON, 5000)
player = player.Player(50, 50, 500, 500, 0.5, direction="down", health=5,
                       weapon="pistol", weapon_index=0, color="red")
players = pygame.sprite.Group()
player.add(players)
# define keys_pressed earlier to make sure it's redefined before use
keys_pressed = -1
projectiles = pygame.sprite.Group()
mobs = pygame.sprite.Group()
weapons = pygame.sprite.Group()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
run = True
while run:

    screen.fill(BG)
    players.draw(screen)
    mobs.update(player)
    mobs.draw(screen)
    projectiles.update()
    projectiles.draw(screen)
    weapons.update()
    weapons.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if keys_pressed != -1 and keys_pressed[pygame.K_SPACE]:
            char_pos_x, char_pos_y = player.get_position()
            char_direction = player.get_direction()
            if player.current_weapon == "pistol":
                proj = projectile.Projectile(char_pos_x, char_pos_y, 10, char_direction, 5, 2, "black")
                proj.add(projectiles)
            elif player.current_weapon == "shotgun":
                proj1 = projectile.Projectile(char_pos_x, char_pos_y, 10, directions[(directions.index(char_direction) + 1) % 4], 5, 2,
                                              "black")
                proj2 = projectile.Projectile(char_pos_x, char_pos_y, 10, char_direction, 5, 2, "black")
                proj3 = projectile.Projectile(char_pos_x, char_pos_y, 10, directions[(directions.index(char_direction) - 1) % 4], 5, 2,
                                              "black")
                proj1.add(projectiles)
                proj2.add(projectiles)
                proj3.add(projectiles)

        if event.type == SPAWNENEMY:
            mob_pos_x, mob_pos_y = random.randint(50, 1450), random.randint(50, 950)
            new_mob = mob.Mob(5, .2, 2, mob_pos_x, mob_pos_y, "white")
            new_mob.add(mobs)

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

    # This will tell me which mob has collided with a bullet
    # make hit_mob go first so mobs aren't appended to a list (causing update errors)
    mob_proj_collision = pygame.sprite.groupcollide(mobs, projectiles, False, True)
    mob_player_collision = pygame.sprite.groupcollide(players, mobs, False, False)
    weapon_player_collision = pygame.sprite.groupcollide(players, weapons, False, False)
    if mob_proj_collision:
        for hit_mob, hit_projectiles in mob_proj_collision.items():
            for hit_projectile in hit_projectiles:
                hit_mob.health -= hit_projectile.damage

    # collision seems to take into account masking, while vectorization doesn't, thus we are "colliding" more than
    # once prior to the rectangle resetting to a farther position. Need to use masking.
    '''
    if mob_player_collision:
        for hit_player, hit_mobs in mob_player_collision.items():
            for hit_mob in hit_mobs:
                hit_player.health -= hit_mob.damage
    if not players:
        break
    '''
    if weapon_player_collision:
        for cur_player, cur_weapon in weapon_player_collision.items():

            for weapon in cur_weapon:
                weapon_name = weapon.name
                if weapon_name not in cur_player.weapon_map:
                    cur_player.weapon_arsenal.append(weapon_name)
                    cur_player.weapon_map[weapon_name] = len(cur_player.weapon_arsenal)-1
                cur_player.weapon_index = cur_player.weapon_map[weapon_name]
                cur_player.current_weapon = cur_player.weapon_arsenal[cur_player.weapon_index]
                print(cur_player.current_weapon, cur_player.weapon_arsenal, cur_player.weapon_index)
                weapon.kill()

    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed)

    pygame.display.flip()

pygame.quit()
