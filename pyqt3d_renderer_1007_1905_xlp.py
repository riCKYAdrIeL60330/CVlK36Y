# 代码生成时间: 2025-10-07 19:05:22
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QQuaternion
from PyQt5.Qt3DCore import QEntity, QTransform
from PyQt5.Qt3DRender import QCamera, QPointLight, QRenderSettings, QTextureLoader
from PyQt5.Qt3DExtras import QPhongMaterial, QTorusMesh, QFirstPersonCameraController, QOrbitCameraController

"""
A simple 3D rendering engine using PyQt and its 3D module.
This program creates a window displaying a torus mesh with lighting.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Window setup
        self.setWindowTitle('PyQt 3D Renderer')
        self.setGeometry(100, 100, 800, 600)

        # Create a widget and set as the central widget of the window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a layout for the widget
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Create a 3D scene and add it to the layout
        self.scene = self.create_scene()
        layout.addWidget(self.scene)

    def create_scene(self):
        # Create the root entity
        root_entity = QEntity()

        # Create a camera
        camera = QCamera()
        camera.setProjectionType(QCamera.PerspectiveProjection)
        camera.setFieldOfView(45)
        camera.setAspectRatio(16/9)
        camera.setPosition(0, 0, 10)
        camera.lookAt(QVector3D(0, 0, 0))
        root_entity.addComponent(camera)

        # Create a point light
        light = QPointLight()
        light.setPosition(QVector3D(0, 10, 10))
        light.setColor(QColor(255, 255, 255))
        root_entity.addComponent(light)

        # Create a torus mesh
        torus_mesh = QTorusMesh()
        torus_mesh.setRadius(2.5)
        torus_mesh.setMinorRadius(0.5)
        root_entity.addComponent(torus_mesh)

        # Create a material
        material = QPhongMaterial()
        material.setAmbient(QColor(150, 150, 150))
        material.setDiffuse(QColor(255, 0, 0))
        material.setSpecular(QColor(255, 255, 255))
        material.setShininess(32)
        torus_mesh.setDefaultMaterial(material)

        # Create a render window
        render_window = QRenderWindow()
        render_window.setRootEntity(root_entity)
        render_window.defaultFrameGraph().setClearColor(QColor(50, 50, 50))
        render_window.activeFrameGraph().setActiveFrameGraph(QFrameGraph.ForwardRenderGraph)

        # Create a viewer and add the render window
        viewer = QAbstractViewer()
        viewer.setRenderWidget(render_window)

        # Create a camera controller
        self.create_camera_controller(viewer, root_entity)

        return viewer

    def create_camera_controller(self, viewer, root_entity):
        # Create a camera controller
        self.controller = QOrbitCameraController()
        self.controller.setCamera(viewer.camera())
        self.controller.setLookAt(QVector3D(0, 0, 0))

        # Assign the controller to the viewer
        viewer.setCameraController(self.controller)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())