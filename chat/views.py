from django.shortcuts import (
    render,
    redirect,
)

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from chat.forms import (
    ChatForm,
)

from chat.services.chat_service import (
    ChatService,
)

from mentor.repositories.repository_ingestion_workflow import (
    RepositoryIngestionWorkflow,
)


@require_http_methods(["GET", "POST"])
def chat_page(request):

    if "messages" not in request.session:
        request.session["messages"] = []

    messages = request.session["messages"]

    if request.method == "POST":

        github_url = request.POST.get(
            "github_url"
        )

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

        question = request.POST.get(
            "question",
            "",
        )

        if question:

            repo_url = (
                request.session.get(
                    "repo_url"
                )
            )

            if not repo_url:
                return JsonResponse(
                    {
                        "answer": "Load a GitHub repository before asking a question."
                    },
                    status=400,
                )

            try:
                answer = ChatService().ask(
                    question,
                    repo_url,
                    request.session.session_key,
                )
            except Exception as error:
                # Keep AJAX responses JSON so the client can display the
                # server error instead of failing while parsing an HTML page.
                print(f"Chat request failed: {error}")
                return JsonResponse(
                    {
                        "answer": "Unable to answer that question right now. Please try again."
                    },
                    status=500,
                )

            

            answer = answer.strip()

            if answer.startswith("```markdown"):
                answer = answer.replace(
                    "```markdown",
                    "",
                    1
                ).rstrip("```").strip()

            elif answer.startswith("```"):
                answer = answer.replace(
                    "```",
                    "",
                    1
                ).rstrip("```").strip()

            messages.append(
                {
                    "role": "user",
                    "content": question,
                }
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

            print(
                "RETURNING JSON"
            )

            print(
                answer
            )

            return JsonResponse(
                {
                    "answer": answer
                }
            )

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
