---
article_id: 360028145211
category: CRM - Dúvidas Gerais
content_hash: a976c1b9e3f3d37f1bd671b382435f6929db474e80ef18637f63beadc6d854a9
fetched_at: '2026-06-28T22:40:27.451098+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Erro no inicializador de
  AD2_NOMVEN
type: support-article
updated_at: '2024-04-25T11:55:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028145211-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Erro-no-inicializador-de-AD2-NOMVEN
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23048068968983)** Tempo aproximado para leitura: **00:04:00 min**

**Ocorrência**Ao alterar a oportunidade de venda, gerou o erro:

*variable does not exist ACOLS on {|a,b,c| FWInitCpo(a,b,c),xRet:=(If(!INCLUI,Posicione("SA3",1,xFilial("SA3")+GDFieldGet("AD2\_VEND", Len( aCols ) ),"A3\_NOME"),""))*

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Causa**O erro ocorre por que o  x3\_relação (inicializador padrão) do campo **AD2\_NOMVEN**, está incorreto.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o configurador, Dicionário, Base de dados, e selecione a tabela **AD2**;  
2. Ajuste o inicializador padrão do campo **AD2\_NOMVEN para****IIF(!INCLUI,POSICIONE("SA3",1,XFILIAL("SA3")+AD2->AD2\_VEND,"A3\_NOME"),"")**;  
3. Salve o campo, salve a tabela e atualize o dicionário de dados.

![Altera__o_da_AD2_NOMVEN.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360028020052)
