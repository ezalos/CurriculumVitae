#!/usr/bin/env bash

# Check if files were passed
if [ "$#" -eq 0 ]; then
  echo "No files specified."
  exit 1
fi

non_authorized_keyword_part_1="!no"
non_authorized_keyword_part_2="commit"
non_authorized_keyword="$non_authorized_keyword_part_1$non_authorized_keyword_part_2"

# Get the list of staged files
# staged_files=$(git diff --cached --name-only)

# Initialize a flag to track if any issues are found
issues_found=false

# Loop through each staged file
# for file in $staged_files; do
for file in "$@"; do

  # Skip the .pre-commit-config.yaml file
  if [[ "$file" == ".pre-commit-config.yaml" ]]; then
    continue
  fi

  # Check if the file contains the non_authorized string
  matches=$(grep -nH "$non_authorized_keyword" "$file")

  if [[ -n "$matches" ]]; then
    # Set the flag to true if any matches are found
    issues_found=true
	COLOR_RESET="\e[0m"
	COLOR_RED="\e[1;31m"
	file_and_line=$(echo "$matches" | cut -d':' -f1,2)
	rest_of_string=$(echo "$matches" | cut -d':' -f3-)


	# Process each matching line
	echo "$matches" | while IFS= read -r match; do
		file_and_line=$(echo "$match" | cut -d':' -f1,2)
		rest_of_string=$(echo "$match" | cut -d':' -f3-)
		echo -e "ERROR '$non_authorized_keyword' found: $COLOR_RED$file_and_line$COLOR_RESET line content: $rest_of_string"
	done
    # echo -e "ERRROR '$non_authorized_keyword' found: $COLOR_RED $file_and_line $COLOR_RESET $rest_of_string"
  fi
done

# If issues were found, print a message and exit with a non-zero status
if $issues_found; then
#   echo
#   echo "Remove the '$non_authorized_keyword' string and try again."
  exit 1
else
  exit 0
fi
