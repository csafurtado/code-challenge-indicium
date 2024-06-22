import psycopg2
import dotenv, os


# dotenv.load_dotenv('.env')
dotenv.load_dotenv('desafio_indicium/.env')

# Configurações de conexão
host = 'localhost'
port = 44444
dbname = os.getenv('TAP_POSTGRES_NAME')
user = os.getenv('TAP_POSTGRES_USER')
password = os.getenv('TAP_POSTGRES_PASSWORD')

try:
    # Conecta ao banco de dados
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    cursor = conn.cursor()

    # Executa a consulta
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()

    # Exibe os resultados
    for row in rows:
        print(row)

    # Fecha a conexão
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Erro ao conectar ou executar a consulta: {e}")
