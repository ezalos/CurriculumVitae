from typing import List

from MakeResume.files.Experience import Experience
from MakeResume.tex.Elements.TexElement import TexElement


class TexExperienceShort(TexElement):
    def __init__(self, experience: Experience) -> None:
        super().__init__(experience)

    # ---------------------------------------------------------------------------- #
    #                              Low level creation                              #
    # ---------------------------------------------------------------------------- #

    def _get_logistc(self):
        title = self.experience.get_title()
        company = self.experience.get_company()
        from_, to = self.experience.get_dates()
        # where = self.experience.get_location()
        # details = f"{where} | {from_} - {to}"
        details = f"{from_} - {to}"

        tex = ""
        tex += f"\\experienceheader{{{title}}}{{{company}}}{{{details}}}\n"
        # tex += f"\\experiencetitle{{{title}}}\n"
        # tex += 	"\\begin{minipage}[t]{0.90\\textwidth}\n"
        # tex += f"\\experiencetitledetails{{{company}}}{{{details}}}\n"
        return tex

    def _get_elem_title(self):

        tex = ""
        # tex += f"\\sectionprimary{{{title}}}\n"
        # # tex += f"\\hfill\n"
        # tex += f"\\sectionsecondary{{{at}}}\n"
        # tex += f"\\sectiondouble{{{title}}}{{{at}}}\n"
        return tex

    def _escape_string(self, string: str) -> str:
        string = string.replace("&", "\\&")
        string = string.replace("%", "\\%")
        string = string.replace("$", "\\$")
        string = string.replace("#", "\\#")
        string = string.replace("_", "\\_")
        string = string.replace("{", "\\{")
        string = string.replace("}", "\\}")
        return string

    def _get_list(self, list_str: List[str]) -> str:
        tex = ""
        tex += "\\begin{tightitemize}\n"
        for i, elem in enumerate(list_str):
            if i > 2:
                break
            if type(elem) != type(""):
                continue
            elem = self._escape_string(elem)
            tex += f"\\item {{{elem}}} \n"
        tex += "\\end{tightitemize}\n"
        return tex

    # ---------------------------------------------------------------------------- #
    #                               High Level Parts                               #
    # ---------------------------------------------------------------------------- #

    def _get_header(self):
        tex = ""
        # tex += self._get_elem_title()
        tex += self._get_logistc()
        return tex

    def _get_body(self):
        context = self.experience.get_context()
        missions = self.experience.get_missions()
        realisations = self.experience.get_realisations()

        tex = ""
        tex += f"\\experiencedescription{{{context}}}\n"
        if missions and realisations:
            l_mission = self._get_list(missions)
            l_realisations = self._get_list(realisations)
            tex += f"\\experiencedoublelist{{{l_mission}}}{{{l_realisations}}}\n"
        elif missions:
            l_mission = self._get_list(missions)
            tex += f"\\experiencesimplelist{{{l_mission}}}\n"
        elif realisations:
            l_realisations = self._get_list(realisations)
            tex += f"\\experiencesimplelist{{{l_realisations}}}\n"
        return tex

    def _get_tail(self):
        tex = ""
        techs = self.experience.get_technologies()
        if techs:
            tex += f"\\experiencetechno{{{techs}}}\n"
        # tex += "\\sectionspace\n"
        return tex

    # ---------------------------------------------------------------------------- #
    #                                      API                                     #
    # ---------------------------------------------------------------------------- #

    def get_tex(self):
        tex = ""
        # tex += 	"\\begin{minipage}[t]{0.05\\textwidth}\n"
        # tex += 	"\\end{minipage} % The end of the left column\n"
        tex += self._get_header()
        tex += self._get_body()
        tex += self._get_tail()
        # tex += 	"\\end{minipage} % The end of the left column\n"
        return tex
