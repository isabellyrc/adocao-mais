# 🐾 Adoção+ – Sistema de Gestão de Centro de Adoção de Animais

Bem-vindo ao **Adoção+**, um sistema em Python focado em facilitar o gerenciamento de abrigos de animais! Com uma interface amigável via terminal, o sistema centraliza o cadastro de pets, cruza perfis de adotantes com animais compatíveis (Matching), gerencia tarefas do dia a dia (banhos, vacinas) e oferece sugestões inteligentes de cuidados.

---

## 📌 Funcionalidades Principais

*   **🐶 Gestão de Animais (CRUD):** Cadastre, consulte, edite e remova animais do sistema.
*   **❤️ Matching de Adoção:** Um algoritmo que calcula uma pontuação de compatibilidade entre o perfil do adotante e os animais disponíveis.
*   **⏰ Tarefas e Alertas:** Controle de rotinas (vacinas, consultas, banhos, treinos) com cálculo de contagem regressiva e alertas de datas próximas.
*   **💡 Sugestões Inteligentes:** Dicas de cuidados geradas automaticamente de acordo com a espécie, idade e comportamento do animal.
*   **💾 Persistência de Dados:** Os dados são salvos de forma segura em arquivos `.csv`, garantindo que nenhuma informação seja perdida ao fechar o sistema.

---

## 🚀 Manual do Usuário

### Pré-requisitos
*   **Python 3.x** instalado em sua máquina.

### Como Executar o Sistema
1. Abra o seu terminal.
2. Navegue até a pasta do projeto:
   ```bash
   cd caminho/para/adocao-mais
   ```
3. Execute o arquivo principal da interface:
   ```bash
   python interface.py
   ```
*(Nota: O arquivo principal que gerencia o menu e a execução inicial está nomeado como `interface.py`).*

### Navegando pelos Menus
Ao iniciar o programa, você será recebido por um Menu Geral intuitivo:
*   **1 - Menu de Animais:** Para inserir novos pets que chegaram ao abrigo ou gerenciar os já existentes.
*   **2 - Menu de Matching:** Para cadastrar o perfil de uma pessoa interessada em adotar e descobrir quais animais dão o "match" perfeito com o estilo de vida dela.
*   **3 - Menu de Sugestões:** Receba dicas automáticas de como cuidar de um animal específico da sua base de dados (Ex: Filhotes precisam de mais atenção).
*   **4 - Menu de Tarefas:** Acesse para cadastrar ou verificar pendências como "Vacina em 3 dias".
*   **0 - Sair:** Encerra a aplicação e salva todos os dados em CSV automaticamente.

---

## 🏗 Estrutura do Projeto

A arquitetura foi dividida em módulos para facilitar o desenvolvimento em equipe, evitar conflitos e deixar o código limpo:

```text
adocao-mais/
│
├── interface.py       # Arquivo principal (Menus, fluxos e inicialização)
├── crud_animais.py    # Lógica de Cadastro, Edição, Consulta e Exclusão de animais
├── tarefas.py         # Gerenciamento de alertas e atividades diárias (vacinas, etc)
├── arquivos.py        # Centraliza a leitura e gravação dos arquivos CSV
├── matching.py        # Algoritmo de cruzamento de perfis (Adotante x Animal)
├── sugestoes.py       # Regras automáticas para dicas de cuidados
├── validacao.py       # Validações globais (idade negativa, campos vazios, etc)
│
├── dados/             # Pasta gerada automaticamente pelo sistema
│   ├── animais.csv
│   ├── tarefas.csv
│   └── adotantes.csv
│
└── README.md          # Esta documentação
```

---

## 👥 Divisão Oficial de Responsabilidades (Equipe)

O projeto foi construído por 6 integrantes, onde cada um focou no desenvolvimento de um módulo específico, integrado de forma coesa através de funções.

| Integrante | Responsabilidade Principal | Arquivo(s) Base |
| :--- | :--- | :--- |
| **Isabelly Ribeiro** | CRUD de Animais | `crud_animais.py` |
| **Heitor Torres** | Persistência de Dados (CSV) | `arquivos.py` |
| **Yasmin Lopes** | Matching de Adoção & Integração | `matching.py` |
| **Miguel Cabral** | Interface (Menus), UX e Documentação | `interface.py`, `README.md` |
| **Leandro Henrique** | Gerenciamento de Tarefas e Alertas | `tarefas.py` |
| **Maria Carolina** | Sugestões Inteligentes e Validações | `sugestoes.py`, `validacao.py` |

---

## 🔧 Estratégia de Desenvolvimento (Git & GitHub)

Para garantir a colaboração sem atritos, a equipe seguiu um fluxo estrito de controle de versão:
1. **Módulos Separados:** Cada programador atuou no seu próprio arquivo, importando as funcionalidades quando necessário (Ex: `from crud_animais import listar_animais`).
2. **Branching Model:** 
   * `main`: Produção / Entrega Final (Apenas código 100% testado).
   * `develop`: Branch de integração da equipe.
   * `feature/*`: Branches individuais de cada funcionalidade.
3. **Regra de Ouro:** Ninguém comita direto na `main` ou `develop`. O fluxo utilizado foi criar a branch funcional, desenvolver as alterações e abrir um **Pull Request (PR)** para a `develop`.
