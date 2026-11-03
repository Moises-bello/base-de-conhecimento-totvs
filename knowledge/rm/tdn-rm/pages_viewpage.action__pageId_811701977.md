---
content_hash: 60899fdb2a7f05f9a729e18636c339b3d5253658ca7196b45741ce68cfef23e4
fetched_at: '2026-06-29T00:11:44.241952+00:00'
page_id: '811701977'
product: rm
source: tdn-rm
title: DT - S-1210 - Possibilitar a geração do XML quando o valor da assistência médica
  for zero
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=811701977
version: 7
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1210 - Possibilitar a geração do XML quando o valor da assistência médica for zero |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8190](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8190) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2302.242
* 12.1.2306.189
* 12.1.2310.123

## **03. SITUAÇÃO/REQUISITO**

Gerar o XML do evento S-1210, permitindo sua criação sem o preenchimento do grupo <planSaude> quando o valor da assistência médica for zero no envelope de pagamento.

## **04. SOLUÇÃO**

Aprimoramento na geração do XML do evento S-1210 para não considerar o preenchimento do grupo <planSaude> quando o valor da assistência médica for zerado no envelope de pagamento.

## **05.****ASSUNTOS RELACIONADOS**
