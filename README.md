# InfraHuntersWebInterface

Command & Control web interface.

***For educational purposes only***

## Installation

### Requirements

```bash
python -m pip install -r requirements.txt
cd IFHWI
```

### Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Run

```bash
python manage.py runserver
```

## Usage

### Agent list

```
http://<host>:<port>/
ex: http://127.0.0.1:8000/
```

### Agent info

```
http://<host>:<port>/agent/?id=<agent_id>
ex: http://127.0.0.1:8000/agent/?id=3
```

### Edit database

```
http://<host>:<port>/admin/
ex: http://127.0.0.1:8000/admin/
```

## Screenshots

![agent list](https://raw.githubusercontent.com/LucasJeanpierre/InfraHuntersWebInterface/main/IFHWI/C2/static/C2/images/screenshot0.png)

![agent info](https://raw.githubusercontent.com/LucasJeanpierre/InfraHuntersWebInterface/main/IFHWI/C2/static/C2/images/screenshot1.png)

![change agent](https://raw.githubusercontent.com/LucasJeanpierre/InfraHuntersWebInterface/main/IFHWI/C2/static/C2/images/screenshot2.png)

![command list](https://raw.githubusercontent.com/LucasJeanpierre/InfraHuntersWebInterface/main/IFHWI/C2/static/C2/images/screenshot3.png)

![agent type](https://raw.githubusercontent.com/LucasJeanpierre/InfraHuntersWebInterface/main/IFHWI/C2/static/C2/images/screenshot4.png)