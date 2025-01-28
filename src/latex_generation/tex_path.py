import os

from dynaconf import settings

from src.latex_generation.types import TexSectionData
from src.resume_sources.all_experiences import ExperienceData

t_path = str

# ---------------------------------------------------------------------------- #
#                                    ELEMENT                                   #
# ---------------------------------------------------------------------------- #


def get_element_path_to_save_tex(section_name: str, experience: ExperienceData) -> t_path:
    begin_date = experience.from_.replace("/", "-")
    company = experience.at
    title = experience.title
    tex_name = begin_date + "_" + "_" + company + "_" + title + ".auto_gen.tex"
    tex_path = os.path.join(settings.LATEX_CV_PARTS, section_name, tex_name)
    return tex_path


def get_element_path_for_relative_tex_input(path_to_save_tex: t_path) -> t_path:
    input_path = path_to_save_tex.replace("./resume/latex/", "")
    return input_path


# ---------------------------------------------------------------------------- #
#                                    SECTION                                   #
# ---------------------------------------------------------------------------- #


def get_section_path_to_save_tex(tex_section_data: TexSectionData) -> t_path:
    input_path = os.path.join(settings.LATEX_CV_PARTS, tex_section_data.section_name, "input.tex")
    return input_path


def get_section_path_for_relative_tex_input(tex_section_data: TexSectionData) -> t_path:
    input_path = tex_section_data.path_to_save_tex.replace("./resume/latex/", "")
    return input_path


# ---------------------------------------------------------------------------- #
#                                TOP TEX IMPORT                                #
# ---------------------------------------------------------------------------- #

TOP_TEX_IMPORT_PATH = os.path.join(settings.LATEX_CV_PARTS, "input.tex")
