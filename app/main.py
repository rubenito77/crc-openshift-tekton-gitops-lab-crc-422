import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

APP_NAME = os.getenv("APP_NAME", "app-demo")
APP_VERSION = os.getenv("APP_VERSION", "2.0.0")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "dev")
GIT_COMMIT = os.getenv("GIT_COMMIT", "local")

app = FastAPI(
    title="CRC Tekton GitOps App Demo",
    version=APP_VERSION,
)


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return f"""
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CRC Tekton GitOps Lab - V2</title>
    <style>
      body {{
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #071952, #088395);
        color: #17212b;
      }}
      main {{
        width: min(720px, 90%);
        padding: 2rem;
        border-top: 6px solid #37b7c3;
        border-radius: 8px;
        background: white;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
      }}
      .version {{
        display: inline-block;
        padding: 0.4rem 0.8rem;
        border-radius: 999px;
        background: #088395;
        color: white;
        font-weight: bold;
      }}
      code {{
        padding: 0.15rem 0.35rem;
        border-radius: 4px;
        background: #eef1f4;
      }}
    </style>
  </head>
  <body>
    <main>
      <span class="version">V2 - Version {APP_VERSION}</span>
      <h1>OpenShift Tekton GitOps en CRC</h1>
      <p>V2 incorpora una nueva identidad visual y despliegue automatico mediante GitHub, Tekton y Argo CD.</p>
      <p>Ambiente: <code>{APP_ENVIRONMENT}</code></p>
      <p>Commit: <code>{GIT_COMMIT}</code></p>
    </main>
  </body>
</html>
"""


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict[str, str]:
    return {"status": "ready"}


@app.get("/info")
def info() -> dict[str, str]:
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENVIRONMENT,
        "git_commit": GIT_COMMIT,
    }
