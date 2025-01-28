from typing import List

from src.resume_sources.all_experiences import ExperienceData


class BaselineTailoring:
    @staticmethod
    def tailor_experience(experience: ExperienceData) -> ExperienceData:
        experience.Body.sentence_summary = BaselineTailoring.get_sentence_summary(experience)
        experience.Body.highlights_realisations = BaselineTailoring.get_realisations(experience)
        experience.Body.highlights_technologies = BaselineTailoring.get_technologies(experience)
        return experience

    @staticmethod
    def get_sentence_summary(experience: ExperienceData) -> str:
        if experience.Body.sentence_summary is not None:
            return experience.Body.sentence_summary
        return experience.Body.context

    @staticmethod
    def get_realisations(experience: ExperienceData) -> List[str]:
        if experience.Body.highlights_realisations is not None:
            return experience.Body.highlights_realisations
        return []
        # return experience.Body.realisations

    @staticmethod
    def get_technologies(experience: ExperienceData) -> List[str]:
        if experience.Body.highlights_technologies is not None:
            return experience.Body.highlights_technologies
        # return []
        return experience.Body.technologies
