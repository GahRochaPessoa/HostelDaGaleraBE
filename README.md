# HostelDaGaleraBE

**Comandos para rodar o projeto depois de clonado:**

- criar um banco de dados postgreSQL chamado 'hostel_galera'

- criar um arquivo chamado secret.py, no diretório 'HOSTELDAGALERRABE', com a sua django_key, postgre_key e postgre_port

**- Instalar as dependências do projeto com o comando:**
    - pip install -r requirements.txt

**Para colocar o Projeto no ar use os seguintes comandos:**
- python manage.py makemigrations
- python manage.py migrate
- py manage.py loaddata api_hostel/fixtures/initial_data.json
- python manage.py runserver
