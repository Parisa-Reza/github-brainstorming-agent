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

from mentor.repositories.repository_service import (
    RepositoryService,
)

from mentor.repositories.repository_ingestion_workflow import (
    RepositoryIngestionWorkflow,
)

def chat_page(request):

    if "messages" not in request.session:
        request.session["messages"] = []

    messages = (
        request.session["messages"]
    )

    if request.method == "POST":

        github_url = (
            request.POST.get(
                "github_url"
            )
        )

        # if github_url:

        #     request.session[
        #         "repo_url"
        #     ] = github_url

        #     return redirect("/")

        if github_url:

            RepositoryIngestionWorkflow(
            ).ingest(
                github_url
            )

            request.session[
                "repo_url"
            ] = github_url

            request.session[
                "messages"
            ] = []

            return redirect("/")

        question = (
            request.POST.get(
                "question",
                "",
            )
        )

        if question:

            repo_url = (
                request.session.get(
                    "repo_url"
                )
            )

            messages.append(
                {
                    "role": "user",
                    "content": question,
                }
            )

            answer = (
                ChatService().ask(
                    question,
                    repo_url,
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

            request.session.modified = (
                True
            )

            return redirect("/")

    return render(
        request,
        "chat/chat.html",
        {
            "chat_form": ChatForm(),
            "messages": messages,
            "repo_url": request.session.get(
                "repo_url"
            ),
        },
    )



# from django.shortcuts import (
#     render,
#     redirect,
# )

# from chat.forms import (
#     ChatForm,
# )

# from chat.services.chat_service import (
#     ChatService,
# )


# def chat_page(request):

#     if "messages" not in request.session:

#         request.session[
#             "messages"
#         ] = []

#     messages = request.session[
#         "messages"
#     ]

#     if request.method == "POST":

#         question = request.POST.get(
#             "question",
#             ""
#         )

#         if question:

#             messages.append(
#                 {
#                     "role": "user",
#                     "content": question,
#                 }
#             )

#             answer = (
#                 ChatService().ask(
#                     question
#                 )
#             )

#             messages.append(
#                 {
#                     "role": "assistant",
#                     "content": answer,
#                 }
#             )

#             request.session[
#                 "messages"
#             ] = messages

#             request.session.modified = True

#         return redirect("/")

#     return render(
#         request,
#         "chat/chat.html",
#         {
#             "chat_form": ChatForm(),
#             "messages": messages,
#         },
#     )