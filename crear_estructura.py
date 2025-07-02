
import sqlite3

def crear_bd(nombre_bd="mibd.sqlite"):
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()

    # --- Tabla ENTIDADES_SOLICITANTES ---
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ENTIDADES_SOLICITANTES (
        Ent_IdEntidad INTEGER PRIMARY KEY,
        Ent_Nombre_Corto TEXT,
        Ent_Nombre_Largo TEXT,
        Ent_CIF TEXT,
        Ent_Num_Habitantes_2022 INTEGER
    );
    """)

    # --- Tabla ESTADOS ---
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ESTADOS (
        Est_IdEstado INTEGER PRIMARY KEY,
        Est_Nombre TEXT
    );
    """)

    # --- Tabla SOLICITUDES ---
    cur.execute("""
    CREATE TABLE IF NOT EXISTS SOLICITUDES (
        Sol_IdSolicitud INTEGER PRIMARY KEY,
        Sol_IdEntidad INTEGER,
        Sol_IdEstado INTEGER,
        Sol_Nom_Proyecto TEXT,
        Sol_Importe_Presupuesto_total REAL,
        FOREIGN KEY (Sol_IdEntidad) REFERENCES ENTIDADES_SOLICITANTES(Ent_IdEntidad),
        FOREIGN KEY (Sol_IdEstado) REFERENCES ESTADOS(Est_IdEstado)
    );
    """)

    conn.commit()
    conn.close()
    print("Base de datos SQLite creada con estructura.")

if __name__ == "__main__":
    crear_bd()
