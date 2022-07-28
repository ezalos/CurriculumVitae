import abc
from typing import Dict

import yaml

from MakeResume.files.Experience import Experience


class TexElement(abc.ABC):
    def __init__(self, experience: Experience) -> None:
        self.experience = experience

    @abc.abstractmethod
    def get_tex(self) -> Dict:
        pass
