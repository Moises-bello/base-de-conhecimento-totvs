---
content_hash: 21d98fa2cf921550db2f74ba9665f512b4fcec8a35a0aada6e60cd460e013cfd
fetched_at: '2026-06-29T00:12:08.012570+00:00'
page_id: '927561882'
product: rm
source: tdn-rm
title: DT - Informações do Local de Trabalho nos eventos S-2200, 2206, 2300 e 2306
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=927561882
version: 12
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Informações do Local de Trabalho nos eventos S-2200, 2206, 2300 e 2306 |
| País: | Brasil |
| Issue: | [DRHROTRM-12754](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12754) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.256
* 12.1.2410.199
* 12.1.2502.120 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ajustar a geração dos eventos S-2200, 2206, 2300 e 2306 para que, quando o funcionário estiver alocado em um único tomador de serviço, e este for uma obra própria, a tag <localtrabalho> seja gerada com o CEI correspondente a esse tomador de serviço.

## **04. SOLUÇÃO**

**ATENÇÃO: ESTE TDN FOI SUBSTITUIDO POR ESSE OUTRO [LINK](https://tdn.totvs.com.br/pages/viewpage.action?pageId=934636669)**

O produto foi ajustado para que o grupo <localtrabalho>, referente às informações do Tomador de Serviço, seja impresso com o CEI do tomador quando o funcionário tiver apenas um tomador de obra própria.

O sistema buscará o tomador no histórico do Rateio por Tomador para gerar essa informação.

**Exemplo XML 2206**

## **05.****ASSUNTOS RELACIONADOS**

[Mapeamento S-2200](https://tdn.totvs.com/display/LRM/Evento+S-2200)

[Mapeamento S-2206](https://tdn.totvs.com/display/LRM/Evento+S-2206)

[Mapeamento S-2300](https://tdn.totvs.com/display/LRM/Evento+S-2300)

[Mapeamento S-2306](https://tdn.totvs.com/display/LRM/Evento+S-2306)
