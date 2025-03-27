#!/usr/bin/env python3

import os

def main():
    # Display available repository options
    print("Select a repository for creating hyperlinks:")
    print("1) https://github.com/AMDEPYC/Linux_Backport/commit/")
    print("2) https://github.com/torvalds/linux/commit/")
    
    # Get repository selection
    while True:
        try:
            repo_choice = int(input("Enter your choice (1 or 2): "))
            if repo_choice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Set base URL based on selection
    if repo_choice == 1:
        base_url = "https://github.com/AMDEPYC/Linux_Backport/commit/"
    else:
        base_url = "https://github.com/torvalds/linux/commit/"
    
    # Get commit IDs
    print("\nEnter commit IDs (one per line).")
    print("When finished, enter an empty line.")
    
    commit_ids = []
    while True:
        commit_id = input("Commit ID: ").strip()
        if not commit_id:
            break
        commit_ids.append(commit_id)
    
    if not commit_ids:
        print("No commit IDs provided. Exiting.")
        return
    
    # Generate HTML content
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>GitHub Commit Hyperlinks</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            max-width: 800px;
        }
        h1 {
            color: #333;
        }
        .link-container {
            margin: 20px 0;
        }
        a {
            color: #0366d6;
            text-decoration: none;
            display: block;
            margin: 5px 0;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>GitHub Commit Hyperlinks</h1>
    <div class="link-container">
"""
    
    # Add hyperlinks to HTML content
    for commit_id in commit_ids:
        full_url = f"{base_url}{commit_id}"
        # Display only the first 12 characters of the commit ID as link text
        display_text = commit_id[:12] if len(commit_id) >= 12 else commit_id
        html_content += f'        <a href="{full_url}" target="_blank">{display_text}</a>\n'
    
    # Close HTML tags
    html_content += """    </div>
</body>
</html>
"""
    
    # Write HTML content to file
    output_file = "github_commits.html"
    with open(output_file, "w") as f:
        f.write(html_content)
    
    print(f"\nHTML file with hyperlinks created: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
