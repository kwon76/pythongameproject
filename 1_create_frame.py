import pygame

pygame.init()  #초기화(반드시 필요)

#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640  #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("JunHyuk Game")  #게임 이름

#pygame에서는 event loop가 실행 되고 있어야 화면이 꺼지지 않는다.
#이벤트 루프
running = True #게임이 진행 중인가?
while running:
  for event in pygame.event.get(): #어떤 이벤트가 발생한다면
    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생한다면
      running = False #게임 진행을 종료

#pygame 종료
pygame.quit()
