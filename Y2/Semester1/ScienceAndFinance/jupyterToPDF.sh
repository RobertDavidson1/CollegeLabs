#!/bin/bash


# Enable tab completion for filenames
shopt -s extglob
shopt -s nullglob

# Prompt the user to enter the Jupyter notebook file name
read -e -p "Jupyter file to convert > " notebook_file

# Check if the file exists
if [[ -f "$notebook_file" ]]; then
    # Convert the Jupyter notebook to PDF
    echo "Converting $notebook_file to PDF..."
    jupyter nbconvert --to pdf "$notebook_file"

    # Extract the filename without the extension
    filename="${notebook_file%.ipynb}"

    # Move the generated PDF to the pdf directory
    mv "${filename}.pdf" pdf/

    echo "Conversion complete. The PDF has been moved to the pdf folder."
else
    echo "Error: The file 'Notebooks/$notebook_file' does not exist."
fi

