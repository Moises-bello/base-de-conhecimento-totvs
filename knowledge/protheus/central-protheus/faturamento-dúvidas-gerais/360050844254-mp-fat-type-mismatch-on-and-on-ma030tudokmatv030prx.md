---
article_id: 360050844254
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 23b050a1eced0a3dc41aeab423da67e09aeae18a98d11f98d33f4120ab1fa552
fetched_at: '2026-06-28T22:38:32.692774+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-type mismatch on .AND.  on MA030TUDOK(MATV030.PRX) '
type: support-article
updated_at: '2021-04-28T15:53:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050844254-MP-FAT-type-mismatch-on-AND-on-MA030TUDOK-MATV030-PRX
---

**Ocorrência**Ao salvar o cadastro do cliente(**MATA030**), gera o erro:

**type mismatch on .AND.  on MA030TUDOK(MATV030.PRX) 30/04/2020 15:44:52 line : 134**

**Ambiente**

Microsiga Protheus - todas as versões.

**Causa**

O erro ocorre por que exite uma integração com o módulo de TMS, mas o parâmetro que integra o módulo Faturamento com o TMS, **MV\_INTTMS ,** foi criado com o tipo ***caracter*,** quando no correto é tipo ***lógico*.**

stack do parâmetro no erro:

 Index (0) :\*\*SX60101  X6\_FIL+X6\_VAR  
    Field 1: X6\_FIL(C) :02  
**Field 2: X6\_VAR(C) :MV\_INTTMS**  
**Field 3: X6\_TIPO(C) :C---tipo carácter**  
   ...                                               
**Field 13: X6\_CONTEUD(C) :T--->conteúdo lógico**  
**Field 16: X6\_PROPRI(C) :U**  
   
 **Solução**  
 Para solucionar essa ocorrência, ajuste o tipo do parâmetro **MV\_INTTMS** para ***lógico*,** conforme a tela do configurador abaixo.

![](https://totvssuporte.zendesk.com/attachments/token/sLcae0xirRDHE9T8dd1OAVbQU/?name=inline375117102.png)
