from typing import List, Optional

from MakeResume.resume_sources.all_experiences import ExperienceData
from pydantic import BaseModel


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
