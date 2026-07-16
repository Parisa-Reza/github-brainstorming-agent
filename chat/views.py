from django.shortcuts import (
    render,
    redirect,
)

from chat.forms import (
    ChatForm,
)

from chat.services.chat_service import (
    ChatService,
)


def chat_page(request):

    if "messages" not in request.session:

        request.session[
            "messages"
        ] = []

    messages = request.session[
        "messages"
    ]

    if request.method == "POST":

        question = request.POST.get(
            "question",
            ""
        )

        if question:

            messages.append(
                {
                    "role": "user",
                    "content": question,
                }
            )

            answer = (
                ChatService().ask(
                    question
                )
            )

            messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                }
            )

            request.session[
                "messages"
            ] = messages

            request.session.modified = True

        return redirect("/")

    return render(
        request,
        "chat/chat.html",
        {
            "chat_form": ChatForm(),
            "messages": messages,
        },
    )