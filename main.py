from fastapi import FastAPI
from supabase import create_client
import os

app = FastAPI()

SUPABASE_URL = os.getenv("https://xjjdmtsuyketghsckaqw.supabase.co")
SUPABASE_KEY = os.getenv("sb_publishable_6d_r0lElEd-2wgYfZQT22A_gTuZN3z3")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def home():
    return {"message": "Felix Media API jalan 🚀"}

@app.get("/posts")
def get_posts():
    data = supabase.table("posts").select("*").execute()
    return data.data

@app.post("/posts")
def create_post(user_id: str, content: str):
    data = supabase.table("posts").insert({
        "user_id": user_id,
        "content": content
    }).execute()
    return data.data