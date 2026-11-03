---
content_hash: 96412d97b01b9c1ab47beea4eca28dece9595d849b7bc50ec3dd06e775f4f2f1
fetched_at: '2026-06-29T00:12:03.699307+00:00'
page_id: '912375825'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Tipo "24 - Total Guia FGTS Digital" tratativa
  da multa rescisória de diferença salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=912375825
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro - Tipo "24-Total Guia FGTS Digital" tratativa da multa rescisória de diferença salarial |
| País: | Brasil |
| Issue: | [DRHROTRM-12129](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12129) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2402.276
* 12.1.2406.235
* 12.1.2410.167
* 12.1.2502.100 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratar a geração do lançamento financeiro do tipo **"24-Total Guia FGTS Digital"** para que, quando houver diferença salarial apurada após o mês da rescisão de um funcionário demitido, o sistema não calcule a multa rescisória do FGTS sobre essa diferença.

## **04. SOLUÇÃO**

Foi implementado um tratamento no processo de geração do lançamento financeiro **"24 - Total Guia FGTS Digital"** para que, ao realizar um lançamento financeiro para um funcionário demitido após o mês da rescisão, o valor da multa rescisória sejacalculado com base no FGTS da diferença salarial.

## **05.****DOCUMENTAÇÃO**
