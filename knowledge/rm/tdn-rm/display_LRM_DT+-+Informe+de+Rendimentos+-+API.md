---
content_hash: a5baea9bc3e3daa521d7c84c067e378b6468a537b3d7d47a2c823752436c2dd5
fetched_at: '2026-06-29T00:11:29.352030+00:00'
page_id: '736188988'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos - API
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Informe+de+Rendimentos+-+API
version: 13
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Informe de Rendimentos - API |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-619 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o informe de rendimentos utilizando o DataServer **FOPDIRFDAT**, o sistema busca as informações pela chapa, o ideal seria buscar pelo CPF, para tratar a situação onde a pessoa tem mais de uma chapa na coligada.

## **03. SOLUÇÃO**

Tratativa no DataServer **FOPDIRFDAT**para permitir realizar a consulta através da chapa ou através do CPF.

**Observação:**

Quando o funcionário tiver mais de uma chapa ativa, deverá usar a chapa mais antiga para consultar na API.

Caso tenha chapa Ativa e Demitida, deverá usar a chapa Ativa.
