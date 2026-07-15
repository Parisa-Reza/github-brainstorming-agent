class QueryKeywords:

    STOP_WORDS = {
        "how",
        "what",
        "is",
        "are",
        "the",
        "in",
        "of",
        "to",
        "implemented",
        "does",
        "do",
        "a",
        "an",
        "and",

    }

    def extract(
        self,
        question: str,
    ):

        words = (
            question.lower()
            .replace("?", "")
            .split()
        )

        return [
            word
            for word in words
            if word not in self.STOP_WORDS
        ]