#!/usr/bin/env bash
# Activar entorno virtual en Git Bash (Windows)
# Uso: source ./activate.sh

if [ ! -d ".venv" ]; then
  echo "❌ No existe .venv. Crea el entorno con:"
  echo "   py -m venv .venv"
  return 1 2>/dev/null || exit 1
fi

source ".venv/Scripts/activate"
echo "✅ Entorno activado: $(python -c "import sys; print(sys.executable)")"
