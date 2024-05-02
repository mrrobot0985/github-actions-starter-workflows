# Commit Message Guidelines for Automated Versioning

To streamline our release process, we use automated versioning based on the content of commit messages. This document provides guidelines on how to structure your commit messages to automatically trigger the correct version increment.

## Semantic Versioning

We follow semantic versioning (`MAJOR.MINOR.PATCH`), where:
- `MAJOR` versions introduce breaking changes,
- `MINOR` versions add new functionality in a backwards-compatible manner,
- `PATCH` versions introduce backwards-compatible bug fixes.

## Commit Message Format

Commit messages should be structured as follows to enable automatic parsing and versioning:

```
<type>: <description>
[optional body]
[optional footer]
```

### Types

- `feat`: A new feature for the user, not a new feature for build script.
- `fix`: A bug fix for the user, not a fix to a build script.
- `BREAKING CHANGE`: Commits that contain breaking changes should include `BREAKING CHANGE:` with a space or two newlines in the footer to describe the changes in detail.

### Examples

#### Feature Commit

```
feat: add OAuth2 support to user authentication
```
This commit will result in a MINOR version bump.

#### Bug Fix Commit
```
fix: resolve an issue where user session expires prematurely
```
This commit will result in a PATCH version bump.

#### Breaking Change Commit
```
feat: change API endpoints for user services

BREAKING CHANGE: API endpoints have been modified to improve security. This change is not backwards-compatible.
```
This commit will result in a MAJOR version bump.

## Pull Request Labels

To assist with the automation process, pull requests should be labeled with one of the following:
- `bug`: For pull requests that fix a bug — correlates to a PATCH bump.
- `feature`: For pull requests that introduce new functionality — correlates to a MINOR bump.
- `breaking`: For pull requests that cause breaking changes — correlates to a MAJOR bump.

## Automated Versioning Scenarios

For a more comprehensive look at automatic versioning scenarios, it's useful to consider a variety of real-world changes that developers might introduce to a software project. Below, I outline detailed scenarios that trigger different types of version increments based on semantic versioning rules. This document extends the basic commit message guidelines and includes more nuanced examples.

Automatic versioning is crucial for maintaining the lifecycle of software in a predictable and organized manner. Below are detailed scenarios categorized by the type of version increment they trigger. These scenarios will help contributors understand precisely how their changes might impact the versioning of the software.

## PATCH Version Increment

**PATCH** versions are incremented when changes are purely fixes that do not add any new functionality or make any backward-incompatible changes.

### Scenario: Bug Fix in User Interface

**Commit Message:**
```
fix: resolve tooltip display bug on configuration page
```

**Description:**
A tooltip on the configuration page overlaps other text when hovered over. This fix adjusts the tooltip's positioning, ensuring it no longer obscures underlying content.

### Scenario: Security Patch

**Commit Message:**
```
fix: patch SQL injection vulnerability in search functionality
```

**Description:**
A security vulnerability was identified in the search functionality, allowing SQL injection. This fix sanitizes input from the user, closing the vulnerability without altering functionality.

## MINOR Version Increment

**MINOR** versions are incremented when new, backward-compatible functionality is introduced to the public API.

### Scenario: New Feature Addition

**Commit Message:**
```
feat: add user tagging feature to posts
```

**Description:**
This new feature allows users to tag others in their posts. It includes updates to the database schema, UI adjustments, and new server-side logic but maintains backward compatibility with existing features.

### Scenario: Minor Feature Enhancement

**Commit Message:**
```
feat: improve search algorithm to include synonyms
```

**Description:**
The search functionality is enhanced to consider synonyms of search terms, improving the relevance of search results. This change extends existing capabilities without breaking them.

## MAJOR Version Increment

**MAJOR** versions are incremented for any changes that make backward-incompatible API changes.

### Scenario: API Redesign

**Commit Message:**
```
feat: redesign user API to support multi-tenancy

BREAKING CHANGE: This change modifies the user API endpoints to support multi-tenancy, affecting all existing integrations that use the user API. Endpoint parameters have been changed, and JSON response structures have been updated.
```

**Description:**
The user API is updated to support multi-tenancy, requiring changes to the endpoint URLs and parameters, as well as the format of responses. This update breaks compatibility with clients designed for the previous API version.

### Scenario: Removal of Deprecated Features

**Commit Message:**
```
feat: remove deprecated "legacyLogin" endpoint

BREAKING CHANGE: The "legacyLogin" endpoint has been removed after being deprecated for one year. Clients still using this endpoint must migrate to "newLogin" immediately.
```

**Description:**
A previously deprecated feature, the "legacyLogin" endpoint, is removed. Such removals are typical in major releases to clean up the codebase, requiring clients to update their integrations.

## Guidance for Contributors

Contributors should:
- Ensure commit messages accurately reflect the nature of the change.
- Label pull requests correctly to assist automated tools in versioning.
- Be aware of the broader impact of their changes, especially in terms of backward compatibility.

These detailed scenarios provide a clear framework for understanding how different changes affect software versioning, facilitating a smooth development process and clear communication within the team and with stakeholders.
