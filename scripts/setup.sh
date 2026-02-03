#!/usr/bin/env bash
set -e

py -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "✅ Entorno listo. Activa con: source .venv/Scripts/activate"
