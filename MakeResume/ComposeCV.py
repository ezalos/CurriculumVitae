from typing import List

from MakeResume.latex_generation.TexElement import TexElement
from MakeResume.latex_generation.WriteLaTeX import WriteLaTeX
from MakeResume.position_tailoring.BaselineTailoring import BaselineTailoring
from MakeResume.resume_sources.all_experiences import ExperienceData, work_experience


class ComposeCV:
    def __init__(self) -> None:
        self.WriteLaTeX = WriteLaTeX()

    def prepare_experiences(self, experience_datas: List[ExperienceData]) -> List[TexElement]:
        # self.llm_tailoring = LLM_Tailoring()
        tex_elements = []
        for experience_data in experience_datas:
            experience_data = BaselineTailoring.tailor_experience(experience_data)
            # experience_data = self.llm_tailoring.tailor_experience(experience_data)
            tex_element = TexElement(experience_data=experience_data)
            tex_elements.append(tex_element)
        return tex_elements

    def make(self):
        # Work Experience Section
        self.WriteLaTeX.create_section(
            "Expériences",
            self.prepare_experiences(work_experience),
        )

        # # Volunteering Section
        # self.WriteLaTeX.create_section(
        #     "Volontariat",
        #     self.prepare_experiences(volunteering_experience),
        # )

        self.WriteLaTeX.to_draft()
        self.WriteLaTeX.from_draft()

        self.WriteLaTeX.export_to_latex()
