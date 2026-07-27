
        document
            .querySelectorAll(
                ".markdown-content"
            )
            .forEach(
                function (element) {

                    const markdown =
                        element.textContent;

                    element.innerHTML =
                        marked.parse(
                            markdown,
                            {
                                breaks: true,
                                gfm: true
                            }
                        );

                    element
                        .querySelectorAll(
                            "pre code"
                        )
                        .forEach(
                            (block) => {
                                hljs.highlightElement(
                                    block
                                );
                            }
                        );

                }
            );