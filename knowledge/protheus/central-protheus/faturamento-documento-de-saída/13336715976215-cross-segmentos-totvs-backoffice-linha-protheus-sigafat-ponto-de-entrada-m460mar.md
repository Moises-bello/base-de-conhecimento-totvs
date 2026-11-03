---
article_id: 13336715976215
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: bf3c4cfe9d4d1445998aded5cbb3eaf82dd7fac276c49164ca9d71f4bb3688dd
fetched_at: '2026-06-28T22:38:45.432853+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M460MARK
type: support-article
updated_at: '2023-03-24T12:51:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13336715976215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460MARK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M460MARK - Validação de pedidos marcados**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada **M460MARK** é utilizado para **validar os pedidos marcados** e está localizado no início da função a460Nota (endereça rotinas para a geração dos arquivos SD2/SF2).  
Será informado no terceiro parâmetro a série selecionada na geração da nota e o número da nota fiscal poderá ser verificado pela variável private cNumero.  
  
**Observações**

Caso a variável "**lInver**t" esteja marcado como **.T.**, será necessário **inverter** a ordem considerando os **marcados como não marcados** e os **não marcados como marcados** em conjunto com os campos necessários conforme as validações da regra e legenda.

Utilizar as funções de FrameWork (**Thismark(), ThisInv() e Ismark()**), para realizar as validações da marcação dos registros. **Não utilizar** as validações pelo **campo C9\_OK**, devido orientações da equipe técnica.  
  
**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'PARMTYPE.CH'  
  
User Function M460MARK()  
  
   local cMark   := PARAMIXB[1] // MARCA UTILIZADA  
   local lInvert := PARAMIXB[2] // SELECIONOU "TRAZER PED MARCADOS"  
   local aArea   := GetArea("SC9")  
  
   SC9->(DbGoTop())  
  
   While (SC9->(!EOF()))  
  
      If (lInvert) // "TRAZER PED MARCADOS" OPCAO SELECIONADA  
         If  SC9->(IsMark("C9_OK")) .AND. (AllTrim(SC9->C9_BLEST) =='' .AND. AllTrim(SC9->C9_BLCRED)=='')  
            MsgInfo("Marcado - Pedido: " + SC9->C9_PEDIDO + " - Item: " + SC9->C9_ITEM, "1-Ponto de Entrada M460MARK")           
         Else  
            MsgInfo("Desmarcado - Pedido: " + SC9->C9_PEDIDO + " - Item: " + SC9->C9_ITEM, "1-Ponto de Entrada M460MARK")  
         EndIf  
      Else // "TRAZER PED MARCADOS" OPCAO NAO SELECIONADA  
         If SC9->(IsMark("C9_OK"))  
            MsgInfo("Marcado - Pedido: " + SC9->C9_PEDIDO + " - Item: " + SC9->C9_ITEM, "2-Ponto de Entrada M460MARK")  
         Else  
            MsgInfo("Desmarcado - Pedido: " + SC9->C9_PEDIDO + " - Item: " + SC9->C9_ITEM, "2-Ponto de Entrada M460MARK")  
         EndIf  
      EndIf  
  
      SC9->(DbSkip())  
  
   EndDo  
  
   RestArea(aArea)  
  
Return (MsgYesNo("Continuar o processo atual?", "Ponto de Entrada M460MARK"))
```

**Saiba Mais**  
**[M460MARK - Validação de pedidos marcados](https://tdn.totvs.com/x/vYRn)**
