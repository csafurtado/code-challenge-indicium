from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Defina o nome da sua DAG e a frequência de execução
dag_name = 'TESTE_DAG_INICIAL'
default_args = {
    'owner': 'seu_nome',
    'start_date': datetime(2024, 6, 21),
    'retries': 1,
}

# Crie a DAG
dag = DAG(
    dag_name,
    default_args=default_args,
    schedule_interval='@daily',  # Executa diariamente
    catchup=False,  # Não recupera tarefas perdidas
)

# Tarefas
start_task = DummyOperator(task_id='start', dag=dag)

def minha_tarefa_python():
    print("\n\n\n\n\n\n\nExecutando minha tarefa Python!\n\n\n\n\n\n\n\n")

python_task = PythonOperator(
    task_id='minha_tarefa',
    python_callable=minha_tarefa_python,
    dag=dag,
)

end_task = DummyOperator(task_id='end', dag=dag)

# Defina a ordem das tarefas
start_task >> python_task >> end_task