from MakeResume.files.Experience import Experience
from MakeResume.tex.Elements.TexElement import TexElement


class TexExperienceShort(TexElement):
    def __init__(self, experience: Experience) -> None:
        super().__init__(experience)

    # ---------------------------------------------------------------------------- #
    #                              Low level creation                              #
    # ---------------------------------------------------------------------------- #

    def _get_elem_location_and_date(self):
        where = self.experience.get_location()
        from_, to = self.experience.get_dates()

        tex = ""
        tex += f"\\location{{{from_} - {to} | {where}}}\n"
        return tex

    def _get_elem_title(self):
        title = self.experience.get_title()
        at = self.experience.get_company()

        tex = ""
        tex += f"\\runsubsection{{{title}}}\n"
        tex += f"\\descript{{ | {at}}}\n"
        return tex

    # ---------------------------------------------------------------------------- #
    #                               High Level Parts                               #
    # ---------------------------------------------------------------------------- #

    def _get_header(self):
        tex = ""
        tex += self._get_elem_title()
        tex += self._get_elem_location_and_date()
        return tex

    def _get_body(self):
        context = self.experience.get_context()

        tex = ""
        tex += f"{context}\n"
        return tex

    def _get_tail(self):
        tex = ""
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
