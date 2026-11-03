---
article_id: 360024939273
category: CRM - Dúvidas Gerais
content_hash: 723846e91814d650680fdaf66bccccbc9ca6fca602a56d9c98961e62d4b05b00
fetched_at: '2026-06-28T22:40:27.385027+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - CRM - variable does not
  exist ACOLS on {|a,b,c| FWInitCpo(a,b,c),xRet:=(If(!INCLUI,Posicione("AC4",1,xFilial("AC4")+GDFieldGet("AD4_PARTNE",Len(aCols)),"AC4_NOME
type: support-article
updated_at: '2023-01-31T21:19:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024939273-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-CRM-variable-does-not-exist-ACOLS-on-a-b-c-FWInitCpo-a-b-c-xRet-If-INCLUI-Posicione-AC4-1-xFilial-AC4-GDFieldGet-AD4-PARTNE-Len-aCols-AC4-NOME
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Após gravar e salvar a oportunidade (**CRMA110/FATA300**), ao tentar alterar a mesma, o sistema apresentar o error log abaixo:

*variable does not exist ACOLS on {|a,b,c| FWInitCpo(a,b,c),xRet:=(If(!INCLUI,Posicione("AC4",1,xFilial("AC4")+GDFieldGet("AD4\_PARTNE",Len(aCols)),"AC4\_NOME"),"")),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet }(PROTHEUSFUNCTIONMVC.PRX) 18/04/2019 18:21:40*

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - CRM - a partir da release 12.1.17.  
  
**Causa**O erro ocorre por que o inicializador padrão do campo **AD4\_NOMPAR** está com a validação:

*(If(!INCLUI,Posicione("AC4",1,xFilial("AC4")+GDFieldGet("AD4\_PARTNE",Len(aCols)),"AC4\_NOME"),""))*

**Solução**Abaixo inicializador padrão correto.  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o configurador, Dicionário, Base de dados, e selecione a tabela **AD4**;  
2. Ajuste o inicializador padrão do campo **AD4\_NOMPAR para  IIF(!INCLUI,POSICIONE("AC4",1,XFILIAL("AC4")+AD4->AD4\_PARTNE,"AC4\_NOME"),"")**;  
3. Salve o campo, salve a tabela e atualize o dicionário de dados.

**![ad4_nompar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360038202834/ad4_nompar.gif)**
