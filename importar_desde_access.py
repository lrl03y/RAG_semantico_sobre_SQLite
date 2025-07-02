
import pyodbc
import sqlite3

# Ruta de tu BD Access
access_path = r"C:\Users\Papi\Google Drive\Trabajo\IA\Pruebas BD\AYUDAS_SMARTREGION.accdb"
sqlite_path = "mibd.sqlite"

# Tablas que importaremos (ya estructuradas en SQLite)
tablas_objetivo = [
    "ENTIDADES_SOLICITANTES",
    "ESTADOS",
    "SOLICITUDES",
    "TIPOS_DE_GASTO",
    "GASTOS_PROYECTOS"
]

def importar_access_a_sqlite():
    # Conexión a Access
    conn_access = pyodbc.connect(
        fr"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_path};"
    )
    cursor_access = conn_access.cursor()

    # Conexión a SQLite
    conn_sqlite = sqlite3.connect(sqlite_path)
    cursor_sqlite = conn_sqlite.cursor()

    # Listar tablas de Access
    print("📋 Tablas en Access:")
    for row in cursor_access.tables(tableType='TABLE'):
        print(" -", row.table_name)

    # Importar cada tabla objetivo
    for tabla in tablas_objetivo:
        print(f"⏳ Importando tabla: {tabla}...")

        try:
            rows = cursor_access.execute(f"SELECT * FROM {tabla}").fetchall()
            columnas = [column[0] for column in cursor_access.description]
            placeholders = ", ".join("?" * len(columnas))
            insert_sql = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({placeholders})"

            for row in rows:
                cursor_sqlite.execute(insert_sql, row)

            print(f"✅ {len(rows)} filas insertadas en {tabla}.")
        except Exception as e:
            print(f"⚠️ Error al importar {tabla}: {e}")

    conn_sqlite.commit()
    conn_sqlite.close()
    conn_access.close()
    print("🚀 Importación completada.")

if __name__ == "__main__":
    importar_access_a_sqlite()
