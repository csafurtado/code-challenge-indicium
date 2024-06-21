import subprocess, os, dotenv, json


dotenv.load_dotenv('.env')

## CONFIGURAÇÃO EXTRATORES (extractors)
# Adiciona os extratores para o postgres e para arquivos csv
subprocess.run(["meltano", "add", "extractor", "tap-csv", "tap-postgres"])

# Configura o extrator para o Postgres
subprocess.run(["meltano", "config", "tap-postgres", "set", "host", os.getenv('TAP_POSTGRES_HOST')])
subprocess.run(["meltano", "config", "tap-postgres", "set", "port", os.getenv('TAP_POSTGRES_PORT')])
subprocess.run(["meltano", "config", "tap-postgres", "set", "database", os.getenv('TAP_POSTGRES_NAME')])
subprocess.run(["meltano", "config", "tap-postgres", "set", "user", os.getenv('TAP_POSTGRES_USER')])
subprocess.run(["meltano", "config", "tap-postgres", "set", "password", os.getenv('TAP_POSTGRES_PASSWORD')])

# Configura o extrator de csv
json_config_csv = os.getenv('TAP_CSV_FILES')

json_config_csv_string = f"[{json.dumps(json_config_csv)}]"

print(json_config_csv_string)

subprocess.run(["meltano", "config", "tap-csv", "set", "files", json_config_csv_string])


## CONFIGURAÇÃO LOADERS (carregadores)
# Adiciona os loaders de dados para o formato csv e para o Postgres
subprocess.run(["meltano", "add", "loader", "target-postgres", "target-csv"])

# Configura o loader de csv
subprocess.run(["meltano", "config", "target-csv", "set", "destination_path", os.getenv('TARGET_CSV_DESTINATION_PATH')])


## CRIAÇÃO DE JOBS (PIPELINES) DE EXTRAÇÃO E COLETA DE DADOS
# Cria o job para realizar o pipeline de extração de dados do csv e das tabelas do Postgres para arquivos csv
subprocess.run(["meltano", "job", "add", "pipeline_extracao_local_csv", "--tasks", f'"tap-csv target-csv"'])
subprocess.run(["meltano", "job", "add", "pipeline_extracao_local_postgres", "--tasks", f'"tap-postgres target-csv"'])

# subprocess.run(["meltano", "run", "pipeline_extracao_local_postgres"])