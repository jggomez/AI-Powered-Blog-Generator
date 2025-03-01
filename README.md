# AI-Powered Blog Generator

This repository contains an application that utilizes AI agents to automatically generate complete blog posts from a provided topic. It uses the AG2 (Multi-Agent Conversation Framework) framework to orchestrate the interaction between different agents.

## Key Features

* **AI-Driven Content Generation**:
    * Uses Gemini 2.0 with grounding to generate relevant and accurate content.
    * Detects important entities in the text and searches for related tweets to enrich the content.
* **Automatic Blog Creation**:
    * Generates engaging titles, detailed text content, and relevant reference links.
* **Relevant Image Generation**:
    * Analyzes blog content to create a prompt that generates a related image.
* **Multi-Agent Workflow**:
    * Implements a sequential orchestration of three specialized agents.
* **Intuitive User Interface**:
    * Uses Gradio to provide an easy-to-use user interface.
    * Allows inputting the topic via audio or text.

## Agents Used

1.  **Content Generation Agent**:
    * Responsible for generating blog content using Gemini 2.0 and grounding.
    * Performs entity detection and related tweet search.
2.  **Blog Creation Agent**:
    * Responsible for structuring the generated content into a complete blog post, including title, text, and reference links.
3.  **Image Generation Agent**:
    * Analyzes the blog text and generates a prompt to create a relevant image.

## Technologies Used

* Python
* AG2 (Multi-Agent Conversation Framework)
* Gemini 2.0
* Gradio

## Requirements

* Python 3.6 or higher
* Access to the Gemini 2.0 APIs
* Basic knowledge of AI Agent frameworks.

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/borkdude/html/blob/main/.dir-locals.el](https://github.com/borkdude/html/blob/main/.dir-locals.el)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure Gemini 2.0 API credentials.
4.  Run the application:
    ```bash
    python app.py
    ```

## Usage

1.  Open the Gradio interface in your browser.
2.  Enter a topic for the blog via text or audio.
3.  Wait for the AI agents to generate the complete blog post.
4.  Review and download the generated blog.

## Contributing

Contributions are welcome! If you find bugs or have suggestions for improving the application, please open an issue or submit a pull request.

## License

This project is licensed under the [Indicate license] license.
```

Espero que esto ayude.
