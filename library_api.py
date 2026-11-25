"""Demo library API: safe stdlib-only runtime, separate from SCA fixture dependencies.

The vulnerable dependencies in top-level manifests are deliberately not needed to run this.
This is not a production application.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import json
import sqlite3
import tempfile

DB_PATH = Path(tempfile.gettempdir()) / "autosca_library_sca_fixture.sqlite3"


def initialize_database():
    with sqlite3.connect(DB_PATH) as db:
        db.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, stock INTEGER NOT NULL)")
        count = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
        if count == 0:
            db.executemany("INSERT INTO books (id, title, stock) VALUES (?, ?, ?)", [
                (1, "The Little Prince", 4),
                (2, "A Brief History of Time", 2),
                (3, "The Hobbit", 3),
            ])


def list_books():
    with sqlite3.connect(DB_PATH) as db:
        rows = db.execute("SELECT id, title, stock FROM books ORDER BY id").fetchall()
    return [{"id": x, "title": y, "stock": z} for x, y, z in rows]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/api/books":
            self.send_error(404, "Not found")
            return
        payload = json.dumps({"items": list_books()}, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    initialize_database()
    print("Demo-only library API: http://127.0.0.1:8765/api/books")
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
