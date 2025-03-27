# Prompt user for input
print("Enter commit IDs line by line. Type 'END' to finish input:")

# Initialize an empty list to store commit IDs
commit_ids = []

# Read commit IDs from user input until 'END' is entered
while True:
    commit_id = input()
    if commit_id.upper() == "END":
        break
    commit_ids.append(commit_id)

# Reverse the list of commit IDs
reversed_commit_ids = commit_ids[::-1]

# Print the reversed list of commit IDs
print("\nReversed list of commits:")
for commit_id in reversed_commit_ids:
    print(commit_id)

