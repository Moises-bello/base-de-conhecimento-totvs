---
content_hash: 990450d0e28c3e913677910bc346c172cdc137d4633ce1b335d4434852e20980
fetched_at: '2026-06-29T00:08:12.025549+00:00'
page_id: '243633878'
product: rm
source: tdn-rm
title: DT_CPMOV001-357_Movimento_Rastreabilidade_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-357_Movimento_Rastreabilidade_Cotacao
version: 112
---

# EDIÇÃO DE SOLICITAÇÃO DE COMPRA E EDIÇÃO DA COTAÇÃO NA RASTREABILIDADE DE MOVIMENTOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Proejtos.* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Rastreabilidade de Movimentos* | *MovRastreabilidadeAction* | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *PCREQ-9558 e CPMOV001-357* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

**Edição de Movimentos na Cotação**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para visualizar a aba de Itens de Movimento no clique duplo na Grid no Item de Movimento será exibido o Movimento associado ao mesmo, tanto para Solicitação de Compra quanto para Ordem de Compra. No anexo de Itens de Movimento será possível visualizar o movimento associado, portanto, não sendo necessário editar a cotação.

**Edição da Cotação em Rastreabilidade de Movimentos**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Solicitação de Compras**e visualizar a rastreabilidade do movimento que originou a cotação no clique duplo da Grid será exibida a Cotação.

## Procedimento para Utilização

**Edição de Movimentos na Cotação**

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.  
   O sistema apresenta a janela de **Filtros - Cotação - Composição.**
2. Selecione uma opção de filtro e clique em Executar.
3. Na visão de Cotação selecione uma Cotação clique em **Editar**.  
   O sistema apresenta a janela **Cotação:...**
4. Na pasta **Itens de Movimento** clique duas vezes sobre uma linha da grid.  
   O sistema apresenta a janela de edição Movimentos - Solicitação de Compra.

**Edição da Cotação em Rastreabilidade de Movimentos**

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Solicitação de Compra**.  
   O sistema apresenta a janela de **Solicitação de Compras (Gestão de Compras).**
2. Informe o **Tipo de Movimento** e clique em **OK**.  
   O sistema apresenta a janela de **Filtros - Solicitação de Compras (Gestão de Compras).** Selecione um opção e clique em **Executar.**
3. Na visão de Movimentos selecione um registro e clique em **Rastreamento de movimentos**.  
   O sistema apresenta a janela **Rastreabilidade.**
4. Na pasta **Cotação** clique duas vezes sobre o registro da Cotação.  
   O sistema apresenta a janela de edição Cotação.

divs
