class MCPRouter:

    def route(
        self,
        question: str,
        owner: str,
        repo: str,
    ):

        normalized_question = question.lower()

        if (
            "this commit" in normalized_question
            or "specific commit" in normalized_question
            or "commit details" in normalized_question
            or "details of" in normalized_question and "commit" in normalized_question
            or "changes in" in normalized_question and "commit" in normalized_question
            or "files modified" in normalized_question
        ):

            return {
                "tool": "get_commit_details",
                "args": {
                    "owner": owner,
                    "repo": repo,
                    "question": question,
                },
            }

        question = normalized_question

        if "readme" in question:

            return {
                "tool": "get_file_contents",
                "args": {
                    "owner": owner,
                    "repo": repo,
                    "path": "README.md",
                },
            }

        if (
            "latest commit" in question
            or "commits" in question
            or "commit history" in question
            or "recent commit" in question
            or "last commit" in question
            
        ):

            return {
                "tool": "list_commits",
                "args": {
                    "owner": owner,
                    "repo": repo,
                },
            }

        if (
            "author" in question
            or "who wrote" in question
            or "who created" in question
            or "who made" in question
        ):

            return {
                "tool": "list_commits",
                "args": {
                    "owner": owner,
                    "repo": repo,
                },
            }

        if (
            "pull request" in question
            or "pull requests" in question
            or "pr" in question
        ):

            return {
                "tool": "list_pull_requests",
                "args": {
                    "owner": owner,
                    "repo": repo,
                },
            }

        if (
            "branch" in question
            or "branches" in question
        ):

            return {
                "tool": "list_branches",
                "args": {
                    "owner": owner,
                    "repo": repo,
                },
            }

        return None
