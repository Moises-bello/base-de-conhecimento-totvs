---
article_id: 360047790374
category: Comércio Exterior - Easy Import Control - Solic. de Importação
content_hash: d434cc726e1ce41e3b205197aa520f916ebe623805398ba0a5c8d417dd06069e
fetched_at: '2026-06-28T22:39:46.683405+00:00'
product: protheus
section_id: 1500001538401
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Diferença de gravação
  Import para Imporx no campo C1_COTACAO
type: support-article
updated_at: '2023-06-14T17:14:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047790374-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Diferen%C3%A7a-de-grava%C3%A7%C3%A3o-Import-para-Imporx-no-campo-C1-COTACAO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min**

**Dúvida** Qual a diferença da gravação do campo **C1\_COTACAO** de **Import** para **Imporx** ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Ao gerar a Solicitação de Compras **"SC"** o campo **C1\_COTACAO**  é  com conteúdo **'IMPORT'**, significa que o produto é importado.  
- O conteúdo "**IMPORT**" no campo **C1\_COTACAO**, significa que a "**SC"** possui item importado.  
Ao gerar a Solicitação de Importação **"SI"** além do campo **C1\_COTACAO**  ficar com conteúdo "**IMPORX"** o campo **C1\_SI\_NUM** é preenchido com o numero da "SI" gerada.   
- O conteúdo "**IMPORX**" no campo **C1\_COTACAO**, significa que foi gerada **"SI"** no , SIGAEIC.  
  
Ao Incluir a Purchase Order**"PO"** o campo **C1\_COTACAO** é gravado com conteúdo **'XXXXX'**, isso significa que há um vinculo da Solicitação de Compras **"SC",** com o Pedido de Compras **"PC",** e o sistema preenche como **'XXXXXX'** o campo de cotação porque não houve o processo de análise de cotação para preencher conteúdo.
