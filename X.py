import sys

class ActionsX:
    def __init__(self):
        self.minor_count = 0
        self.patch_count = 0
        self.breaking_count = 0

    def determine_version_bump(self):
        """Determine the type of version bump required based on the input counts."""
        if self.breaking_count > 0:
            return "Major version bump required."
        elif self.minor_count > 0:
            return "Minor version bump required."
        elif self.patch_count > 0:
            return "Patch version bump required."
        else:
            return "No version change required."

    def interpret_commits(self, commit_messages):
        """Parse a list of commit messages and update versioning counts based on keywords."""
        seen_messages = set()
        for message in commit_messages:
            # Consider each unique message only once
            if message in seen_messages:
                continue
            seen_messages.add(message)

            if "BREAKING CHANGE" in message:
                self.breaking_count += 1
            elif "feat:" in message:
                self.minor_count += 1
            elif "fix:" in message:
                self.patch_count += 1

if __name__ == "__main__":
    # Command line argument is expected to be a list of commit messages.
    if len(sys.argv) < 2:
        print("Usage: python x.py 'commit message 1' 'commit message 2' ...")
        sys.exit(1)

    # Initialize the class
    actions_x = ActionsX()

    # Parse commit messages from command line arguments (excluding the first argument which is the script name)
    actions_x.interpret_commits(sys.argv[1:])

    # Determine and print the version bump
    print(actions_x.determine_version_bump())
