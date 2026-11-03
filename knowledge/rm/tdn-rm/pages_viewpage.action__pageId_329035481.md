---
content_hash: 5ce278d97b01d45a50424641c94aeed843ad9fdaad335c206ff86c33b2e0d06f
fetched_at: '2026-06-29T00:08:49.300559+00:00'
page_id: '329035481'
product: rm
source: tdn-rm
title: DT Exportação de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329035481
version: 8
---

# Exportação de Lançamentos Contábeis

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | **Educacional** |
| **Módulo:** | ****Gestão Contábil**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Módulo de exportação de Lançamentos Contábeis | CtbGeradorSaidasModule |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Layout do Gerador de Saídas | GenLayoutAction | |  |  | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Parâmetros para geração da exportação.* |
| **Ponto de Entrada:** | **Não se aplica*.* |
| **Tickets relacionados** | [1798883](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%221798883%22 "1798883"); [1550607](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%221550607%22 "1550607") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [CONTROLADORIA01-590](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-590) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | ***SQL Server e Oracle*.** |
| **Tabelas Utilizadas:** | ***Não se aplica.*** |
| **Sistema(s) Operacional(is):** | ***Windows*** |

## Descrição

Foi criado template no Gerador de Saídas para exportação dos lançamentos contábeis, bem como seus rateios e campos complementares conforme layout de Importação de Lançamentos Contábeis "<http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.LayoutImpLancamentoContabil.aspx>". O template criado no gerador é alimentado pelo Module "RM.Ctb.Exportacao.CtbGeradorSaidasModule".

**Procedimentos para exportação**

1 - Importar o layout de gerador de saídas "CTBLAY0003 - Exportacao Lançamento Contabil.TotvsGen" localizado na pasta 'ObjetosGerenciais'.

2 - Marcar os parâmetros para geração da exportação.

3 - Após a execução será gerado o arquivo .txt conforme o layout citado na descrição.
