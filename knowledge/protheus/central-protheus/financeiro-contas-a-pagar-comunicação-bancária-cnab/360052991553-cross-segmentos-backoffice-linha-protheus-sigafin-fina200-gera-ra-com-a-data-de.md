---
article_id: 360052991553
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ccd9d73895bbc1e6a3c66ecaa3f2d23e8543c6094f1357553096932bc807f86f
fetched_at: '2026-06-28T22:37:55.261418+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  -  FINA200 -  Gera RA
  com a data de crédito ou database com o parâmetro MV_REC2TIT = 1
type: support-article
updated_at: '2024-05-20T20:37:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052991553-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-Gera-RA-com-a-data-de-cr%C3%A9dito-ou-database-com-o-par%C3%A2metro-MV-REC2TIT-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Com o parâmetro **MV\_REC2TIT = 1,** o sistema gera um **RA,** ocorre que o sistema deveria gerar com a data de crédito (que consta no retorno do banco) ou gerar com a data do processamento do retorno. Existe alguma parametrização para alterar isso?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Não tem parametrização para determinar a data que vai gerar, o sistema sempre gera com a **database**, a data que efetua a baixa do retorno.

**Importante:**Existe o ponto de entrada **F200GERA,** onde é possível alterar a data utilizada, porém deverá utilizar este array:

**//Montagem do Array para ExecAuto  
                aAdd(aTitulos,{"E1\_PARCELA"    , cParcRA                , Nil })  
                aAdd(aTitulos,{"E1\_TIPO"    , Substr(MVRECANT,1,3)    , Nil })  
                aAdd(aTitulos,{"E1\_PORTADO"    , cBanco                , Nil })  
                aAdd(aTitulos,{"E1\_AGEDEP"    , cAgencia                , Nil })  
                aAdd(aTitulos,{"E1\_CONTA"    , cConta                , Nil })  
                aAdd(aTitulos,{"E1\_EMISSAO"    , dDataBase                , Nil })  
                aAdd(aTitulos,{"E1\_EMIS1"    , dDataBase                , Nil })  
                aAdd(aTitulos,{"E1\_VENCTO"    , dDataBase                , Nil })  
                aAdd(aTitulos,{"E1\_VENCREA"    , dDataBase                , Nil })  
                aAdd(aTitulos,{"E1\_VALOR"    , nValRa                , Nil })  
                aAdd(aTitulos,{"E1\_VLCRUZ"    , nValRa                , Nil })  
                aAdd(aTitulos,{"E1\_SALDO"    , nValRa                , Nil })  
                aAdd(aTitulos,{"E1\_MOEDA"    , 1                        , Nil })  
                aAdd(aTitulos,{"E1\_SITUACA" , "0"                    , Nil })  
                aAdd(aTitulos,{"E1\_STATUS"    , "A"                    , Nil })  
                aAdd(aTitulos,{"E1\_ORIGEM"    , "FINA040"                , Nil })  
                aAdd(aTitulos,{"E1\_FLUXO"    , "S"                    , Nil })  
                aAdd(aTitulos,{"E1\_MULTNAT" , "2"                    , Nil })  
                aAdd(aTitulos,{"E1\_PROJPMS" , "2"                    , Nil })  
                aAdd(aTitulos,{"E1\_HIST"    , c070Hist                , Nil })  
                If SpbInUse()  
                    aAdd(aTitulos,{"E1\_MODSPB"    , "1"                , Nil })  
                Endif**
