%----------------------------------------------------------------------------------------
%	CLASS OPTIONS AND REQUIRED PACKAGES
%----------------------------------------------------------------------------------------

\ProvidesClass{deedy-resume}[2014/04/30 CV class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass{article}

\usepackage[hmargin=1.25cm, vmargin=0.75cm, includefoot]{geometry} % Specifies horizontal and vertical page margins
\usepackage[hidelinks]{hyperref} % Required for links

%----------------------------------------------------------------------------------------
%	COLORS
%----------------------------------------------------------------------------------------

\usepackage[usenames,dvipsnames]{xcolor} % Required for custom colors

\definecolor{primary}{HTML}{2b2b2b} % The primary document color for content text
% \definecolor{headings}{HTML}{3333FF} % The color of the large sections
% \definecolor{headings}{HTML}{6A6A6A} % The color of the large sections
\definecolor{headings}{HTML}{424242} % The color of the large sections
\definecolor{subheadings}{HTML}{5271FF} % The color of subsections and places worked/studied
% \definecolor{subheadings}{HTML}{333333} % The color of subsections and places worked/studied
\definecolor{date}{HTML}{666666} % The color used for the Last Updated text at the top right
\definecolor{white}{HTML}{ffffff} % The color used for the Last Updated text at the top right

%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------

\usepackage{fontspec} % Required for specifying custom fonts in XeLaTeX

\setmainfont[Color=primary, Path = fonts/assistant/,BoldFont=Assistant-SemiBold]{Assistant-ExtraLight} % The primary font for content text; defines bold, italic and bold-italic as well

\setsansfont[Scale=MatchLowercase,Mapping=tex-text, Path = fonts/raleway/]{Raleway-ExtraLight} % The font used where \sfffamily is called

%----------------------------------------------------------------------------------------
%	LAST UPDATED COMMAND
%----------------------------------------------------------------------------------------

\usepackage[absolute]{textpos} % Required for positioning the Last Updated text at the top right of the page
\usepackage[UKenglish]{isodate} % Prints the Last Updated date in UK English format

\setlength{\TPHorizModule}{0.01\paperwidth} % Sets the units for the horizontal position used in the \begin{textblock} argument
\setlength{\TPVertModule}{0.01\paperwidth} % Sets the units for the vertical position used in the \begin{textblock} argument

\newcommand{\lastupdated}{ % Create a new command for printing the Last Updated text
\begin{textblock}{25}(75,2) % The position of the Last Updated text on the page (75% of the page across, 2% down)
\color{date}\fontspec[Path = fonts/raleway/]{Raleway-ExtraLight}\fontsize{6pt}{8pt}\selectfont % Text styling of the text
Last Updated on \today % Last Updated text
\end{textblock}}

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
			\fontsize{60pt}{80pt} % Font size
			\fontspec[Color=headings, Path=fonts/voga/]{Voga-Regular}\selectfont #1  \nolinebreak % Last name font
			\fontspec[Color=headings, Path=fonts/voga/]{Voga-Bold}\selectfont #2 % First name font
			% \hspace{2\linewidth}
			\Hrule[subheadings!40]{30pt}{10pt}{3pt}
			% \noindent\makebox[\linewidth]{\color{subheadings}\rule{\paperwidth}{4pt}} % Horizontal rule
			% \linebreak
			\fontsize{20pt}{30pt} % Font size
			\fontspec[Color=subheadings, Path=fonts/raleway/]{Raleway-Medium}\selectfont #3 % First name font
			% \fontspec[Color=subheadings, Path=fonts/voga/]{Voga-Bold}\selectfont #3 % First name font
		\endgroup
	\end{minipage} % The end of the left column
	\begin{minipage}[t]{0.1\textwidth}
		\fontsize{1pt}{1pt}
		\fontspec[Color=white, Path=fonts/raleway/]{Raleway-Medium}\selectfont .
	\end{minipage} % The end of the left column
	\begin{minipage}[t]{0.2\textwidth}
		\strut\vspace*{-\baselineskip}\newline\includegraphics[height=4cm,cfbox=subheadings 2pt 0pt]{#4}
	\end{minipage} % The end of the left column
}

%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------

\usepackage{titlesec} % Required for customizing section/subsection/etc titles

\titlespacing{\section}{0pt}{0pt}{0pt} % Removes the spacing around the main section titles
\titlespacing{\subsection}{0pt}{0pt}{0pt} % Removes the spacing around the subsections
\newcommand{\sectionspace}{\vspace{8pt}} % Defines a command to add a set amount of space after sections and subsections

\titleformat{\section}{ % Customize the large section titles
\color{headings}\scshape\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{16pt}{24pt}\selectfont \raggedright\uppercase}{}{0em}{}

\titleformat{\subsection}{ % Customize the subsections and places worked/studied titles
\color{subheadings}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{10pt}{12pt}\selectfont\bfseries\uppercase}{}{0em}{}

\newcommand{\runsubsection}[1]{ % Used for creating subsections where a description is required on the same line
\color{subheadings}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{10pt}{12pt}\selectfont\bfseries\uppercase {#1} \normalfont}

\newcommand{\descript}[1]{ % Used for describing the subsection either on the same line or underneath
\color{subheadings}\raggedright\scshape\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont {#1 \\} \normalfont}

\newcommand{\location}[1]{ % Used for specifying a duration and/or location under a subsection
\color{headings}\raggedright\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{10pt}{12pt}\selectfont {#1\\} \normalfont}

%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------

\newenvironment{tightitemize} % Defines the tightitemize environment which modifies the itemize environment to be more compact
{\vspace{-\topsep}\begin{itemize}\itemsep1pt \parskip0pt \parsep0pt}
{\end{itemize}\vspace{-\topsep}}

%----------------------------------------------------------------------------------------
%	Packages added by myself
%----------------------------------------------------------------------------------------

% \usepackage{import}
\usepackage{subfiles}
\usepackage{xcolor}
\usepackage[export]{adjustbox}
% \usepackage{indentfirst}
\setlength{\parindent}{5mm}
