import os
import mysql.connector
def connection():
    return mysql.connector.connect(host=os.getenv("DB_HOST","localhost"),user=os.getenv("DB_USER","root"),password=os.getenv("DB_PASSWORD",""),database=os.getenv("DB_NAME","smartflow_ai"),connection_timeout=3)
def get_junctions():
    con=connection(); cur=con.cursor(dictionary=True)
    try:
        cur.execute("SELECT id,name,vehicles,density,signal,duration FROM junctions ORDER BY id")
        return cur.fetchall()
    finally: cur.close(); con.close()
def save_junctions(items):
    con=connection(); cur=con.cursor()
    try:
        for x in items: cur.execute("UPDATE junctions SET duration=%s WHERE id=%s",(x.get("green_seconds",x.get("duration",30)),x["id"]))
        con.commit()
    except Exception: con.rollback(); raise
    finally: cur.close(); con.close()
