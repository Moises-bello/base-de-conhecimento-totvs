---
article_id: 360058711753
category: ADVPL - Ponto de Entrada
content_hash: 11b216e54bfed785da5775fdf47e4da6680ae32439f07a73eb897c02bc1285c3
fetched_at: '2026-06-28T22:40:12.889875+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tela temporária
  Montagem de Carga: incluir campo'
type: support-article
updated_at: '2021-12-30T18:00:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058711753-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tela-tempor%C3%A1ria-Montagem-de-Carga-incluir-campo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Como adicionar campos na tela temporária da Montagem de Carga OMSA200?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para a inclusão do campo e seu conteúdo, deve usar os pontos de entrada **OM200GRV(), DL200TRB() e** **DL200BRW().**Exemplo de uso dos pontos de entrada.

```
#include'totvs.ch'  
  
//////////////////////////////////////////////  
User Function OM200GRV()  
DBSelectArea("SC5")  
DBSETORDER( 1 )     
  
IF SC5->(DBSeek(xFilial("SC5")+TRBPED->PED_PEDIDO))            
    TRBPED->PED_TPFRET := SC5->C5_TPFRETE  
    MsUnlock()  
  
ENDIF  
Return Nil  
  
//////////////////////////////////////////////  
User Function DL200TRB()  
Local aRet := PARAMIXB    
AADD(aRet,{"PED_TPFRET" ,"C",2,2})  
Return aRet  
  
//////////////////////////////////////////////  
  
User Function DL200BRW()  
Local aRet := PARAMIXB  
AADD(aRet, {"PED_TPFRET" , ,'Tipo Frete'} )  
Return aRet
```

**Saiba mais**

[OM200GRV - Arquivo Temporário da Carga](https://tdn.totvs.com/pages/releaseview.action?pageId=6091378)  
[DL200TRB - Grava Arquivo Temporário da Carga](https://tdn.totvs.com/pages/releaseview.action?pageId=6091259)

[DL200BRW - Manipulação das Colunas do Browse de Pedidos da Montagem de Carga](https://tdn.totvs.com/pages/releaseview.action?pageId=361439050)
