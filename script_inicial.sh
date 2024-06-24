python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cat configs_container_postgres_desafio.txt > ~/.config/cni/net.d/desafio_indicium_default.conflist
cat configs_containers_airflow_desafio.txt > ~/.config/cni/net.d/airflow-docker_default.conflist
podman-compose up --detach
meltano init desafio_indicium --force
cp configurar_projeto.py desafio_indicium/
cp .env desafio_indicium/
cd airflow-docker
echo -e "AIRFLOW_UID=$(id -u)" > .env
podman-compose up --detach
cd ../desafio_indicium
python configurar_projeto.py
