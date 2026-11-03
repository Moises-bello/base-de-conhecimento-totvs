---
content_hash: 43ba83abbb30fcf76795b2bc81c0209f4160643fefc4918e462c2e2718f41632
fetched_at: '2026-06-29T00:12:08.495774+00:00'
page_id: '937245717'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Envio da Matricula Anterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=937245717
version: 3
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Envio da Matricula Anterior |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11906](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11906 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.264
* 12.1.2410.215
* 12.1.2502.133

## **03. SITUAÇÃO/REQUISITO**

Na integração entre o TOTVS Folha de Pagamento e o produto Ponto Web da Ahgora, quando houver uma transferência de funcionário, o sistema deverá enviar tanto a matrícula atual quanto a matrícula anterior no primeiro envio. Nos envios subsequentes, a matrícula anterior não será mais enviada.

## **04. SOLUÇÃO**

Realizamos uma tratativa no produto para garantir que a tag de matrícula anterior, após o primeiro envio do funcionário transferido, não será mais enviada nos envios subsequentes

## **05. DEMAIS INFORMAÇÕES**

**[Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=877866931)**

**[Integração RM X Ahgora - API Resultados - Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=867812432)**
