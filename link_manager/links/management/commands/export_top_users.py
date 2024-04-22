import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()


conn = psycopg2.connect(
    database=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"]
)


cursor = conn.cursor()
cursor.execute("SELECT id, name FROM links_collection;")
collections = cursor.fetchall()


sql_query = "SELECT cu.username,"


for collection in collections:
    collection_id, collection_name = collection
    sql_query += f" SUM(CASE WHEN llc.collection_id = '{collection_id}' THEN 1 ELSE 0 END) AS \"{collection_name}\","


sql_query = sql_query.rstrip(",")


sql_query += """
 FROM
     custom_user cu
 LEFT JOIN
     links_link ll
 ON
     cu.id = ll.user_id
 LEFT JOIN
     links_link_collections llc
 ON
     ll.id = llc.link_id
 LEFT JOIN
     links_collection lc
 ON
     llc.collection_id = lc.id
 GROUP BY
     cu.username,
     cu.created_at
 ORDER BY
     COUNT(llc.collection_id) DESC,
     cu.created_at ASC
 LIMIT 10;
"""

cursor.execute(sql_query)
results = cursor.fetchall()


df = pd.DataFrame(results, columns=["username"] + [collection[1] for collection in collections])


excel_filename = "user_collections.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Данные сохранены в {excel_filename}")


cursor.close()
conn.close()
