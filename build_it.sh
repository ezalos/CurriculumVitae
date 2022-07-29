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
CV_DIR_LATEX=`pwd`/resume_latex


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

echo -e $COLOR_YELLOW "INIT: " $COLOR_RESET "Verifying your conda environment..."

if [[ "$CI" ]]
then
    echo -e $COLOR_PURPLE "Skipping test because we are in Github actions" $COLOR_RESET
elif [ -z "$CONDA_DEFAULT_ENV" ]
then
    echo -e $COLOR_RED "No conda environment" $COLOR_RESET
        echo "You can create one by executing the folowing command:"
    echo -e $COLOR_YELLOW "conda create -n $CONDA_ENV python=3.8" "\n" "conda activate $CONDA_ENV" $COLOR_RESET
        exit 1

elif [ "$CONDA_DEFAULT_ENV" == "$CONDA_ENV" ]
then
    echo -e $COLOR_GREEN "Good conda environment" $COLOR_RESET

# elif [ "$CONDA_DEFAULT_ENV" == "base" ]
else
    echo -e $COLOR_RED "Conda environment is not active" $COLOR_RESET

        echo "If necessary, you can create your environment with:"
    echo -e $COLOR_YELLOW "conda env create -f environment.yml" $COLOR_RESET

        echo "Activate your environment with:"
    echo -e $COLOR_YELLOW "conda activate $CONDA_ENV" $COLOR_RESET
        exit 1
fi


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

eval "$(conda shell.bash hook)"
conda activate $CONDA_ENV
python -m MakeResume

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

docker run --rm -i -v ${CV_DIR_LATEX}:/data -v ${CV_DIR_LATEX}/fonts:/root/.fonts mingc/latex xelatex cv_12.tex

if [ $? == 0 ]
then
    echo -e $COLOR_GREEN "pdf has been generated !" $COLOR_RESET
else
    echo -e $COLOR_RED "ERROR: pdf could not be generated from LaTeX" $COLOR_RESET
    exit 1
fi

mv -f ${CV_DIR_LATEX}/cv_12.pdf ${CV_NAME}.pdf


################################################################################
# PNG generation
################################################################################

pdftoppm ${CV_NAME}.pdf ${CV_NAME} -png -f 1 -singlefile

if [ $? == 0 ]
then
    echo -e $COLOR_GREEN "png has been generated !" $COLOR_RESET
else
    echo -e $COLOR_RED "ERROR: png could not be generated from pdf" $COLOR_RESET
    exit 1
fi
