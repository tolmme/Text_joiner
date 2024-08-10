import tkinter as tk
from tkinter import filedialog, simpledialog
import os
from datetime import datetime

def join_text_files():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select multiple files
    file_paths = filedialog.askopenfilenames(title="Select text, markdown, or HTML files to join",
                                             filetypes=[("Text, Markdown, and HTML Files", "*.txt *.md *.html")])

    if not file_paths:
        print("No files selected. Exiting.")
        return

    # Ask user for the output format
    output_format = simpledialog.askstring("Output Format", "Enter output format (txt, md, or html):")
    if output_format not in ["txt", "md", "html"]:
        print("Invalid format selected. Exiting.")
        return

    # Prepare the output file name
    file_count = len(file_paths)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file_name = f"Merged_text_of_{file_count}_files_{timestamp}.{output_format}"
    output_dir = os.path.dirname(file_paths[0])
    output_file_path = os.path.join(output_dir, output_file_name)

    # Join the files
    with open(output_file_path, 'w') as output_file:
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            with open(file_path, 'r') as input_file:
                # Add file name before the text
                output_file.write(f"\n\n{file_name}\n")
                # Write the content of the file
                output_file.write(input_file.read())
                output_file.write("\n")  # Add one free line after text

    print(f"Files have been successfully merged into {output_file_path}")

if __name__ == "__main__":
    join_text_files()