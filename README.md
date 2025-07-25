# Calculadora Avançada – Teste Técnico

Este projeto é uma aplicação **Django** com autenticação de usuário, uma **calculadora** (soma, subtração, multiplicação e divisão) e um **histórico de operações**.  
O layout foi estilizado com **TailwindCSS** para oferecer uma interface moderna.

---

## **Funcionalidades**
- **Autenticação de usuários** (login/logout).
- **Calculadora básica** (quatro operações).
- **Registro e exibição das últimas 10 operações por usuário**.
- **Administração via painel do Django Admin**.
- **Layout responsivo com TailwindCSS**.

---

## **Instalação e execução**

### **1. Criar ambiente virtual**
```bash
python -m venv .venv
```

Ative o ambiente:

**Windows (PowerShell):**
```bash
.venv\Scripts\activate
```

---

### **2. Instalar dependências**
```bash
pip install -U pip
pip install -r requirements.txt
```

---

### **3. Configurar o banco de dados**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **4. Criar superusuário**
```bash
python manage.py createsuperuser
```
Use este usuário para acessar **/admin**.

---

### **5. Rodar o servidor local**
```bash
python manage.py runserver
```

Acesse:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) – Tela principal.
- [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) – Painel Admin.

---

## **Testes**
Para rodar os testes:
```bash
python manage.py test
```

---

## **Estrutura do projeto**
```
calcportal_ui_v2/
├─ manage.py
├─ requirements.txt
├─ README.md
├─ calcportal_ui_v2/
│   ├─ settings.py
│   ├─ urls.py
│   ├─ wsgi.py
│   └─ asgi.py
├─ calculator/
│   ├─ models.py
│   ├─ forms.py
│   ├─ views.py
│   ├─ urls.py
│   ├─ tests.py
│   └─ admin.py
└─ templates/
    ├─ base.html
    ├─ registration/
    │    └─ login.html
    └─ calculator/
         └─ index.html
