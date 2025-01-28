from datetime import datetime
from typing import List

from src.latex_generation.types import TexElementData
from src.resume_sources.all_experiences import ExperienceData

t_path = str


def tex_escape_string(string: str) -> str:
    replace_dict = {
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "{": "\\{",
        "}": "\\}",
    }
    for raw_char, escaped_char in replace_dict.items():
        string = string.replace(raw_char, escaped_char)
    return string


def list_to_tex(list_str: List[str]) -> str:
    tex = ""
    if not len(list_str):
        return tex
    tex += "\\begin{tightitemize}\n"
    for i, elem in enumerate(list_str):
        if i > 2:
            break
        if not isinstance(elem, str):
            continue
        elem = tex_escape_string(elem)
        tex += f"\\item {{{elem}}} \n"
    tex += "\\end{tightitemize}\n"
    return tex


class TexElement:
    def __init__(self, experience_data: ExperienceData) -> None:
        print(f"Creating {experience_data = }")
        self.data = TexElementData(experience_data=experience_data)
        self.data.tex_content = self.get_tex()
        print(f"Created {self.data = }")

    # ---------------------------------------------------------------------------- #
    #                               High Level Parts                               #
    # ---------------------------------------------------------------------------- #
    def get_date_details(self, from_: str, to: str) -> str:
        if self.data.experience_data.date_details:
            total_time = self.data.experience_data.date_details
        else:
            # Convert dates to years of experience
            date_format = "%m/%Y"
            from_date = datetime.strptime(from_, date_format)

            if to.lower() == "present":
                to_date = datetime.now()
                # to = "présent"
            else:
                to_date = datetime.strptime(to, date_format)
            diff = to_date - from_date
            total_days = diff.days
            years = total_days // 365
            remaining_days = total_days % 365
            months = remaining_days // 30

            total_time = ""
            if years > 0:
                total_time += f"{years} an" + ("s" if years > 1 else "")

            if months > 0:
                total_time += f" {months} mois"  # + ("s" if months > 1 else "")

        details = f"{total_time} [{from_} - {to}]"
        details = tex_escape_string(details)
        return details

    def _get_header(self) -> str:
        title = tex_escape_string(self.data.experience_data.title)
        company = tex_escape_string(self.data.experience_data.at)
        from_, to = self.data.experience_data.from_, self.data.experience_data.to
        date_details = self.get_date_details(from_, to)
        tex = ""
        tex += f"\\experienceheader{{{title}}}{{{company}}}{{{date_details}}}\n"
        return tex

    def _get_body(self) -> str:
        context = self.data.experience_data.Body.sentence_summary
        missions = self.data.experience_data.Body.missions
        realisations = self.data.experience_data.Body.highlights_realisations
        technologies = self.data.experience_data.Body.highlights_technologies

        tex = ""
        tex += f"\\experiencedescription{{{context}}}\n"
        if missions and realisations:
            l_mission = list_to_tex(missions)
            l_realisations = list_to_tex(realisations)
            tex += f"\\experiencedoublelist{{{l_mission}}}{{{l_realisations}}}\n"
        elif missions:
            l_mission = list_to_tex(missions)
            tex += f"\\experiencesimplelist{{{l_mission}}}\n"
        elif realisations:
            l_realisations = list_to_tex(realisations)
            tex += f"\\experiencesimplelist{{{l_realisations}}}\n"
        elif technologies:
            tex += "\n\n"
        return tex

    def _get_tail(self) -> str:
        tex = ""
        technologies = self.data.experience_data.Body.highlights_technologies
        if technologies:
            tex += f"\\experiencetechno{{{technologies}}}\n"
        return tex

    # ---------------------------------------------------------------------------- #
    #                                      API                                     #
    # ---------------------------------------------------------------------------- #

    def get_tex(self) -> str:
        tex = ""
        tex += self._get_header()
        tex += self._get_body()
        tex += self._get_tail()
        return tex

    # ---------------------------------------------------------------------------- #
    #                                   Interface                                  #
    # ---------------------------------------------------------------------------- #

    @classmethod
    def from_dict(cls, dict_obj: dict) -> TexElementData:
        instance = cls.__new__(cls)
        experience = TexElementData.model_validate(dict_obj)
        instance.data = experience
        return instance

    def to_dict(self) -> dict:
        return self.data.model_dump()
