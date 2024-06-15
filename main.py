import pythreejs as p3
import IPython.display as display

# Create a simple cube geometry and a basic material
geometry = p3.BoxGeometry(1, 1, 1)
material = p3.MeshBasicMaterial(color='red', wireframe=True)

# Combine them into a mesh
cube = p3.Mesh(geometry=geometry, material=material)

# Set up the scene, camera, and renderer
scene = p3.Scene(children=[cube, p3.AmbientLight(color='#dddddd')])
camera = p3.PerspectiveCamera(position=[3, 3, 3], fov=20, children=[p3.DirectionalLight(color='white', position=[0, 0, 1], intensity=0.5)])
controller = p3.OrbitControls(controlling=camera)
renderer = p3.Renderer(camera=camera, scene=scene, controls=[controller], width=800, height=600)

# Display the rendered cube
display.display(renderer)