import pandas as pd
import os

def create_html_files_and_update_excel(input_excel_path, output_excel_path, html_output_dir="html_files"):
    """
    Reads an Excel file with questions in Column A and answers in Column B,
    creates an HTML file for each cell's content, and updates a new Excel
    file with the paths to these HTML files.

    Args:
        input_excel_path (str): Path to the input Excel file.
        output_excel_path (str): Path to save the new output Excel file.
        html_output_dir (str, optional): Directory to save the HTML files.
                                        Defaults to "html_files".
    """
    try:
        df = pd.read_excel(input_excel_path)
    except FileNotFoundError:
        print(f"Error: Input Excel file not found at '{input_excel_path}'")
        return

    if df.shape[1] < 2:
        print("Error: The input Excel file must have at least two columns (A and B).")
        return

    os.makedirs(html_output_dir, exist_ok=True)

    new_question_paths = []
    new_answer_paths = []

    for index, row in df.iterrows():
        question = str(row.iloc[0])  # Get value from Column A
        answer = str(row.iloc[1])    # Get value from Column B

        # Create HTML file for the question
        question_filename = f"question_{index + 1}.html"
        question_filepath = os.path.join(html_output_dir, question_filename)
        with open(question_filepath, "w", encoding="utf-8") as f:
            f.write(f"<!DOCTYPE html>\n<html>\n<head><title>Question {index + 1}</title></head>\n<body>\n<p>{question}</p>\n</body>\n</html>")
        new_question_paths.append(question_filepath)

        # Create HTML file for the answer
        answer_filename = f"answer_{index + 1}.html"
        answer_filepath = os.path.join(html_output_dir, answer_filename)
        with open(answer_filepath, "w", encoding="utf-8") as f:
            f.write(f"<!DOCTYPE html>\n<html>\n<head><title>Answer {index + 1}</title></head>\n<body>\n<p>{answer}</p>\n</body>\n</html>")
        new_answer_paths.append(answer_filepath)

    # Create a new DataFrame for the output Excel file
    new_df = pd.DataFrame({'Question HTML Path': new_question_paths, 'Answer HTML Path': new_answer_paths})

    # Save the new DataFrame to a new Excel file
    try:
        new_df.to_excel(output_excel_path, index=False)
        print(f"Successfully created HTML files in '{html_output_dir}' and updated Excel file at '{output_excel_path}'")
    except Exception as e:
        print(f"Error saving the output Excel file: {e}")

if __name__ == "__main__":
    input_excel_file = "Path_"  # Replace with the actual path to your input Excel file
    output_excel_file = "New_Output_File"  # Name for the new output Excel file
    html_directory = "'Directory_'"  # Directory to save the HTML files

    create_html_files_and_update_excel(input_excel_file, output_excel_file, html_directory)
