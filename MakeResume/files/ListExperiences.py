import os
from typing import Dict, List, Set

from dynaconf import settings

from MakeResume.files.Experience import Experience


class ListExperiences:
    def __init__(self) -> None:
        self.base_dir = f"{settings.YAML_CV_PARTS}{settings.YAML_EXPERIENCE}"
        self.experiences_paths = self.load_experiences_paths()
        self.experiences = self.load_experiences()

    def load_experiences(self):
        experiences = []
        for name, experiences_paths in self.experiences_paths.items():
            for experience_path in experiences_paths:
                xp = Experience(experience_path)
                experiences.append(xp)
        return experiences

    def _load_individual_experiences(self, directory):
        experiences = []
        for root, _, files in os.walk(directory, topdown=False):
            for name in files:
                if name.endswith(".yaml"):
                    experience_path = os.path.join(root, name)
                    experiences.append(experience_path)
        experiences.sort()
        return experiences

    def load_experiences_paths(self) -> Dict[str, List[str]]:
        dict_experiences = {}
        for root, dirs, _ in os.walk(self.base_dir, topdown=False):
            for company_name in dirs:
                company_dir = os.path.join(root, company_name)
                experiences = self._load_individual_experiences(company_dir)
                dict_experiences[company_name] = experiences
        return dict_experiences

    def get_experiences(self) -> List[Experience]:
        return self.experiences

    def get_all_company_names(self) -> Set[str]:
        names = set()
        for this_xp in self.experiences:
            this_company = this_xp.get_company()
            names.add(this_company)
        return names

    def get_experiences_by_company(self) -> Dict[str, List[Experience]]:
        all_companies_all_xps = {}
        for this_xp in self.experiences:
            this_company = this_xp.get_company()
            company_all_xps = all_companies_all_xps.get(this_company, [])
            company_all_xps.append(this_xp)
            all_companies_all_xps[this_company] = company_all_xps
        return all_companies_all_xps
