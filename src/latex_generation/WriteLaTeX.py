import json
import os
from typing import List

from MakeResume.latex_generation.tex_path import TOP_TEX_IMPORT_PATH
from MakeResume.latex_generation.TexElement import TexElement
from MakeResume.latex_generation.TexSection import TexSection

t_path = str


class WriteLaTeX:
    def __init__(self) -> None:
        self.tex_sections: List[TexSection] = []
        self.path_to_save_tex = TOP_TEX_IMPORT_PATH

    def get_content_of_input(self):
        tex = ""
        for section in self.tex_sections:
            tex += f"\input{{{section.data.path_for_relative_tex_input}}}\n"
        tex += "\\sectionspace\n"
        return tex

    # ---------------------------------------------------------------------------- #
    #                           Multi Elements Management                          #
    # ---------------------------------------------------------------------------- #

    def create_section(
        self,
        section_name: str,
        experiences: List[TexElement],
    ):
        print(f"Creating {section_name = } with {len(experiences) = }")
        print(f"Creating {type(experiences[0]) = }")
        ts = TexSection(section_name=section_name, experiences=[exp.data for exp in experiences])
        self.tex_sections.append(ts)
        print(f"Created {section_name = } with {len(self.tex_sections) = }")

    # ---------------------------------------------------------------------------- #
    #                                  WRITE LATEX                                 #
    # ---------------------------------------------------------------------------- #

    def _write_file(self, content: str, path: t_path):
        directory = os.path.dirname(path)
        os.makedirs(directory, exist_ok=True)
        with open(path, "w+", encoding="utf-8") as f:
            f.write(content)

    def export_to_latex(self):
        for section in self.tex_sections:
            for subsection in section.data.tex_elements:
                # Write experience
                path = subsection.path_to_save_tex
                content = subsection.tex_content
                self._write_file(content, path)
            # Write section input
            path = section.data.path_to_save_tex
            content = section.data.tex_content
            self._write_file(content, path)
        # Write top input
        content = self.get_content_of_input()
        path = self.path_to_save_tex
        self._write_file(content, path)

    # ---------------------------------------------------------------------------- #
    #                                 SERIALIZATION                                #
    # ---------------------------------------------------------------------------- #

    def to_draft(self):
        json_path = "resume/out/drafts/full_draft.json"
        dict_obj = {}
        for section in self.tex_sections:
            dict_obj[section.data.section_name] = section.to_dict()

        print(f"Writing {json_path = }")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(dict_obj, f, indent=4)

    def from_draft(self):
        json_path = "resume/out/drafts/full_draft.json"
        with open(json_path, "r", encoding="utf-8") as f:
            dict_obj = json.load(f)
        print(f"Loading {json_path = }")
        for section_name, section in dict_obj.items():
            ts = TexSection(section_name=section_name, experiences=[])
            ts.from_dict(section)
