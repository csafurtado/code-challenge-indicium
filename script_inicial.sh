python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cat configs_container_desafio.txt > ~/.config/cni/net.d/desafio_indicium_default.conflist
podman-compose up --detach
meltano init desafio_indicium
cp configurar_projeto.py desafio_indicium/
cp .env desafio_indicium/
cd desafio_indicium
python configurar_projeto.py
