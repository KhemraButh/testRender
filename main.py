from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Test App</title>
    </head>
    <body>
        <h1>Welcome to FastAPI on Render</h1>
        <p>Your deployment is successful!</p>
    </body>
    </html>
    """
    return html_content
