---
article_id: 360035887193
category: NFe - Nota Fiscal Eletrônica
content_hash: 50de693800c7ed82396a62132888c8cebe1d42513605b474697340533b9300d0
fetched_at: '2026-06-28T22:40:00.176460+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: '   Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - argument error
  in function Len() on SPEDNFETRF(SPEDNFE.PRX)'
type: support-article
updated_at: '2021-10-08T17:43:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035887193--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-argument-error-in-function-Len-on-SPEDNFETRF-SPEDNFE-PRX
---

**Dúvida**

Como corrigir argument error in function Len() on SPEDNFETRF(SPEDNFE.PRX)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Este erro ocorre quando é utilizado algum carácter especial no conteúdo da nota.**

Para correção do erro, será necessário que verifique todos os cadastros que envolvem essa nota, cadastros de produtos, clientes, endereço, informações complementares.

* Exemplos de caracteres especiais que podem ocasionar este erro:

**({[<>(TAB)#¨  ~ ´`º ¹²³£¢¬]})**

Um dos fatores que mais ocasiona esse tipo de erro é, copiar o conteúdo de outros editores de texto como, Word ou Excel e colar nas mensagens complementares da nota C5\_MENNOTA.

Recomendamos que sempre digite toda a mensagem manualmente para que esse tipo de erro seja evitado.
