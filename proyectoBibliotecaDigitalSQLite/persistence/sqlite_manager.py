from __future__ import annotations

import os
import sqlite3

from typing import List, Optional

from models import RecursoDigital


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
        autor       TEXT NOT NULL,
        anio        INTEGER NOT NULL,

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


def cargar_recursos(db_path: str) -> List[RecursoDigital]:
    # init_db(db_path)

    with _connect(db_path) as conn:
        rows = conn.execute("SELECT * FROM recursos ORDER BY id ASC").fetchall()

    recursos: List[RecursoDigital] = []
    for row in rows:
        data = dict(row)

        # Limpieza: sqlite devuelve un None en campos no utilizados (nulls)
        data = {k: v for k, v in data.items() if v is not None}

        recursos.append(RecursoDigital.from_dict(data))

    return recursos


def guardar_recursos(db_path: str, recursos: List[RecursoDigital]) -> None:
    # Inicializas BD
    init_db(db_path)

    sql_insert = """
    INSERT INTO recursos
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    with _connect(db_path) as conn:
        conn.execute("DELETE FROM recursos")
        for r in recursos:
            d = r.to_dict()
            conn.execute(sql_insert, (
                int(d.get("id")) if d.get("id") is not None else None,
                d.get("tipo"),
                d.get("titulo"),
                d.get("autor"),
                d.get("anio"),

                d.get("isbn"),
                d.get("num_paginas"),
                d.get("formato"),

                d.get("duracion"),
                d.get("nivel"),

                d.get("episodio"),
                d.get("url")
            ))
