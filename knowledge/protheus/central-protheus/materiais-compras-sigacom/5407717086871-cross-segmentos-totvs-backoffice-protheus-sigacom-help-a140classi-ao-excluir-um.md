---
article_id: 5407717086871
category: Materiais - Compras (SIGACOM)
content_hash: e9371873c60a49eafe9d91aa92b9d616804f9d6be2d96ce0f34d7ecb6c09c9d1
fetched_at: '2026-06-28T22:41:18.881029+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP A140CLASSI ao
  excluir um documento de entrada
type: support-article
updated_at: '2025-03-11T10:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5407717086871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A140CLASSI-ao-excluir-um-documento-de-entrada
---

**Ocorrência**Ao tentar excluir um documento de entrada na rotina MATA140 apresenta o HELP A140CLASSI:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5407557044119/mceclip1.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões.  
  
**Causa**O HELP A140CLASSI é apresentado, pois indica que o campo D1\_TES ou o D1\_TESACLA, já encontra-se  preenchido.

**Solução**Verifique se na pré nota que está tentando excluir os campos D1\_TES  e D1\_TESACLA estão preenchidos.

Caso estejam é necessário que fiquem em branco para que o sistema entenda que não há classificação nessa pré nota e permita a exclusão da mesma.  
   
Caso o D1\_TES esteja em branco, verifique o campo D1\_TESACLA. Pois na opção classificar no documento de entrada, se por acaso a classificação foi cancelada por algum motivo, o sistema pergunta se quer salvar as alterações efetuadas até o momento do cancelamento. Se clicar em Sim, o sistema gravará o D1\_TESACLA.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5407629830679/mceclip2.png)

![](https://totvssuporte.zendesk.com/attachments/token/mXHMsUQazBeVYvfnwv3LG9ZoI/?name=inline-1674719261.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5407660046359/mceclip3.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
