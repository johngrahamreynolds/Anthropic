#!/usr/bin/bash

while getopts "d:f:" opt
do
   case "$opt" in
      d ) dir_path="$OPTARG" ;;
      f ) file_name="$OPTARG" ;;
   esac
done

### SCRIPT ### 

# compile the tex file Claude gave us and create a PDF
latexmk -pdf $dir_path/$file_name.tex
# move it to the relevant directory where we house Claude's tex work
mv /workspaces/Anthropic/$file_name.pdf /workspaces/Anthropic/src/latex/
# clean up lingering non-pdf tex files
latexmk -c $dir_path/$file_name.tex


# hardcoded subprocess testing - keeping for future debugging
# latexmk -pdf /workspaces/Anthropic/src/latex/hello_world_latex.tex
# mv /workspaces/Anthropic/hello_world_latex.pdf /workspaces/Anthropic/src/latex/
# latexmk -c /workspaces/Anthropic/src/latex/hello_world_latex.tex # must still point to original tex file

