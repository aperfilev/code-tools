import os
import re
import argparse


def count_lines_of_code(directory, file_format):
    total_lines = 0
    file_count = 0

    # Regular expressions to identify comments and empty lines
    single_line_comment = re.compile(r'^\s*//')
    multi_line_comment_start = re.compile(r'^\s*/\*')
    multi_line_comment_end = re.compile(r'\*/\s*$')
    empty_line = re.compile(r'^\s*$')
    single_brace_line = re.compile(r'^\s*{\s*}$|^\s*}\s*$')

    # Iterate over all files in the given directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(f'.{file_format}'):
                file_count += 1
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    in_multi_line_comment = False
                    for line in f:
                        line = line.rstrip()  # Remove trailing spaces
                        if in_multi_line_comment:
                            if multi_line_comment_end.search(line):
                                in_multi_line_comment = False
                            continue
                        if multi_line_comment_start.search(line):
                            in_multi_line_comment = True
                            continue
                        if empty_line.match(line) or single_line_comment.match(line) or single_brace_line.match(line):
                            continue
                        total_lines += 1

    return total_lines, file_count


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Count lines of code in source files.")
    parser.add_argument('-f', '--format', type=str, default='java',
                        help='File format to search for (default is "java")')
    parser.add_argument('-s', '--source', type=str, default='.',
                        help='Source folder to scan (default is current directory)')

    args = parser.parse_args()

    # Output selected options
    print(f"Selected file format: {args.format}")
    print(f"Scanning source folder: {args.source}")

    # Count lines of code and number of files
    loc, file_count = count_lines_of_code(args.source, args.format)

    # Output results
    print(f"Total lines of code: {loc}")
    print(f"Total files discovered: {file_count}")


if __name__ == "__main__":
    main()
