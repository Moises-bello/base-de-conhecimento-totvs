---
article_id: 28866394693143
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1d9502a076817d3546f8fa9b10119e2457b0acebd8eedd7f49409d0f837d4ed1
fetched_at: '2026-06-28T22:38:57.062790+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - ExecAuto
  da rotina de Endereçamento
type: support-article
updated_at: '2025-03-12T12:17:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28866394693143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-ExecAuto-da-rotina-de-Endere%C3%A7amento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28866363118359) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Qual o exemplo de Execução Automatica da rotina MATA265?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**Exemplo para endereçar apenas um item:**

|  |
| --- |
| #Include "RwMake.CH" #include "tbiconn.ch"  User Function TMATA265() Local aCabSDA       := {} Local aItSDB        := {} Local \_aItensSDB    := {}  Private lMsErroAuto := .F.    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "EST"  //Cabecalho com a informaçãoo do item e NumSeq que sera endereçado. aCabSDA := {{"DA\_PRODUTO" ,"PROD-ENDER",Nil},; {"DA\_NUMSEQ"  ,"001419",Nil}}  //Dados do item que será endereçado aItSDB := {{"DB\_ITEM"   ,"0001"      ,Nil},; {"DB\_ESTORNO"  ," "       ,Nil},; {"DB\_LOCALIZ"  ,"LOCAL"    ,Nil},; {"DB\_DATA"   ,dDataBase   ,Nil},; {"DB\_QUANT"  ,20           ,Nil}} aadd(\_aItensSDB,aitSDB)  //Executa o endereзamento do item MATA265( aCabSDA, \_aItensSDB, 3) If lMsErroAuto MostraErro() Else MsgAlert("Processamento Ok!") Endif  Return |

**Exemplo para endereçar mais de um item:**

|  |
| --- |
| #Include "RwMake.CH" #include "tbiconn.ch"  User Function TMATA265() Local aCabSDA       := {} Local aItSDB        := {} Local \_aItensSDB    := {}  Private lMsErroAuto := .F.    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "EST"  //Cabeçalho com a informação do item e NumSeq que sera endereçado. aCabSDA := {{"DA\_PRODUTO" ,"PROD-ENDER",Nil},; {"DA\_NUMSEQ"  ,"001419",Nil}}  //Dados do item que será endereçado aItSDB := {{"DB\_ITEM"   ,"0001"   ,Nil},; {"DB\_ESTORNO" ,"S "      ,Nil},; {"DB\_LOCALIZ" ,"LOCAL"    ,Nil},; {"DB\_DATA"   ,dDataBase  ,Nil},; {"DB\_QUANT"   ,20         ,Nil}} aadd(\_aItensSDB,aitSDB)  //Executa o estorno do item MATA265( aCabSDA, \_aItensSDB, 4) If lMsErroAuto MostraErro() Else MsgAlert("Processamento Ok!") Endif Return |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
