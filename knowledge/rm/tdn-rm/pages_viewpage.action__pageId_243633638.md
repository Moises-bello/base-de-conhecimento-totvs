---
content_hash: a531fef84a175493e2a7f4a663f34903e1e450ca226baf389f53b62ad912b833
fetched_at: '2026-06-29T00:08:12.017556+00:00'
page_id: '243633638'
product: rm
source: tdn-rm
title: DT_CPMOV001-357_Registrar_Orçamento_Negociação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243633638
version: 118
---

# REGISTRAR ORÇAMENTO E REGISTRAR NEGOCIAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos;.* |
| **Módulo:** | **Gestão de Compras*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Registrar Orçamento* | *Não se aplica.* | | *Registrar Negociação* | *Não se aplica.* | |
| **Cadastros Iniciais:** | ****Registrar Orçamento:** o **Status da Cotação** deve ser igual a **Aguardando Resposta Fornecedores**.**  ***Registrar Negociação:** o **Status da Cotação** deve ser igual a **Negociação da Melhor Oferta**.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *PCREQ-9558 e CPMOV001-357* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *TCITMORCAMENTO - Itens de Orçamento.* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

**Registrar Orçamento**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para **Registrar Orçamentos**foi realizado a seguinte melhoria:

* Não será permitido editar informações nos campos: **Unidade Solicitada, Coligada Movimento, Código e Descrição do Produto e Quantidade Solicitada e Orçada.**
* Os campos **Percentual e Valor de Desconto e Despesa** que são habilitados por parâmetro da Cotação terão o mesmo comportamento quando não se permitir a edição.
* O processo de **Incrementar Preço Cotado** teve seu nome alterado para **Alterar Preço Cotado.** Seu comportamento foi alterado para permitir diminuir o valor cotado informando valor ou percentual negativo.

**Registrar Negociação**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para **Registrar Negociação** foi realizado a seguinte melhoria:

* Não será permitido editar informações nos campos: **Preço Cotado, Unidade Solicitada, Unidade Orçada, Prazo Entrega, Coligada Movimento, Código e Descrição do Produto, Quantidade Solicitada, Quantidade Orçada e Negociada, % ICMS Orçado, %ICMSST e Margem de Lucro ICMS ST.**Estes campos ficarão esmaecidos (aspecto acinzentado).
* Os campos de **Percentual e Valor de Desconto e Despesa** que são habilitados por parâmetro da Cotação terão o mesmo comportamento quando não se permitir a edição.
* O processo de **Incrementar Preço Negociado** teve seu nome alterado para **Alterar Preço Negociado.** Seu comportamento foi alterado para permitir diminuir o valor negociado informando valor ou percentual negativo.

divs
