import sys

class ClassX:
    def __init__(self, minor, patch, breaking):
        self.minor_count = minor
        self.patch_count = patch
        self.breaking_count = breaking

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

if __name__ == "__main__":
    # Expecting command line arguments: minor_count, patch_count, breaking_count
    if len(sys.argv) != 4:
        print("Usage: python script.py <minor_count> <patch_count> <breaking_count>")
        sys.exit(1)

    minor = int(sys.argv[1])
    patch = int(sys.argv[2])
    breaking = int(sys.argv[3])

    class_x = ClassX(minor, patch, breaking)
    print(class_x.determine_version_bump())
