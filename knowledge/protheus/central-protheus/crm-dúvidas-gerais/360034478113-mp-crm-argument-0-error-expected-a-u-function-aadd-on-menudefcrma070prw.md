---
article_id: 360034478113
category: CRM - Dúvidas Gerais
content_hash: 1be9944eddc962ced4f527e262a69a245776312618cc203c09584d3db6be2c98
fetched_at: '2026-06-28T22:40:27.547959+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-CRM-argument #0 error, expected A->U,  function aadd on MENUDEF(CRMA070.PRW)'
type: support-article
updated_at: '2021-04-28T14:49:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034478113-MP-CRM-argument-0-error-expected-A-U-function-aadd-on-MENUDEF-CRMA070-PRW
---

**Ocorrência**

Ao acessar o cadastro de cliente no CRM, gera o erro: **argument #0 error, expected A->U, function aadd on MENUDEF(CRMA070.PRW) 03/05/2019 13:49:36 line : 97**  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 12.

**Causa**

O erro ocorre por que o menu do cadastro de clientes para CRM tem outro formato, que é o mvc, neste caso, é necessário utilizar o parâmetro  **MV\_MVCSA1** como .T. e assim, o sistema substituirá no menu a chamada **MATA030** por **CRMA980**.  
   
 **Solução**

Para solucionar essa ocorrência, deixe o parâmetro **MV\_MVCSA1** igual a T.
