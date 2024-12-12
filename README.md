<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>





<p align="center"><i>Xircuits Component Library for Gemini – Seamless Integration with Google Generative AI.</i></p>

---
### Xircuits Component Library for Gemini
Seamlessly integrate Google Generative AI into Xircuits. This library enables efficient authorization, content generation, token management, and chat-based interactions with Gemini models.

## Table of Contents

- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Preview

### The Example:

<img src="https://github.com/user-attachments/assets/3fb2ec14-ebeb-403e-83e8-f468655ded85" alt="gemini_example" />

### The Result:

<img src="https://github.com/user-attachments/assets/197b57ba-dbb6-4a9e-b160-bbad79d1bdf3" alt="gemini_example_result" />

## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.

## Main Xircuits Components

### GeminiAuthorize Component:
Configures API authorization for the Gemini library using an API key, either provided directly or from an environment variable.

<img src="https://github.com/user-attachments/assets/1dd131c8-0122-4c51-aeda-2924c34d8ecd" alt="GeminiAuthorize" width="200" height="100" />

### GeminiGenerateContent Component:
Creates content using input data and a specified generative model.

<img src="https://github.com/user-attachments/assets/7d99754e-c2bc-4048-a442-06ad7097f1a4" alt="GeminiGenerateContent" width="200" height="100" />

### GeminiGenerateContentStream Component:
Generates content in real-time using a streaming approach, allowing dynamic responses.

### GeminiStartChat Component:
Starts a conversational session with the Gemini model, enabling interactive AI chats.

### GeminiChatSendMessage Component:
Sends a message in an ongoing chat and retrieves the AI's response.

### GeminiChatSendMessageStream Component
Facilitates real-time chat interactions using streaming for continuous response delivery.

### GeminiCountTokens Component:
Calculates token count for input text to optimize API usage and cost management.

## Installation
To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the Gemini library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install gemini
```
You can also do it manually by cloning and installing it:
```
# base Xircuits directory
git clone https://github.com/XpressAI/xai-gemini xai_components/xai_gemini
pip install -r xai_components/xai_gemini/requirements.txt
```

## Usage

Store your Google API key in an environment variable for enhanced security and convenience. Example:

```bash
export GOOGLE_API_KEY='your_api_key_here'
```