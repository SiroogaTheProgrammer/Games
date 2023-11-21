import pygame
import random
import math

def main():
    pygame.init()

    display_info = pygame.display.Info()
    width = display_info.current_w
    height = display_info.current_h
    display = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("Bouncing Square and Controllable Rectangles")

    black = (0, 0, 0)
    white = (255, 255, 255)

    rect_width = 50
    rect_height = 150
    rect_speed = 5

    line_color = (100, 100, 100)
    line_thickness = 10
    line_x = (width - line_thickness) // 2

    font = pygame.font.Font("C:/Users/sergtsy/programing/fff-forward.regular.ttf", 60)
    score1 = 0
    score2 = 0

    clock = pygame.time.Clock()

    rect1_x = 100
    rect1_y = (height - rect_height) // 2

    rect2_x = width - rect_width - 100
    rect2_y = (height - rect_height) // 2

    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    square_size = 45
    square_speed = 10
    square_x = (width - square_size) // 2
    square_y = (height - square_size) // 2
    square_velocity = [0, 0]
    launch_timer = 180

    def launch_square(direction):
        nonlocal square_x, square_y, square_velocity, launch_timer
        angle = math.radians(45 * direction)  # 45-degree or -45-degree angle
        square_x = (width - square_size) // 2
        square_y = (height - square_size) // 2
        square_velocity = [square_speed * math.cos(angle), square_speed * math.sin(angle)]
        launch_timer = 180

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            rect1_y -= rect_speed
        if keys[pygame.K_s]:
            rect1_y += rect_speed

        if keys[pygame.K_UP]:
            rect2_y -= rect_speed
        if keys[pygame.K_DOWN]:
            rect2_y += rect_speed

        rect1_y = max(0, min(rect1_y, height - rect_height))
        rect2_y = max(0, min(rect2_y, height - rect_height))

        if launch_timer > 0:
            launch_timer -= 1
        else:
            if square_velocity == [0, 0]:
                launch_square(random.choice([-1, 1]))  # Randomly choose left or right direction

        square_x += square_velocity[0]
        square_y += square_velocity[1]

        # Collision detection and handling with rectangles
        if (rect1_x <= square_x + square_size <= rect1_x + rect_width and
            rect1_y <= square_y + square_size <= rect1_y + rect_height) or \
           (rect2_x <= square_x + square_size <= rect2_x + rect_width and
            rect2_y <= square_y + square_size <= rect2_y + rect_height) or \
           (rect1_x <= square_x <= rect1_x + rect_width and
            rect1_y <= square_y <= rect1_y + rect_height) or \
           (rect2_x <= square_x <= rect2_x + rect_width and
            rect2_y <= square_y <= rect2_y + rect_height):
            # Calculate new velocity based on angle of incidence
            angle_of_incidence = math.atan2(square_velocity[1], square_velocity[0])
            angle_of_reflection = angle_of_incidence - math.pi
            square_velocity = [square_speed * math.cos(angle_of_reflection),
                               -square_speed * math.sin(angle_of_reflection)]

        if square_x <= 0:
            square_x = 0
            square_velocity[0] *= -1
            score2 += 1
            launch_square(random.choice([-1, 1]))
        if square_x >= width - square_size:
            square_x = width - square_size
            square_velocity[0] *= -1
            score1 += 1
            launch_square(random.choice([-1, 1]))
        if square_y <= 0:
            square_y = 0
            square_velocity[1] *= -1
        if square_y >= height - square_size:
            square_y = height - square_size
            square_velocity[1] *= -1

        display.fill(black)

        pygame.draw.line(display, line_color, (line_x, 0), (line_x, height), line_thickness)

        pygame.draw.rect(display, white, (rect1_x, rect1_y, rect_width, rect_height))
        pygame.draw.rect(display, white, (rect2_x, rect2_y, rect_width, rect_height))

        pygame.draw.rect(display, white, (square_x, square_y, square_size, square_size))

        score_text1 = font.render(str(score1), True, white)
        score_text2 = font.render(str(score2), True, white)
        score_x1 = (width - line_thickness) // 4 - score_text1.get_width() // 2
        score_x2 = 3 * (width - line_thickness) // 4 - score_text2.get_width() // 2
        display.blit(score_text1, (score_x1, 20))
        display.blit(score_text2, (score_x2, 20))

        pygame.display.update()

        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
