%----------------------------------------------------------------------------------------
%	CLASS OPTIONS AND REQUIRED PACKAGES
%----------------------------------------------------------------------------------------

\ProvidesClass{resume-structured-blue}[2022/07/30 CV class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass{article}

\usepackage[hmargin=1.25cm, vmargin=0.75cm, includefoot]{geometry} % Specifies horizontal and vertical page margins
\usepackage[hidelinks]{hyperref} % Required for links
\usepackage{ragged2e}

%----------------------------------------------------------------------------------------
%	COLORS
%----------------------------------------------------------------------------------------

\usepackage[usenames,dvipsnames]{xcolor}	% Required for custom colors

\definecolor{primary}{HTML}{2b2b2b} 		% dark grey
\definecolor{secondary}{HTML}{5271FF}		% blue
\definecolor{tertiary}{HTML}{424242} 		% light grey

\definecolor{black}{HTML}{010101} 			% for name
\definecolor{white}{HTML}{ffffff} 			% for the invisible elements


%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------
\usepackage{enumitem}
\setlist[itemize]{leftmargin=5mm}
% \setlist[itemize]{align=parleft,left=0pt..1em}

\newenvironment{tightitemize} % Defines the tightitemize environment which modifies the itemize environment to be more compact
{\vspace{-\topsep}\begin{itemize}\itemsep1pt \parskip0pt \parsep0pt}
{\end{itemize}\vspace{-\topsep}}


%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------

\usepackage{fontspec} % Required for specifying custom fonts in XeLaTeX

% The primary font for content text; defines bold, italic and bold-italic as well
\setmainfont[Color=tertiary, Path = fonts/assistant/,BoldFont=Assistant-SemiBold]{Assistant-ExtraLight}
% The font used where \sfffamily is called
\setsansfont[Scale=MatchLowercase,Mapping=tex-text, Path = fonts/raleway/]{Raleway-ExtraLight}


%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------

\usepackage{titlesec} % Required for customizing section/subsection/etc titles

\titlespacing{\titlename}{0pt}{0pt}{0pt} % Removes the spacing around the main section titles
\titlespacing{\section}{0pt}{0pt}{0pt} % Removes the spacing around the main section titles
\titlespacing{\jobtitle}{0pt}{0pt}{0pt} % Removes the spacing around the subsections

\newcommand{\sectionspace}{\vspace{8pt}} % Defines a command to add a set amount of space after sections and subsections
\newcommand{\undertitle}{\vspace{4pt}} % Defines a command to add a set amount of space after sections and subsections


%---------------------------------------%
% Titles
%---------------------------------------%

% Resume Name
\newcommand{\titlename}[2]{
\color{black}\scshape\fontspec[Path = fonts/voga/]{Voga-Regular}\fontsize{60pt}{90pt}\selectfont \raggedright {#1} \normalfont
\color{black}\scshape\fontspec[Path = fonts/voga/]{Voga-Bold}\fontsize{60pt}{90pt}\selectfont \raggedright {#2} \normalfont
}

% Applied Positon
\newcommand{\titlejob}[1]{
\color{secondary}\scshape\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{25pt}{45pt}\selectfont \raggedright {#1} \normalfont}

% Title of sections (Education, Experience, ...)
\titleformat{\section}{
\color{primary}\scshape\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{16pt}{24pt}\selectfont \raggedright\uppercase}{}{0em}{}


%---------------------------------------%
% Experience Header
%---------------------------------------%

% Job title
% Customize the subsections and places worked/studied titles
\newcommand{\sectionprimary}[1]{
\color{secondary}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{12pt}{14pt}\bfseries\flushleft\selectfont {#1 \\ } \normalfont}

% Company name
% Used for creating subsections where a description is required on the same line
\newcommand{\sectionsecondary}[1]{
\color{primary}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{10pt}{12pt}\selectfont\bfseries\uppercase { #1 } \normalfont}

% location | dates
% Used for specifying a duration and/or location under a subsection
\newcommand{\sectiontertiary}[1]{
\color{tertiary}\raggedright\scshape\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{8pt}{10pt}\selectfont { #1 \\} \normalfont}


\newcommand{\experienceheader}[3]{
	{\color{secondary}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{12pt}{14pt}\bfseries\flushleft\selectfont {#1 \\ } \normalfont}
	{\undertitle}
	{\color{primary}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{10pt}{12pt}\selectfont\bfseries\uppercase { #2 } \normalfont}
	{\color{tertiary}\raggedright\scshape\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{8pt}{10pt}\selectfont {\hfill #3 \\} \normalfont}
	{\undertitle}
}

\newcommand{\experiencetitle}[1]{
	{\color{secondary}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{12pt}{14pt}\bfseries\flushleft\selectfont {#1 \\ } \normalfont}
	{\undertitle}
}

\newcommand{\experiencetitledetails}[2]{
	{\color{primary}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{10pt}{12pt}\selectfont\bfseries\uppercase { #1 } \normalfont}
	{\color{tertiary}\raggedright\scshape\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{8pt}{10pt}\selectfont {\hfill #2 \\} \normalfont}
	{\undertitle}
}
%---------------------------------------%
% Content
%---------------------------------------%


\newcommand{\experiencedescription}[1]{
\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-Light}\fontsize{10pt}{10pt}\selectfont {\justifying #1 \undertitle} \normalfont
}

\newcommand{\experiencesimplelist}[1]{
	% \color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-SemiBold}\fontsize{10pt}{8pt}\selectfont { #1 \\ } \normalfont
	% {\undertitle}
	\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-Light}\fontsize{10pt}{10pt}\selectfont { #1 } \normalfont
}

\newcommand{\experiencedoublelist}[2]{
	\begin{minipage}[t]{0.45\textwidth}
		\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-SemiBold}\fontsize{10pt}{8pt}\selectfont { Missions \\ } \normalfont
		{\undertitle}
		\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-Light}\fontsize{8pt}{6pt}\selectfont { #1 } \normalfont
		% \color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-Light}\fontsize{8pt}{6pt}\selectfont {
		% 	\begin{tightitemize}
		% 	\item #1
		% 	\item #1
		% 	\end{tightitemize}
		%  } \normalfont
	\end{minipage} % The end of the left column
	\begin{minipage}[t]{0.45\textwidth}
		\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-SemiBold}\fontsize{10pt}{8pt}\selectfont { Realisations \\ } \normalfont
		{\undertitle}
		\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-Light}\fontsize{8pt}{6pt}\selectfont { #2 } \normalfont
	\end{minipage} % The end of the left column
}

\newcommand{\experiencetechno}[1]{
{\undertitle}
\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-SemiBold}\fontsize{10pt}{10pt}\selectfont { Technologies : } \normalfont
\color{tertiary}\raggedright\fontspec[Path = fonts/assistant/]{Assistant-Light}\fontsize{9pt}{10pt}\selectfont { #1 \\ } \normalfont
}
% Content
%	#	blocks
%	#	description

% Seems uncesary for the moment
%----------------------------------------------------------------------------------------
%	Packages added by myself
%----------------------------------------------------------------------------------------

% \usepackage{import}
\usepackage{subfiles}
\usepackage{xcolor}
\usepackage[export]{adjustbox}
% \usepackage{indentfirst}
\setlength{\parindent}{5mm}


%----------------------------------------------------------------------------------------
%	MAIN HEADING COMMAND
%----------------------------------------------------------------------------------------

\newcommand{\Hrule}[4][.]{%
  \par\addvspace{#2}%
  \begingroup\color{#1}%
  \hrule height #4
  \endgroup
  \addvspace{#3}%
}

\newcommand{\resumeheader}[4]{ % Defines the command for the main heading
	\begin{minipage}[t]{0.7\textwidth}
		\begingroup
      		\vspace{0pt}
			\titlename{#1}{#2}
			\Hrule[secondary!40]{20pt}{10pt}{3pt}
			\titlejob{#3}
		\endgroup
	\end{minipage} % The end of the left column
	\begin{minipage}[t]{0.1\textwidth}
		\fontsize{1pt}{1pt}
		\fontspec[Color=white, Path=fonts/raleway/]{Raleway-Medium}\selectfont .
	\end{minipage} % The end of the left column
	\begin{minipage}[t]{0.2\textwidth}
		\strut\vspace*{-\baselineskip}\newline\includegraphics[height=4cm,cfbox=secondary 2pt 0pt]{#4}
	\end{minipage} % The end of the left column
}
