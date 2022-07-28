import os
from pathlib import Path
from typing import Dict, List

from dynaconf import settings

from MakeResume.files.Experience import Experience
from MakeResume.tex.Elements.TexElement import TexElement

t_path = str


class WriteLaTeX:
    def __init__(self, BodyElement: TexElement) -> None:
        self.BodyElement = BodyElement
        self.files_to_write: Dict[t_path, str] = {}
        self.all_inputs: List[t_path] = []

    # ---------------------------------------------------------------------------- #
    #                                Paths creation                                #
    # ---------------------------------------------------------------------------- #

    def _get_input_path_of_all_inputs(self) -> t_path:
        all_input_path = os.path.join(settings.LATEX_CV_PARTS, "input.tex")
        # all_input_path = all_input_path.replace("./resume_latex/", "")
        return all_input_path

    def _get_input_path_of_experience(self, tex_path: str) -> t_path:
        input_path = tex_path.replace("./resume_latex/", "")
        return input_path

    def _get_input_path_of_section(self, section_name: str) -> t_path:
        input_path = os.path.join(settings.LATEX_CV_PARTS, section_name, "input.tex")
        return input_path

    def _get_path_of_section_element(self, section_name: str, experience: Experience) -> t_path:
        file_path = experience.get_file_path()
        file_name = Path(file_path).parts[-1]
        tex_name = file_name.replace(".yaml", ".tex")
        tex_path = os.path.join(settings.LATEX_CV_PARTS, section_name, tex_name)
        return tex_path

    # ---------------------------------------------------------------------------- #
    #                               Content creation                               #
    # ---------------------------------------------------------------------------- #

    def _get_input(self, includes: List[str]) -> str:
        tex = ""
        for inc in includes:
            tex += f"\input{{{inc}}}\n"
        return tex

    def _get_input_content_of_section(self, section: str, includes: List[str]):
        tex = ""
        if section:
            tex += f"\\section{{{section}}}\n"
        tex += self._get_input(includes)
        return tex

    # ---------------------------------------------------------------------------- #
    #                           Multi Elements Management                          #
    # ---------------------------------------------------------------------------- #

    def create_section(self, section_name: str, experiences: List[Experience]):
        element_inputs = []
        for i, experience in enumerate(experiences):
            # Create LaTeX path
            element_tex_path = self._get_path_of_section_element(section_name, experience)
            # Create LaTeX element
            element_tex_content = self.BodyElement(experience).get_tex()
            self._add_file_to_write(element_tex_path, element_tex_content)

            # Save input dependency
            element_inputs_path = self._get_input_path_of_experience(element_tex_path)
            element_inputs.append(element_inputs_path)

        # Create input file for this section
        element_input_content = self._get_input_content_of_section(section_name, element_inputs)
        element_input_path = self._get_input_path_of_section(section_name)
        self._add_file_to_write(element_input_path, element_input_content)

        # Save input path reference
        element_input_path = self._get_input_path_of_experience(element_input_path)
        self.all_inputs.append(element_input_path)

    def _add_file_to_write(self, path: t_path, content: str):
        self.files_to_write[path] = content

    # ---------------------------------------------------------------------------- #
    #                              Write all the files                             #
    # ---------------------------------------------------------------------------- #

    def _write_file(self, content: str, path: t_path):
        directory = os.path.dirname(path)
        os.makedirs(directory, exist_ok=True)
        with open(path, "w+") as f:
            f.write(content)

    def save(self):
        input_path = self._get_input_path_of_all_inputs()
        input_content = self._get_input(self.all_inputs)
        self._add_file_to_write(input_path, input_content)

        for path, content in self.files_to_write.items():
            print(f"Writing file:")
            print(f"\t{path = }")
            print(f"\t{content = }")
            print(f"")
            self._write_file(content, path)
