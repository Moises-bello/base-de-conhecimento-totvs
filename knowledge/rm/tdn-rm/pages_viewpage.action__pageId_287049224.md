---
content_hash: 11b2d7f06a50d3c7f35fa87c4e509759e20c51ae996e2babe582514d28e36155
fetched_at: '2026-06-29T00:08:42.094379+00:00'
page_id: '287049224'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-679 DT - Assistente de Cotação na Visão de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287049224
version: 109
---

# ASSISTENTE DE COTAÇÃO NA VISÃO DE MOVIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **TOTVS Gestão de Estoque, Compras e Faturamento*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Assistente de Cotação.* | **CmpAssistenteCotacaoAction*.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Movimento*.* | *MovMovimentoAction.* | |  |  | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Movimentos | Compra/Venda - Outros Dados | Tipo do Movimento de Compra.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *Não se aplica.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *MATESTCNTFTOF01-679.* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Implementado o Assistente de Cotação a partir da Visão de Movimentos de Solicitação de Compras.

A partir de agora será possível selecionar os movimentos na visão e abrir uma cotação a partir dos mesmos, sem a necessidade de acessar diretamente a tela de cotação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.18.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Em **Gestão de Estoque, Compras e Faturamento,** acesse **Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Tipo de Movimento Utilizado na Cotação.**
2. Acesse os **parâmetros** do tipo de movimento em questão **| Etapa Compra/Venda - Outros Dados | Tipo do Movimento de Compra = Solicitação de Compras:**
3. Ao criar a cotação a partir da Visão de Movimentos, a **Coligada**, **Filial** e o **Tipo de Movimento** considerados serão as informações do próprio contexto.

****CONFIGURAÇÃO DE PERMISSÕES****

1. A permissão no perfil do usuário para permitir a criação de cotações a partir do movimento de Solicitação de Compras é a mesma utilizada no processo de Assistente da Cotação a partir da Visão de Cotações.
2. Para isso acesse o **Cadastro de Perfil do Usuário** | Aba **Acesso a Menus** | **03 Compras** | **03.01 Gestão de Compras** | **03.01.02 Cotação** | **03.01.02.01 Inserir Cotação**:

## Procedimento para Utilização

1. Na Visão de Movimentos, selecione as **Solicitações de Compra** que terão os itens participando do processo de cotação | **Processos** | **Assistente de Cotação**:
2. Os produtos serão apresentados conforme seleção realizada na visão de movimentos e parametrização vigente:

## Documentos de Referência

* [Item Não Exibido Na Cotação](http://tdn.totvs.com/display/LRM/COT0003_Item_Nao_Exibido_Na_Cotacao)
* [Aprovação de Movimentos na Solicitação de Compras](http://tdn.totvs.com/pages/viewpage.action?pageId=4812992)

divs
