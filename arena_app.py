
import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
from scraper import fetch_website_contents

load_dotenv()

# Initialize LLM clients
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def ask(client, model, article_content):
    prompt = f"""
    You are an expert article summarization assistant.

    Analyze the following website content and provide:

    1. Main topic
    2. Key findings
    3. Important takeaways
    4. Overall conclusion

    Keep the summary structured, informative and concise.

    Website content:
    {article_content}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def battle(url):
    if not url.strip():
        return "Please enter a website URL.", "Please enter a website URL."

    # Step 1: Scrape website
    article_content = fetch_website_contents(url)

    if article_content.startswith("Could not fetch"):
        return article_content, article_content

    # Step 2: Check extracted content
    if len(article_content.strip()) < 100:
        return "Insufficient website content extracted.", "Insufficient website content extracted."

    # Step 3: Send identical content to both models
    try:
        response_a = ask(
            openai_client,
            "gpt-4o-mini",
            article_content
        )

        response_b = ask(
            groq_client,
            "openai/gpt-oss-120b",
            article_content
        )

        return response_a, response_b

    except Exception as e:
        error = f"Model execution failed: {str(e)}"
        return error, error


def vote(label):
    return f"🗳️ Thanks! You voted: **{label}**"


with gr.Blocks(title="LLM Arena") as demo:

    gr.Markdown("# 🥊 LLM Arena — One Article, Two Models")

    url = gr.Textbox(
        label="Enter a website URL",
        placeholder="https://example.com/article"
    )

    go = gr.Button("⚔️ Battle!", variant="primary")

    with gr.Row():

        with gr.Column():
            gr.Markdown("### 🤖 Model A — GPT-4o-mini")
            out_a = gr.Markdown()

            with gr.Row():
                up_a = gr.Button("👍")
                down_a = gr.Button("👎")

        with gr.Column():
            gr.Markdown("### 🤖 Model B — Groq GPT-OSS-120B")
            out_b = gr.Markdown()

            with gr.Row():
                up_b = gr.Button("👍")
                down_b = gr.Button("👎")

    verdict = gr.Markdown()

    go.click(
        battle,
        inputs=url,
        outputs=[out_a, out_b]
    )

    up_a.click(
        lambda: vote("👍 Model A"),
        outputs=verdict
    )

    down_a.click(
        lambda: vote("👎 Model A"),
        outputs=verdict
    )

    up_b.click(
        lambda: vote("👍 Model B"),
        outputs=verdict
    )

    down_b.click(
        lambda: vote("👎 Model B"),
        outputs=verdict
    )


demo.launch(share=True)
