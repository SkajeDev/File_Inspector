# File Inspector

## How it work?

You can check files without extension and compare it with table of files.
Table will be updated and this is not final script. Im going to add work with metadata and upload this in file.

## Check a single file

Open directory with script in command line and write `python3 fileinspect.py -f {your_file}`
Output of script will be extension of file if it exists in signature table.

## Check directory

Open directory with script in command line and write `python3 fileinspect.py -d {your_directory}`
Output of script will be extensions of files if it exists in signature table.

## Check directory with saving files in output directory

Open directory with script in command line and write:
`python3 fileinspect.py -d {your_directory} -o {output}`
Output of script will be files with extensions in your output directory.
