---
content_hash: 37e0dcba5b99cdd66fef9f4ef32e5ff0313992b35fa09a7c68b6b63a79b55c94
fetched_at: '2026-06-29T00:08:11.425846+00:00'
page_id: '242392508'
product: rm
source: tdn-rm
title: DT_CPMOV001-7_Visualizar_Cadastros_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-7_Visualizar_Cadastros_Cotacao
version: 112
---

# VISUALIZAR CADASTROS UTILIZADOS NA COTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Gestão de Compras.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cotação | CmpCotacaoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Produto | EstPrdAction | | Cliente/Fornecedor | FinCFOAction | | Filial | FisFilialAction | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica* |
| **Requisito (ISSUE):** | *CPMOV001-7* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

Revitalização do módulo de compras baseado nos levantamentos feitos através do projeto de *Design Thinking* (UX), visando melhorar a usabilidade e experiência do usuário.

Será permitido ao usuário módulo de Compras acessar informações de alguns cadastros durante o processo de Cotação para que ele possa obter maiores informações das solicitações de compras, produtos e fornecedores entre outras informações.

As melhorias implementadas são:

* Nas rotinas de **Registrar Orçamento e Registrar Negociação** foi disponibilizado a opção de **Maximizar** a tela. Ao acessar estas funcionalidades ela será exibida maximizada para melhor visualização dos dados.
* Permitir acessar o cadastro de **Produto** através da Cotação nos seguintes pontos:

  + Pasta **Produto** em **Registrar Orçamento**;
  + Pasta **Produto** em **Registrar Negociação**;
  + Pasta **Item de Movimento** na janela de edição da **Cotação**;
  + **Assistente de Inclusão da Cotação** passo **Filtro de Produtos**;
  + Processo de **Inclusão de novos Itens na Cotação** passo ****Inserção de Itens na Cotação;****
* Permitir acessar o cadastro da **Filial** através da Cotação. Para este item consulte o tópico abaixo Procedimento para Utilização.
* Permitir o acesso e cadastro do **Fornecedor** através da cotação nos seguintes pontos:

  + **Assistente de Inclusão da Cotação** passo **Escolha de Fornecedores** e **Escolha de Fornecedores - Qualificação**;
  + Pasta **Orçamentos**ao clicar no botão **Incluir Fornecedor na Cotação** será permitido cadastrar um novo fornecedor, clicando no botão **Incluir**. Além disso pode-se também utilizar o recurso de **Ações Associadas** que será detalhada no tópico Procedimento para utilização.
* Na janela de edição da **Cotação** as pastas **Orçamentos** e **Itens de Movimento** foram padronizadas, apresentando a barra de recursos.

Para obter maiores detalhes acesse a .

## Procedimento para Utilização

Os cadastros disponibilizados, podem ser acessados também através da funcionalidade **Ações Associadas**que fica localizada na barra de recursos. Como exemplo de utilização iremos descrever abaixo uma ação relacionada para acessar o cadastro de Fornecedor.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, ao editar uma cotação, na pasta **Orçamentos** existe o recurso de **Definição das Actions Associadas da Visão.** Através deste recurso pode ser associado o acesso ao cadastro de **Fornecedor** realizando os seguintes procedimentos:

1. Na tela **Definição das Actions Associadas da Visão** clicar no botão **Adicionar**
2. Na tela Pesquisar informar o nome da action de Fornecedor: **FinCFOAction**.
3. Definir a **Chave de Execução da Ação** informando no campo **Coluna** o valor referente à **Chave**, sendo que para a chave CODCOLIGADA selecionar a coluna CODCOLCFO e para a chave CODCFO selecionar a coluna Fornecedor.
4. Para acessar os dados do **Fornecedor**clique com o botão direito do mouse sobre a visão de **Orçamentos** e acesse **Ações Associadas \ Cliente/Fornecedor**.

divs
