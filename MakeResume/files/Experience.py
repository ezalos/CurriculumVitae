from typing import ContextManager, Dict

import yaml


class Experience:
    def __init__(self, yaml_path: str) -> None:
        self.yaml_path = yaml_path
        self.yaml = self.load_yaml(yaml_path)

    # ---------------------------------------------------------------------------- #
    #                               File interaction                               #
    # ---------------------------------------------------------------------------- #

    def load_yaml(self, yaml_path: str) -> Dict:
        with open(yaml_path, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def get_file_path(self):
        return self.yaml_path

    # ---------------------------------------------------------------------------- #
    #                                 Body elements                                #
    # ---------------------------------------------------------------------------- #

    def get_context(self):
        context = self.yaml["Body"]["Contexte"]
        return context

    def get_missions(self):
        context = self.yaml["Body"].get("Missions", None)
        return context

    def get_realisations(self):
        context = self.yaml["Body"].get("Réalisations", None)
        return context

    def get_technologies(self):
        context = self.yaml["Body"].get("Technologies", None)
        return context

    # ---------------------------------------------------------------------------- #
    #                               Header elements                                #
    # ---------------------------------------------------------------------------- #

    def get_title(self):
        title = self.yaml["title"]
        return title

    def get_company(self):
        at = self.yaml["at"]
        return at

    def get_date_from(self):
        from_ = self.yaml["from"]
        return from_

    def get_date_to(self):
        to = self.yaml["to"]
        return to

    def get_dates(self):
        from_ = self.get_date_from()
        to = self.get_date_to()
        return from_, to

    def get_location(self):
        where = self.yaml["where"]
        return where
