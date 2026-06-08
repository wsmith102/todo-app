from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
    <head>
        <title>AI Dashboard</title>
    </head>
    <body>
        <h1>Self-Learning AI Dashboard</h1>
        <p>Use /predict and /teach endpoints to interact with the model.</p>
        <p>Vector memory and background training are active.</p>
    </body>
    </html>
    """
