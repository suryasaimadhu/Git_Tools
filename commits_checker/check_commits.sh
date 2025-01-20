#!/bin/bash

# Colors
GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[0;33m"
RESET="\033[0m"

# Default log file path
default_log_file="./git_log.txt"

# Function to update the Git log file if necessary
update_git_log_file() {
    # Get the latest commit hash from the repository
    latest_commit=$(git rev-parse HEAD 2>/dev/null)
    if [[ $? -ne 0 ]]; then
        echo -e "${RED}Error: This directory is not a Git repository.${RESET}"
        exit 1
    fi

    # Check if the log file exists
    if [[ -f "$default_log_file" ]]; then
        # Get the latest commit hash from the log file
        log_tip=$(head -1 "$default_log_file" | grep -oE '[a-f0-9]{40}')
        if [[ "$latest_commit" == "$log_tip" ]]; then
            echo -e "${YELLOW}The log file is already up to date.${RESET}"
            return
        fi
    fi

    # Update the log file
    echo -e "${GREEN}Updating the Git log file...${RESET}"
    git log > "$default_log_file"
    if [[ $? -eq 0 ]]; then
        echo -e "${GREEN}Git log file updated successfully.${RESET}"
    else
        echo -e "${RED}Failed to update the Git log file.${RESET}"
        exit 1
    fi
}

# Check and update the Git log file
update_git_log_file

# Load all commit hashes from the Git log into a variable (improves speed)
log_commits=$(grep -oE '[a-f0-9]{40}' "$default_log_file")

# Prompt for commit IDs
echo "Enter commit IDs one by one (type 'done' when finished):"
commit_list=()

# Read commits until 'done' is entered
while true; do
    read -r commit
    if [[ "$commit" == "done" ]]; then
        break
    fi
    if [[ -n "$commit" ]]; then
        commit_list+=("$commit")
    fi
done

# Separate found and not found commits
found_commits=()
not_found_commits=()

for commit in "${commit_list[@]}"; do
    if echo "$log_commits" | grep -q "$commit"; then
        found_commits+=("$commit")
    else
        not_found_commits+=("$commit")
    fi
done

# Display results in the desired format
echo ""
echo -e "${GREEN}commits found:${RESET}"
echo "--------------"
printf "${GREEN}%s${RESET}\n" "${found_commits[@]}"
echo "--------------"

echo -e "${RED}commits not found:${RESET}"
echo "------------------"
printf "${RED}%s${RESET}\n" "${not_found_commits[@]}"
echo "------------------"

# Display summary
echo ""
echo -e "${GREEN}Summary:${RESET}"
echo "------------------"
echo "Total commits provided: ${#commit_list[@]}"
echo -e "${GREEN}Commits found:${RESET} ${#found_commits[@]}"
echo -e "${RED}Commits not found:${RESET} ${#not_found_commits[@]}"
echo "------------------"

