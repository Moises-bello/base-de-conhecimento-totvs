---
article_id: 360020589731
category: ADVPL - Web Service
content_hash: 160131a22b4be5051e04a68235d9f07a9a14e28bd4230dd9877f30d90299b33e
fetched_at: '2026-06-28T22:40:10.270492+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - HTTPPOST cGetParms
  "400 Bad Request"
type: support-article
updated_at: '2025-07-30T14:28:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020589731-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-HTTPPOST-cGetParms-400-Bad-Request
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Estou tentando fazer uma comunicação com uma API do moodle porém está me retornando o erro "400 Bad Request" creio que seja alguma limitação do protheus pois fiz a mesma chamada via PostMan e funcionou normalmente.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**O retorno "*400 Bad Request"* pode indicar um possível erro de sintaxe nos parâmetros informados, nestes casos relacionado a codificação HTTP dos parâmetros, como por exemplo um espaço entre as informações no valor de um parâmetro GET, onde a função [HttpPost](http://tdn.totvs.com/display/tec/HTTPPost) não trata automaticamente, diferentemente da aplicação Postman.  
Conforme consta na documentação da função, o tratamento deve ser realizado pela função [ESCAPE](http://tdn.totvs.com/pages/releaseview.action?pageId=6814745), seguindo o exemplo documentado.
