---
article_id: 1500000618241
category: ADVPL - Classe e Função
content_hash: e49d53ad39e40f5ccd81e09384ea224943faf8ec7ae9d44cfbd6627e721a1a7e
fetched_at: '2026-06-28T22:40:18.088308+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Thread: Status
  da Thread'
type: support-article
updated_at: '2022-06-13T21:41:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000618241-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Thread-Status-da-Thread
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como saber se a thread está ativa ou não?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.017  
  
**Solução**Pode se obter o status via **GetUserInfoArray**(), que traz um *array* contendo todas as threads em execução. Basta pesquisar se o ID da thread desejada encontra-se no *array* retornado, ou caso prefira, criar sua própria função que retorne .T. ou .F. após fazer uma pesquisa no *array*.  
  
**Saiba Mais  
[GetUserInfoArray](https://tdn.totvs.com/display/tec/GetUserInfoArray)**
