import pyautogui as auto
auto.click()
distancia = 200
while distancia > 0:
    print(distancia, 0)
    auto.dragRel(-distancia, 0, duration=1)
    distancia = distancia - 25
    print(0, distancia)
    auto.dragRel(0, distancia, duration=1)
    print(-distancia, 0)
    auto.dragRel(distancia, 0, duration=1)
    distancia = distancia - 25
    print(0, -distancia)
    auto.dragRel(0, -distancia, duration=1)

    anuncios, chat de usuarios
    