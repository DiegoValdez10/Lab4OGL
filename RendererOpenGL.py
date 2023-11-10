import pygame as pg
from pygame.locals import *
from OpenGL.GL import glReadPixels, GL_RGB, GL_UNSIGNED_BYTE, GL_TRUE

from gl import Renderer
from Model import Model
from shaders import vertexShader, fragmentShader, customShader1, customShader2, customShader3

width = 960
height = 960

pg.init()

screen = pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF)
clock = pg.time.Clock()

renderer = Renderer(screen)

# Lista de shaders disponibles
shaders = [vertexShader, fragmentShader, customShader1, customShader2, customShader3]
current_shader_index = 0

renderer.setShader(*shaders[current_shader_index])

renderer.loadModel(filename="umbreonHighPoly.obj",
                   textureFile="umbreon.bmp",
                   position=(0, 0, -3),
                   rotation=(0, 45, 0),
                   scale=(1, 1, 1))

speed = 1
isRunning = True
while isRunning:
    keys = pg.key.get_pressed()
    deltaTime = clock.tick(50) / 20

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isRunning = False
            elif event.key == pg.K_SPACE:
                size = screen.get_size()
                buffer = glReadPixels(0, 0, *size, GL_RGB, GL_UNSIGNED_BYTE)
                pg.display.flip()
                screen_surf = pg.image.fromstring(buffer, size, "RGB", GL_TRUE)
                pg.image.save(screen_surf, "output.jpg")
            elif event.key in [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5]:
                # Cambiar el shader con las teclas numéricas (1, 2, 3, ...)
                current_shader_index = int(event.unicode) - 1
                renderer.setShader(*shaders[current_shader_index])

    if keys[K_RIGHT]:
        renderer.camPosition.x += deltaTime * speed
    elif keys[K_LEFT]:
        renderer.camPosition.x -= deltaTime * speed
    if keys[K_UP]:
        renderer.camPosition.y += deltaTime * speed
    elif keys[K_DOWN]:
        renderer.camPosition.y -= deltaTime * speed
    if keys[K_MINUS]:
        renderer.camPosition.z += deltaTime * speed
    elif keys[K_PERIOD]:
        renderer.camPosition.z -= deltaTime * speed

    if keys[K_a]:
        renderer.camRotation.y += deltaTime * speed ** 2
    elif keys[K_d]:
        renderer.camRotation.y -= deltaTime * speed ** 2
    if keys[K_w]:
        renderer.camRotation.x += deltaTime * speed ** 2
    elif keys[K_s]:
        renderer.camRotation.x -= deltaTime * speed ** 2

    renderer.render()
    pg.display.flip()

pg.quit()