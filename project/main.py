import pygame as pg
import moderngl as mgl
import numpy as np
import glm

import struct
import inspect
import os
import sys



def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            return True
    return False

def main():
    #соотнощение окна
    sWidth, sHeight = 500, 500
    #смотрим в текущую директорию скрипта
    os.chdir(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)))

    # init pygame modules
    pg.init()
    pg.display.set_caption('Guitar model')
    # set opengl attr
    pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
    pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
    pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
    # create opengl context
    pg.display.set_mode((sWidth, sHeight), flags=pg.OPENGL | pg.DOUBLEBUF)
    # detect and use existing opengl context 
    gl = mgl.create_context()

    #загружаем шейдеры, создаем программу
    program = None
    with open('vert.c', 'r') as vShade:
        with open('frag.c', 'r') as fShade:
            program = gl.program( 
                vertex_shader   = vShade.read(),
                fragment_shader = fShade.read()
            )
    
    #инициализация состояния
    gl.enable(flags=mgl.DEPTH_TEST) # | mgl.CULL_FACE

    #загрузка и распаковка данных модели
    modelName = 'guitar'
    varCount = os.path.getsize('{}.bin'.format(modelName)) 
    data = None
    result = []
    with open('{}.bin'.format(modelName), 'rb') as file:
        data = file.read()

    cursor = 0
    while cursor != varCount:
        result.append(struct.unpack('ffffffff', data[cursor:cursor+32]))
        cursor+=32
    #загрузка текстуры
    texture = pg.image.load('{}.png'.format(modelName)).convert()
    texture = gl.texture(
        size = texture.get_size(), 
        components=3,
        data=pg.image.tostring(texture, 'RGB')
    )
    program['tex'] = 0
    texture.use()

    #загрузка данных в программу
    vbo = gl.buffer(
        #triangle --- [(-1.0, -1.0, -0.5),(1.0, -1.0, -0.5),(0.0, 1.0, -0.5)]
        np.array(result, dtype='f4')
    )
    vao = gl.vertex_array(program, [(vbo, '3f 3f 2f', 'glVertex', 'glNormal', 'glTexCoord')])

    #преобразования
    mPerspective = glm.perspective(glm.radians(50), sWidth/sHeight, 1.0, 10.0)
    mModel= glm.mat4()#glm.translate(glm.mat4(), glm.vec3(0.0, -2.0, 0))
    mView = glm.lookAt(
        glm.vec3(0.0, 1.75, 4.0),
        glm.vec3(0.0, 1.75, 0.0),
        glm.vec3(0.0, 1.0, 0.0)
    )
    #инициализация переменных шейдерных программ
    program['mPerspective'] .write(mPerspective)
    program['mView']        .write(mView)
    program['mModel']       .write(mModel)
    program['vLightPos']    .value = 1.0, 1.0, 1.0, 1.0
    
    frameRate = 45
    rotDeg  = 5/frameRate/2
    clock = pg.time.Clock()
    while True:
        time  = pg.time.get_ticks()
        if check_events():
            break
        
        mModel = glm.rotate(mModel, rotDeg, glm.vec3(0.0, 1.0, 0.0))
        program['mModel'].write(mModel)

        gl.clear(color=(0.70, 0.70, 0.70))
        vao.render()
        pg.display.flip()

        clock.tick(frameRate)
        # 50 frame per sec
        #while pg.time.get_ticks() - time < 20:
        #    pass

    #высвобождение памяти
    pg.quit()
    vao     .release()
    program .release()
    vbo     .release()


if __name__ == '__main__':
    main()
    
