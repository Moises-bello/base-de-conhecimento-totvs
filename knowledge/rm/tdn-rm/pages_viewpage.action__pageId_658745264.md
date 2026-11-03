---
content_hash: 133e776f269a138c142b89775bb93d78f4248e9f35374223ddb63ffd0979cb51
fetched_at: '2026-06-29T00:11:13.347338+00:00'
page_id: '658745264'
product: rm
source: tdn-rm
title: FISCAL01-16863 - DT - Código da receita nas guias de imposto de importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=658745264
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Escrituração |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16863 |

## **02. SITUAÇÃO/REQUISITO**

Ao escriturar um movimento de entrada o código de receita não é carregado, para tributos de importação.

TESTES REALIZADOS

Em base exemplo foi incluído um Movimento de Entrada com o Tributo PIS Importação.

Na parametrização do movimento foi informado código de receita cadastrado no sistema e ao incluir o movimento, o mesmo foi carregado.

Ao escriturar a nota, o código de receita não é apresentado na aba Outros Tributos do lançamento, e com isso, ao gerar a guia do tributo, a mesma fica sem o Código de Receita informado.

O mesmo problema ocorre para os Tributos COFINS Importação, IRRF Importação.

## **03. SOLUÇÃO**

Foi acrescentado, na regra de preenchimento do código da Receita do lançamento, no processo de escrituração, mais três tipos de tributo:

* PIS Importação;
* COFINS Importação;
* IRRF Importação.
