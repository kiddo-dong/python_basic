import os
import pygame
pygame.init()
import sys
from button import Button
import random
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
SCREEN = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Slime Pang")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

backmusic = pygame.mixer.Sound("assets/backgroundmusic.wav")
backmusic.set_volume(0.2)
backmusic.play(-1)

def play():
    while True:
        
        stage1 = 0
        # 화면 크기 설정
        screen_width = 800 # 가로 크기
        screen_height = 450 # 세로 크기
        screen = pygame.display.set_mode((screen_width, screen_height))

        # 화면 타이틀 설정
        pygame.display.set_caption("Slime Pang")

        # FPS
        clock = pygame.time.Clock()
        ##############################################################

        # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
        current_path = os.path.dirname("image") # 현재 파일의 위치 반환
        image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

        # 배경 만들기
        background = pygame.image.load(os.path.join(image_path, "background.png"))

        # 스테이지 만들기
        stage = pygame.image.load(os.path.join(image_path, "stage.png"))
        stage_size = stage.get_rect().size
        stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

        # 캐릭터 만들기
        character = pygame.image.load(os.path.join(image_path, "character.png"))
        character_size = character.get_rect().size
        character_width = character_size[0]
        character_height = character_size[1]
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = screen_height - character_height - stage_height

        # 캐릭터 이동 방향
        character_to_x = 0

        # 캐릭터 이동 속도
        character_speed = 10

        # 무기 만들기
        weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
        weapon_size = weapon.get_rect().size
        weapon_width = weapon_size[0]

        # 무기는 한 번에 여러 발 발사 가능
        weapons = []

        # 무기 이동 속도
        weapon_speed = 18

        # 공 만들기 (4개 크기에 대해 따로 처리)
        ball_images = [
            pygame.image.load(os.path.join(image_path, "balloon1.png")),
            pygame.image.load(os.path.join(image_path, "balloon2.png")),
            pygame.image.load(os.path.join(image_path, "balloon3.png")),
            pygame.image.load(os.path.join(image_path, "balloon4.png"))]

        # 공 크기에 따른 최초 스피드
        ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값

        # 공들
        balls = []

        # 최초 발생하는 큰 공 추가
        balls.append({
            "pos_x" : 50, # 공의 x 좌표
            "pos_y" : 50, # 공의 y 좌표
            "img_idx" : 0, # 공의 이미지 인덱스
            "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "to_y": -6, # y축 이동방향,
            "init_spd_y": ball_speed_y[0]})# y 최초 속도

        # 사라질 무기, 공 정보 저장 변수
        weapon_to_remove = -1
        ball_to_remove = -1

        # Font 정의
        game_font = pygame.font.Font(None, 40)
        total_time = 30
        start_ticks = pygame.time.get_ticks() # 시작 시간 정의

        # 게임 종료 메시지 
        # Time Over(시간 초과 실패)
        # Mission Complete(성공)
        # Game Over (캐릭터 공에 맞음, 실패)
        game_result = "Game Over"

        running = True
        while running:
            dt = clock.tick(30)
            
            # 2. 이벤트 처리 (키보드, 마우스 등)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                        character_to_x -= character_speed
                    elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                        character_to_x += character_speed
                    elif event.key == pygame.K_SPACE: # 무기 발사
                        weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                        weapon_y_pos = character_y_pos
                        weapons.append([weapon_x_pos, weapon_y_pos])
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        character_to_x = 0

            # 3. 게임 캐릭터 위치 정의
            character_x_pos += character_to_x

            if character_x_pos < 0:
                character_x_pos = 0
            elif character_x_pos > screen_width - character_width:
                character_x_pos = screen_width - character_width

            # 무기 위치 조정
            # 100, 200 -> 180, 160, 140, ...
            # 500, 200 -> 180, 160, 140, ...
            weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로

            # 천장에 닿은 무기 없애기
            weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
            
            # 공 위치 정의
            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                ball_size = ball_images[ball_img_idx].get_rect().size
                ball_width = ball_size[0]
                ball_height = ball_size[1]

                # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
                if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                    ball_val["to_x"] = ball_val["to_x"] * -1

                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
                if ball_pos_y >= screen_height - stage_height - ball_height:
                    ball_val["to_y"] = ball_val["init_spd_y"]
                else: # 그 외의 모든 경우에는 속도를 증가
                    ball_val["to_y"] += 0.5

                ball_val["pos_x"] += ball_val["to_x"]
                ball_val["pos_y"] += ball_val["to_y"]

            # 4. 충돌 처리

            # 캐릭터 rect 정보 업데이트
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos

            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                # 공 rect 정보 업데이트
                ball_rect = ball_images[ball_img_idx].get_rect()
                ball_rect.left = ball_pos_x
                ball_rect.top = ball_pos_y

                # 공과 캐릭터 충돌 체크
                if character_rect.colliderect(ball_rect):
                    overmusic = pygame.mixer.Sound("assets/over.wav")
                    overmusic.set_volume(0.4)
                    overmusic.play()
                    running = False

                # 공과 무기들 충돌 처리
                for weapon_idx, weapon_val in enumerate(weapons):
                    weapon_pos_x = weapon_val[0]
                    weapon_pos_y = weapon_val[1]

                    # 무기 rect 정보 업데이트
                    weapon_rect = weapon.get_rect()
                    weapon_rect.left = weapon_pos_x
                    weapon_rect.top = weapon_pos_y

                    # 충돌 체크
                    if weapon_rect.colliderect(ball_rect):
                        weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                        ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정

                        pangmusic = pygame.mixer.Sound("assets/Pang_sound.wav")
                        pangmusic.set_volume(0.4)
                        pangmusic.play()

                        # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                        if ball_img_idx < 3:
                            # 현재 공 크기 정보를 가지고 옴
                            ball_width = ball_rect.size[0]
                            ball_height = ball_rect.size[1]

                            # 나눠진 공 정보
                            small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                            small_ball_width = small_ball_rect.size[0]
                            small_ball_height = small_ball_rect.size[1]

                            # 왼쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                            # 오른쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                        break
                else: # 계속 게임을 진행
                    continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
                break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출

            # for 바깥조건:
            #     바깥동작
            #     for 안쪽조건:
            #         안쪽동작
            #         if 충돌하면:
            #             break
            #     else:
            #         continue
            #     break

            # 충돌된 공 or 무기 없애기
            if ball_to_remove > -1:
                del balls[ball_to_remove]
                ball_to_remove = -1

            if weapon_to_remove > -1:
                del weapons[weapon_to_remove]
                weapon_to_remove = -1

            # 모든 공을 없앤 경우 게임 종료 (성공)
            if len(balls) == 0:
                game_result = "Next Stage"
                clearmusic = pygame.mixer.Sound("assets/clear.wav")
                clearmusic.set_volume(0.4)
                clearmusic.play()
                stage1 = 1
                running = False

            # 5. 화면에 그리기
            screen.blit(background, (0, 0))
            
            for weapon_x_pos, weapon_y_pos in weapons:
                screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

            for idx, val in enumerate(balls):
                ball_pos_x = val["pos_x"]
                ball_pos_y = val["pos_y"]
                ball_img_idx = val["img_idx"]
                screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

            screen.blit(stage, (0, screen_height - stage_height))
            screen.blit(character, (character_x_pos, character_y_pos))
            
            # 경과 시간 계산
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
            timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
            screen.blit(timer, (10, 10))

            # 시간 초과했다면
            if total_time - elapsed_time <= 0:
                game_result = "Time Over"
                overmusic = pygame.mixer.Sound("assets/over.wav")
                overmusic.set_volume(0.4)
                overmusic.play()
                running = False

            pygame.display.update()

        # 게임 오버 메시지
        msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
        msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
        screen.blit(msg, msg_rect)
        
        pygame.display.update()
        pygame.time.delay(2000)

        if stage1 == 1 :
            play2()

        main_menu()

def play2():
    while True:
        stage2 = 0
        # 화면 크기 설정
        screen_width = 800 # 가로 크기
        screen_height = 450 # 세로 크기
        screen = pygame.display.set_mode((screen_width, screen_height))

        # 화면 타이틀 설정
        pygame.display.set_caption("Slime Pang")

        # FPS
        clock = pygame.time.Clock()
        ##############################################################

        # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
        current_path = os.path.dirname("image") # 현재 파일의 위치 반환
        image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

        # 배경 만들기
        background = pygame.image.load(os.path.join(image_path, "background2.png"))

        # 스테이지 만들기
        stage = pygame.image.load(os.path.join(image_path, "stage2.png"))
        stage_size = stage.get_rect().size
        stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

        # 캐릭터 만들기
        character = pygame.image.load(os.path.join(image_path, "character.png"))
        character_size = character.get_rect().size
        character_width = character_size[0]
        character_height = character_size[1]
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = screen_height - character_height - stage_height

        # 캐릭터 이동 방향
        character_to_x = 0

        # 캐릭터 이동 속도
        character_speed = 10

        # 무기 만들기
        weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
        weapon_size = weapon.get_rect().size
        weapon_width = weapon_size[0]

        # 무기는 한 번에 여러 발 발사 가능
        weapons = []

        # 무기 이동 속도
        weapon_speed = 18

        #폭탄
        boom_images = [pygame.image.load(os.path.join(image_path, "boom.png"))]
        boom_speed_y = [-12]
        booms = []

        # 공 만들기 (4개 크기에 대해 따로 처리)
        ball_images = [
            pygame.image.load(os.path.join(image_path, "balloon1.png")),
            pygame.image.load(os.path.join(image_path, "balloon2.png")),
            pygame.image.load(os.path.join(image_path, "balloon3.png")),
            pygame.image.load(os.path.join(image_path, "balloon4.png"))]

        # 공 크기에 따른 최초 스피드
        ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값

        # 공들
        balls = []

        # 최초 발생하는 큰 공 추가
        balls.append({
            "pos_x" : 50, # 공의 x 좌표
            "pos_y" : 50, # 공의 y 좌표
            "img_idx" : 0, # 공의 이미지 인덱스
            "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "to_y": -6, # y축 이동방향,
            "init_spd_y": ball_speed_y[0]})# y 최초 속도
        balls.append({
            "pos_x" : 350, # 공의 x 좌표
            "pos_y" : 50, # 공의 y 좌표
            "img_idx" : 0, # 공의 이미지 인덱스
            "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "to_y": -6, # y축 이동방향,
            "init_spd_y": ball_speed_y[0]})# y 최초 속도
        booms.append({
            "b_pos_x" : 350, # 공의 x 좌표
            "b_pos_y" : 50, # 공의 y 좌표
            "b_img_idx" : 0, # 공의 이미지 인덱스
            "b_to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "b_to_y": -6, # y축 이동방향,
            "b_init_spd_y": boom_speed_y[0]})# y 최초 속도

        # 사라질 무기, 공 정보 저장 변수
        weapon_to_remove = -1
        ball_to_remove = -1

        # Font 정의
        game_font = pygame.font.Font(None, 40)
        total_time = 50
        start_ticks = pygame.time.get_ticks() # 시작 시간 정의

        # 게임 종료 메시지 
        # Time Over(시간 초과 실패)
        # Mission Complete(성공)
        # Game Over (캐릭터 공에 맞음, 실패)
        game_result = "Game Over"

        running = True
        while running:
            dt = clock.tick(30)
            
            # 2. 이벤트 처리 (키보드, 마우스 등)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                        character_to_x -= character_speed
                    elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                        character_to_x += character_speed
                    elif event.key == pygame.K_SPACE: # 무기 발사
                        weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                        weapon_y_pos = character_y_pos
                        weapons.append([weapon_x_pos, weapon_y_pos])
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        character_to_x = 0

            # 3. 게임 캐릭터 위치 정의
            character_x_pos += character_to_x

            if character_x_pos < 0:
                character_x_pos = 0
            elif character_x_pos > screen_width - character_width:
                character_x_pos = screen_width - character_width

            # 무기 위치 조정
            # 100, 200 -> 180, 160, 140, ...
            # 500, 200 -> 180, 160, 140, ...
            weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로

            # 천장에 닿은 무기 없애기
            weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

            # 폭탄 위치 정의
            for boom_idx, boom_val in enumerate(booms):
                boom_pos_x = boom_val["b_pos_x"]
                boom_pos_y = boom_val["b_pos_y"]
                boom_img_idx = boom_val["b_img_idx"]

                boom_size = boom_images[boom_img_idx].get_rect().size
                boom_width = boom_size[0]
                boom_height = boom_size[1]

                # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
                if boom_pos_x < 0 or boom_pos_x > screen_width - boom_width:
                    boom_val["b_to_x"] = boom_val["b_to_x"] * -1

                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
                if boom_pos_y >= screen_height - stage_height - boom_height:
                    boom_val["b_to_y"] = boom_val["b_init_spd_y"]
                else: # 그 외의 모든 경우에는 속도를 증가
                    boom_val["b_to_y"] += 0.5

                boom_val["b_pos_x"] += boom_val["b_to_x"]
                boom_val["b_pos_y"] += boom_val["b_to_y"]
            
            # 공 위치 정의
            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                ball_size = ball_images[ball_img_idx].get_rect().size
                ball_width = ball_size[0]
                ball_height = ball_size[1]

                # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
                if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                    ball_val["to_x"] = ball_val["to_x"] * -1

                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
                if ball_pos_y >= screen_height - stage_height - ball_height:
                    ball_val["to_y"] = ball_val["init_spd_y"]
                else: # 그 외의 모든 경우에는 속도를 증가
                    ball_val["to_y"] += 0.5

                ball_val["pos_x"] += ball_val["to_x"]
                ball_val["pos_y"] += ball_val["to_y"]

            # 4. 충돌 처리

            # 캐릭터 rect 정보 업데이트
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos

            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                # 공 rect 정보 업데이트
                ball_rect = ball_images[ball_img_idx].get_rect()
                ball_rect.left = ball_pos_x
                ball_rect.top = ball_pos_y

                # 공과 캐릭터 충돌 체크
                if character_rect.colliderect(ball_rect):
                    overmusic = pygame.mixer.Sound("assets/over.wav")
                    overmusic.set_volume(0.4)
                    overmusic.play()
                    running = False

                #폭탄 정보 업뎃
                boom_rect = boom_images[boom_img_idx].get_rect()
                boom_rect.left = boom_pos_x
                boom_rect.top = boom_pos_y
                
                if character_rect.colliderect(boom_rect):
                    boommusic = pygame.mixer.Sound("assets/boomsound.wav")
                    boommusic.set_volume(0.5)
                    boommusic.play()
                    overmusic = pygame.mixer.Sound("assets/over.wav")
                    overmusic.set_volume(0.4)
                    overmusic.play()
                    running = False


                # 공과 무기들 충돌 처리
                for weapon_idx, weapon_val in enumerate(weapons):
                    weapon_pos_x = weapon_val[0]
                    weapon_pos_y = weapon_val[1]

                    # 무기 rect 정보 업데이트
                    weapon_rect = weapon.get_rect()
                    weapon_rect.left = weapon_pos_x
                    weapon_rect.top = weapon_pos_y

                    if weapon_rect.colliderect(boom_rect):
                        boommusic = pygame.mixer.Sound("assets/boomsound.wav")
                        boommusic.set_volume(0.5)
                        boommusic.play()
                        overmusic = pygame.mixer.Sound("assets/over.wav")
                        overmusic.set_volume(0.4)
                        overmusic.play()
                        running = False

                    # 충돌 체크
                    if weapon_rect.colliderect(ball_rect):
                        weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                        ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정

                        pangmusic = pygame.mixer.Sound("assets/Pang_sound.wav")
                        pangmusic.set_volume(0.4)
                        pangmusic.play()

                        # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                        if ball_img_idx < 3:
                            # 현재 공 크기 정보를 가지고 옴
                            ball_width = ball_rect.size[0]
                            ball_height = ball_rect.size[1]

                            # 나눠진 공 정보
                            small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                            small_ball_width = small_ball_rect.size[0]
                            small_ball_height = small_ball_rect.size[1]

                            # 왼쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                            # 오른쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                        break
                else: # 계속 게임을 진행
                    continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
                break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출

            # for 바깥조건:
            #     바깥동작
            #     for 안쪽조건:
            #         안쪽동작
            #         if 충돌하면:
            #             break
            #     else:
            #         continue
            #     break

            # 충돌된 공 or 무기 없애기
            if ball_to_remove > -1:
                del balls[ball_to_remove]
                ball_to_remove = -1

            if weapon_to_remove > -1:
                del weapons[weapon_to_remove]
                weapon_to_remove = -1

            # 모든 공을 없앤 경우 게임 종료 (성공)
            if len(balls) == 0:
                game_result = "Final Stage"
                clearmusic = pygame.mixer.Sound("assets/clear.wav")
                clearmusic.set_volume(0.4)
                clearmusic.play()
                stage2 = 1
                running = False

            # 5. 화면에 그리기
            screen.blit(background, (0, 0))
            
            for weapon_x_pos, weapon_y_pos in weapons:
                screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

            for idx, val in enumerate(balls):
                ball_pos_x = val["pos_x"]
                ball_pos_y = val["pos_y"]
                ball_img_idx = val["img_idx"]
                screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

            for idx, val in enumerate(booms):
                boom_pos_x = val["b_pos_x"]
                boom_pos_y = val["b_pos_y"]
                boom_img_idx = val["b_img_idx"]
                screen.blit(boom_images[boom_img_idx], (boom_pos_x, boom_pos_y))

            screen.blit(stage, (0, screen_height - stage_height))
            screen.blit(character, (character_x_pos, character_y_pos))
            
            # 경과 시간 계산
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
            timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
            screen.blit(timer, (10, 10))

            # 시간 초과했다면
            if total_time - elapsed_time <= 0:
                game_result = "Time Over"
                overmusic = pygame.mixer.Sound("assets/over.wav")
                overmusic.set_volume(0.4)
                overmusic.play()
                running = False

            pygame.display.update()

        # 게임 오버 메시지
        msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
        msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
        screen.blit(msg, msg_rect)
        
        pygame.display.update()
        pygame.time.delay(2000)

        if stage2 == 1 :
            play3()

        main_menu()

def play3():
    while True:
        # 화면 크기 설정
        screen_width = 800 # 가로 크기
        screen_height = 450 # 세로 크기
        screen = pygame.display.set_mode((screen_width, screen_height))

        # 화면 타이틀 설정
        pygame.display.set_caption("Slime Pang")

        # FPS
        clock = pygame.time.Clock()
        ##############################################################

        # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
        current_path = os.path.dirname("image") # 현재 파일의 위치 반환
        image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

        # 배경 만들기
        background = pygame.image.load(os.path.join(image_path, "background3.png"))

        # 스테이지 만들기
        stage = pygame.image.load(os.path.join(image_path, "stage3.png"))
        stage_size = stage.get_rect().size
        stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

        # 캐릭터 만들기
        character = pygame.image.load(os.path.join(image_path, "character.png"))
        character_size = character.get_rect().size
        character_width = character_size[0]
        character_height = character_size[1]
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = screen_height - character_height - stage_height

        # 캐릭터 이동 방향
        character_to_x = 0

        # 캐릭터 이동 속도
        character_speed = 10

        # 무기 만들기
        weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
        weapon_size = weapon.get_rect().size
        weapon_width = weapon_size[0]

        # 무기는 한 번에 여러 발 발사 가능
        weapons = []

        # 무기 이동 속도
        weapon_speed = 18

        #폭탄
        boom_images = [pygame.image.load(os.path.join(image_path, "boom.png"))]
        boom_speed_y = [-12]
        booms = []

        # 공 만들기 (4개 크기에 대해 따로 처리)
        ball_images = [
            pygame.image.load(os.path.join(image_path, "balloon1.png")),
            pygame.image.load(os.path.join(image_path, "balloon2.png")),
            pygame.image.load(os.path.join(image_path, "balloon3.png")),
            pygame.image.load(os.path.join(image_path, "balloon4.png"))]

        # 공 크기에 따른 최초 스피드
        ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값

        # 공들
        balls = []

        # 최초 발생하는 큰 공 추가
        balls.append({
            "pos_x" : 50, # 공의 x 좌표
            "pos_y" : 50, # 공의 y 좌표
            "img_idx" : 0, # 공의 이미지 인덱스
            "to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "to_y": -6, # y축 이동방향,
            "init_spd_y": ball_speed_y[0]})# y 최초 속도
        balls.append({
            "pos_x" : 600, # 공의 x 좌표
            "pos_y" : 00, # 공의 y 좌표
            "img_idx" : 0, # 공의 이미지 인덱스
            "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "to_y": -6, # y축 이동방향,
            "init_spd_y": ball_speed_y[0]})# y 최초 속도
        booms.append({
            "b_pos_x" : 350, # 공의 x 좌표
            "b_pos_y" : 50, # 공의 y 좌표
            "b_img_idx" : 0, # 공의 이미지 인덱스
            "b_to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "b_to_y": -6, # y축 이동방향,
            "b_init_spd_y": boom_speed_y[0]})# y 최초 속도
        booms.append({
            "b_pos_x" : 150, # 공의 x 좌표
            "b_pos_y" : 50, # 공의 y 좌표
            "b_img_idx" : 0, # 공의 이미지 인덱스
            "b_to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "b_to_y": -6, # y축 이동방향,
            "b_init_spd_y": boom_speed_y[0]})# y 최초 속도

        # 사라질 무기, 공 정보 저장 변수
        weapon_to_remove = -1
        ball_to_remove = -1

        # Font 정의
        game_font = pygame.font.Font(None, 40)
        total_time = 80
        start_ticks = pygame.time.get_ticks() # 시작 시간 정의

        # 게임 종료 메시지 
        # Time Over(시간 초과 실패)
        # Mission Complete(성공)
        # Game Over (캐릭터 공에 맞음, 실패)
        game_result = "Game Over"

        running = True
        while running:
            dt = clock.tick(30)
            
            # 2. 이벤트 처리 (키보드, 마우스 등)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                        character_to_x -= character_speed
                    elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                        character_to_x += character_speed
                    elif event.key == pygame.K_SPACE: # 무기 발사
                        weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                        weapon_y_pos = character_y_pos
                        weapons.append([weapon_x_pos, weapon_y_pos])
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        character_to_x = 0

            # 3. 게임 캐릭터 위치 정의
            character_x_pos += character_to_x

            if character_x_pos < 0:
                character_x_pos = 0
            elif character_x_pos > screen_width - character_width:
                character_x_pos = screen_width - character_width

            # 무기 위치 조정
            # 100, 200 -> 180, 160, 140, ...
            # 500, 200 -> 180, 160, 140, ...
            weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로

            # 천장에 닿은 무기 없애기
            weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
            
            # 폭탄 위치 정의
            for boom_idx, boom_val in enumerate(booms):
                boom_pos_x = boom_val["b_pos_x"]
                boom_pos_y = boom_val["b_pos_y"]
                boom_img_idx = boom_val["b_img_idx"]

                boom_size = boom_images[boom_img_idx].get_rect().size
                boom_width = boom_size[0]
                boom_height = boom_size[1]

                # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
                if boom_pos_x < 0 or boom_pos_x > screen_width - boom_width:
                    boom_val["b_to_x"] = boom_val["b_to_x"] * -1

                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
                if boom_pos_y >= screen_height - stage_height - boom_height:
                    boom_val["b_to_y"] = boom_val["b_init_spd_y"]
                else: # 그 외의 모든 경우에는 속도를 증가
                    boom_val["b_to_y"] += 0.5

                boom_val["b_pos_x"] += boom_val["b_to_x"]
                boom_val["b_pos_y"] += boom_val["b_to_y"]


            # 공 위치 정의
            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                ball_size = ball_images[ball_img_idx].get_rect().size
                ball_width = ball_size[0]
                ball_height = ball_size[1]

                # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
                if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                    ball_val["to_x"] = ball_val["to_x"] * -1

                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
                if ball_pos_y >= screen_height - stage_height - ball_height:
                    ball_val["to_y"] = ball_val["init_spd_y"]
                else: # 그 외의 모든 경우에는 속도를 증가
                    ball_val["to_y"] += 0.5

                ball_val["pos_x"] += ball_val["to_x"]
                ball_val["pos_y"] += ball_val["to_y"]




            # 4. 충돌 처리

            # 캐릭터 rect 정보 업데이트
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos

            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                # 공 rect 정보 업데이트
                ball_rect = ball_images[ball_img_idx].get_rect()
                ball_rect.left = ball_pos_x
                ball_rect.top = ball_pos_y

                # 공과 캐릭터 충돌 체크
                if character_rect.colliderect(ball_rect):
                    overmusic = pygame.mixer.Sound("assets/over.wav")
                    overmusic.set_volume(0.4)
                    overmusic.play()
                    running = False

                #폭탄 정보 업뎃
                boom_rect = boom_images[boom_img_idx].get_rect()
                boom_rect.left = boom_pos_x
                boom_rect.top = boom_pos_y
                
                if character_rect.colliderect(boom_rect):
                    boommusic = pygame.mixer.Sound("assets/boomsound.wav")
                    boommusic.set_volume(0.5)
                    boommusic.play()
                    overmusic = pygame.mixer.Sound("assets/over.wav")
                    overmusic.set_volume(0.4)
                    overmusic.play()
                    running = False


                # 공과 무기들 충돌 처리
                for weapon_idx, weapon_val in enumerate(weapons):
                    weapon_pos_x = weapon_val[0]
                    weapon_pos_y = weapon_val[1]

                    # 무기 rect 정보 업데이트
                    weapon_rect = weapon.get_rect()
                    weapon_rect.left = weapon_pos_x
                    weapon_rect.top = weapon_pos_y

                    if weapon_rect.colliderect(boom_rect):
                        boommusic = pygame.mixer.Sound("assets/boomsound.wav")
                        boommusic.set_volume(0.5)
                        boommusic.play()
                        overmusic = pygame.mixer.Sound("assets/over.wav")
                        overmusic.set_volume(0.4)
                        overmusic.play()
                        running = False
                        
                    # 충돌 체크
                    if weapon_rect.colliderect(ball_rect):
                        weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                        ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정

                        pangmusic = pygame.mixer.Sound("assets/Pang_sound.wav")
                        pangmusic.set_volume(0.4)
                        pangmusic.play()
        
                        # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                        if ball_img_idx < 3:
                            # 현재 공 크기 정보를 가지고 옴
                            ball_width = ball_rect.size[0]
                            ball_height = ball_rect.size[1]

                                # 나눠진 공 정보
                            small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                            small_ball_width = small_ball_rect.size[0]
                            small_ball_height = small_ball_rect.size[1]

                                # 왼쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                                # 오른쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                            if random.random() < 0.1: 
                                booms.append({
                                    "b_pos_x" : 150, # 공의 x 좌표
                                    "b_pos_y" : 50, # 공의 y 좌표
                                    "b_img_idx" : 0, # 공의 이미지 인덱스
                                    "b_to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                    "b_to_y": -6, # y축 이동방향,
                                    "b_init_spd_y": boom_speed_y[0]})# y 최초 속도
                            if random.random() < 0.1: 
                                booms.append({
                                    "b_pos_x" : 600, # 공의 x 좌표
                                    "b_pos_y" : 50, # 공의 y 좌표
                                    "b_img_idx" : 0, # 공의 이미지 인덱스
                                    "b_to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                    "b_to_y": -6, # y축 이동방향,
                                    "b_init_spd_y": boom_speed_y[0]})# y 최초 속도

                            

                        break
                else: # 계속 게임을 진행
                    continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
                break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출

            # for 바깥조건:
            #     바깥동작
            #     for 안쪽조건:
            #         안쪽동작
            #         if 충돌하면:
            #             break
            #     else:
            #         continue
            #     break

            # 충돌된 공 or 무기 없애기
            if ball_to_remove > -1:
                del balls[ball_to_remove]
                ball_to_remove = -1

            if weapon_to_remove > -1:
                del weapons[weapon_to_remove]
                weapon_to_remove = -1

            # 모든 공을 없앤 경우 게임 종료 (성공)
            if len(balls) == 0:
                game_result = "Game Clear"
                clearmusic = pygame.mixer.Sound("assets/clear.wav")
                clearmusic.set_volume(0.4)
                clearmusic.play()
                running = False

            # 5. 화면에 그리기
            screen.blit(background, (0, 0))
            
            for weapon_x_pos, weapon_y_pos in weapons:
                screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

            for idx, val in enumerate(balls):
                ball_pos_x = val["pos_x"]
                ball_pos_y = val["pos_y"]
                ball_img_idx = val["img_idx"]
                screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

            for idx, val in enumerate(booms):
                boom_pos_x = val["b_pos_x"]
                boom_pos_y = val["b_pos_y"]
                boom_img_idx = val["b_img_idx"]
                screen.blit(boom_images[boom_img_idx], (boom_pos_x, boom_pos_y))

            screen.blit(stage, (0, screen_height - stage_height))
            screen.blit(character, (character_x_pos, character_y_pos))
            
            # 경과 시간 계산
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
            timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
            screen.blit(timer, (10, 10))

            # 시간 초과했다면
            if total_time - elapsed_time <= 0:
                game_result = "Time Over"
                overmusic = pygame.mixer.Sound("assets/over.wav")
                overmusic.set_volume(0.4)
                overmusic.play()
                running = False
            pygame.display.update()

        # 게임 오버 메시지
        msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
        msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
        screen.blit(msg, msg_rect)
        
        pygame.display.update()
        pygame.time.delay(2000)


        main_menu()


    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))



        OPTIONS_TEXT = get_font(25).render("How To Play.", True, "#b68f40")

        font1 = pygame.font.Font("assets/휴먼아미체.ttf", 30)
        OPTIONS_TEXT1 = font1.render('캐릭터를 방향키(←, →)와 스페이스바(space bar)로', True, "black")
        OPTIONS_TEXT2 = font1.render('조작하며 슬라임을 없애면 이기는 게임입니다.', True, "black")
        OPTIONS_TEXT3 = font1.render('중간중간 나타나는 폭탄을 터트리거나,', True, "black")
        OPTIONS_TEXT4 = font1.render('폭탄,  슬라임과 캐릭터가 닿으면 게임오버 됩니다.', True, "black")

        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 90))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(400, 150))
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)

        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(400, 185))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(400, 215))
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

        OPTIONS_RECT4 = OPTIONS_TEXT4.get_rect(center=(400, 245))
        SCREEN.blit(OPTIONS_TEXT4, OPTIONS_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(640, 400), 
                            text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("Slime Pang", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 90))
 
        PLAY_BUTTON = Button(image=pygame.image.load("assets/bar.png"), pos=(400, 150), 
                            text_input="PLAY", font=get_font(15), base_color="black", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/bar.png"), pos=(400, 250), 
                            text_input="How To Play", font=get_font(15), base_color="black", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/bar.png"), pos=(400, 350), 
                            text_input="QUIT", font=get_font(15), base_color="black", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()