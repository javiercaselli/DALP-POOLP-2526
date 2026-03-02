from __future__ import annotations

import os
import sqlite3

from typing import List, Optional

def _connect(db_path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    return conn

def init_db(db_path: str) -> None:
    schema = """
    CREATE TABLE IF NOT EXISTS recursos (
        id          INTEGER PRIMARY KEY,
        tipo        TEXT NOT NULL,
        titulo      TEXT NOT NULL,
        autor       TEXT,
        anio        INTEGER,

        -- LibroDigital
        isbn        TEXT,
        num_paginas INTEGER,
        formato     TEXT,

        -- VideoCurso
        duracion    INTEGER,
        nivel       TEXT,

        -- Podcast
        episodio    INTEGER,
        url         TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_recursos_tipo ON recursos(tipo);
    CREATE INDEX IF NOT EXISTS idx_recursos_titulo ON recursos(titulo); 
    """

    with _connect(db_path) as conn:
        conn.executescript(schema)
