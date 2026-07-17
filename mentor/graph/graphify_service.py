import subprocess


class GraphifyService:

    def generate(
        self,
        repository_path: str,
    ):

        print(
            f"Generating graph for: {repository_path}"
        )

        subprocess.run(
            [
                "./venv/bin/graphify",
                "extract",
                repository_path,
            ],
            check=True,
        )

        print(
            "Graph generation complete"
        )