
# Google App Script Repo: Simple Task Automation

This repository contains Google Apps Script code designed for simple task automation directly within Google Apps without relying on any third-party applications.  The scripts are ready to be imported and run at [app script](https://script.google.com/home).

## Contents

- **`app_scripts/`**: This directory contains the individual Apps Script projects.  Each subdirectory within represents a separate script with its own functionality.

    -  Each subdirectory will have a `Code.gs` file containing the script code and potentially other supporting files.


## Usage

1. **Open Google Apps Script:** Navigate to script.google.com in your web browser.
2. **Import a Script:**  
    - Open the specific script directory within `app_scripts` that you wish to use.
    - Select all the code within the `Code.gs` file.
    - Copy the code.
    - In your Google Apps Script editor, go to "File" -> "New Project".
    - Paste the copied code into the script editor.
3. **Authorize the Script:** The script may require authorization to access Google services (like Google Sheets, Gmail, etc.).  Follow the on-screen prompts to grant the necessary permissions.
4. **Run the Script:** Locate the main function within the script (often named `myFunction` or similar) and run it.  The specific instructions for running each script will be documented within its respective folder (look for comments within `Code.gs`).


## Contributing

Contributions are welcome!  If you'd like to add or improve upon the existing scripts, please follow these guidelines:

- Fork this repository.
- Create a new branch for your changes.
- Make your changes and thoroughly test them.
- Submit a pull request with a clear description of your changes.

## Disclaimer

These scripts are provided "as is" without warranty of any kind.  Use them at your own risk.  Always back up your data before running any script that modifies it.

