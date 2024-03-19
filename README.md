# PST to MBOX Converter

This Python script is designed to convert PST (Outlook Personal Folder) files to MBOX files, a commonly used file format for storing emails.

## About

This script was developed to facilitate the conversion of PST files to MBOX, which can be useful for email migrations or for working with email files in a more accessible format.

## Prerequisites

Before running this script, make sure you have the following prerequisites installed on your system:

- Python 3
- `brew` (for macOS users)
- `libpst` (for macOS users)

## Installation

Follow these steps to set up and run the script:

1. Clone the repository:

   `bash
   `git clone https://github.com/hindrav/pst_to_mbox.git`

***

2. Navigate to the project folder:

`bash
`cd pst_to_mbox`

***

3. Create a virtual environment:

`bash
`python3 -m venv venv`

***

4. Activate the virtual environment:

`bash
`source venv/bin/activate`

***

5. Install the dependencies:

`bash
`pip install -r requirements.txt`

***

6. Install libpst (for macOS users):

`bash
`brew install libpst`

***

## Usage
Once you have set up the environment and dependencies, you can run the script to convert PST files to MBOX. Run the following command:

`bash
`python app.py`

This will convert the PST files found in the inputs_folder and save the resulting MBOX files in the results_folder.

