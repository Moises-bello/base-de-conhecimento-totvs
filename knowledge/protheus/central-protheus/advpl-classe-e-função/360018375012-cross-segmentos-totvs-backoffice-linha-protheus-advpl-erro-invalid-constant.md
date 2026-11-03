---
article_id: 360018375012
category: ADVPL - Classe e Função
content_hash: 61c59d54a08f3ce50df790a979ba8a7dec7e34705f4240737e0aeef49647be6b
fetched_at: '2026-06-28T22:40:19.394329+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Erro Invalid constant
type: support-article
updated_at: '2022-01-11T21:50:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018375012-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-Invalid-constant
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Ao Compilar **RDMAKE**, é apresentado o erro*Invalid constant* **STRXXXX**  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Esse erro ocorre pois os includes não estão configurados corretamente ou Constante declarada de forma incorreta, ou no **include (ch)**, está como **Static** ao invés de #**Define**
