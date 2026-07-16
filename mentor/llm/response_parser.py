class ResponseParser:

    def parse(
        self,
        response,
    ):

        content = response.content

        if isinstance(
            content,
            str,
        ):
            return content

        if isinstance(
            content,
            list,
        ):

            texts = []

            for item in content:

                if (
                    isinstance(item, dict)
                    and item.get("type")
                    == "text"
                ):
                    texts.append(
                        item.get(
                            "text",
                            ""
                        )
                    )

            return "\n".join(
                texts
            )

        return str(content)