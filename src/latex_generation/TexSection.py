from typing import List

from MakeResume.latex_generation.tex_path import (
    get_element_path_for_relative_tex_input,
    get_element_path_to_save_tex,
    get_section_path_for_relative_tex_input,
    get_section_path_to_save_tex,
)
from MakeResume.latex_generation.TexElement import TexElementData
from MakeResume.latex_generation.types import TexSectionData

t_path = str


class TexSection:
    def __init__(self, section_name: str, experiences: List[TexElementData]) -> None:
        self.data: TexSectionData = TexSectionData(
            section_name=section_name,
            tex_elements=experiences,
        )
        self.fill_all_paths()
        self.data.tex_content = self.get_section_relative_inputs()

    def fill_all_paths(self):
        self.data.path_to_save_tex = get_section_path_to_save_tex(self.data)
        self.data.path_for_relative_tex_input = get_section_path_for_relative_tex_input(self.data)
        for element in self.data.tex_elements:
            element.path_to_save_tex = get_element_path_to_save_tex(
                self.data.section_name, element.experience_data
            )
            element.path_for_relative_tex_input = get_element_path_for_relative_tex_input(
                element.path_to_save_tex
            )

    # ---------------------------------------------------------------------------- #
    #                               Input management                               #
    # ---------------------------------------------------------------------------- #

    def get_section_relative_inputs(self):
        tex = ""
        tex += f"\\section{{{self.data.section_name}}}\n"
        for subsection in self.data.tex_elements:
            tex += f"\input{{{subsection.path_for_relative_tex_input}}}\n"
        tex += "\\sectionspace\n"
        return tex

    # ---------------------------------------------------------------------------- #
    #                               Draft management                               #
    # ---------------------------------------------------------------------------- #

    def to_dict(self) -> dict:
        out = self.data.model_dump()
        print(f"Dumped TexSectionData {self.data.section_name = }")
        return out

    def from_dict(self, dict_obj: dict) -> None:
        self.data = TexSectionData.model_validate(dict_obj)
        print(f"Loaded TexSectionData {self.data.section_name = }")
