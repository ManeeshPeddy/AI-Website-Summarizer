# AI Website Summarizer

An AI-powered web application that extracts content from websites and transforms lengthy web pages into concise, easy-to-understand summaries.

The project combines web scraping and Large Language Models (LLMs) to simplify information consumption, helping users understand website content without manually reading entire articles or pages.

## Overview

The AI Website Summarizer is designed to automate the process of collecting website content, processing textual information, and generating meaningful summaries.

Instead of spending time navigating lengthy web pages, users can provide a website URL and obtain a summarized version of its content.

## Key Components

| Component | Description |
|---|---|
| `app.py` | Main application interface |
| `arena_app.py` | Alternative application interface |
| `scraper.py` | Extracts and processes website content |
| `summarizer.py` | Handles AI-powered text summarization |
| `.gitignore` | Excludes sensitive and unnecessary files |

## Technology Stack

- **Programming Language:** Python
- **Web Interface:** Gradio
- **Web Scraping:** Python-based web content extraction
- **AI / NLP:** Large Language Models (LLMs)
- **Configuration:** Environment variables

## Project Workflow

1. User provides a website URL.
2. The scraper extracts the relevant website content.
3. Extracted content is processed and prepared for summarization.
4. The summarization component generates a concise summary using an AI model.
5. The summarized output is presented through the application interface.

## Project Structure

```text
AI-Website-Summarizer/
│
├── app.py
├── arena_app.py
├── scraper.py
├── summarizer.py
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:ManeeshPeddy/AI-Website-Summarizer.git
cd AI-Website-Summarizer
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Install the Python packages required by the project.

### 4. Configure Environment Variables

Create a `.env` file in the project root and configure the required API credentials.

**Important:** Never commit API keys, credentials, or `.env` files to GitHub.

### 5. Run the Application

```bash
python app.py
```

To launch the alternative interface:

```bash
python arena_app.py
```

## Future Enhancements

- Support for summarizing multiple URLs.
- Improved content extraction and handling of complex web pages.
- Customizable summary length and output formats.
- Support for additional LLM providers.
- Document summarization and export capabilities.
- Deployment as a publicly accessible web application.

## Author

**Maneesh Peddy**

GitHub: [@ManeeshPeddy](https://github.com/ManeeshPeddy)

---

*This project is part of my continuous exploration of Artificial Intelligence, Machine Learning, Generative AI, and Large Language Model applications.*
