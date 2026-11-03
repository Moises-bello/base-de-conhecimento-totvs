---
article_id: 25916334112791
category: Financeiro - Liquidação a Receber
content_hash: 3120ef1cfb6c1d9c604dc78494f1e0a49efa745cc566e0b9e9aac988bf199816
fetched_at: '2026-06-28T22:37:42.278183+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - Exemplo do
  ponto de entrada FINA460A no modelo MODELCOMMITNTTS para acrescentar informações
  na SE1 no titulo gerado.
type: support-article
updated_at: '2026-03-04T17:01:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25916334112791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Exemplo-do-ponto-de-entrada-FINA460A-no-modelo-MODELCOMMITNTTS-para-acrescentar-informa%C3%A7%C3%B5es-na-SE1-no-titulo-gerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25916327130775) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como adicionar informações na SE1 nos títulos que serão gerados pela liquidação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
Segue exemplo do modelo MODELCOMMITNTTS

```
User Function FINA460A()  
   
  Local lRet           := .T.  
  Local aArea        := GetArea()    // Armazena ultima area utilizada  
  Local aAreaSE1  := SE1->(GetArea()) // Armazena ultima area utilizada  
  Local cIdPonto   := ''  
  Local oMdl  
  Local nY  
   
If PARAMIXB <> NIL  
  cIdPonto    := PARAMIXB[2]  
  If  cIdPonto == 'MODELCOMMITNTTS'  
      oMdl    := PARAMIXB[1]:GETMODEL("TITGERFO2")  
      For nY := 1 To oMdl:Length()  
          oMdl:GoLine(nY)  
          cPref        := oMdl:GetValue("FO2_PREFIX")  
          cNum         := oMdl:GetValue("FO2_NUM")  
          cParc        := oMdl:GetValue("FO2_PARCEL")  
          cTipo        := oMdl:GetValue("FO2_TIPO")  
   
          If SE1->(DbSeek(xFilial("SE1") + cPref + cNum + cParc + cTipo))  
              SE1->(RecLock("SE1", .F.))  
  
  
                    // CAMPOS QUE TERÃO SEU CONTEUDO ALTERADO PELO USUARIO.  
                  // NESSE MOMENTO O REGISTRO NA SE1 JÁ ESTA CRIADO E  
                  // ACASO ALGUMA VALIDAÇÃO DA MODEL NÃO FOR  
                  // ATENDIDA A TRANSAÇÃO SERÁ DESARMADA.  
  
  
                    SE1->E1_HIST := "Hist Teste"  
                   
              SE1->(MsUnLock())  
          Endif  
      Next nY  
  Endif  
EndIf  
   
  RestArea(aArea)  
  RestArea(aAreaSE1)  
  
  
Return lRet
```

**Saiba mais**

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de entrada legado na Fina460](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020656232-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pontos-de-entrada-legado-na-Fina460?source=search)

[FWFormGridModel](https://tdn.totvs.com/display/public/framework/FWFormGridModel)
