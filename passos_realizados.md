# Passos realizados no desafio:

0. Ambiente local:
    * Linux Ubuntu 22.04
    * Podman 3.4.4
    * Python 3.10.12

1. Criação de script para pré-configuração do ambiente na minha máquina local:
    * 1.1. Alteração de portas no arquivo do docker-compose do container

    * 1.2. Mudança de configuração no arquivo de inicialização do container relativo ao BD Postgres e aos containers do Apache Airflow (/home/<user>/.config/cni/net.d/code-challenge-main_default.conflist e airflow-docker_default.conflist), colocando o CNI version para de 1.0.0 para 0.4.0 para adequação em minha máquina

    * 1.3. Mudança da referência da imagem para uma mais descritiva: de 'postgres12' para 'docker.io/library/postgres:12' e de 'apache/airflow:2.9.2' para 'docker.io/apache/airflow:2.9.2'

    * 1.4. Criação de ambiente virtual em Python para instalar as bibliotecas do `meltano`, `psycopg2` e outras necessárias para a execução do desafio.

2. Criação de um projeto Meltano através do comando `meltano init <nome_projeto>`
    * 2.1. Adicionar os extratores do postgres e de csv ao projeto pelo comando `meltano add extractor tap-postgres tap-csv`

    * 2.2. Adicionar variáveis de configuração no .env de dentro do projeto 

    * 2.3. Criação de script python para executar comandos CLI para configurar o projeto (extratores e loaders):
        
        * Pegando as variáveis do .env

        * Adicionando e configurando os extratores, loaders e jobs (que podem incluir o pipeline)

    