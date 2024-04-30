from re import template
from typing import Union
from pytube import YouTube
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/")
def Download():
  youtubeObject = YouTube("https://youtu.be/p-h1LpM1xm4?si=kSaZGqAGLi-tJmfz")
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("An error has occurred")


# async def fake_video_streamer():
#   for i in range(10):
#     yield b"some fake video bytes"

# @app.get("/")
# async def main():
#   return StreamingResponse(fake_video_streamer())

# @app.get("/pydantic", response_class=RedirectResponse, status_code=302)
# async def redirect_pydantic():
#   return "https://docs.pydantic.dev/"

# @app.get("/")
# def read_root():
#   return {"Hello": "World"}

# @app.get("/items")
# def get_full_name(first_name, last_name):
#   full_name = first_name.title() + " " + last_name.title()
#   # return full_name'
#   return te


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}
