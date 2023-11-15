from service import *


class Scene:
    def __init__(self, id, models, flashes, cameras):
        self.id = id
        self.models = models
        self.flashes = flashes
        self.cameras = cameras

    @staticmethod
    def method1(obj) -> object:
        pass

    @staticmethod
    def method2(obj_1, obj_2) -> object:
        pass


class PoligonalModel:
    def __init__(self, textures):
        self.textures = textures
        self.poligon = Poligon([Point3D(1, 1, 1), Point3D(2, 2, 2), Point3D(3, 3, 3)])
        self.poligons = [self.poligon]


class Flash:
    def __init__(self, location, angle, color, power):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, new_angle) -> None:
        pass

    def move(self, new_location) -> None:
        pass


class Camera:
    def __init__(self, location, angle):
        self.location = location
        self.angle = angle

    def rotate(self, new_angle) -> None:
        pass

    def move(self, new_location) -> None:
        pass


class Texture:
    pass


class Poligon:
    def __init__(self, points):
        self.points = points
