---
article_id: 21562964846103
category: Materiais - Compras (SIGACOM)
content_hash: 16cc57248e6ddd7240546457e02ba72e4e6b12b1df1a4eda8cd82071b5d32ecd
fetched_at: '2026-06-28T22:41:25.502945+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos/Totvs Backoffice Prothreus - SIGACOM - Exemplo Ponto de Entrada  MT100TOK
  para verificação dos campos na tabela DKD
type: support-article
updated_at: '2024-07-05T14:45:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21562964846103-Cross-Segmentos-Totvs-Backoffice-Prothreus-SIGACOM-Exemplo-Ponto-de-Entrada-MT100TOK-para-verifica%C3%A7%C3%A3o-dos-campos-na-tabela-DKD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21562964823575) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Exemplo da configuração do ponto de entrada **MT100TOK**, para verificação de campos customizados na tabela DKD.

[**Tabela DKD campos customizados na SD1**](https://tdn.totvs.com/pages/releaseview.action?pageId=699820173)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - A partir do release 12.1.33  
  
**Solução**  
**#Include "[Protheus.ch](http://Protheus.ch)"  
#Include "[RwMake.ch](http://RwMake.ch)"  
#Include "[TbiConn.ch](http://TbiConn.ch)"  
  
User Function MT100TOK()  
  
Local lRet := .T.  
Local nX := 1  
Default aColsDKD := {}  
  
For nX := 1 To Len(aColsDKD)  
    IF Empty(aColsDKD[nX][2])  
  
        MSGALERT(" Você deve digitar uma OBS no campo DKD\_OBS do Item: " +cValToChar(aColsDKD[nX][1]))  
        lRet := .F.  
  
    EndIf  
  
Next nX**

**Return lRet**

**![MT100TOK para DKD.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21574217297943)**

***Saiba Mais :***

[Pontos de entrada disponíveis na MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
