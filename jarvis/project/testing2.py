# write a python script to check the battery status for windows

# import psutil
#
# def battery():
#     batt = psutil.sensors_battery()
#     plugged = batt.power_plugged
#     percent = str(batt.percent)
#     if plugged==0:
#         print("Battery: "+percent+"%")
#     elif plugged==1:
#         print("Battery: "+percent+"%\nCharging via AC")
#     else:
#         print("Battery: "+percent+"%\nCharging via USB")
# if __name__ == '__main__':
#     battery()

import OpenGL.GL as gl
import glfw
import pywavefront

# Initialize the glfw library
if not glfw.init():
    raise RuntimeError("Failed to initialize glfw")

# Create a window
window = glfw.create_window(640, 480, "My Project", None, None)
if not window:
    glfw.terminate()
    raise RuntimeError("Failed to create window")

# Make the context current
glfw.make_context_current(window)

# Load the 3D character model from a file
# character = gl.glGenLists(1)
# gl.glNewList(character, gl.GL_COMPILE)
# with open("E:\mata files\iron-man-mark-42\source\Iron_Man_Mark_42\Mark 42.obj", "r") as file:
#     print("file :",file)


# # Load the OBJ file
# obj_loader = OBJFileLoader()
# scene = obj_loader.parse("E:\mata files\iron-man-mark-42\source\Iron_Man_Mark_42\Mark 42.obj")
scene = pywavefront.Wavefront("E:\mata files\iron-man-mark-42\source\Iron_Man_Mark_42\Mark 42.obj")
# Create a display list for the model
model = gl.glGenLists(1)
gl.glNewList(model, gl.GL_COMPILE)

# Iterate over the meshes in the scene
for mesh in scene.meshes:
    # Set the current material
    if mesh.material:
        gl.glMaterialfv(gl.GL_FRONT_AND_BACK, gl.GL_AMBIENT, mesh.material.ambient)
        gl.glMaterialfv(gl.GL_FRONT_AND_BACK, gl.GL_DIFFUSE, mesh.material.diffuse)
        # ...

    # Iterate over the faces in the mesh
    for face in mesh.faces:
        # Draw the face as a triangle strip
        gl.glBegin(gl.GL_TRIANGLE_STRIP)
        for vertex in face:
            # Set the vertex position, normal, and texture coordinates
            gl.glVertex3fv(mesh.vertices[vertex.vertex - 1])
            gl.glNormal3fv(mesh.normals[vertex.normal - 1])
            gl.glTexCoord2fv(mesh.texcoords[vertex.texcoord - 1])
        gl.glEnd()

    # Parse the OBJ file and create OpenGL display lists
    # ...
gl.glEndList()

# Main loop
while not glfw.window_should_close(window):
    # Clear the screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Draw the 3D character
    gl.glCallList(model)

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

# Terminate glfw
glfw.terminate()
