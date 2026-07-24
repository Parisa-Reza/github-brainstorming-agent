import hashlib
import sys

from mentor.hybrid_retrieval.hybrid_retriever import (
    HybridRetriever,
)

from mentor.llm.answer_generator import (
    AnswerGenerator,
)

from mentor.memory.short_term_memory.short_term_memory import (
    ShortTermMemory,
)

from mentor.memory.long_term_memory.long_term_memory import (
    LongTermMemory,
)

from mentor.mcp.github.github_service import (
    GitHubService,
)

from mentor.mcp.github.router import (
    MCPRouter,
)

from mentor.mcp.github.repository_parser import (
    RepositoryParser,
)

class ChatService:

    def __init__(self):

        self.retriever = HybridRetriever()

        self.generator = AnswerGenerator()

        self.memory = ShortTermMemory()

        self.long_memory = LongTermMemory()

        self.github = GitHubService()

        self.router = MCPRouter()

        self.repository_parser = RepositoryParser()

    async def ask(
        self,
        question: str,
        repo_url: str,
        conversation_id: str,
    ):

        # A browser session can load several repositories.  Keeping memory
        # under only the browser session made answers about a previously
        # loaded repository available to the next repository's prompt.
        repository_conversation_id = (
            self._repository_conversation_id(
                conversation_id,
                repo_url,
            )
        )

        # Load conversation history
        history = self.memory.get_history(
            repository_conversation_id
        )

        
        owner, repo = self.repository_parser.parse(
            repo_url
        )


       
        route = self.router.route(
            question,
            owner,
            repo,
        )

        mcp_context = ""

        if route:

            # GitHub metadata is already an authoritative, user-readable
            # response. Do not send it through hybrid retrieval/LLM, which
            # previously mixed it with another repository and could fail after
            # the MCP call had succeeded.
            answer = await self.github.execute(route)

            if answer:
                self.memory.save_user_message(
                    repository_conversation_id,
                    question,
                )
                self.memory.save_assistant_message(
                    repository_conversation_id,
                    answer,
                )
                return answer

            return "GitHub did not return information for the active repository."

        memories = self.long_memory.get(
            repository_conversation_id
        )

        # Retrieve repository context
        context = self.retriever.retrieve(
            question,
            repo_url,
        )

        print("\n==============================" ,file=sys.stderr)
        print("ACTIVE REPO",file=sys.stderr)
        print(repo_url,file=sys.stderr)
        print("==============================",file=sys.stderr)

        print("\n==============================",file=sys.stderr)
        print("RETRIEVED CONTEXT",file=sys.stderr)
        print(context[:4000],file=sys.stderr)
        print("==============================",file=sys.stderr)

       

        combined_context = f"""
        ==============================
        HYBRID REPOSITORY CONTEXT
        ==============================

        {context}
        """

        if mcp_context:

            combined_context += f"""

        ==============================
        GITHUB MCP CONTEXT
        ==============================

        {mcp_context}
        """
        
        print("\n===================",file=sys.stderr)
        print("MCP CONTEXT:",file=sys.stderr)
        print(mcp_context,file=sys.stderr)
        print("===================",file=sys.stderr)

        print("\n===================",file=sys.stderr)
        print("VECTOR CONTEXT:",file=sys.stderr)
        print(context[:1000],file=sys.stderr)   # first 1000 chars
        print("===================",file=sys.stderr)

        answer = self.generator.generate(
            question=question,
            context=combined_context,
            history=history,
            memories=memories,
        )

        # Save conversation
        self.memory.save_user_message(
            repository_conversation_id,
            question,
        )

        self.memory.save_assistant_message(
            repository_conversation_id,
            answer,
        )
        self.long_memory.process(
            repository_conversation_id,
            question,
            answer,
        )

        return answer

    @staticmethod
    def _repository_conversation_id(
        conversation_id: str,
        repo_url: str,
    ) -> str:
        """Keep one browser's chat context separate for each repository."""
        normalized_url = repo_url.rstrip("/").lower()
        repository_key = hashlib.sha256(
            normalized_url.encode("utf-8")
        ).hexdigest()[:16]

        return f"{conversation_id}:{repository_key}"
