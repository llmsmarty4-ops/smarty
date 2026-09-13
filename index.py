# Vercel Python/Flask entrypoint
# Vercel discovers this file as a Python Function and imports the Flask app.
from main import app

__all__ = ["app"]
