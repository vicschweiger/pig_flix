# PigFlix

## Descrição do Projeto

**PigFlix** é uma aplicação web desenvolvida em Flask que permite aos usuários adicionar, visualizar e gerenciar uma coleção personalizada de filmes disponíveis no YouTube. Os usuários podem adicionar filmes à biblioteca incluindo informações detalhadas como título, descrição, capa (imagem), e link do YouTube. O banco de dados SQLite é utilizado para armazenar as informações dos filmes.

## Funcionalidades Principais

1. **Adicionar Filmes:**
   - Formulário para adicionar novos filmes com campos para título, descrição, link do YouTube e URL da imagem de capa.
   - Validação dos campos para garantir que todos os dados necessários sejam fornecidos.

2. **Visualizar Filmes:**
   - Página principal exibindo a lista de filmes adicionados.
   - Cada filme é exibido com sua capa, título e uma breve descrição.
   - Link para assistir ao filme diretamente no YouTube.

3. **Detalhes do Filme:**
   - Página de detalhes para cada filme com informações completas, incluindo título, descrição, capa e o vídeo incorporado do YouTube.

4. **Editar e Excluir Filmes:**
   - Funcionalidade para editar as informações dos filmes existentes.
   - Opção para excluir filmes da biblioteca.

## Tecnologias Utilizadas

- **Backend:**
  - Flask (framework web em Python)
  - SQLite (banco de dados leve e fácil de usar)

- **Frontend:**
  - HTML5 e CSS3 para a estrutura e estilo das páginas.
  - Jinja2 (template engine do Flask) para renderização dinâmica de páginas.
  - Bootstrap (framework CSS) para design responsivo e estilização.

- **Outras Bibliotecas:**
  - SQLAlchemy para interação com o banco de dados SQLite.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/vicschweiger/pig_flix
   cd pig_flix

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   
4. **Execute a aplicação:**
   flask run

A aplicação estará disponível em http://127.0.0.1:5000/.

## Futuras Melhorias
Implementar autenticação de usuários para permitir bibliotecas personalizadas.
Adicionar funcionalidades de busca e filtragem de filmes.
Permitir a classificação dos filmes por categorias ou gêneros.
   


