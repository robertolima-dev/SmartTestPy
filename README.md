# 📚 **SmartTestPy** - Framework Inteligente para Testes em Python

**SmartTestPy** é um pacote robusto e flexível para a criação de testes automatizados em Python. Com suporte ao `pytest`, `unittest`, geração de dados fake, mocks avançados e integração com APIs e bancos de dados, ele foi projetado para simplificar o processo de testes, desde o básico até casos avançados.

---

## ✨ **Funcionalidades Principais**
- ✅ **Assertions personalizadas** para validações detalhadas.
- 🏗 **Fixtures reutilizáveis** para cenários complexos.
- 🎭 **Mocks inteligentes** para testes isolados.
- 🌐 **Testes de API** com validação de payloads, headers e status.
- 🏦 **Gerenciamento de banco de dados** para testes integrados.
- ⏳ **Manipulação de tempo** com suporte ao `freezegun`.
- 📊 **Cobertura de código** com relatórios automatizados.
- ⚡ **Execução paralela de testes** para maior performance.
- 🛠 **Compatível com frameworks** como Django, Flask e FastAPI.
- 🌍 **Internacionalização (i18n)** para mensagens e logs de testes.

---

## ⚡ **Instalação**

Instale o **SmartTestPy** diretamente do PyPI:

```bash
pip install SmartTestPy
```

> 💡 Requisitos: Python 3.6 ou superior.

---

## 🚀 **Como Usar**

### ✅ **Assertions Customizadas**
```python
from smarttestpy.assertions import assert_status_code

response = MockResponse(200, "OK")
assert_status_code(response, 200)
```

### 🧪 **Fixtures e Mocks**
```python
from smarttestpy.fixtures import fake_user

user = fake_user()
assert user['email'] is not None
```

### 🌐 **Testes de API**
```python
from smarttestpy.response_helpers import assert_json_response

response = client.get("/api/user/1/")
assert_json_response(response, {"id": 1, "name": "John Doe"})
```

### ⏳ **Manipulação de Tempo**
```python
from smarttestpy.time_utils import fixed_time

assert fixed_time().strftime("%Y-%m-%d") == "2025-01-01"
```

---

## 🏃 **Executando os Testes**

```bash
pytest tests/ --maxfail=1 --disable-warnings -v
```

📈 Para gerar relatório de cobertura:

```bash
pytest --cov=smarttestpy --cov-report=html
```

---

## 🏗 **Estrutura do Projeto**
```
SmartTestPy/
│
├── smarttestpy/                # 📦 Código do pacote
│   ├── __init__.py
│   ├── assertions.py           # ✅ Assertions personalizadas
│   ├── fixtures.py             # 🏗 Fixtures e mocks reutilizáveis
│   ├── response_helpers.py     # 🌐 Testes e validações de APIs
│   ├── time_utils.py           # ⏳ Manipulação de tempo
│
├── tests/                      # 🧪 Testes unitários
│   ├── test_assertions.py
│   ├── test_fixtures.py
│   ├── test_response_helpers.py
│   └── test_time_utils.py
│
├── setup.py                    # ⚙️ Configuração do pacote
├── pyproject.toml              # 📦 Configuração moderna
├── README.md                   # 📚 Documentação do projeto
├── LICENSE                     # 📜 Licença MIT
└── MANIFEST.in                 # 📋 Inclusão de arquivos extras
```

---

## 🌐 **Compatibilidade**
- ✅ Python 3.6+
- 🚀 Compatível com **Django**, **Flask** e **FastAPI**.
- 🐍 Suporte a `pytest`, `unittest` e execução paralela com `pytest-xdist`.

---

## 📝 **Licença**

Distribuído sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 **Autor**

Desenvolvido por **[Roberto Lima](https://robertolima-developer.vercel.app/)** 🚀✨

---

## 💬 **Contato**

- 📧 **Email**: robertolima.izphera@gmail.com
- 💼 **LinkedIn**: [Roberto Lima](https://www.linkedin.com/in/roberto-lima-01/)

---

## ⭐ **Gostou do projeto?**

Deixe uma ⭐ no repositório e compartilhe com a comunidade! 🚀✨  

```bash
git clone https://github.com/seuusuario/SmartTestPy.git
cd SmartTestPy
pip install -e .
```

---

## 🌟 **O que este README oferece?**
- 🎯 **Descrição clara** do projeto e seu propósito.  
- 🛠 **Instruções detalhadas de instalação** e **uso prático**.  
- 🧪 **Guia de testes** para garantir que o código funciona.  
- 🏗 **Estrutura do projeto** para facilitar a navegação.  
- 🔄 **Seção de contribuição** para quem deseja ajudar no desenvolvimento.  
- 📝 **Licença e informações do autor** para transparência.
