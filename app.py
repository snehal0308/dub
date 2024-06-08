import os
from typing import Optional

from dotenv import load_dotenv
from dubbing_utils import download_dubbed_file, wait_for_dubbing_completion
from elevenlabs.client import ElevenLabs

from flask import Flask, request, render_template, flash, jsonify
import os
import json

from os import environ as env
from urllib.parse import quote_plus, urlencode
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

# Load environment variables
load_dotenv()

# Retrieve the API key
ELEVENLABS_API_KEY = "sk_94963b2860cc6eb5263d72fe6f0455e1b519e4ae1362e5ea"
if not ELEVENLABS_API_KEY:
    raise ValueError(
        "ELEVENLABS_API_KEY environment variable not found. "
        "Please set the API key in your environment variables."
    )

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

#routes
link=""

    
'''source_url = "https://www.youtube.com/shorts/zLppD1UuP4A" # Charlie bit my finger
    source_language = "en"
    target_language = "hi"
    result = create_dub_from_url(source_url, source_language, target_language)
    if result:
        print("Dubbing was successful! File saved at:", result)
    else:
        print("Dubbing failed or timed out.")'''

link =""
lang1=""
lang2=""
@app.route("/" , methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        link = str(request.form.get('link'))
        lang1 = "en"
        lang2 = "hi"
        print(lang1 , lang2, link)
        result = create_dub_from_url(link, lang1, lang2)
        if result:
            print("Dubbing was successful! File saved at:", result)
        else:
            print("Dubbing failed or timed out.")
    return render_template("index.html" )

def create_dub_from_url(
    source_url: str,
    source_language: str,
    target_language: str,
) -> Optional[str]:
    """
    Downloads a video from a URL, and creates a dubbed version in the target language.

    Args:
        source_url (str): The URL of the source video to dub. Can be a YouTube link, TikTok, X (Twitter) or a Vimeo link.
        source_language (str): The language of the source video.
        target_language (str): The target language to dub into.

    Returns:
        Optional[str]: The file path of the dubbed file or None if operation failed.
    """

    response = client.dubbing.dub_a_video_or_an_audio_file(
        source_url="https://www.youtube.com/shorts/zLppD1UuP4A",
        target_lang="hi",
        mode="automatic",
        source_lang=
        "en",
        num_speakers=1,
        watermark=True,  # reduces the characters used
    )

    dubbing_id = response.dubbing_id
    if wait_for_dubbing_completion(dubbing_id):
        output_file_path = download_dubbed_file(dubbing_id, target_language)
        return output_file_path
    else:
        return None
    


if __name__ == "__main__":
    app.run(debug=True)





