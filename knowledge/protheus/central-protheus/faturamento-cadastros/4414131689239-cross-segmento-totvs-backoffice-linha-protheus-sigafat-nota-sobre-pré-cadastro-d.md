---
article_id: 4414131689239
category: Faturamento - Cadastros
content_hash: a8c540abbeb7d2b73dae30972a90bcd593ae3bda9907cf3baca2f8bc085b0278
fetched_at: '2026-06-28T22:38:35.367067+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Nota sobre pré-cadastro
  de cliente
type: support-article
updated_at: '2021-11-25T20:29:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414131689239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-pr%C3%A9-cadastro-de-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Nota sobre pré-cadastro de cliente.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

Não há uma rotina de pré-cadastro no módulo faturamento para clientes, somente o cadastro de clientes (**mata030/crma980**) em si.

Também não há esta opção em outros módulos, por que é o módulo de faturamento que é o detentor do cadastro de cliente, sendo que ele pode ser usado em vários módulos como financeiro, compras, venda assistida, etc..., mas a equipe de desenvolvimento de produto que trata o cadastro de clientes é o Faturamento, por isso, se houvesse um pré-cadastro partiria deste módulo para que outros pudessem ou não utilizar.

O que pode ser feito, de forma paliativa, é gerar o cadastro do cliente com informações básicas, como código, loja, nome de cliente, nome fantasia, endereço, tipo de cliente, estado e município, que ficaria como uma espécie de pré-cadastro e no momento que tiver as demais informações, alterar e complementar as informações para uso nas rotinas do módulo faturamento e financeiro.
