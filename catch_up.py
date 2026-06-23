from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
display.set_icon(image.load('Media/run.png'))

#задай фон сцены
background = transform.scale(image.load("Media/background.png"), (700, 500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load("Media/sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("Media/sprite2.png"), (100, 100))

game = True
#обработай событие «клик по кнопке "Закрыть окно"»

clock = time.Clock()

x1 = 100
y1 = 100
x2 = 500
y2 = 200

while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    keys = key.get_pressed()

    if keys[K_UP] and y1 > 5:
        y1 -= 10
    if keys[K_DOWN] and y1 < 345:
        y1 += 10
    if keys[K_LEFT] and x1 > 5:
        x1 -= 10
    if keys[K_RIGHT] and x1 < 595:
        x1 += 10

    if keys[K_w] and y2 > 5:
        y2 -= 10
    if keys[K_s] and y2 < 345:
        y2 += 10
    if keys[K_a] and x2 > 5:
        x2 -= 10
    if keys[K_d] and x2 < 595:
        x2 += 10

    for events in event.get():
        if events.type == QUIT:
            game = False
    
    clock.tick(40)
    display.update()