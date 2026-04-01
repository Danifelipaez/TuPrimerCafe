# Cafe Chatbot

## Run locally
pip install -r requirements.txt
uvicorn app.main:app --reload

## Deploy
Use Render.com and set:
uvicorn app.main:app --host 0.0.0.0 --port 10000
