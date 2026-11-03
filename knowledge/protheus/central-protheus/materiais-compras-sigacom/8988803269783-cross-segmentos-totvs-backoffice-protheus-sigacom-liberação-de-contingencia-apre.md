---
article_id: 8988803269783
category: Materiais - Compras (SIGACOM)
content_hash: 0834f964681af12584acb6b8e8e08924fa8aeda2b124ce2ec5e08cb2b4596291
fetched_at: '2026-06-28T22:41:20.031544+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Liberação de contingencia  apresenta
  a mensagem "Chave não encontrada [CO+Centro de Custo+ItemConta]"
type: support-article
updated_at: '2022-09-19T18:45:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8988803269783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Libera%C3%A7%C3%A3o-de-contingencia-apresenta-a-mensagem-Chave-n%C3%A3o-encontrada-CO-Centro-de-Custo-ItemConta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00min****Ocorrência**Ao tentar liberar um pedido de compras pela contingência do PCO, o sistema apresenta a mensagem "**Chave não encontrada [CO+Centro de Custo+ItemConta]**"  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Compras - Todas as versões  
  
**Causa**Divergência entre os campos **ALJ\_CC, AKD\_CC e C7\_CC** .  
  
**Solução**Quando essa mensagem é apresentada, é necessário verificar se os campos **ALJ\_CC, AKD\_CC e C7\_CC** estão com o mesmo tamanho. Isso ocorre pois o campos **ALJ\_CC** não esta dentro do grupo de campos onde estão **AKD\_CC e C7\_CC**.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
