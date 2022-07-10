import pygame

pygame.init()  #초기화(반드시 필요)

#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640  #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("JunHyuk Game")  #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("/home/runner/pythongameproject/background.png")

#캐릭터 불러오기
character = pygame.image.load("/home/runner/pythongameproject/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #첫번째값이 가로 크기
character_height = character_size[1] #두번째값이 세로 크기
character_x_pos = (screen_width - character_width) / 2 #화면 가로의 절반 크기에 해당하는 곳에 위치하도록 설정
character_y_pos = screen_height - character_height
#화면 세로 크기 가장 아래에 해당하는 곳에 위치하도록 설정

#pygame에서는 event loop가 실행 되고 있어야 화면이 꺼지지 않는다.
#이벤트 루프
running = True #게임이 진행 중인가?
while running:
  for event in pygame.event.get(): #어떤 이벤트가 발생한다면
    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생한다면
      running = False #게임 진행을 종료
  screen.blit(background, (0, 0)) #왼쪽위 모서리에서부터 background를 그려줌(blit)
  screen.blit(character, (character_x_pos, character_y_pos))  
  #screen.fill((0, 0, 255)) : 화면을 RGB값으로 채워줄 수도 있음
  
  pygame.display.update() #pygame에서는 매순간 배경을 업데이트해야한다.
  
#pygame 종료
pygame.quit()
