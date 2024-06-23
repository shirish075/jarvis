# from ursina import *
# from ursina.prefabs.first_person_controller import FirstPersonController
# import time
#
# uapp = Ursina(borderless=False)
# player = FirstPersonController()
#
# ground = Entity(model='plane', texture='grass', scale=(100, 1, 100), collider='mesh')
#
# # window.size(400,600)
#
# window.title = 'Jarvis'
# window.size = (500,900)
#
# #
# # mesh = load_model('Mark 42.obj')
# #
# # #create an entity
# # model = Entity(model="Mark 42.obj",texture="Mark 42.mtl",scale=5,position=(2, 0, 2))#(-2,-19.5,0)
# #
# # model.animations = FrameAnimation3d('obj2/untitled', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #                            position=(2, 0, 2))
#
# Sky()
#
# # camera.position = (8.89604, 25.4023, 0)
# # Get the default camera
# # camera.position=(12,5,0)
# camera.position+=(2, 1, 1)
#
#
#
#
# anima = Animator( animations = {
#     "idle":Entity(model="Mark 42.obj",texture='SIGMA/maps/42.png', scale=2, position=(2, 0, 2)),
#     # "hai": FrameAnimation3d('SIGMA/obj2/untitled', fps=35, loop=True, autoplay=True, scale=1000, texture='SIGMA/maps/42.png',
#     #                         position=(2, 0, 2)),
# # "03":FrameAnimation3d('SIGMA/03/03', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Armm Strctig":FrameAnimation3d('SIGMA/Armm Strctig/Armm Strctig', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Dance":FrameAnimation3d('SIGMA/Dance/Dance', fps=35, loop=False, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Dying":FrameAnimation3d('SIGMA/Dying/Dying', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Entry":FrameAnimation3d('SIGMA/Entry/Entry', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Falling":FrameAnimation3d('SIGMA/Falling/Falling', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Flair":FrameAnimation3d('SIGMA/Flair/Flair', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "IDLE":FrameAnimation3d('SIGMA/IDLE/IDLE', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# "L IDLE":FrameAnimation3d('SIGMA/L IDLE/L IDLE', fps=35, loop=False, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#         position=(2, 0, 2)),
# # "Nerviously Looking Around":FrameAnimation3d('SIGMA/Nerviously Looking Around/Nerviously Looking Around', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "New Folder":FrameAnimation3d('SIGMA/New Folder/New Folder', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Phone":FrameAnimation3d('SIGMA/Phone/Phone', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Pointig Forward":FrameAnimation3d('SIGMA/Pointig Forward/Pointig Forward', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Praying":FrameAnimation3d('SIGMA/Praying/Praying', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Sititng Clap":FrameAnimation3d('SIGMA/Sititng Clap/Sititng Clap', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Sititng Talking":FrameAnimation3d('SIGMA/Sititng Talking/Sititng Talking', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Standing":FrameAnimation3d('SIGMA/Standing/Standing', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Standing ClAp":FrameAnimation3d('SIGMA/Standing ClAp/Standing ClAp', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Standing Jump":FrameAnimation3d('SIGMA/Standing Jump/Standing Jump', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Thankful":FrameAnimation3d('SIGMA/Thankful/Thankful', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# "Thinking":FrameAnimation3d('SIGMA/Thinking/Thinking', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#         position=(2, 0, 2)),
# # "Walking":FrameAnimation3d('SIGMA/Walking/Walking', fps=35, loop=False, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "Wave HIP HOP":FrameAnimation3d('SIGMA/Wave HIP HOP/Wave HIP HOP', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2)),
# # "WOBLING":FrameAnimation3d('SIGMA/WOBLING/WOBLING', fps=35, loop=True, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
# #         position=(2, 0, 2))
#
#     })
#
# # anima.state='IDLE'
# # anima.state='Walking'
#
#
#
# # def input(key):
# #     if key == 'p':
# #         # print(camera.position())
# #         print(camera.get_position())
# #
# #         anima.state='dance'
# #     if key=='u':
# #         camera.look_at((2, 10, 2))
#         # print(camera.position())
# #     if key == 'o':
# #         anima.state = 'Thankful'
# #     if key == 'i':
# #         anima.state = 'Pointig Forward'
# #     if key=='k':
# #         anima.state='IDLE'
# #     if key == 'h':
# #         anima.state = 'hai'
#
#
# # def update():
# #     if held_keys['q']:                          # If q is pressed
# #         camera.position += (0, time.dt*5, 0)      # move up vertically
# #         print(time.dt*5)
# #     if held_keys['z']:                          # If z is pressed
# #         camera.position -= (0, time.dt*5, 0)
#
# if __name__ == '__main__':
#     uapp.run()
