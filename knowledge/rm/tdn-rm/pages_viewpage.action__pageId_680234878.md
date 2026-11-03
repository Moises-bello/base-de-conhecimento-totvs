---
content_hash: 390389744d6e5f589ee7930a391e3c9b1debd7a218952b8ea87f62d491cc7388
fetched_at: '2026-06-29T00:11:17.404915+00:00'
page_id: '680234878'
product: rm
source: tdn-rm
title: Ambientes.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680234878
version: 58
---

## O que é?

Um Ambiente é uma configuração essencial que direciona a execução de seu Projeto de Testes para uma versão específica do RM. Cada versão do RM requer a criação de um Ambiente correspondente. Além disso, é possível utilizar propriedades customizáveis dentro dos Ambientes, que irão substituir os seus valores dinamicamente, promovendo a reutilização de atividades em diferentes ambientes do RM.

## Para que serve?

Ele serve para:

* Definir diferentes versões do RM para testes.
* Utilizar propriedades customizáveis para montar caminhos de diretórios dinamicamente e substituir parâmetros em diversas atividades com variáveis de ambiente.

## Exemplo de Uso

Como cadastrarComo Cadastrar 1. Início de Cadastro 

1. Navegue no menu do TOTVS Automação de Testes e clique em **Ambientes.**

       2. Na tabela que será mostrada, clique no botão verde em destaque para adicionar ambiente.

2. Preenchimento dos Campos3. Nome de exibição

Aqui você deverá atribuir um nome para identificar sua atividade de ambiente.

4. Permissões de Grupos

Grupos no TOTVS Automação de Testes organizam e controlam o acesso dos usuários aos **ambientes**,garantindo que cada usuário acesse apenas os ambientes pertinentes ao seu papel ou projeto. Adicione um grupo ao seu ambiente para gerenciar essas permissões de forma eficiente.

(Saiba mais sobre o que são os [Grupos](https://tdn.totvs.com/display/LRM/6+-+Grupos) no TOTVS Automação de Testes.)

5. Credencial de Banco de dados padrão do Ambiente

Ao associar uma Credencial de Banco de Dados ao Ambiente, caso não exista nenhuma conexão criada no contexto durante a execução do projeto, as atividades que dependem de conexão por contexto utilizarão automaticamente a credencial definida neste campo.

* Selecione uma [Credencial de Banco de Dados](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados) existente.

6. Diretório

Aqui você deverá informar o diretório do RM referente a um determinado ambiente. Por exemplo:

* + - Para um ambiente que se refere à versão de desenvolvimento do RM, o diretório deve ser: C:\RM\Atual\Release\Bin
    - Para um ambiente que se refere a uma versão legado do RM, o diretório deve ser:  C:\RM\Legado\{versão}\Bin. Exemplo: C:\RM\Legado\12.1.2404\Bin

7. Propriedades customizáveis

É recomendado usar as Propriedades customizadas no TOTVS Automação de Testes, pois elas permitem ajustes específicos por **ambiente**, centralizando configurações, melhorando a manutenção, automação e segurança, além de evitar conflitos entre versões.

**Chave**: A chave é o identificador único da propriedade customizada.

* Por exemplo: **Versao**

Escreva o nome da Propriedade Customizada de forma natural, sem nenhum tipo de caractere especial. **Ex:** **{** , **}**, **\***, **&**, etc... 

**Valor:** O valor é a informação atribuída à chave, que será usada durante a execução.

* Por exemplo: **12.1.2510**

É possível excluir uma propriedade clicando no botão destacado.

Para excluir todas, clique aqui:

Variáveis de ambiente

Variáveis de ambiente são parâmetros dinâmicos configuráveis para diferentes ambientes, permitindo que uma atividade seja executada em várias versões do RM sem modificações diretas. Elas definem valores que ajustam a execução de atividades conforme a versão especifica do RM, gerando caminhos de diretórios ou outros parâmetros de forma dinâmica e automatizada.

Sendo assim, podemos ter:

Parâmetros de Atividade

Para cada atividade, existe uma lista de parâmetros que podem ser substituídos pelas variáveis configuradas. Utilizando variáveis de ambiente, a manutenção dessas atividades torna-se mais fácil.

* + - [Soap](https://tdn.totvs.com/pages/viewpage.action?pageId=842285169): Parâmetros como: ***Uri (Wsdl), Soap Endpoint, Descrição, Soap Action, Envelope, Usuário, Senha, Domínio***.
    - [Script SQL](https://tdn.totvs.com/pages/viewpage.action?pageId=842287134): Parâmetros como: ***ConnectionString e Script SQL***.
    - [HTTP](https://tdn.totvs.com/pages/viewpage.action?pageId=842289210): Parâmetros como: ***Descrição, Usuário, Senha, Headers, Body, Queries, Cookies*.**
    - [Comparação de Diretório](https://tdn.totvs.com/pages/editpage.action?pageId=863911900): Parâmetros como: ***Padrão de busca de arquivos, Caminho do diretório da esquerda, Caminho do diretório da direita.***
    - [Comparação de Banco](https://tdn.totvs.com/pages/viewpage.action?pageId=863909804): Parâmetros como: ***ConnectionString e Script SQL***.
    - [Restauração de Banco](https://tdn.totvs.com/pages/viewpage.action?pageId=873219509): Parâmetros como: ***Caminho do Arquivo de Backup.***
    - [Comparação de Arquivo:](https://tdn.totvs.com/pages/viewpage.action?pageId=864995980) Parâmetros como: ***Caminho do diretório da esquerda, Caminho do diretório da direita.***
    - [Script WinForms](https://tdn.totvs.com/pages/viewpage.action?pageId=874592146)[:](https://tdn.totvs.com/pages/viewpage.action?pageId=874592146) Parâmetros como: ***Ações de Texto.***
Exemplo prático

Imagine que você precisa realizar uma atividade de restauração de base de dados, utilizando um servidor que guarda todos os backups das bases do RM em um mesmo diretório. A única diferença entre os backups é o nome do arquivo, que se diferem pelo acréscimo da sua versão referente ao final. Você deve executar um projeto de teste que utiliza essa atividade para duas versões diferentes do RM: 12.1.2406 e 12.1.2404. Para evitar a criação de duas atividades praticamente idênticas, você pode configurar dois ambientes distintos: um para a versão 12.1.2406 e outro para a versão 12.1.2404, e definir uma variável para gerenciar essa diferença.

**Exemplo:**

Ambiente da 12.1.2404

Ambiente da 12.1.2406

Agora, você pode criar a atividade de forma que o parâmetro de versão seja preenchido dinamicamente conforme o ambiente escolhido, no momento da execução.

Para uma variável ser utilizada corretamente ela deve está entre chaves simples.

**Exemplo: {Versao}**

Assim, ao executar a atividade, você poderá selecionar o ambiente desejado e o parâmetro de versão será automaticamente substituído pela versão correspondente ao ambiente escolhido.

---

# Saiba mais

Propriedades customizadas permitem que você experimente diferentes configurações rapidamente, ajudando a otimizar o desempenho e identificar a melhor configuração para cada cenário.

Um ambiente não pode ser excluído enquanto o Agendamento assimilado estiver ativo.

É obrigatório definir o caminho do diretório para que o ambiente seja criado.

Centralizar configurações e usar variáveis de ambiente reduz a probabilidade de erros de configuração. Isso também reduz o número de atividades a serem criadas.

# FAQ

**P: O que é um Ambiente?**  
R: É através de um Ambiente que você direciona a execução de seu Projeto de Testes para uma versão específica do RM.

**P: Quantos Ambientes devo incluir?**

R: Deve ser incluído um Ambiente para cada versão do RM que você deseja testar.

**P: Posso usar propriedades customizáveis?**  
R: Sim, você pode se utilizar das propriedades customizáveis para montar, por exemplo, caminhos de diretórios dinamicamente.

**P: O que acontece se eu definir uma propriedade customizável com o valor ou chave nula?**

R: Não será permitido a criação desse ambiente.

**P: O que acontece se eu não definir o caminho do diretório?**  
R: Não será permitido a criação desse ambiente
