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
        return tex

    def _get_elem_title(self):

        tex = ""
        # tex += f"\\sectionprimary{{{title}}}\n"
        # # tex += f"\\hfill\n"
        # tex += f"\\sectionsecondary{{{at}}}\n"
        # tex += f"\\sectiondouble{{{title}}}{{{at}}}\n"
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

        tex = ""
        tex += f"\\experiencedescription{{{context}}}\n"
        tex += f"\\experiencedoublelist{{{context}}}{{{context}}}\n"
        return tex

    def _get_tail(self):
        tex = ""
        techs = self.experience.get_technologies()
        if techs:
            tex += f"\\experiencetechno{{{techs}}}\n"
        tex += "\\sectionspace\n"
        return tex

    # ---------------------------------------------------------------------------- #
    #                                      API                                     #
    # ---------------------------------------------------------------------------- #

    def get_tex(self):
        tex = ""
        tex += self._get_header()
        tex += self._get_body()
        tex += self._get_tail()
        return tex
