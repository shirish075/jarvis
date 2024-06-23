# Import the OpenMaya and OpenMayaAnim libraries
import time

from maya import OpenMaya, OpenMayaAnim

# Create a new Maya scene
OpenMaya.MFileIO.newFile(True)

# Load the character Maya file
model = OpenMaya.MFileIO.importFile("E:\mata files\BUT_C_Jasper.ma")  # ('path/to/character.ma')

# Create an MFnMesh object from the model data
mesh = OpenMaya.MFnMesh(model)

# Create an MFnCharacter object from the model data
character = OpenMayaAnim.MFnCharacter(model)

# Set the character's current time to the start of the animation
character.setCurrentTime(OpenMaya.MTime(0))

# Set the character's animation start time
character.setStartTime(OpenMaya.MTime(0))

# Set the character's animation end time
character.setEndTime(OpenMaya.MTime(100))

# Set the character's animation frame rate
character.setOutputFPS(30.0)

# Set the character's animation frame range
character.setPlaybackByFrame(True)

# Set the character's pose at the start of the animation
character.setInitialPose()

# Start the character animation
character.play()

# Wait for the animation to finish
while character.isPlaying():
    time.sleep(0.1)

# Save the animated character as a Maya file
OpenMaya.MFileIO.saveAs(r'E:\mata files\BUT_C_Jasper.ma')
