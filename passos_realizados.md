# Passos realizados no desafio:

1. Criação de script para pré-configuração do ambiente:
    * 1.1. Alteração de portas no arquivo do docker-compose do container

    * 1.2. Mudança de configuração no arquivo de inicialização do container (/home/<user>/.config/cni/net.d/code-challenge-main_default.conflist), colocando o CNI version para de 1.0.0 para 0.4.0

    * 1.3. Mudança da referência da imagem para uma mais descritiva: de 'postgres12' para 'docker.io/library/postgres:12'

    * 1.4. Criação de ambiente virtual em Python para instalar as bibliotecas do `meltano`, `psycopg2` e outras necessárias para a execução do desafio.

2. Criação de um projeto Meltano através do comando `meltano init <nome_projeto>`
    * 2.1. Adicionar os extratores do postgres e de csv ao projeto pelo comando `meltano add extractor tap-postgres tap-csv`

    * 2.2. Adicionar variáveis de configuração no .env de dentro do projeto 

    * 2.3. Criação de script python para executar comandos CLI para configurar o projeto (extratores e loaders):
        
        * Pegando as variáveis do .env

        * Adicionando e configurando os extratores, loaders e jobs (que podem incluir o pipeline)




-------------------
Pegar conteúdo do .csv e colocá-lo na pasta:
`/data/postgres/{table}/2024-01-02/file.format` OU 
`/data/csv/2024-01-02/file.format`
    