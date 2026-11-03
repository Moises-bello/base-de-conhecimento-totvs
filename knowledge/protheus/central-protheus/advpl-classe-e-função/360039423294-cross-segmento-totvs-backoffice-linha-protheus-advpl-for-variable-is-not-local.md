---
article_id: 360039423294
category: ADVPL - Classe e Função
content_hash: 700369b729272d5b0d143efa03e2c99a64225fa20974210b659d54eadfff357b
fetched_at: '2026-06-28T22:40:16.743263+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - For variable is
  not local
type: support-article
updated_at: '2022-02-02T12:15:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039423294-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-For-variable-is-not-local
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao tentar realizar a compilação de um fonte ao qual tenha um laço de repetição `For` e a variável de controle não esteja declarada, é gerado o erro de compilação `For variable is not Local`.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12.1.23  
  
**Causa**Esta mensagem ocorre devido a variável de controle do laço não estar declarada com escopo local.

Este tipo de implementação pode gerar inconsistências quando há chamadas de funções que tenham laços recursivos, pois caso seja utilizado o mesmo nome de variável em ambos os laços, a atribuição de valores no laço interno, vai alterar o laço externo a função.  
   
**Solução**Declarar a variável de controle do laço como local.
