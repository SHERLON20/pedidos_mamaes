🍔 Sistema de Gerenciamento de Pedidos com Flet + PostgreSQL

Aplicação desktop desenvolvida em Python utilizando o framework <a href="https://flet.dev/">Flet</a> integrada ao banco de dados PostgreSQL para gerenciamento de pedidos em tempo real.

O sistema permite controlar pedidos de mesas, delivery e atendimento externo, oferecendo funcionalidades de atualização automática, fechamento de conta, exclusão de pedidos e controle de visibilidade dos pedidos para clientes.

O projeto demonstra conhecimentos avançados em:

Interfaces modernas com Flet
Integração com banco de dados PostgreSQL
CRUD completo
Manipulação de eventos
Atualização dinâmica da interface
Sistemas administrativos em tempo real
🚀 Tecnologias Utilizadas
🐍 Python
🎨 Flet
🐘 PostgreSQL
🔌 Psycopg2
⚡ Programação Orientada a Eventos
🖥️ Interface Desktop
🎯 Objetivo do Projeto

Este sistema foi desenvolvido com o objetivo de praticar:

Desenvolvimento desktop moderno
Integração com banco de dados remoto
Atualização automática de pedidos
Manipulação de interfaces dinâmicas
Controle de estados
CRUD completo
Sistemas de gerenciamento comercial

O projeto simula um sistema real utilizado em restaurantes, lanchonetes e estabelecimentos de atendimento ao público.

📂 Estrutura do Projeto
📦 sistema-pedidos
 ┣ 📂 assets
 ┃ ┣ 📜 delete.webp
 ┃ ┣ 📜 negativo.webp
 ┃ ┗ 📜 positivo.webp
 ┣ 📜 tela.py
 ┗ 📜 README.md
⚙️ Funcionalidades

✅ Listagem de pedidos em tempo real
✅ Integração com PostgreSQL
✅ Atualização automática da interface
✅ Controle por mesas
✅ Sistema delivery
✅ Pedidos externos ("fora")
✅ Exclusão permanente de pedidos
✅ Remoção lógica de pedidos
✅ Controle de visibilidade para clientes
✅ Fechamento de conta por mesa
✅ Interface gráfica moderna
✅ Atualização dinâmica sem reiniciar sistema

🧠 Conceitos Aplicados

O projeto utiliza conceitos importantes do desenvolvimento Python moderno:

Programação orientada a eventos
Manipulação de banco de dados PostgreSQL
Interfaces reativas
Componentização
CRUD completo
Atualização dinâmica de estado
Eventos de clique
Persistência de dados
Controle de interface em tempo real
🗄️ Banco de Dados

O sistema utiliza PostgreSQL hospedado remotamente.

Tabela principal utilizada:

CREATE TABLE pedidos_mamae (
    id SERIAL PRIMARY KEY,
    numero_mesa VARCHAR(50),
    pedido TEXT,
    visivel BOOLEAN,
    is_delete BOOLEAN,
    valor NUMERIC
);
▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/SEU-USUARIO/seu-repositorio.git
2️⃣ Acesse a pasta do projeto
cd sistema-pedidos
3️⃣ Crie um ambiente virtual
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
4️⃣ Instale as dependências
pip install flet psycopg2
5️⃣ Execute o sistema
python tela.py

ou

flet run tela.py
💻 Funcionalidades da Interface
📋 Gerenciamento de Pedidos

O sistema exibe:

Pedidos ativos
Pedidos delivery
Pedidos externos
Pedidos por mesa
🔄 Atualização Automática

O sistema possui um switch para atualização automática dos pedidos diretamente do banco de dados.

👁️ Controle de Visibilidade

Permite ocultar ou exibir pedidos na tela do cliente através de um botão visual.

🗑️ Exclusão de Pedidos

Existem dois tipos de remoção:

Exclusão lógica (is_delete = True)
Exclusão permanente do banco
💰 Fechamento de Conta

O sistema calcula automaticamente:

Valor total por mesa
Encerramento de pedidos
Limpeza automática da interface
📸 Interface Inspirada
6
🏗️ Arquitetura do Projeto

A aplicação foi construída utilizando:

Interface reativa com Flet
Banco PostgreSQL remoto
Atualização dinâmica
Estrutura baseada em eventos
Componentes reutilizáveis

Fluxo principal:

Interface Flet
      ↓
Eventos do usuário
      ↓
Manipulação PostgreSQL
      ↓
Atualização dinâmica da interface
🔥 Possíveis Melhorias Futuras
 Sistema de autenticação
 Dashboard administrativo
 Relatórios financeiros
 Impressão automática
 Integração com API
 WebSocket para tempo real
 Docker
 Deploy em nuvem
 Tema dark mode
 Controle de usuários
🔒 Segurança

⚠️ O código atual possui credenciais do banco diretamente no arquivo Python.

O recomendado é utilizar variáveis de ambiente:

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

Isso melhora significativamente a segurança da aplicação.

📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

Desenvolvimento desktop moderno com Python
Integração com PostgreSQL
CRUD completo
Interfaces gráficas reativas
Manipulação de estados
Atualização automática de dados
Sistemas administrativos comerciais

Projetos desse tipo são amplamente utilizados em:

Restaurantes
Lanchonetes
Sistemas POS
Controle de pedidos
Gestão comercial
👨‍💻 Desenvolvedor

Desenvolvido por Sherlon Machado.

GitHub: https://github.com/SHERLON20/

LinkedIn: https://www.linkedin.com/in/sherlon-machado/
