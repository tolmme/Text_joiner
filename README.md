# Text_joiner

This Python script allows you to join multiple text, markdown, HTML, or DOCX files into a single file. The script prompts you to select the files you want to merge, then combines their contents into one file with the name of each file inserted as a separator between the contents. The resulting merged file is saved in the same directory as the first selected file.

## Features

- Select multiple text, markdown, HTML, or DOCX files to merge using a file dialog.
- Each file's contents are separated by the file name, with customizable spacing around the file name.
- The merged file can be saved in either `.txt`, `.md`, `.html`, or `.docx` format, based on user input.
- The merged file is named based on the number of files merged and the current date and time.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)
- `python-docx` library (install using `pip install python-docx`)
- `pypandoc` library (install using `pip install pypandoc`)
- `pandoc` library (install using `brew install pandoc`)

## Usage

1. Clone or download this repository.
2. Open the script in PyCharm CE or any other Python IDE.
3. Run the script.
4. Select the text, markdown, HTML, or DOCX files you want to merge.
5. Enter the desired output format (`txt`, `md`, `html`, or `docx`) when prompted.

## Example

The merged file will be named in the format:
Merged_text_of_X_files_YYYY-MM-DD_HH-MM-SS.txt or .md or .html or .docx
Where `X` is the number of files merged and `YYYY-MM-DD_HH-MM-SS` is the current date and time.

## License

This project is licensed under the [MIT License](LICENSE).