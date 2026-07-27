import re


class EntityExtractor:

    def extract(
        self,
        text: str,
    ):

        pattern = r"\b[A-Z][A-Za-z0-9_]+\b"

        return list(
            set(
                re.findall(
                    pattern,
                    text,
                )
            )
        )