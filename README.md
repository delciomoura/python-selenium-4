# Projeto de Testes Automatizados com Selenium e Pytest

Este projeto contém testes automatizados desenvolvidos em **Python 3**, utilizando o **Selenium WebDriver** para automação de navegadores e o **Pytest** como framework de testes.

---

## 📋 Pré-requisitos

Antes de executar os testes, certifique-se de ter instalado:

- [Python 3](https://www.python.org/downloads/) (3.8 ou superior recomendado)
- [Google Chrome](https://www.google.com/chrome/) ou outro navegador compatível
- [ChromeDriver](https://chromedriver.chromium.org/downloads) correspondente à versão do Chrome instalado
  > Dica: você pode usar o [WebDriver Manager](https://pypi.org/project/webdriver-manager/) para evitar configurações manuais.

---

## 📦 Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

   ```

2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Execução dos testes

1. Exemplo: rodar o teste contact_save.py com relatório em HTML:
   ```bash
   pytest -v tests/contacts/contact_save.py --html=report.html
   ```
2. Rodar todos os testes do projeto
   ```bash
   pytest -v tests/ --html=report.html
   ```