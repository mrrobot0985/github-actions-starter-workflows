import sys
from pydantic import BaseModel
from subprocess import check_output, CalledProcessError

class VersionBump(BaseModel):
    bump_type: str

class GithubWorkflow:
    def __init__(self):
        self.minor_count = 0
        self.patch_count = 0
        self.breaking_count = 0

    def set_git_config(self, email: str, name: str):
        try:
            check_output(['git', 'config', '--global', 'user.email', email])
            check_output(['git', 'config', '--global', 'user.name', name])
            return {"status": "success", "message": "Git config set successfully"}
        except CalledProcessError as e:
            return {"status": "error", "message": str(e)}

    def fetch_tags(self):
        try:
            check_output(['git', 'fetch', '--tags'])
            return {"status": "success", "message": "Tags fetched successfully"}
        except CalledProcessError as e:
            return {"status": "error", "message": str(e)}

    def determine_latest_tag(self):
        try:
            latest_tag = check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()
            return {"status": "success", "latest_tag": latest_tag}
        except CalledProcessError as e:
            return {"status": "error", "message": "No tags available"}

    def get_commit_messages(self, tag: str):
        try:
            commits = check_output(['git', 'log', f'{tag}..HEAD', '--oneline']).decode().strip().split('\n')
            return {"status": "success", "commits": commits}
        except CalledProcessError as e:
            return {"status": "error", "message": str(e)}

    def determine_version_bump(self):
        if self.breaking_count > 0:
            bump_type = "Major version bump required."
        elif self.minor_count > 0:
            bump_type = "Minor version bump required."
        elif self.patch_count > 0:
            bump_type = "Patch version bump required."
        else:
            bump_type = "No version change required."
        return VersionBump(bump_type=bump_type)

    def interpret_commits(self, commit_messages):
        seen_messages = set()
        for message in commit_messages:
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
    workflow = GithubWorkflow()
    print(workflow.set_git_config("email@example.com", "GitHub User"))
    print(workflow.fetch_tags())
    latest_tag_info = workflow.determine_latest_tag()
    print(latest_tag_info)
    if latest_tag_info['status'] == 'success':
        commits_info = workflow.get_commit_messages(latest_tag_info['latest_tag'])
        print(commits_info)
        if commits_info['status'] == 'success':
            workflow.interpret_commits([c.split(' ', 1)[1] if ' ' in c else c for c in commits_info['commits']])
    print(workflow.determine_version_bump().json())
