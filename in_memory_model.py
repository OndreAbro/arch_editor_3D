from abc import abstractmethod, ABC
from model_elements import *


class IModelChangeObserver(ABC):
    @abstractmethod
    def apply_update_model(self) -> None:
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender) -> None:
        pass


class ModelStore(IModelChanger, ABC):
    def __init__(self, change_observers):
        self.__change_observers = change_observers

        self.model = PoligonalModel(['textures_1', 'textures_2'])
        self.flash = Flash(Point3D(1, 2, 3), Angle3D(10, 20, 30), color, power)
        self.camera = Camera(Point3D(4, 5, 6), Angle3D(40, 50, 60))
        self.scene = Scene(1, [self.model], [], [self.camera])

        self.models = [self.model]
        self.flashes = [self.flash]
        self.cameras = [self.camera]
        self.scenes = [self.scene]

    def get_scene(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_changes(self):
        return super().notify_change(sender)
