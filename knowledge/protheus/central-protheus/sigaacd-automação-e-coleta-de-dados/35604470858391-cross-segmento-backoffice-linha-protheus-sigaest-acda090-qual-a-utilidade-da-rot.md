---
article_id: 35604470858391
category: SIGAACD - Automação e Coleta de Dados
content_hash: 4caa2634ec0f5828821b76ae41b71b7a9076e52d9f932261946e159274cb54d5
fetched_at: '2026-06-28T22:39:13.900050+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ACDA090 - Qual a utilidade
  da rotina Amarração Produto x Endereço?
type: support-article
updated_at: '2025-10-13T20:12:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35604470858391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ACDA090-Qual-a-utilidade-da-rotina-Amarra%C3%A7%C3%A3o-Produto-x-Endere%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35604470846231) Tempo aproximado para leitura: **00:02:11 min**  
  
**Dúvida**  
Qual a utilidade da rotina Amarração Produto x Endereço?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A rotina de Amarração Produto x Endereço (ACDA090) é uma rotina destinada à cadastrar as Sugestões de Endereços que serão utilizados na rotina de Preparação de Endereçamento (ACDV220).  
  
Já a rotina de Preparação de Endereçamento (ACDV220) é destinada aos cenários onde a Etiqueta de Produto (CB0) é gerada no ato do cadastro do Pedido de Compra (SC7) e, ao utilizá-la, o campo Endereço Sugerido (CB0\_ENDSUG) será preenchido com o endereço escolhido durante a Preparação de Endereçamento.  
  
Vale ressaltar que o preenchimento do campo Endereço Sugerido (CB0\_ENDSUG) por meio da rotina de Preparação de Endereçamento (ACDV220) não irá impedir que o produto seja posteriormente endereçado para um endereço diferente (até mesmo para um endereço não relacionado na Amarração Produto x Endereço), pois trata-se somente de uma sugestão. Sendo assim, essa rotina não prevê delegar para qual endereço o produto irá.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
