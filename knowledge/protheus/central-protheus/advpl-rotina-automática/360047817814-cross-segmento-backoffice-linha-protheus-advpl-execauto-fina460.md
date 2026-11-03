---
article_id: 360047817814
category: ADVPL - Rotina Automática
content_hash: cd8b7d0e2cd24e9d8d3a57d64a324af32c66fd4a416f12973905c7e0e261196f
fetched_at: '2026-06-28T22:40:23.999681+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - EXECAUTO - FINA460
type: support-article
updated_at: '2025-08-29T13:26:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047817814-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-EXECAUTO-FINA460
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34540769957911)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Como informar os valores de juros, descontos entre outros via ExecAuto.  
  
**Ambiente**  
Protheus - ADVPL - A partir da versão 12.  
  
**Solução**

Os campos FO1\_TXJUR, FO1\_VLJUR, FO1\_TXMUL ,FO1\_DESCON, FO1\_ACRESC, FO1\_DECRE são importados automaticamente do próprio título SE1 que aparece na grid de títulos a negociar.  
Por sua vez, os campos FO1\_TXJUR e FO1\_TXMUL podem ser alterados através de envio dos novos valores no cabeçalho da negociação (últimos campos do array aCab).  
Os campos FO1\_ACRESC, FO1\_DECRE por regra não podem ser manipulados via Execauto.

Exemplo de cabeçalho modificando a taxa de multa e de juros. Nesse caso, para todos os títulos negociados serão consideradas essas taxas, desde que estejam vencidos.  
aCab:={{"cCondicao" ,cCond },;  
{"cNatureza" ,cNaturez },;  
{"E1\_TIPO" ,cTipoLiq },;  
{"cCliente" ,cCliLiq },;  
{"nMoeda" ,nMoeda },;

{"cLoja" ,cLojaLiq },;  
{"FO0\_TXMUL" ,3.0 },;  
{"FO0\_TXJUR" ,2.0 }}

Saiba mais:

[Liquidação a receber (FINA460) - ExecAuto](https://tdn.totvs.com/pages/releaseview.action?pageId=650494634)
