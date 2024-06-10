# Line of Code Counter

This script counts the lines of code in source files within a specified directory and its subdirectories. It excludes empty lines, commented lines, and single `{` or `}` lines. The script supports specifying the file format and source directory via command-line arguments.

## Features

- Counts lines of code in specified file formats.
- Excludes empty lines, commented lines, and single `{` or `}` lines.
- Supports scanning a specified directory and its subdirectories.
- Reports the total number of lines of code and the total number of files discovered.

## Requirements

- Python 3.x

## Usage

1. Save the script to a file, for example, `count_source_lines.py`.
2. Run the script using Python with the desired parameters.

### Command-line Arguments

- `-f` or `--format`: Specifies the file format to search for (default is "java").
- `-s` or `--source`: Specifies the source folder to scan (default is the current directory).

### Examples

To count lines of code in Java files in the current directory:
```sh
python count_source_lines.py -f java -s .
```

Sample output:
```log
Selected file format: java
Scanning source folder: .
Total lines of code: 49615
Total files discovered: 872
```

              
```sh
python count_source_lines.py -f py
```

Sample output:
```log
Selected file format: py
Scanning source folder: .
Total lines of code: 296
Total files discovered: 49
```