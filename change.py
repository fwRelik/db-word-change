import sys

import pymysql


def find_and_replace_word(host, user, password, db, word_to_find, word_to_replace):
    try:
        connection = pymysql.connect(host=host, user=user, password=password, db=db)
        cursor = connection.cursor()

        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]

        for table in tables:
            cursor.execute(f"DESCRIBE {table}")
            columns = [column[0] for column in cursor.fetchall()]

            print(f'\r\n{table=}')
            print(f'{columns=}\r\n')

            for column in columns:
                update_query = f"""
                    UPDATE {table}
                    SET `{column}` = REPLACE(`{column}`, '{word_to_find}', '{word_to_replace}')
                    WHERE `{column}` LIKE '%{word_to_find}%';
                """
                cursor.execute(update_query)

        connection.commit()
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if connection:
            connection.close()


find_and_replace_word(
    host='localhost',
    user='root',
    password='',
    db='db_name',
    word_to_find='old_word',
    word_to_replace='new_word'
)
