import os
from typing import List

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.llms import Ollama
from MakeResume.resume_sources.all_experiences import ExperienceData


class ResumeTailor:
    def __init__(self, use_claude=False):
        """Initialize with either local model or Claude."""
        load_dotenv()

        self.is_claude = use_claude
        if self.is_claude:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY not found in .env file")
            self.llm = ChatAnthropic(
                model_name="claude-3-sonnet-20240229",
                anthropic_api_key=api_key,
                temperature=0.3,  # Lower temperature for more focused responses
            )
        else:
            self.llm = Ollama(model="deepseek-r1:32b-qwen-distill-q4_K_M", temperature=0.3)

    def get_tailored_context(self, job_description, your_position):
        prompt = f"""
        Tâche : Analyse l'offre d'emploi et l'expérience professionnelle pour donner UNIQUEMENT 1-2 phrases de contexte sur l'expérience professionnelle.
        Le but est de permettre au recruteur de voir apparaitre ce qui est le plus pertinent (si c'est possible) dans le contexte de l'offre d'emploi.

        Offre d'emploi : {job_description}

        Expérience professionnelle : {your_position}

        N'inventes rien et donnes UNIQUEMENT les compétences/expériences les plus importantes à mettre en valeur.
        Sois extrêmement concis.
        """

        if self.is_claude:
            from langchain.schema import HumanMessage

            response = self.llm.invoke([HumanMessage(content=prompt)])
            return response.content
        else:
            return self.llm.invoke(prompt)

    def get_tailored_technologies(self, job_description, your_position):
        prompt = f"""
        Tâche : Analyse l'offre d'emploi et l'expérience professionnelle pour lister les technologies maitrisées les plus pertinentes.
        Le but est de permettre au recruteur de voir apparaitre ce qui est le plus pertinent (si c'est possible) dans le contexte de l'offre d'emploi.
        Tu peux conserver les technologies peripheriques a celles demandees (exemple: demande docker, n'hesite pas a mettre docker et docekr compose si elles font partie de l'experience).

        Offre d'emploi : {job_description}

        Expérience professionnelle : {your_position}

        N'inventes rien et donnes UNIQUEMENT les technologies presentes dans l'experience professionnelle, mets en entre 3 et 10 (grand maximum).
        """

        if self.is_claude:
            from langchain.schema import HumanMessage

            response = self.llm.invoke([HumanMessage(content=prompt)])
            return response.content
        else:
            return self.llm.invoke(prompt)


class LLM_Tailoring:
    def __init__(self):
        self.tailor = ResumeTailor(use_claude=False)

    def tailor_experience(self, experience: ExperienceData) -> ExperienceData:
        experience.Body.sentence_summary = self.get_sentence_summary(experience)
        # experience.Body.highlights_realisations = self.get_realisations(experience)
        experience.Body.highlights_technologies = self.get_technologies(experience)
        return experience

    def get_sentence_summary(self, experience: ExperienceData) -> str:
        with open("positions/2025_FINAXYS/job_descritpion.txt", "r") as file:
            job_description = file.read()
        my_position = f"""
        Experience professionnelle: {experience.title} chez {experience.at}
        {experience.Body = }
        """

        sentence_summary = self.tailor.get_tailored_context(job_description, my_position)
        sentence_summary = sentence_summary.split("</think>")[-1].strip()
        print(f"{sentence_summary = }")
        return sentence_summary

    def get_realisations(self, experience: ExperienceData) -> List[str]:
        return []
        # return experience.Body.realisations

    def get_technologies(self, experience: ExperienceData) -> List[str]:
        return experience.Body.technologies

        # with open("positions/2025_FINAXYS/job_descritpion.txt", "r") as file:
        #     job_description = file.read()
        # my_position = f"""
        # Experience professionnelle: {experience.title} chez {experience.at}
        # {experience.Body = }
        # """

        # sentence_summary = self.tailor.get_tailored_technologies(
        #     job_description, my_position
        # )
        # sentence_summary = sentence_summary.split("</think>")[-1].strip()
        # print(f"{sentence_summary = }")
        # return sentence_summary


def main():
    # Example usage
    job_description = input("Paste the job posting here: ")
    your_position = input("Describe your current/past relevant position: ")

    try:
        # Start with local model for quick testing
        tailor = ResumeTailor(use_claude=False)
        print("\nAdvice (using local model):")
        print(tailor.get_tailored_context(job_description, your_position))

        # Optionally switch to Claude for final version
        proceed = input("\nWant to get Claude's opinion? (y/n): ")
        if proceed.lower() == "y":
            tailor = ResumeTailor(use_claude=True)
            print("\nAdvice (using Claude):")
            print(tailor.get_tailored_context(job_description, your_position))

    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure Ollama is running and you have pulled the mistral model:")
        print("1. Start Ollama")
        print("2. Run: ollama pull mistral")


if __name__ == "__main__":
    main()
