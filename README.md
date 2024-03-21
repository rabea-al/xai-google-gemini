# Google Generative AI Components for Xircuits

This repository offers a suite of components designed to integrate the [Google Generative AI library](https://github.com/google/generative-ai-python) into the Xircuits framework. These components facilitate various operations, including content generation, chat sessions, and token counting, leveraging Google's advanced AI models.

## Prerequisites

- Python 3.8 or higher

## Installation

Once Xircuits is installed, simply run

bash```
xircuits install google_gemini
```

You may also manually clone this repository to `xai_components` and install the requirements.txt.

## Usage

It is recommended to store your Google API key in an environment variable for security and ease of use, or export it via:

```bash
export GOOGLE_API_KEY='your_api_key_here'
```

## Components Overview

The library includes the following components for seamless integration with Google's Generative AI capabilities:

  - **`GeminiAuthorize`**: Handles authorization with the Google Generative AI library using an API key, which can be provided directly or fetched from an environment variable named `GOOGLE_API_KEY`.
  - **`GeminiGenerateContent`**: Generates content based on provided input data using a specified generative model.
  - **`GeminiGenerateContentStream`**: Offers real-time content generation through streaming, similar to `GeminiGenerateContent`.
  - **`GeminiStartChat`**: Initiates a chat session using a specified generative model.
  - **`GeminiChatSendMessage`**: Sends a message and receives a response within an active chat session.
  - **`GeminiChatSendMessageStream`**: Enables real-time chat interaction through streaming, similar to `GeminiChatSendMessage`.
  - **`GeminiCountTokens`**: Counts the number of tokens in the provided input data using a specified generative model.
