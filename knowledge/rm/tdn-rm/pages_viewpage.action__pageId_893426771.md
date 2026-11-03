---
content_hash: f0f273b83637147e99e64c725e4bde712a500dc7d99dd1f11f6b8312b072553a
fetched_at: '2026-06-29T00:12:01.334377+00:00'
page_id: '893426771'
product: rm
source: tdn-rm
title: DT - S-1200 - Tratar código de cálculo 371 na geração Anual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=893426771
version: 3
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1200 - Tratar código de cálculo 371 na geração Anual |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8716](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8716 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.249
* 12.1.2406.195
* 12.1.2410.127 e superiores

## **03. SITUAÇÃO/REQUISITO**

Na geração do XML do evento **S-1200,**  quando um funcionário possui apenas o lançamento de 13º sobre o salário-maternidade (evento **371 - Segunda Parcela 13º Licença Maternidade Provento**), o sistema está gerando como mensal em vez de anual.

## **04. SOLUÇÃO**

Foi tratada a geração do evento **S-1200** para considerar o envelope de pagamento como anual quando o funcionário tiver o lançamento de verba referente ao 13º salário com o código de cálculo **371 - Segunda Parcela 13º Licença Maternidade Provento**.

Essa correção garante que o evento seja gerado corretamente, conforme o regime anual aplicável a esse tipo de lançamento.

## **05. DEMAIS INFORMAÇÕES**
