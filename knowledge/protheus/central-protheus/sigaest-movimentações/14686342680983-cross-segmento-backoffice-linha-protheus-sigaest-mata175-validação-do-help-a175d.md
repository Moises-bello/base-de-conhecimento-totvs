---
article_id: 14686342680983
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1b5dbadccf7a0f3dd6e784695962b5ced38c5a1653e7f32e9af0a47cf5e7e298
fetched_at: '2026-06-28T22:38:55.787478+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 - Validação
  do Help A175DATA
type: support-article
updated_at: '2023-05-18T19:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14686342680983-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-Valida%C3%A7%C3%A3o-do-Help-A175DATA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:12 min** **Dúvida**O que causa a exibição do help A175DATA na rotina de Liberação de CQ (MATA175)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O Help ocorre quando a tentativa de liberação do C.Q ocorre numa data anterior à data do saldo original que chegou ao CQ. Também acontece quando a data do saldo original que chegou ao CQ é superior à data-base do Sistema. Veja abaixo exemplos:

Produto **PA-0001** chegou ao armazém de C.Q no dia 19/05/2023 mas a data-base do Sistema está em 18/05/2023.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14686149173271)

Ao tentar salvar ou pressionar a seta para baixo, ocorrerá o Help:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14686135704727)

Nestes cenários é recomendável validar:

- Se o movimento que originou o Saldo no armazém de CQ foi com data futura à data atual, validando se realmente foi um erro de digitação e se poderá estornar o movimento;

- Checar se a data-base não está retroagida ao acessar a rotina MATA175.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
