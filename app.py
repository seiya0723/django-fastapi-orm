import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from bbs.models import Topic
from asgiref.sync import sync_to_async

@sync_to_async
def get_topics():
    return list(Topic.objects.all().values)


from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():

    global topics_cache
    topics_cache = await get_topics()


@app.get("/")
async def index():
    print("サーバー起動時のトピック")

    return { "topics": topics_cache }

