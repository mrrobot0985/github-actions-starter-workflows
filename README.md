# github-actions-starter-workflows

This repository contains various Continuous Integration (CI) workflows for different branches and scenarios.

## Workflows

CI/CD Workflow starters

### CI for Main Branch (Production)

- Workflow file: [ci-for-main.yml](ci-for-main.yml)
- Description: This workflow runs on pushes and pull requests to the main branch. It includes steps to print workflow details, handle pull requests, and tag releases.

### CI for Develop Branch

- Workflow file: [ci-for-develop.yml](ci-for-develop.yml)
- Description: This workflow runs on pushes and pull requests to the develop branch. It includes steps to print workflow details and handle pull requests.

### CI for Feature Branches

- Workflow file: [ci-for-feature.yml](ci-for-feature.yml)
- Description: This workflow runs on pushes to feature branches. It includes steps to print workflow details, build, test, and perform code quality checks for feature branches.

### CI for Bugfix Branches

- Workflow file: [ci-for-bugfix.yml](ci-for-bugfix.yml)
- Description: This workflow runs on pushes to bugfix branches. It includes steps to print workflow details, build, test, and perform code quality checks for bugfix branches.

### CI for Hotfix Branches

- Workflow file: [ci-for-hotfix.yml](ci-for-hotfix.yml)
- Description: This workflow runs on pushes to hotfix branches. It includes steps to print workflow details, build, test, and perform code quality checks for hotfix branches.

### CI for Release Branches

- Workflow file: [ci-for-release.yml](ci-for-release.yml)
- Description: This workflow runs on pushes to release branches. It includes steps to print workflow details, build, test, and perform code quality checks for release branches.

## Usage

To use these workflows in your repository:
1. Copy the desired workflow file content.
2. Create a new workflow file in your repository and paste the content.
3. Customize the workflow as needed for your project.

## Contributions

Contributions are welcome! If you have any suggestions or improvements for these workflows, feel free to open an issue or pull request.

## License

This project is licensed under the [MIT License](LICENSE).