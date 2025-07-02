
# Proyecto RAG Semántico - Estructura + Importación desde Access

## Contenido:
- `crear_estructura.py`: crea la base de datos SQLite (`mibd.sqlite`) con la estructura limpia.
- `importar_desde_access.py`: importa datos desde tu archivo `.accdb` a las tablas correspondientes.

## Requisitos:
- Tener instalado el driver ODBC de Access (Microsoft Access Database Engine)
- Instalar pyodbc: `pip install pyodbc`

## Uso:

1. Ejecuta primero:
```bash
python crear_estructura.py
```

2. Luego importa los datos:
```bash
python importar_desde_access.py
```
