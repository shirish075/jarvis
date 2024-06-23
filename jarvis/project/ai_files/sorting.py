import os

mfldr = 'SIGMA'
k = ['03', 'Armm Strctig', 'Dance', 'Dying', 'Entry', 'Falling', 'Flair', 'IDLE', 'L IDLE', 'Nerviously Looking Around',
     'New Folder', 'Phone', 'Pointig Forward', 'Praying', 'Sititng Clap', 'Sititng Talking', 'Standing',
     'Standing ClAp', 'Standing Jump', 'Thankful', 'Thinking', 'Walking', 'Wave HIP HOP', 'WOBLING']
cou = -1
for root, dir, files in os.walk(mfldr):
    for i in dir:
        folder = (os.path.join('SIGMA', i))
        # print(sorted(os.listdir(folder), key=len))
        sorted(os.listdir(folder), key=len)
        j = 0
        cou += 1
        for i in sorted(os.listdir(folder), key=len):
            # print(i)
            if ".obj" not in i:
                os.rename(os.path.join(folder, i), os.path.join(folder, k[cou] + '_' + ("%03d" % j) + ".mtl"))
            if ".obj" in i:
                os.rename(os.path.join(folder, i), os.path.join(folder, k[cou] + "_" + ("%03d" % j) + ".obj"))
                print(os.path.join(folder, k[cou] + "_" + ("%03d" % j) + ".obj"))
                j += 1
# import os
#
# cou = 0
k = ['03', 'Armm Strctig', 'Dance', 'Dying', 'Entry', 'Falling', 'Flair', 'IDLE', 'L IDLE', 'maps',
     'Nerviously Looking Around', 'New Folder', 'obj2', 'Phone', 'Pointig Forward', 'Praying', 'Sititng Clap',
     'Sititng Talking', 'Standing', 'Standing ClAp', 'Standing Jump', 'Thankful', 'Thinking', 'Walking', 'Wave HIP HOP',
     'WOBLING']
# for root, dir, files in os.walk('ai_files/SIGMA'):
#     for i in dir:
for i in k:
    print(
        i + '''v=0
def ''' + i + '''():
    global ''' + i + 'v\n' +
        '\tif ' + i + '''v==0:
        anima.animations[\'''' + i + '\'] = FrameAnimation3d(\'SIGMA/' + i + '/' + i + '\'' + ''', fps=35, loop=False, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
        position=(2, 0, 2))
        ''' + '\t' + i + '''v=1'''
                         '''\n\tanima.state = \'''' + i + '''\'
        ''')
    # print(dir)

#         print("\"" + i + "\"" + ":" + '''FrameAnimation3d('SIGMA/''' + i + '/' + k[cou] + '\'' + ''', fps=35, loop=True, autoplay=True, scale=200, texture='maps/42.png',
#         position=(2, 0, 2)),''')
#         cou += 1
