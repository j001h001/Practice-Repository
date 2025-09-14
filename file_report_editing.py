import os

def get_path_depth(path):
    """Calculates the depth of a normalized file path."""
    path = os.path.normpath(path)
    return len(path.split(os.sep))

def generate_dir_report(path, report_file_path, show_files=True, num_files=True, file_size=True, hl='log'):
    """
    Walks a directory path and generates a tree-like report in a text file.
    """
    # Calculate the depth of the starting path ONCE before the loop.
    main_path_depth = get_path_depth(path)
    
    with open(report_file_path, 'w') as report_file:
        for root, dirs, files in sorted(os.walk(path)):
            #Need to count the number of files in the current directory.
            num_files_in_dir = len(files)
            file_count_add_on = ""

            # Get just the name of the current directory.
            basename = os.path.basename(root)
            
            # --- Indentation Logic ---
            # Calculate the relative depth of the current directory.
            dir_level = get_path_depth(root) - main_path_depth

            # Determine the indentation strings based on the level.
            # Directories are indented based on their level minus one.
            dir_indent_str = '  ' * (dir_level - 1)
            # Files are indented based on their parent directory's level.
            file_indent_str = '  ' * dir_level

            if num_files == True:
                #counting add on for number of files if there is even a file involved
                file_count_add_on = f" ({num_files_in_dir} files)"

            else:
                file_count_add_on = ""

            #Adding in a file size = true if/then statement
            if file_size == True:
                total_file_size = sum(os.path.getsize(os.path.join(root, f)) for f in files)
                file_size_add_on = f" ({total_file_size} bytes)"
            else:
                file_size_add_on = ""

            #Checking file extensions for which ones are .log extensions and subsequently highlighting them with '<--'
            for file_name in sorted(files):
                highlight_add_on = ""
                name_of_file, extension = os.path.splitext(file_name) 
                if hl is not None:
                    target_extension = "." + hl
                    if target_extension == extension: 
                        highlight_add_on = "<--"
                else:
                    highlight_add_on = ""


            # --- Directory Printing ---
            if root == path:
                # Special case for the top-level directory.
                report_file.write(f'+ {basename}{file_count_add_on}{file_size_add_on}\n')
            else:
                # For all other subdirectories.
                report_file.write(f'{dir_indent_str}|-+ {basename}{file_count_add_on}{file_size_add_on}\n')
            if show_files == True:
                # --- File Printing ---
                # This loop now runs for EVERY directory, including the top-level one.
                for file_name in sorted(files):
                    report_file.write(f'{file_indent_str}|-- {file_name}\n')
            else:
                continue

# Example of how to run the function
# You would need a 'data/dir-top' directory structure for this to work.
# generate_dir_report('data/dir-top', 'dir-report.txt')