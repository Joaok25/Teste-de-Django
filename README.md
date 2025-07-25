# Teste-de-Django
# Calculadora Avançada – Teste Técnico

Este projeto é uma aplicação **Django** com autenticação de usuário, uma **calculadora** (soma, subtração, multiplicação e divisão) e um **histórico de operações**.  
O layout foi estilizado com **TailwindCSS** para oferecer uma interface moderna.

---

## **Funcionalidades**
- Autenticação de usuários (login/logout).
- Calculadora básica (quatro operações).
- Registro e exibição das últimas 10 operações por usuário.
- Administração via painel do Django Admin.
- Layout responsivo com TailwindCSS.

---

## **Tecnologias utilizadas**
- Python 3.10+
- Django 5.x
- SQLite (banco local)
- TailwindCSS (CDN)
- HTML5 / Template Tags do Django

---

## **Instalação e execução**

### **1. Criar ambiente virtual**
```Terminal
python -m venv .venv

Ative o ambiente:
Windows (PowerShell):
.venv\Scripts\activate


### **2. Instalar dependências**
pip install -U pip
pip install -r requirements.txt


## **3. Configurar o banco de dados**
python manage.py makemigrations
python manage.py migrate


### **4. Criar superusuário**

python manage.py createsuperuser
Use este usuário para acessar /admin.

### **5. Rodar o servidor local**
python manage.py runserver
Acesse:
http://127.0.0.1:8000/ – Tela principal.
http://127.0.0.1:8000/admin – Painel Admin
