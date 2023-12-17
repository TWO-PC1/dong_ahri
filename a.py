import pygame
import sys
import math

# 초기화
pygame.init()

# 창 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Engine with Shockwaves")

class Ball:
    def __init__(self, x, y, radius, color, level):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.level = level
        self.speed_x = 0
        self.speed_y = 0

    def update(self, gravity, air_resistance):
        # 중력 적용
        self.speed_y += gravity

        # 공기 저항 적용
        self.speed_x *= air_resistance
        self.speed_y *= air_resistance

        self.y += self.speed_y
        self.x += self.speed_x

        # 바운스 처리
        if self.y >= height - self.radius:
            self.y = height - self.radius
            self.speed_y = -self.speed_y * 0.75  # 바운스 효과 및 에너지 감소

        if self.x >= width - self.radius:
            self.x = width - self.radius
            self.speed_x = -self.speed_x * 0.95  # 우측 벽에 부딪힐 때 속도 감소
        elif self.x <= self.radius:
            self.x = self.radius
            self.speed_x = -self.speed_x * 0.95  # 좌측 벽에 부딪힐 때 속도 감소

    def check_collision(self, other_ball):
        # 두 공 간의 거리 계산
        distance = math.sqrt((self.x - other_ball.x)**2 + (self.y - other_ball.y)**2)

        # 충돌한 경우
        if distance < self.radius + other_ball.radius:
            angle = math.atan2(self.y - other_ball.y, self.x - other_ball.x)
            total_speed = math.hypot(self.speed_x, self.speed_y)

            # 충돌 지점의 각도에 따라 틀기의 방향을 조절
            self.speed_x = total_speed * math.cos(angle)
            self.speed_y = total_speed * math.sin(angle)

            other_ball.angle = angle + math.pi
            other_ball.speed_x = total_speed * math.cos(other_ball.angle)
            other_ball.speed_y = total_speed * math.sin(other_ball.angle)

            # 충돌 지점을 벗어나도록 보정
            overlap = self.radius + other_ball.radius - distance
            self.x += math.cos(angle) * overlap * 0.5
            self.y += math.sin(angle) * overlap * 0.5
            other_ball.x -= math.cos(angle) * overlap * 0.5
            other_ball.y -= math.sin(angle) * overlap * 0.5

            # 레벨 업 및 색과 크기 변경
            if self.level == other_ball.level:
                new_level = self.level + 1
                new_color = (min(255, self.color[0] + 30), min(255, self.color[1] + 30), min(255, self.color[2] + 30))
                new_radius = self.radius + 5

                # 새로운 공 추가
                new_ball = Ball(self.x, self.y, new_radius, new_color, new_level)
                new_ball.speed_x = (self.speed_x + other_ball.speed_x) / 2
                new_ball.speed_y = (self.speed_y + other_ball.speed_y) / 2

                # 기존의 두 공 제거
                balls.remove(self)
                balls.remove(other_ball)

                # 새로운 공 추가
                balls.append(new_ball)

                # 충격파 효과
                self.apply_shockwave()
                other_ball.apply_shockwave()

    def apply_shockwave(self):
        # 충격파 적용
        for ball in balls:
            distance = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
            if distance > 0 and distance < 100 and ball != self:
                angle = math.atan2(self.y - ball.y, self.x - ball.x)
                speed = 5 / distance  # 조절 가능한 충격파 속도
                ball.speed_x += speed * math.cos(angle)
                ball.speed_y += speed * math.sin(angle)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# 초기 공 설정
balls = [Ball(width // 2, height // 2, 20, (255, 0, 0), 1)]
gravity = 0.5
air_resistance = 0.99  # 공기 저항 계수

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 새로운 공 추가
            new_ball = Ball(pygame.mouse.get_pos()[0], 0, 20, (0, 0, 255), 1)
            balls.append(new_ball)

    # 각 공 업데이트
    for ball in balls:
        ball.update(gravity, air_resistance)

    # 다른 공들과의 충돌 검사
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if i < len(balls) and j < len(balls):
                balls[i].check_collision(balls[j])
    # 화면 초기화
    screen.fill((0, 0, 0))

    # 각 공 그리기
    for ball in balls:
        ball.draw()

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 제한
    clock.tick(60)
