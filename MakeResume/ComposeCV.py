from MakeResume.files.ListExperiences import ListExperiences
from MakeResume.tex.Elements.TexExperienceShort import TexExperienceShort
from MakeResume.tex.WriteLaTeX import WriteLaTeX


class ComposeCV:
    def __init__(self) -> None:
        self.ListExperiences = ListExperiences()
        self.WriteLaTeX = WriteLaTeX(TexExperienceShort)

    def make(self):
        experiences = self.ListExperiences.get_experiences_by_company()
        for company, xps in experiences.items():
            print(f"For {company = }")
            for xp in xps:
                print(f"\t{xp.get_title() = }")

        xps = []
        # for c in ["Revolve", "Pole Emploi", "Cartier", "Natixis"]:
        for c in ["Revolve"]:
            xps.extend(experiences[c])
        self.WriteLaTeX.create_section("Experience", xps)

        xps = experiences["42 Artificial Intelligence"]
        self.WriteLaTeX.create_section("Volunteering", xps[:2])

        self.WriteLaTeX.save()
