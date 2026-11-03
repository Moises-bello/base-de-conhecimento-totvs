---
content_hash: e65b3e67a5a7fbd78b27575b40ae14638a81e552f1cc7407e7063e6a446d9c07
fetched_at: '2026-06-29T00:08:08.509175+00:00'
page_id: '238038512'
product: rm
source: tdn-rm
title: ER_CPMOV001-7_Visualizacao_Cadastros_Utilizados_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPMOV001-7_Visualizacao_Cadastros_Utilizados_Cotacao
version: 129
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_CP\_MOV 2016/2017 | **IRM1** | CPMOV001-4 |
| **Requisito1** | CPMOV001-7 | **Subtarefa1** | Não se aplica |
| **Chamado2** | Não se aplica. | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Não se aplica. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Revitalização do módulo de compras baseado nos levantamentos feitos através do projeto de UX, visando melhorar a usabilidade e experiência do usuário. 

## Definição da Regra de Negócio

Neste release, elencamos os seguintes itens para a segunda fase do processo de revitalização do módulo de compras.

* ## Disponibilizar os botão "maximizar" nas telas de Orçamento e Registro de Orçamento/Negociação.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, ao abrir a tela de uma cotação haverá a opção de maximizar a tela. Nesta mesma tela, na aba **Orçamentos** existem duas opções, **Registrar Orçamento** e **Registrar Negociação**, em que é aberta um tela para registro. Nesta tela de registro haverá a opção de maximizar a tela, para que se tenha uma melhor visualização dos itens de orçamento.

* ## Permitir acessar o cadastro de Produto através da Cotação.

**Desejo:** como usuário do processo de compras, eu quero acessar as informações de Produto através da Cotação.

As informações dos Produtos que participam do processo de compras poderão ser acessadas através da Cotação quando forem utilizadas as rotinas **Registrar Orçamento**, **Registrar Negociação**, **Item de Movimento** e **Assistente de Inclusão de Cotação.**

### **Registrar Orçamento**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Editar** é apresentada a janela de **Cotação.** Na pasta **Orçamentos**, clique no botão **Registrar Orçamento** e acesse a pasta **Produtos**. Para visualizar as informações do Produto, clique no link do campo **Descrição Produto.**

### **Registrar Negociação**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Editar** é apresentada a janela de **Cotação.** Na pasta **Orçamentos**, clique no botão **Registrar Negociação**e acesse a pasta **Produtos**. Para visualizar as informações do Produto, clique no link do campo **Descrição Produto.**

### **Item de Movimento**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Editar** é apresentada a janela de **Cotação.** Na pasta **Itens de Movimento** também será possível visualizar as informações do Produto clicando no link disponível no campo **Descrição Produto.**

### **Assistente de Inclusão**

**Desejo:** como usuário do processo de compras, eu quero acessar as informações de Produto no Assistente de Inclusão da Cotação.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Incluir** é apresentado o **Assistente de Cotação.** No passo **Filtro de Produto,** em que serão escolhidos os produtos necessários para realizar a cotação, será possível visualizar as informações do Produto, bastando para isso clicar no link disponível no campo **Descrição Produto.**

### **Inclusão de novos Itens na Cotação**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Inserir Itens na Cotação,** é apresentada a janela de **Inserção de Itens na Cotação.** No passo que seleciona os **Itens de Movimento** também será possível visualizar as informações do Produto ao clicar no link disponível no campo **Descrição Produto.**

* ## Permitir acessar o cadastro da Filial através da Cotação.

Como um usuário do processo de compras, eu quero acessar as informações da Filial no cadastro de Cotação. Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e abrir uma cotação, na pasta **Itens de Movimento** existe o recurso **Definição das Actions Associadas da Visão.** Através deste recurso pode ser associado o acesso ao cadastro da **Filial**. Para isso devem ser feitos os seguintes procedimentos:

1. Na tela **Definição das Actions Associadas da Visão** clicar no botão Adicionar
2. Na tela **Pesquisar** informar o nome da action de Filial: **FisFilialAction**
3. Definir a **Chave de Execução da Ação** informando no campo **Coluna** o valor referente à **Chave**, sendo que para a chave CODCOLGIADA selecionar a coluna **Coligada Mov.** e para a chave CODFILIAL selecionar a coluna **Cod. Filial Mov. Origem**.
4. Para acessar os dados da Filial, clique com o botão direito do mouse sobre a visão de Itens de Movimento e acesse **Ações Associadas \ Filial.**

* ## Permitir o acesso e cadastro do fornecedor através da cotação.

### **Cotação**

* Ao acessar ****Gestão de Estoque, Compras e Faturamento | Compras | Cotação**,** ao editar uma cotação é apresentada a janela de **Cotação**. Nesta tela, as abas **Orçamentos** e **Itens de Movimento** foram padronizadas, apresentando a barra de recursos. Dessa forma, ao clicar no botão **Incluir Fornecedor na Cotação,** na aba **Orçamentos**, na tela que será apresentada haverá a possibilidade de cadastro de um novo fornecedor, clicando no botão **Incluir**.

### **Orçamentos**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, ao editar uma cotação, na pasta **Orçamentos** existe o recurso de **Definição das Actions Associadas da Visão.** Através deste recurso pode ser associado o acesso ao cadastro de **Fornecedor** realizando os seguintes procedimentos:

1. Na tela **Definição das Actions Associadas da Visão** clicar no botão **Adicionar**
2. Na tela Pesquisar informar o nome da action de Fornecedor: **FinCFOAction**.
3. Definir a **Chave de Execução da Ação** informando no campo **Coluna** o valor referente à **Chave**, sendo que para a chave CODCOLIGADA selecionar a coluna CODCOLCFO e para a chave CODCFO selecionar a coluna Fornecedor.
4. Para acessar os dados do **Fornecedor**clique com o botão direito do mouse sobre a visão de **Orçamentos** e acesse **Ações Associadas \ Cliente/Fornecedor**.

**Inclusão de Cotação**

* Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e incluir uma nova cotação, na etapa de **Escolha de fornecedores**, ao clicar no botão **Incluir**, na janela que será apresentada haverá a possibilidade de cadastro de um novo fornecedor ao clicar no botão **Incluir**. Será possível também a edição de cadastro de fornecedor ao clicar no botão **Editar**.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
