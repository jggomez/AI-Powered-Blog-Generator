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

## Screenshots

![Screenshot 2025-02-28 at 8 47 25 p m](https://github.com/user-attachments/assets/68089305-42b9-4622-892c-6840cec2329a)

![Screenshot 2025-02-28 at 8 47 34 p m](https://github.com/user-attachments/assets/6d3f3f8d-9a42-4177-9958-ab0ed585e385)


## Requirements

* Python 3.10 or higher
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


Made with ❤ by  [jggomez](https://devhack.co).
Made with ❤ by  [haruiz](https://github.com/haruiz).

[![Twitter Badge](https://img.shields.io/badge/-@jggomezt-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/jggomezt)](https://twitter.com/jggomezt)
[![Linkedin Badge](https://img.shields.io/badge/-jggomezt-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/jggomezt/)](https://www.linkedin.com/in/jggomezt/)
[![Medium Badge](https://img.shields.io/badge/-@jggomezt-03a57a?style=flat-square&labelColor=000000&logo=Medium&link=https://medium.com/@jggomezt)](https://medium.com/@jggomezt)

## License

    Copyright 2025 Juan Guillermo Gómez and Henry Ruiz

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS
