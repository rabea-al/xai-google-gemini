from xai_components.base import InArg, OutArg, Component, xai_component, secret
import os
import google.generativeai as genai
import PIL.Image


@xai_component
class GeminiAuthorize(Component):
    """A Xircuits component to authorize the Google Generative AI library.

    ##### inPorts:
    - api_key: The API key for authorization.
    - from_env: Flag to indicate if API key should be fetched from environment.

    """
    api_key: InArg[secret]
    from_env: InArg[bool]

    def execute(self, ctx) -> None:
        if self.from_env.value:
            genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        else:
            genai.configure(api_key=self.api_key.value)


@xai_component
class GeminiGenerateContent(Component):
    """A Xircuits component to generate content using the Google Generative AI library.

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
        model = genai.GenerativeModel(self.model_name.value if self.model_name.value is not None else 'gemini-pro')
        response = model.generate_content(self.input_data.value, stream=False)
        self.output.value = response.text


@xai_component
class GeminiGenerateContentStream(Component):
    """A Xircuits component to generate content using the Google Generative AI library with streaming.

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
        model = genai.GenerativeModel(self.model_name.value if self.model_name.value is not None else 'gemini-pro')
        response = model.generate_content(self.input_data.value, stream=True)
        self.output.value = (chunk.text for chunk in response)


@xai_component
class GeminiStartChat(Component):
    """A Xircuits component to start a chat using the Google Generative AI library.

    ##### inPorts:
    - model_name: The name of the generative model to use.
    - history: The chat history.

    ##### outPorts:
    - chat: The chat session object.
    """
    model_name: InArg[str]
    history: InArg[list]

    chat: OutArg[genai.ChatSession]

    def execute(self, ctx) -> None:
        model = genai.GenerativeModel(self.model_name.value if self.model_name.value is not None else 'gemini-pro')
        chat = model.start_chat(history=self.history.value)
        self.chat.value = chat


@xai_component
class GeminiChatSendMessage(Component):
    """A Xircuits component to send a message in a chat using the Google Generative AI library.

    ##### inPorts:
    - chat: The chat session object.
    - message: The message to send.

    ##### outPorts:
    - response: The response to the message.
    """
    chat: InArg[genai.ChatSession]
    message: InArg[str]

    response: OutArg[str]

    def execute(self, ctx) -> None:
        response = self.chat.value.send_message(self.message.value, stream=False)
        self.output_response.value = response.text


@xai_component
class GeminiChatSendMessageStream(Component):
    """A Xircuits component to send a message in a chat using the Google Generative AI library with streaming.

    ##### inPorts:
    - chat: The chat session object.
    - message: The message to send.

    ##### outPorts:
    - output_response: The response to the message stream.
    """
    chat: InArg[genai.ChatSession]
    message: InArg[str]

    output_response: OutArg[any]

    def execute(self, ctx) -> None:
        response = self.chat.value.send_message(self.message.value, stream=True)
        self.output_response.value = (chunk.text for chunk in response)


@xai_component
class GeminiCountTokens(Component):
    """A Xircuits component to count tokens using the Google Generative AI library.

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
        model = genai.GenerativeModel(self.model_name.value)
        self.output_tokens.value = model.count_tokens(self.input_data.value)
