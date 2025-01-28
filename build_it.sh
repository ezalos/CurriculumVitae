#! /bin/bash -

################################################################################
################################################################################
#
# Setup
#
################################################################################
################################################################################

################################################################################
# Default variables
################################################################################
COLOR_RED="\e[1;31m"
COLOR_GREEN="\e[1;32m"
COLOR_YELLOW="\e[1;33m"
COLOR_BLUE="\e[1;34m"
COLOR_PURPLE="\e[1;35m"
COLOR_CYAN="\e[1;36m"
COLOR_RESET="\e[0m"

CONDA_ENV="resume"
CV_NAME="CV_Louis_DEVELLE"
CV_DIR_LATEX=$(pwd)/resume/latex

PYTHON_COMMAND="uv run python"

################################################################################
# Help
################################################################################
Help()
{
   # Display Help
   echo "Script to execute after the git clone of the project"
   echo "IT MUST BE LAUNCHED FROM THE PROJECT TOP DIRECTORY"
   echo
   echo "usage: bash .42AI/init.sh [--help] [python_path]"
   echo "options:"
   echo "       --help          Print this Help."
   echo "   	cv_name     Optional name for the end CV file"
   echo "                   Defaults to: $CV_NAME"
   echo
}


################################################################################
# Process the input options. Add options as needed.
################################################################################
while test $# -gt 0
do
    case "$1" in
        --help) # Display Help
                        Help
                        exit 0
            ;;
        --*) # Bad option used
                        echo "bad option $1"
                        echo
                        Help
                        exit 1
            ;;
        *) # Setting up python path
                        CV_NAME=$1
                        echo "CV name has been set to: $CV_NAME"
            ;;
    esac
    shift
done


################################################################################
# CONDA Environment
################################################################################

echo -e $COLOR_YELLOW "INIT: " $COLOR_RESET "Verifying uv installation and environment..."

# Check if uv is installed
if ! uv --version
then
	echo -e $COLOR_RED "uv is not installed" $COLOR_RESET
	echo "Install uv first with:"
	echo -e $COLOR_YELLOW "curl -LsSf https://astral.sh/uv/install.sh | sh" $COLOR_RESET
	exit 1
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]
then
	echo -e $COLOR_RED "No virtual environment found" $COLOR_RESET
	echo "You can create one by executing the following command:"
	echo -e $COLOR_YELLOW "uv venv .venv" $COLOR_RESET
	exit 1
fi

if [ -f ".envrc" ]; then
    source .envrc
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Verify uv environment is working
if ! uv tree > /dev/null 2>&1
then
	echo -e $COLOR_RED "uv environment is not properly set up" $COLOR_RESET
	exit 1
fi

echo -e $COLOR_GREEN "uv installation and environment are properly set up" $COLOR_RESET


################################################################################
################################################################################
#
# Main program
#
################################################################################
################################################################################

################################################################################
# Latex generation
################################################################################

$PYTHON_COMMAND -m src

if [ $? == 0 ]
then
    echo -e $COLOR_GREEN "LaTeX files have been generated !" $COLOR_RESET
else
    echo -e $COLOR_RED "ERROR: in python script" $COLOR_RESET
    exit 1
fi


################################################################################
# PDF generation
################################################################################

# from: https://tex.stackexchange.com/a/332692
docker run --rm -i -v ${CV_DIR_LATEX}:/data -v ${CV_DIR_LATEX}/fonts:/root/.fonts mingc/latex xelatex -output-driver="xdvipdfmx -q -E -V 7" cv_12.tex

if [ $? == 0 ]
then
    echo -e $COLOR_GREEN "pdf has been generated !" $COLOR_RESET
else
    echo -e $COLOR_RED "ERROR: pdf could not be generated from LaTeX" $COLOR_RESET
    exit 1
fi

# qpdf ${CV_DIR_LATEX}/cv_12.pdf --pages . 1-1 -- ${CV_DIR_LATEX}/cv_12_1.pdf

cp -f ${CV_DIR_LATEX}/cv_12.pdf resume/out/pdf/${CV_NAME}.pdf
cp -f resume/out/pdf/${CV_NAME}.pdf resume/out/pdf/latest.pdf


################################################################################
# PNG generation
################################################################################

pdftoppm resume/out/pdf/${CV_NAME}.pdf resume/out/latest -png -f 1 -singlefile

if [ $? == 0 ]
then
    echo -e $COLOR_GREEN "png has been generated !" $COLOR_RESET
else
    echo -e $COLOR_RED "ERROR: png could not be generated from pdf" $COLOR_RESET
    exit 1
fi

# Compress PNG with pngquant
pngquant --quality=75-90 --strip --force --output resume/out/latest.png resume/out/latest.png
