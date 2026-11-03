---
article_id: 360024201771
category: ADVPL - Web Service
content_hash: 611a622c0827bd9879486682a452a2d1607cecd770204611598a3d32793c9782
fetched_at: '2026-06-28T22:40:10.267137+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Extração de arquivo
  do repositório imagens via REST
type: support-article
updated_at: '2023-05-30T23:12:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024201771-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Extra%C3%A7%C3%A3o-de-arquivo-do-reposit%C3%B3rio-imagens-via-REST
---

**Dúvida**É possível criar um *web service* no Protheus consumindo o cadastro de produto e trazendo a imagem do Produto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**

Sim neste caso pode utiliza as funções de acesso ao Repositório de Imagem

1. [LoadBitmap - Nome da imagem do repositório](http://tdn.totvs.com/pages/releaseview.action?pageId=6815071)
2. [RepExtract - Extração de arquivo do repositório imagens](http://tdn.totvs.com/pages/releaseview.action?pageId=6815070)

**Segue exemplo de customizado**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "RESTFUL.ch"  
#Include "TBICONN.ch"  
  
// SERVIÇO REST  
WSRESTFUL wsmatarp DESCRIPTION "REST web service for product"  
    WSDATA product AS STRING // CÓDIGO DO PRODUTO  
  
    // MÉTODO PARA OBTER A IMAGEM  
    WSMETHOD GET mt010images DESCRIPTION "Method to get a product image" WSSYNTAX "/wsmatarp/mt010images/{id}" PATH "mt010images"  
END WSRESTFUL  
  
// MÉTODO PARA OBTER A IMAGEM  
WSMETHOD GET mt010images WSRECEIVE product WSSERVICE wsmatarp  
    Local oFile := NIL // CONVERSÃO DE .BMP PARA BINÁRIO     
  
    // PREPARAÇÃO DE AMBIENTE (REMOVER SE EXECUTADO VIA GUI)  
    RPCSetEnv("99", "01", NIL, NIL, "COM", NIL, {"SB1", "SB5"})  
  
    // ABRE O ARQUIVO DA TABELA SB1 E PESQUISA PELO ÍNDICE 01  
    DbSelectArea("SB1")  
    DbSetOrder(1)  
  
    // VERIFICA SE O PRODUTO INFORMADO TEM IMAGEM CADASTRADA  
    If (MsSeek(FwXFilial("SB1") + PadR(AllTrim(::product), TamSX3("B1_COD")[1])))  
        // CASO O PRODUTO TENHA IMAGEM, EFETUA E EXTRAÇÃO PARA O ROOTHPATH  
        If (RepExtract(AllTrim(SB1->B1_BITMAP), "\images\" + AllTrim(::product) + ".bmp" , .T.))  
            oFile := FwFileReader():New("/images/" + AllTrim(::product) + ".bmp")  
  
            // EFETUA A MANIPULAÇÃO DO ARQUIVO  
            If (oFile:Open())  
                // RETORNA O ARQUIVO PARA DOWNLOAD  
                Self:SetHeader("Content-Disposition", "attachment; filename=" + AllTrim(::product) + ".bmp")  
                Self:SetResponse(oFile:FullRead())  
  
                // APAGA O ARQUIVO GERADO  
                FErase("/images/" + AllTrim(::product) + ".bmp")  
            Else  
                SetRestFault(002, "can't load file") // GERA MENSAGEM DE ERRO CUSTOMIZADA  
            EndIf  
        Else  
            SetRestFault(002, "can't load image")  
        EndIf  
    Else // SE NÃO ACHA A IMAGEM  
        SetRestFault(404, "product image not found")  
    EndIf  
Return (.T.)
```
