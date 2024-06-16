from transformers import pipeline

from dotenv import load_dotenv
from os import getenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from gtts import gTTS

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")

def img_to_text(img):
    nlp = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = nlp(img, max_new_tokens=100)[0]["generated_text"]

    return text

def create_story(text):
    template = """
    Você é um especialista em criar histórias intrigantes.

    Crie uma história curta que tenha no máximo 20 palavras. A história deve ser intrigante e deixar o leitor curioso.

    CONTEXT: {text}
    """

    prompt = PromptTemplate.from_template(template)

    llm = OpenAI(temperature=1)

    llm_chain = prompt | llm

    story = llm_chain.invoke(text)

    return story

def text_to_audio(text):
    tts = gTTS(text, lang="pt-br")
    tts.save("audio.mp3")
    
if __name__ == "__main__":
    text = img_to_text("img.jpg")
    story = create_story(text)
    text_to_audio(story)