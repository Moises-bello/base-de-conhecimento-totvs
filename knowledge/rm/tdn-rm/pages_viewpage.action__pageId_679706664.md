---
content_hash: d56ef0936df21a14684a5e78e92a5a0056dce4f3fb8a3da1f7faaec3129b6742
fetched_at: '2026-06-29T00:11:17.370196+00:00'
page_id: '679706664'
product: rm
source: tdn-rm
title: 13776688 FISCAL01-17774 - DT - Código Variação Tributo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679706664
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais |
| País: | Brasil |
| Ticket: | [13776688](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2213776688%22 "13776688") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17774 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a rotina DCTF, registro R10 do tributo IRRF PJ, o campo 7 (Código da Receita) não é gerado com o Código Oficial disponível no cadastro do código de Receita, e sim com o valor do campo código:

## **03. SOLUÇÃO**

Foi ajustado o campo 7 do registro R10 ( e nos registros que usam código de receita), passa-se a utilizar o Código Oficial quando há Variação do Código de Receita cadastrada.

Disponível a partir da versão 12.1.34
