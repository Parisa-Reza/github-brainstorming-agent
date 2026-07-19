const form = document.getElementById("chat-form");

const chatWindow = document.getElementById("chat-window");

if (form) {
  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const input = document.querySelector("[name='question']");

    const question = input.value.trim();

    if (!question) {
      return;
    }

    chatWindow.insertAdjacentHTML(
      "beforeend",
      `
                <div class="message user">
                    <div class="bubble">
                        ${question}
                    </div>
                </div>
                `,
    );

    const thinkingId = "thinking-" + Date.now();

    chatWindow.insertAdjacentHTML(
      "beforeend",
      `
                <div
                    class="message assistant"
                    id="${thinkingId}"
                >
                    <div class="bubble thinking">
                        Thinking...
                    </div>
                </div>
                `,
    );

    input.value = "";

    chatWindow.scrollTop = chatWindow.scrollHeight;

    const formData = new FormData();

    formData.append("question", question);

    formData.append(
      "csrfmiddlewaretoken",
      document.querySelector("[name=csrfmiddlewaretoken]").value,
    );

    try {
      const response = await fetch("/", {
        method: "POST",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
        body: formData,
      });

      const data = await response.json();

      const html = marked.parse(data.answer, {
        breaks: true,
        gfm: true,
      });

      const thinkingBubble = document.getElementById(thinkingId);

      if (thinkingBubble) {
        thinkingBubble.innerHTML = `
                        <div class="bubble markdown-body">
                            ${html}
                        </div>
                        `;

        thinkingBubble.querySelectorAll("pre code").forEach((block) => {
          hljs.highlightElement(block);
        });
      }

      chatWindow.scrollTop = chatWindow.scrollHeight;
    } catch (error) {
      console.error(error);

      const thinkingBubble = document.getElementById(thinkingId);

      if (thinkingBubble) {
        thinkingBubble.innerHTML = `
                        <div class="bubble">
                            Error getting response.
                        </div>
                        `;
      }
    }
  });
}
