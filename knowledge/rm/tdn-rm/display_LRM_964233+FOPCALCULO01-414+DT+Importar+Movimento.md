---
content_hash: 8cfc7798b54963446b88edfcb805b7a4d150f8d1411e525732be1a5c03863ff2
fetched_at: '2026-06-29T00:08:36.894222+00:00'
page_id: '284480836'
product: rm
source: tdn-rm
title: 964233 FOPCALCULO01-414 DT Importar Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/964233+FOPCALCULO01-414+DT+Importar+Movimento
version: 100
---

# Folha Mensal - Importação do Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Importação do Movimento |
| **Situação/Requisito:** | Erro ao realizar o processo de Importar Movimento : Arithmetic overflow error converting expression to data type smallint  Processo: Aba Folha Mensal > Importação > Importação do Movimento    O mesmo ocorre no seguinte contexto:   * O evento utilizado for do tipo HORA * A posição para Hora no layout estiver zerada * A posição para Referência no layout estiver preenchida (Obs: Onde a referência será transformado em Horas) * Utilizar a Ação SOMAR na importação * E a soma de Horas Ultrapassar o limite de 546:07hs |
| **Solução/Implementação:** | Ajuste realizado para validação da quantidade de horas a ser importada, esta validação ja ocorre no cadastro e não ocorria na processo de importação de movimento  Layout para arquivo de importação:   <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ImportacaoMovimento.aspx> |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 964233 |
| **Requisito:** |  |

divs
