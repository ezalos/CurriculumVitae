from typing import List, Optional

from pydantic import BaseModel

from MakeResume.resume_sources.all_experiences import ExperienceData


class TexElementData(BaseModel):
    path_to_save_tex: Optional[str] = None
    path_for_relative_tex_input: Optional[str] = None
    experience_data: ExperienceData
    tex_content: Optional[str] = None


class TexSectionData(BaseModel):
    section_name: str
    path_to_save_tex: Optional[str] = None
    path_for_relative_tex_input: Optional[str] = None
    tex_elements: List[TexElementData] = []
    tex_content: Optional[str] = None
