---
article_id: 4407193041559
category: Faturamento - Cadastros
content_hash: 55e3479148f3874e60d473f0772086249900da63e986f06881f76461469400a8
fetched_at: '2026-06-28T22:38:35.362098+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- É possível atribuir
  mais de uma tabela de preço (OMSA010) para o mesmo cliente
type: support-article
updated_at: '2021-08-26T19:27:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407193041559-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-%C3%89-poss%C3%ADvel-atribuir-mais-de-uma-tabela-de-pre%C3%A7o-OMSA010-para-o-mesmo-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**É possível atribuir mais de uma tabela de preço (OMSA010) para o mesmo cliente?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Não é possível, hoje no padrão, se consegue amarrar apenas uma tabela  através do campo **a1\_tabela**.

Não há uma saída de contorno, por que ao selecionar o cliente no pedido, será apresentada a tabela que está associada ao cadastro do cliente via campo **a1\_tabela**, outra forma, só escolhendo manualmente diretamente no pedido de vendas (**MATA410**). 

Não há ponto de entrada no cabeçalho do pedido que possibilite um tratamento diferente.

Ainda dentro do padrão de sistema, é possível ter uma única tabela e esta tabela ser utilizada por mais de um cliente , um relacionamento de 1 para N. ou criar várias tabelas individuais, associar a tabela a um cliente específico, gerando um relacionamento 1 para 1,tudo dependerá da regra de negócio de cada cliente.
