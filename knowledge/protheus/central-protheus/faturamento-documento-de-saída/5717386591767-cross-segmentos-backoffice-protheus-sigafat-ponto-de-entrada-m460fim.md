---
article_id: 5717386591767
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 1237fb3d69ed8a91140808aa09c98c0821b89ac0bc72b7aa8893b32fce0844db
fetched_at: '2026-06-28T22:38:44.118676+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de Entrada M460FIM
type: support-article
updated_at: '2025-07-23T16:53:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5717386591767-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-Entrada-M460FIM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31751263342231) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual exemplo do ponto de entrada **M460FIM**?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Exemplo de uso abaixo:

```
#INCLUDE 'PROTHEUS.CH'
#INCLUDE "FWMVCDEF.CH"
 
//*****************************************************************************
// Ponto de entrada M460FIM - Gravação da NF saida
// Este P.E. é chamado após a gravação da NF de Saída e fora da transação.
//#Par01    - PARAMIXB[1] - Número da NF
//#Par02    - PARAMIXB[2] - Série da NF
//#Par03    - PARAMIXB[3] - Cliente/fornecedor da NF
//#Par03    - PARAMIXB[4] - Loja da NF
//*Return   - Sem nenhuma retorno
//*****************************************************************************
 
User Function M460FIM()
 
    Local cNumNFS   := PARAMIXB[1] // Número da NF
    Local cSerieNFS := PARAMIXB[2] // Série da NF
    Local cClieFor  := PARAMIXB[3] // Cliente/fornecedor da NF
    Local cLoja     := PARAMIXB[4] // Loja da NF
 
    If cClieFor == "ZZZ010" .And. cLoja == "02"
        Alert("NF gerada para o cliente:" + cClieFor + " e loja:"+ cLoja)
    EndIf
 
Return
```
