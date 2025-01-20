README: Git Commit Checker Script

This script verifies whether specific Git commit hashes exist in the current repository by comparing them against a Git log file. It automatically ensures the log file is up to date by checking the tip of the repository branch.

Features

Automatic Log File Update: Automatically generates or updates git_log.txt if the tip of the repository has changed.

Interactive Input: Allows users to input commit IDs one by one and type done when finished.

Color-Coded Output:

Green: For commits found in the log file.

Red: For commits not found in the log file.

Detailed Summary:

Displays total commits provided.

Shows counts of found and not found commits.

Prerequisites

The script must be run inside a valid Git repository.

Ensure you have Git installed on your system.

A Unix-like terminal (Linux, macOS, or WSL) is required.

Setup

Save the Script

Save the script as check_git_commits.sh in your desired directory.

Make It Executable

Run the following command to grant execution permissions:

chmod +x check_git_commits.sh

Usage

Running the Script

Execute the script with:

./check_git_commits.sh

Input Instructions

Enter Commit IDs: Enter commit hashes one by one when prompted.

Finish Input: Type done and press Enter to end input.

The script will automatically:

Check if git_log.txt exists.

Compare the latest commit in the repository with the first commit in the log file.

Update git_log.txt if needed.

Example Input

Enter commit IDs one by one (type 'done' when finished):
7da61c1b5134
5d858bfc9d69
f5c061da7f63
done

Example Output

Updating the Git log file...
Git log file updated successfully.

commits found:
--------------
7da61c1b5134
5d858bfc9d69
--------------

commits not found:
------------------
f5c061da7f63
------------------

Summary:
------------------
Total commits provided: 3
Commits found: 2
Commits not found: 1
------------------

Troubleshooting

Error: "This script must be run inside a Git repository."

This error occurs if the script is executed outside of a Git repository. Navigate to the directory containing the .git folder and re-run the script.

Error: "Failed to update the Git log file."

Ensure you have write permissions for the directory and that Git is installed and accessible from the terminal.

Notes

Log File: The script uses git_log.txt in the current directory to store and compare commit logs.

Efficiency: The script only updates the log file if the repository's latest commit hash has changed.





