---
article_id: 360023116432
category: ADVPL - Ponto de Entrada
content_hash: 269b3b765eadce0cd50ae2fd72ad94e41ad4eb0ea7ccd09b10c681e5f2b37585
fetched_at: '2026-06-28T22:40:11.668946+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Campos da aba frete/despesas
  no pedido de compra
type: support-article
updated_at: '2022-06-21T17:57:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023116432-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Campos-da-aba-frete-despesas-no-pedido-de-compra
---

**Ocorrência**Ao utilizar os pontos de entrada da rotina de geração de Pedidos de Compra (MATA121), não consigo encontrar os campos da aba Frete/Despesas na variável aCols.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**  
Os campos da aba Frete/Despesas são armazenados em vetores e variáveis para a montagem dos campos da MsGet(), contudo por não pertencerem a grid de dados, os mesmos não constam na variável aCols.  
  
**Solução**Utilizar as variáveis abaixo:

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | Variável |
| C7\_TPFRETE | Tp. Frete | cTpFrete |
| C7\_DESPESA | Despesas | aValores[4] |
| C7\_FRETE | Valor do Frete | aValores[3] |
| C7\_SEGURO | Seguro | aValores[7] |
| C7\_TOTAL | Total (Frete + Despesas) | aValores[8] |
| C7\_TRANSP | Transportadora | cTransp |
| C7\_TRANSLJ | Loja | cTransLj |
| C7\_FRETCON | Vl. Frete Contratado | nFreteCon |

**Observação**  
Por serem variáveis de escopo privado as mesmas podem ser alteradas sem aviso prévio, assim sendo, será necessária a realização do processo de depuração (debug) para validar se as mesmas se mantém nas mesmas variáveis.
