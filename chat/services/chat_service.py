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

    def ask(
        self,
        question: str,
        repo_url: str,
        conversation_id: str,
    ):

        # Load conversation history
        history = self.memory.get_history(
            conversation_id
        )

        # if self.router.use_mcp(question):

        #     owner = "Parisa-Reza"

        #     repo = repo_url.rstrip("/").split("/")[-1]

        #     answer = self.github.get_file_contents(

        #         owner,

        #         repo,

        #         "README.md",

        #     )

        #     if answer:

        #         self.memory.save_user_message(

        #             conversation_id,

        #             question,

        #         )

        #         self.memory.save_assistant_message(

        #             conversation_id,

        #             answer,

        #         )

        #         return answer

        owner, repo = self.repository_parser.parse(
            repo_url
        )


        # route = self.router.route(

        #     question,

        #     owner,

        #     repo,

        # )

        # if route:

        #     answer = self.github.execute(route)

        #     self.memory.save_user_message(

        #         conversation_id,

        #         question,

        #     )

        #     self.memory.save_assistant_message(

        #         conversation_id,

        #         answer,

        #     )

        #     return answer

        route = self.router.route(
            question,
            owner,
            repo,
        )

        mcp_context = ""

        if route:

            mcp_context = self.github.execute(route)

        memories = self.long_memory.get(
            conversation_id
        )

        # Retrieve repository context
        context = self.retriever.retrieve(
            question,
            repo_url,
        )

        print("\n==============================")
        print("ACTIVE REPO")
        print(repo_url)
        print("==============================")

        print("\n==============================")
        print("RETRIEVED CONTEXT")
        print(context[:4000])
        print("==============================")

        # Generate answer
        # answer = self.generator.generate(
        #     question=question,
        #     context=context,
        #     history=history,
        #     memories=memories,
        # )

        # combined_context = context

        # if mcp_context:

        #     combined_context += "\n\n"

        #     combined_context += mcp_context

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
        
        print("\n===================")
        print("MCP CONTEXT:")
        print(mcp_context)
        print("===================")

        print("\n===================")
        print("VECTOR CONTEXT:")
        print(context[:1000])   # first 1000 chars
        print("===================")

        answer = self.generator.generate(
            question=question,
            context=combined_context,
            history=history,
            memories=memories,
        )

        # Save conversation
        self.memory.save_user_message(
            conversation_id,
            question,
        )

        self.memory.save_assistant_message(
            conversation_id,
            answer,
        )
        self.long_memory.process(

            conversation_id,

            question,

            answer,

        )

        return answer

