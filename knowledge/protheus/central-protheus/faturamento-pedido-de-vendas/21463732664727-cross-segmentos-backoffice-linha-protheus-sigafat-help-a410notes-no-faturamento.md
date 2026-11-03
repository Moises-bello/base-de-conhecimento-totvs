---
article_id: 21463732664727
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b8504c9d642e3e5ebdc9c3a9fcdb8eabbf734f2f13300d25e801e9b99168c5d2
fetched_at: '2026-06-28T22:38:39.596297+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Help A410NOTES no
  Faturamento
type: support-article
updated_at: '2024-02-20T11:43:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21463732664727-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Help-A410NOTES-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21463732632343) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**

Como resolver o Help A410NOTES?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Esse erro ocorre quando o sistema considera a TES inválida, motivos:

1 - Cheque se a TES no campo C6\_TES é maior que 500, não pode ser.

2 - Cheque se a tabela SF4 está exclusiva por filial e a filial da tabela SC6 é uma filial diferente da mesma.

3 - Cheque se o campo C6\_TES está no padrão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21463732634391)![](https://centraldeatendimento.totvs.com/hc/article_attachments/21463732640407)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21463763746199)

4 - Cheque se há gatilhos customizados na tabela SC6 ou se foi alterado os gatilhos do padrão. Filtre por X7\_CDOMIN = 'C6\_TES' e X7\_PROPRI diferente de 'U'. Teste sem eles.

5 - Cheque se a TES informada existe na tabela SF4 "TES".

6 - Certifique-se que não há pontos de entrada influenciando em qualquer vertente do processo.
