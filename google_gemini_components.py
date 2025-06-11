from xai_components.base import InArg, OutArg, Component, xai_component, secret
import os
from google import genai


@xai_component
class GeminiAuthorize(Component):
    """A Xircuits component to authorize the Google GenAI library.

    ##### inPorts:
    - api_key: The API key for authorization.
    - from_env: Flag to indicate if API key should be fetched from environment.
    """
    api_key: InArg[secret]
    from_env: InArg[bool]

    def execute(self, ctx) -> None:
        key = os.getenv('GOOGLE_API_KEY') if self.from_env.value else self.api_key.value
        ctx["genai_client"] = genai.Client(api_key=key)



@xai_component
class GeminiGenerateContent(Component):
    """A Xircuits component to generate content using the Google GenAI library.

    ##### inPorts:
    - model_name: The name of the generative model to use.
    - input_data: The input data for content generation.

    ##### outPorts:
    - output: The generated content text.
    """
    model_name: InArg[str]
    input_data: InArg[str]

    output: OutArg[str]

    def execute(self, ctx) -> None:
        client = ctx.get("genai_client")
        if not client:
            raise ValueError("Missing genai_client. Please make sure GeminiAuthorize was executed first.")

        model = self.model_name.value or "models/gemini-1.5-flash"
        response = client.models.generate_content(
            model=model,
            contents=[self.input_data.value]
        )
        self.output.value = response.text


@xai_component
class GeminiGenerateContentStream(Component):
    """A Xircuits component to generate content using the Google GenAI library with streaming.

    ##### inPorts:
    - model_name: The name of the generative model to use.
    - input_data: The input data for content generation.

    ##### outPorts:
    - output: The generated content text stream.
    """
    model_name: InArg[str]
    input_data: InArg[str]

    output: OutArg[any]

    def execute(self, ctx) -> None:
        client = ctx.get("genai_client")
        if not client:
            raise ValueError("Missing genai_client. Please make sure GeminiAuthorize was executed first.")

        model = self.model_name.value or "models/gemini-1.5-flash"
        stream = client.models.generate_content_stream(
            model=model,
            contents=[self.input_data.value]
        )
        self.output.value = (chunk.text for chunk in stream)


@xai_component
class GeminiStartChat(Component):
    """A Xircuits component to start a chat using the Google GenAI library.

    ##### inPorts:
    - model_name: The name of the generative model to use.
    - history: The chat history.

    ##### outPorts:
    - chat: The chat session object.
    """
    model_name: InArg[str]
    history: InArg[list]

    chat: OutArg[any]

    def execute(self, ctx) -> None:
        client = ctx.get("genai_client")
        if not client:
            raise ValueError("Missing genai_client. Please make sure GeminiAuthorize was executed first.")

        model = self.model_name.value or "models/gemini-1.5-flash"
        chat = client.chats.create(
            model=model,
            history=self.history.value
        )
        self.chat.value = chat


@xai_component
class GeminiChatSendMessage(Component):
    """A Xircuits component to send a message in a chat using the Google GenAI library.

    ##### inPorts:
    - chat: The chat session object.
    - message: The message to send.

    ##### outPorts:
    - response: The response to the message.
    """
    chat: InArg[any]
    message: InArg[str]

    response: OutArg[str]

    def execute(self, ctx) -> None:
        response = self.chat.value.send_message(message=self.message.value)
        self.response.value = response.text


@xai_component
class GeminiChatSendMessageStream(Component):
    """A Xircuits component to send a message in a chat using the Google GenAI library with streaming.

    ##### inPorts:
    - chat: The chat session object.
    - message: The message to send.

    ##### outPorts:
    - response: The response to the message stream.
    """
    chat: InArg[any]
    message: InArg[str]

    response: OutArg[any]

    def execute(self, ctx) -> None:
        stream = self.chat.value.send_message_stream(message=self.message.value)
        self.response.value = (chunk.text for chunk in stream)


@xai_component
class GeminiCountTokens(Component):
    """A Xircuits component to count tokens using the Google GenAI library.

    ##### inPorts:
    - model_name: The name of the generative model to use.
    - input_data: The input data for token counting.

    ##### outPorts:
    - output_tokens: The total number of tokens.
    """
    model_name: InArg[str]
    input_data: InArg[str]

    output_tokens: OutArg[int]

    def execute(self, ctx) -> None:
        client = ctx.get("genai_client")
        if not client:
            raise ValueError("Missing genai_client. Please make sure GeminiAuthorize was executed first.")

        model = self.model_name.value or "models/gemini-1.5-flash"
        result = client.models.count_tokens(
            model=model,
            contents=[self.input_data.value]
        )
        self.output_tokens.value = result.total_tokens