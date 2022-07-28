from dynaconf import settings

from MakeResume.files.ListExperiences import ListExperiences


class ListEducations(ListExperiences):
    def __init__(self) -> None:
        self.base_dir = f"{settings.YAML_CV_PARTS}Education"
        self.experiences_paths = self.load_experiences_paths()
        self.experiences = self.load_experiences()
