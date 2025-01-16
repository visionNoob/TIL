import os
import openai
import gradio as gr


def check_openai_api_key(client):

    try:
        client.models.list()

    except openai.AuthenticationError:
        return False
    else:
        return True


def init_client(api_key):
    client = openai.OpenAI(api_key=api_key)
    status = check_openai_api_key(client)

    if status:
        return client
    else:
        return None
