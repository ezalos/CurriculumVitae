from typing import List, Optional

from pydantic import BaseModel, Field


class ExperienceBody(BaseModel):
    sentence_summary: Optional[str] = Field(default=None)
    highlights_realisations: Optional[List[str]] = Field(default=None)
    highlights_technologies: Optional[str] = Field(default=None)

    context: Optional[str] = Field(default=None)
    missions: Optional[List[str]] = Field(default=None)
    realisations: Optional[List[str]] = Field(default=None)
    technologies: Optional[str] = Field(default=None)


class ExperienceData(BaseModel):
    at: str
    title: str
    contract: Optional[str] = None
    where: str
    from_: str
    to: str
    date_details: Optional[str] = None
    logo: Optional[str] = None
    Body: ExperienceBody

    class Config:
        populate_by_name = True


# ---------------------------------------------------------------------------- #
#                                    ICONO                                     #
# ---------------------------------------------------------------------------- #

icono_experience = ExperienceData(
    at="ICONO",
    title="Machine Learning Engineer",
    contract="Permanent",
    where="Paris, France",
    from_="11/2022",
    to="02/2025",
    logo="resume_parts/experience/2022-11_ICONO/Icono Logo V4.png",
    Body=ExperienceBody(
        sentence_summary="""Co-fondateur d'icono, un moteur de recherche vidéo. Responsabilités totales sur l'IA, la Data, l'Infra et l'API.""",
        context="""Co-fondateur d'icono, un moteur de recherche vidéo multimodal in-house (pas d'API externe). Responsabilité totale sur l'IA, la Data, l'Infra et l'API.""",
        # https://www.icono-search.com/""",
        highlights_realisations=[
            "Stack ML sans API externe permettant une recherche multimodale (visuelle, visages, paroles) dans les vidéos.",
            "Système d'analyse distribuée avec multi cloud et multi nodes GPU. La pipeline d'ingestion ML est capable de dépasser les 1M de vidéo shots traités par jour.",
            "Throughput de 2.75s (p95) pour une page de recherche, avec plus de 70 millions de vidéo shots recherchables (> 7 ans de vidéos).",
        ],
        realisations=[
            """Pour permettre la recherche zero-shot dans les vidéos, création d'une stack ML propriétaire complète avec embeddings multimodaux, permettant l'analyse de plus de 70M de segments vidéo sans dépendance à des API externes.""",
            """Pour permettre des releases quotidiennes, mise en place d'une stack MLOps complète avec CI/CD, tests automatisés et déploiement containerisé, incluant monitoring et auto-healing des instances.""",
            """Pour optimiser les coûts d'infrastructure, architecture d'une solution multi-cloud avec nodes GPU distribués, permettant l'analyse de plus d'1M de vidéos/jour pour moins de 0.19€/heure.""",
            """Stack ML proprietaire (aucune API externe), avec multi modality search :
			\n- Recherche audio et vidéo croisee: trouve un sujet aborde par une personnalite donee.""",
            """Stack ML proprietaire (aucune API externe), avec multi modality search :
            \n- Recherche de vidéo par text ou image, en zero-shot classification.
            \n- Reconnaissance de personnalite dans les vidéos, wikipedia comme ground truth.
        """,
            """Ingestion scalable :
            \n- Système d'analyse distribuee avec multi nodes GPU. La pipeline d'ingestion depasse facilement les 1M vidéo shots analyses par jour en production,
            \n- Compatibility Multicloud (AWS, Scaleway) + On-premise, compute stack only needs servers with open-ssh, docker-compose, and nvidia-drivers.
            \n- Cost-effective, < 0.19 € / h de vidéo analysee, grace a une utilisation de petites instances CPU pour la data preparation.
            \n- Autohealing et monitoring des instances CPU et GPU.
        """,
            """Fast-search:
			\n- Système de recherche optimisé pour la latence (p50=1.5s) et le throughput (@128 p95=2.75s)
            \n- Système de donnees resiliant avec plus de 70 millions de vidéo shots cherchables (7 ans de vidéos)
            \n- Création, et mise a jour d'index embeddings, ainsi que de materialized views par utilisateur et projets.
            \n- Up to 20k de visiteurs par mois
            \n- Pre-load des modèles, et warmup pour reduction de la latence
            \n- Auto-healing de l'api backend, avec monitoring et alerting
		""",
            """Reconnaissances:
        	\n- Label DeepTech par la BPI
            \n- Future 40 par Station F
            \n- Prix de 25k du Fond Regional d'Investissement des Hauts de France
            \n- Prix IA de l'Institut des Mines Telecom
        """,
        ],
        technologies="Python (Pytorch, Hugging-Face, Scikit-learn, Pandas, FastAPI, Pydantic, Pytest), SQL, Cloud (AWS, GCP, Scaleway), Terraform, bash, Docker, Docker-Compose",
    ),
)

# ---------------------------------------------------------------------------- #
#                           Amsterdam Tech University                          #
# ---------------------------------------------------------------------------- #

amsterdam_tech_experience = ExperienceData(
    at="Amsterdam Tech University",
    title="Enseignant",
    contract="Temps partiel",
    where="Amsterdam, Netherlands (remote)",
    from_="04/2024",
    to="Present",
    logo="resume_parts/experience/2024-04_Amsterdamtech/Amsterdamtech Logo.png",
    Body=ExperienceBody(
        context="Sessions hebdomadaires, aux 2e et 4e année en Master Machine Learning / Data Science",
        realisations=[
            "Transmissions de connaissance et de methodologie de projet, lecture et analyse de papiers de recherche",
            "Suivi de projets de fin d'étude, transmission de méthodologie de R&D pour ML/DS.",
        ],
        technologies="Powerpoint, Jupyter Notebooks, python, scikit-learn, pytorch, numpy, pandas, matplotlib, seaborn",
        highlights_technologies="",
    ),
)

# ---------------------------------------------------------------------------- #
#                                  STATION F                                   #
# ---------------------------------------------------------------------------- #

station_f_experience = ExperienceData(
    at="STATION F",
    title="AI Lead",
    contract="associative",
    where="Paris, France",
    from_="12/2023",
    to="02/2025",
    logo="resume_parts/experience/2022-11_ICONO/station_f.png",
    Body=ExperienceBody(
        context="Nommé AI Club Leader a Station F, le plus grand incubateur de startups au monde",
        realisations=[
            "Conseil des startups sur l'IA en fast paced environnement",
            "Rencontre des nouvelles startups en IA pour les connecter avec des opportunités",
            "Organisations de dejeuners IA pour dynamiser l'ecosysteme.",
        ],
    ),
)

# ---------------------------------------------------------------------------- #
#                                   Revolve                                    #
# ---------------------------------------------------------------------------- #

revolve_summary = ExperienceData(
    at="Revolve Devoteam",
    title="Machine Learning Engineer",
    contract="Apprenticeship",
    where="Paris, France",
    from_="10/2021",
    to="10/2022",
    logo="resume_parts/experience/2021-10_Revolve/logo.png",
    Body=ExperienceBody(
        context="Apprentissage. Recherche en machine learning pour prédiction de victoire sur League of Legends, et ML-Ops pour déploiements de modèles sur Slack.",
        highlights_realisations=[
            "Déploiement de modèles de machine learning sur Slack, avec un Bot Serverless.",
            "Entrainement de modèles de prédictions de victoire sur League of Legends.",
            "Création d’un template de déploiement sur AWS de modèles de Machine Learning.",
        ],
        realisations=[
            """Création d’un Bot Slack en Serverless s’occupant de la gestion de modèles de Machine Learning et de Deep Learning:
- Déploiement des Endpoints Sage Maker automatique et quotidien
- Interaction modèles <-> utilisateur depuis Slack avec données tabulaires / textes / images. Stockage des inputs utilisateurs / prédictions des modèles / feedback utilisateurs. Système de remontée d’erreurs in-Slack
- Création d’un template de déploiement sur AWS de modèles de Machine Learning et de Deep Learning. Tests en local sur le modèle conteneurisé, puis tests en remote une fois le modèle déployé.
- Releases en environnement de Développement / Staging / Production avec Continuous Integration & Continuous Development""",
            """Conception et déploiement, en autonomie, d’un modèle de Deep Learning servant d’adversaire pour l'entraînement d’une équipe d’e-sport de niveau international.
- State of the art
- Exploratory Data Analysis et Data Preparation sur Big Data (~500K games)
- Design d’un ensemble de modèles
- Recherche d’architecture et d'hyper-paramètres
- Entraînement et Fine Tuning: Embeddings (CBOW) + Dense Neural Network + Recurrent Neural Network)
- Mise en production du modèle
""",
        ],
        technologies="Python, (PyTorch, Hydra, Optuna, Pandas), AWS (Sagemaker, IAM, S3, Cloud Watch, ECR, Lambda,, ECR), ML-Flow, DVC, Docker, Gitlab-CI, Python (Chalice, Boto3, Hugging-Face, Flask, Pytest), Gitlab-CI",
    ),
)


revolve_dl_research = ExperienceData(
    at="Revolve",
    title="Deep learning Research",
    contract="Apprenticeship",
    where="Paris, France",
    from_="04/2022",
    to="10/2022",
    logo="resume_parts/experience/2021-10_Revolve/logo.png",
    Body=ExperienceBody(
        context="Conception et déploiement, en autonomie, d'un modèle de Deep Learning servant d'adversaire pour l'entraînement d'une équipe d'e-sport de niveau international.",
        realisations=[
            "Analyse détaillée de la littérature scientifique du State of the Art",
            "Exploratory Data Analysis et Data Preparation sur Big Data (~500K games)",
            "Design d'un ensemble de modèles",
            "Recherche d'architecture et d'hyper-paramètres",
            "Entraînement et Fine Tuning: Embeddings (CBOW) + Dense Neural Network + Recurrent Neural Network)",
            "Mise en production du modèle",
        ],
        technologies="Python, (PyTorch Lightning, Hydra, Optuna, Pandas, Numpy, Ray, Matplotlib, Pytest), AWS, ML-Flow, DVC",
    ),
)

revolve_ml_ops = ExperienceData(
    at="Revolve",
    title="Machine Learning Operations",
    contract="Apprenticeship",
    where="Paris, France",
    from_="10/2021",
    to="04/2022",
    logo="resume_parts/experience/2021-10_Revolve/logo.png",
    Body=ExperienceBody(
        context="Création d'un Bot Slack en Serverless, controlant des inferences de Machine-Learning en interaction avec les utilisateurs.",
        realisations=[
            "Déploiement des Endpoints Sage Maker automatique et quotidien",
            "Interaction modèles / utilisateurs depuis Slack avec données tabulaires / textes / images",
            "Création d'un template de déploiement sur AWS de modèles de Machine Learning et de Deep Learning.",
            "Releases en environnement de Développement / Staging / Production avec Continuous Integration & Continuous Development",
        ],
        technologies="AWS (Sagemaker, IAM, S3, Cloud Watch, ECR), Python (Chalice, Boto3, Hugging-Face, Flask, Pytest), Docker, Gitlab-CI",
    ),
)

# ---------------------------------------------------------------------------- #
#                                    42 AI                                     #
# ---------------------------------------------------------------------------- #

ai_42_president = ExperienceData(
    at="42 Artificial Intelligence",
    title="President",
    contract="associative",
    where="Paris, France",
    from_="09/2021",
    to="09/2022",
    logo="resume_parts/experience/2021-09_42AI/logo.png",
    Body=ExperienceBody(
        context="""42AI, l'association d'Intelligence Artificielle de l'école 42, regroupe une 60 aine de membres actifs et touche une communauté de 4000 personnes. Nos missions sont de sensibiliser, former et accompagner les étudiants à l'Intelligence Artificielle. Aujourd'hui les cours que nous produisons sont partie intégrante du cursus diplômant de 42, et sont diffusés à l'international.""",
        realisations=[
            "Gestion d'une équipe de 30 personnes, dont 6 en rapport direct.",
            "Collecte de fonds et gestion administrative et financière: Trésorerie x 253%",
            "Recrutements et communications: membres actifs x 150%",
            "Pédagogie: Intégration de deux bootcamps dans le cursus de l'école 42",
            "Evenementiel, Cycle de conférence : participation moyenne 30 personnes",
            "Congrès d'intelligence artificielle: 22 conférenciers, 146 participants",
            "Evenementiel: Organisation de deux bootcamps, d'une semaine chacun, en Python et Machine Learning. 40 apprenants formes",
            "Partenariat inter-école: organisation d'un bootcamp commun",
            "Partenariat externe: projet commun avec des chercheurs du CNRS",
        ],
    ),
)

ai_42_hand2text = ExperienceData(
    at="42 Artificial Intelligence",
    title="Lead",
    contract="associative",
    where="Paris, France",
    from_="04/2022",
    to="09/2022",
    logo="resume_parts/experience/2021-09_42AI/logo.png",
    Body=ExperienceBody(
        context="Création d'un traducteur du langage des signes dans le but de faciliter la communication lors des visioconférences. Lead d'une équipe de 5. https://github.com/AI-2-The-Sky/Hand2Text",
        missions=[
            "Design du projet (objectif et feuille de route)",
            "Recrutement étudiant (entretiens d'embauches et tests techniques)",
            "Mise en place d'un squelette de projet permettant un démarrage Jour 1.",
            "Suivi hebdomadaire des équipes: Méthode agile, conseils sur les choix techniques, et restitution de cours en groupe.",
            "Résolution des points de blocage et transmissions des connaissances nécessaires au projet.",
        ],
        realisations=[
            "State of the art",
            "Datasets Collection",
            "Recherche d'architecture (ViT/ResNet Feature Extractor + Dense + RNN)",
            "Hyper-Parameter search + Training",
        ],
        technologies="Python, (PyTorch Lightning, Hydra, Optuna, Numpy, Matplotlib, Pytest), AWS, ML-Flow, DVC",
    ),
)

ai_42_elegant_elegans = ExperienceData(
    at="42 Artificial Intelligence",
    title="Product Owner",
    contract="associative",
    where="Paris, France",
    from_="04/2022",
    to="09/2022",
    logo="resume_parts/experience/2021-09_42AI/logo.png",
    Body=ExperienceBody(
        context="""Création d'outils de computer vision pour le tracking d'expériences de microscopie sur C. Elegans (organisme multicellulaire le plus utilisé en recherche biologique). Projet en collaboration avec deux laboratoires du CNRS.
Lead d'une équipe de 10
https://github.com/42-AI/Elegant-Elegans""",
        missions=[
            "Design du projet (objectif et feuille de route)",
            "Recrutement étudiant (entretiens d'embauches et tests techniques)",
            "Mise en place d'un squelette de projet permettant un démarrage Jour 1.",
            "Suivi hebdomadaire des équipes: Méthode agile, conseils sur les choix techniques, et restitution de cours en groupe.",
            "Résolution des points de blocage et transmissions des connaissances nécessaires au projet.",
        ],
    ),
)

ai_42_sentimental = ExperienceData(
    at="42 Artificial Intelligence",
    title="Lead",
    contract="associative",
    where="Paris, France",
    from_="03/2022",
    to="05/2022",
    logo="resume_parts/experience/2021-09_42AI/logo.png",
    Body=ExperienceBody(
        context="""Il est d'enjeu démocratique de veiller à l'équité du débat présidentiel à la télévision, pourtant les réseaux sociaux manquent encore d'un appareil à la hauteur de leur influence. Avec ce projet nous avons offert une analyse journalière du sentiment associé aux tweets mentionnant les candidats durant les élections 2022.
Lead d'une équipe de 6 personnes
https://github.com/42-AI/SentimentalBB""",
        missions=[
            "Design du projet (objectif et feuille de route)",
            "Recrutement étudiant (entretiens d'embauches et tests techniques)",
            "Mise en place d'un squelette de projet permettant un démarrage Jour 1.",
            "Suivi hebdomadaire des équipes: Méthode agile, conseils sur les choix techniques, et restitution de cours en groupe.",
            "Résolution des points de blocage et transmissions des connaissances nécessaires au projet.",
        ],
        realisations=[
            "Scrapping de tweets quotidien, aggregation et stockage",
            "Preprocessing",
            "Entraînement à la détection de sentiment sur Allocine puis inférence sur nos tweets. Naive Bayes / Transformers (pre-trained) + Classifier.",
            "Génération de visuels quotidiens",
            "Création d'un dataset de tweets labellisés pour mesurer l'accuracy des modèles à l'inférence.",
        ],
        technologies="Python (Sklearn,Hugging Face, Matplotlib/Seaborn, Pytest, GitHub Pages), AWS S3, DVC",
    ),
)

ai_42_self_aware = ExperienceData(
    at="42 Artificial Intelligence",
    title="Lead",
    contract="associative",
    where="Paris, France",
    from_="04/2021",
    to="09/2021",
    logo="resume_parts/experience/2021-09_42AI/logo.png",
    Body=ExperienceBody(
        context="""Constitution et lead d'une équipe de 5, pour la Donkey Car Virtual Race.
https://github.com/JBarmentlo/Self-Aware-Driving-Patate""",
        missions=[
            "Design du projet (objectif et feuille de route)",
            "Recrutement étudiant (entretiens d'embauches et tests techniques)",
            "Mise en place d'un squelette de projet permettant un démarrage Jour 1.",
            "Suivi hebdomadaire des équipes: Méthode agile, conseils sur les choix techniques, et restitution de cours en groupe.",
            "Résolution des points de blocage et transmissions des connaissances nécessaires au projet.",
        ],
        realisations=[
            "Deep Reinforcement Learning avec Auto-Encoder, Soft-Actor-Critic",
            "Entrainement distribué",
            "Optimiseur Bayésien",
            "Docker",
            "S3 Buckets",
            "Partenariat avec Qarnot pour la puissance de calcul",
        ],
        technologies="Python (PyTorch, Numpy), Docker, AWS",
    ),
)

ai_42_lab_director = ExperienceData(
    at="école 42",
    title="AI Lab Director",
    contract="associative",
    where="Paris, France",
    from_="08/2021",
    to="11/2022",
    # from_="09/2021",
    # to="09/2022",
    logo="resume_parts/experience/2021-09_42AI/logo.png",
    Body=ExperienceBody(
        sentence_summary="""Direction technique et stratégique, recrutement, création de template de projets, formation, suivi jusqu'aux déploiements, et gestion des projets du Lab.""",
        context="""Le Lab 42AI est un laboratoire de Machine Learning s'attaquant à des problèmes à impact positif pour la société.""",
        # """J'ai personnellement veillé à la création et au bon déroulement de chacun des projets du Lab.""",
        highlights_realisations=[
            "Création d'un outil de tracking de C. Elegans sous microscope pour le CNRS.",
            "Compétition de voiture autonome dans simulateur (DonkeyCar).",
            "Analyse de sentiment quotidienne sur Twitter pour les élections présidentielles de 2022.",
        ],
        realisations=[
            "Design du projet (objectif et feuille de route)",
            "Recrutement étudiant (entretiens d'embauches et tests techniques)",
            "Mise en place d'un squelette de projet permettant un démarrage Jour 1.",
            "Suivi hebdomadaire des équipes: Méthode agile, conseils sur les choix techniques, et restitution de cours en groupe.",
            "Résolution des points de blocage et transmissions des connaissances nécessaires au projet.",
            f"{ai_42_hand2text.Body = }",
            f"{ai_42_elegant_elegans.Body = }",
            f"{ai_42_sentimental.Body = }",
            f"{ai_42_self_aware.Body = }",
        ],
        highlights_technologies="Python, (PyTorch, Sklearn, Hugging Face, Hydra, Optuna, Numpy, Matplotlib, Pytest), GitHub Actions, AWS, ML-Flow, DVC",
    ),
)

# ---------------------------------------------------------------------------- #
#                             Paris AI Society                                 #
# ---------------------------------------------------------------------------- #

paris_ai_society = ExperienceData(
    at="Paris AI Society",
    title="President",
    contract="associative",
    where="Paris, France",
    from_="03/2024",
    to="Present",
    logo="resume_parts/experience/2024-03_ParisAISociety/PAIS_logo_BW.png",
    Body=ExperienceBody(
        context="Organisation d'evenements pour regrouper les professionnels de l'IA a Paris.",
        realisations=[
            "Organisation de conferences IA (70-150 personnes), d'afterworks et dejeuners (30-60 personnes)."
        ],
    ),
)

# ---------------------------------------------------------------------------- #
#                                   Natixis                                    #
# ---------------------------------------------------------------------------- #

# Feature engineering:


natixis_experience = ExperienceData(
    at="Natixis",
    title="Data Scientist",
    contract="internship",
    where="Paris, France",
    from_="02/2020",
    to="08/2020",
    logo="resume_parts/experience/2020-02_Natixis/logo.png",
    Body=ExperienceBody(
        context="Stage de recherche : Développement d'un modèle d'outlier detection contre les cyber-attaques, et mise en production pour surveillance de 60 000 machines.",
        # context="""La détection d'attaques furtives par analyse de signaux faibles
        # Aujourd'hui, la lutte contre les malwares dans les entreprises est principalement une défense en réponse. Dans un but de défense proactive, ce projet fut l'occasion d'étudier et de mettre en pratique les dernières avancées permises par l'IA.
        # À travers la méthodologie Agile, ce stage s'est déroulé lors de la première édition du lab 42 / Natixis.""",
        highlights_realisations=[
            # "Etat de l'art sur l'outlier detection, et securite informatique Windows.",
            "Feature engineering: parseur REGEX de command line résistant aux obfuscations, dictionnaires de comportements machines hebdomadaires",
            "Évaluations et mise en production, avec réécriture pour calcul distribué.",
        ],
        realisations=[
            "Etat de l'art sur l'outlier detection, et securite informatique Windows.",
            "Heavy feature engineering: (parseur REGEX de command line résistant aux offuscations, dictionnaires de comportements machines hebdomadaires)",
            "Evaluation et mise en production, avec reecriture pour calcul distribué.",
            "Création d'un dataset labélisé :",
            "Sélection d'événements intéressants en collaboration avec les analystes de sécurité.",
            "Analyse statistique, puis nettoyage de la donnée labellisée.",
            "Création de features :",
            "État de l'art sur la création de features (Machine Learning / Sécurité informatique)",
            "Création de features depuis des données brutes textuelles (logs Windows/Linux/Apps)",
            "Création d'un parseur de Command-Line en REGEX, résistant contre les techniques d'offuscations.",
            "Mise en place de tables de correspondances CSV",
            "Création automatique de dictionnaires hebdomadaires des couples Processus-Parent et Processus-Enfant, en relation avec le nombre de machines et le nombre d'exécutions du couple.",
            "Entrainement de l'algorithme de détection :",
            "État de l'art sur les modèles de machine Learning (non supervisé et supervisé)",
            "Support Vector Machine, linear regression, NLP, Clustering, PCA",
            "Data Visualisation",
            "Mise en place de métriques d'évaluations :",
            "Quantitatives: recall, précision et F-score sur multiples datasets",
            "Qualitative: Relecture des résultats avec les analystes de sécurité",
            "Mise en production de l'outil :",
            "Réduction de la quantité de calculs et de la mémoire nécessaire",
            "Réécriture du code pour permettre un calcul distribué",
            "POC en Reinforcement Learning:",
            "Mise en place du modèle d'Alpha Zero adapté au Puissance-4, sur 2 semaines.",
        ],
        technologies="Python (Numpy, Pandas, Scikit Learn, Matplotlib), Splunk, REGEX",
    ),
)

# ---------------------------------------------------------------------------- #
#                                  Formations                                   #
# ---------------------------------------------------------------------------- #


# IGPDE: 2*2j + 2*1j
# Dassault Systemes: 2*3j

# 1 jour
formation_aws = ExperienceData(
    at="Pôle Emploi",
    title="Formateur AWS",
    contract="Contract",
    where="Paris, France",
    from_="12/2021",
    to="12/2021",
    logo=None,
    Body=ExperienceBody(
        context="Formateur durant une journee pour une classe de 5 intermédiaires AWS. Formation theorique et pratique au travers d'hands on labs.",
        realisations=["S3, EC2, EBS, EFS, RDS, DynamoDB, VPC, Road 53, IAM, CloudWatch, Lambda"],
        technologies="AWS",
    ),
)

# 5 jours
formation_cartier = ExperienceData(
    at="Cartier",
    title="Formateur Python (Data)",
    contract="Contract",
    where="la Chaux-de-Fonds, Switzerland",
    from_="09/2020",
    to="09/2020",
    logo="resume_parts/experience/2019-12_CYMA/02_logo.png",
    Body=ExperienceBody(
        context="""Formateur durant une semaine pour une classe de 5 développeurs
Python (concepts avancés), Pandas et Numpy

Dans l'objectif de mettre a profit les donnees collectees par Cartier, l'equipe souhaitait obtenir une comprehension avancee de Python, avec une attention portee sur la pratique.""",
        technologies="Python (Flask, MySQL/SQLite, argparse, Numpy, Pandas, Matplotlib, Seaborn), Regex",
    ),
)

# 5 jours
formation_ml = ExperienceData(
    at="Pôle Emploi",
    title="Formateur Machine Learning",
    contract="Contract",
    where="Paris, France",
    from_="05/2021",
    to="05/2021",
    logo="resume_parts/experience/2019-12_CYMA/03_logo.png",
    Body=ExperienceBody(
        context="""Formateur durant une semaine pour une classe de 15 intermédiaires python, pour accompagner leur montée en compétences en Data Sciences.
Prise en charge de la rédaction du support de cours.
Formation portée sur la pratique avec des datasets Kaggle.""",
        realisations=[
            "Exploratory Data Analysis (Data Visualisation, Feature identification)",
            "Preprocessing (Data Cleansing, Missing Value imputation, Feature Création, Feature Engineering, Feature Normalization/Scaling, Dimensionality Reduction)",
            "Classification (Logistic Regression, Random Forest Classification, Support Vector Machine, Dense Neural Network Keras)",
            "Regression (Linear Regression, Random Forest Regresion, SVR)",
            "Model Validation (Scores, Cross Validation, HyperParameter Optimization)",
        ],
        technologies="Python (pandas, numpy, scikit learn, matplotlib, seaborn, keras), Jupyter-notebooks",
    ),
)

# ---------------------------------------------------------------------------- #
#                                  Education                                    #
# ---------------------------------------------------------------------------- #

education_42 = ExperienceData(
    at="42",
    title="Computer Science",
    contract="Master (RNCP 7)",
    where="Paris, France",
    from_="10/2018",
    to="10/2022",
    logo="resume_parts/Education/42/logo.png",
    Body=ExperienceBody(
        context="""Speciality : Artificial Intelligence
Master (RNCP 7 / BAC +5)
Level > 21 in school""",
        missions=[
            "Neural Network From Scratch: librairie de DeepLearning creee a partir numpy : optimizers, costs, layers, fonctions d'activation, model manager,...",
            "Resolution de problèmes Non-Polynomiaux: Sudoku, N-Puzzle, Recouvrement exact du plan, flow maximum dans un graphe non orienté,...",
            "Virtual CPU: Compilation, puis exécution de multiples programmes en simultané. Gestion de registres, virtualisation, et visualisation.",
            "Memory Allocation Manager: Kernel interface, multi-threadée, avec défragmentation. Résolution en temps logarithmique.",
        ],
    ),
)

formation_summary = ExperienceData(
    # at="Independant",
    at="",
    title="Formateur",
    contract="Contract",
    where="Paris, France",
    from_="09/2020",
    date_details="> 200 heures",
    to="Present",
    logo=None,
    Body=ExperienceBody(
        context="""Formateur Machine Learning / Data Science sur des sessions de 1 à 5 jours.\n
Entreprises formées : Dassault Systèmes (US), IGPDE, Cartier, Pôle Emploi,...""",
        # realisations=[
        #     # "Dassault Systemes & IGPDE: Python et Data Science et Machine Learning",
        #     # "Cartier & Pôle Emploi: Python et Data Science",
        #     # "Cartier: Python et Data Science (scikit-learn, pandas, numpy, matplotlib, seaborn, jupyter-notebooks)",
        #     # "Pôle Emploi: AWS (S3, EC2, EBS, EFS, RDS, DynamoDB, VPC, Road 53, IAM, CloudWatch, Lambda)",
        #     # "42: Computer Vision (pytorch, tensorflow, keras, pytorch-lightning, hydra, optuna, numpy, matplotlib, pytest)",
        #     # "42: Reinforcement Learning (pytorch, numpy, matplotlib, pytest)",
        #     # "42: NLP (hugging-face, transformers, spacy, nltk, pytorch, tensorflow, keras, pytorch-lightning, hydra, optuna, numpy, matplotlib, pytest)",
        # ],
        # technologies="Python, Data Science (sklearn, pandas, numpy, matplotlib, jupyter-notebooks), Machine Learning (PyTorch, Optuna)",
        highlights_technologies="",
    ),
)

# ---------------------------------------------------------------------------- #
#                            Experience Categories                              #
# ---------------------------------------------------------------------------- #

work_experience = [
    icono_experience,
    # station_f_experience,
    amsterdam_tech_experience,
    ai_42_lab_director,
    revolve_summary,
    natixis_experience,
    formation_summary,
]

volunteering_experience = [
    # paris_ai_society,
    # ai_42_president,
    # ai_42_hand2text,
    # ai_42_elegant_elegans,
    # ai_42_sentimental,
    # ai_42_self_aware
]

education_experience = [education_42]

# ALL_EXPERIENCES = work_experience + volunteering_experience + education_experience
