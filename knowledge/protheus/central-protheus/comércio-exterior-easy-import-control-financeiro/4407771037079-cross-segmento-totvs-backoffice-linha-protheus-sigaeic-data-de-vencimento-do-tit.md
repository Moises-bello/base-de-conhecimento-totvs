---
article_id: 4407771037079
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 8d0a13a5eb0772e6527c6ba4e55d4b1bd912c9da2a93292bd07eb5bbb669627a
fetched_at: '2026-06-28T22:39:44.350671+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Data de vencimento
  do titulo a pagar
type: support-article
updated_at: '2023-10-06T11:49:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407771037079-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Data-de-vencimento-do-titulo-a-pagar
---

**Dúvida**Como fazer para que a data de vencimento dos títulos a pagar seja considerada a partir da data de emissão da invoice ou data de embarque?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – Todas versões  
  
**Solução**Por padrão o sistema irá contar os dias da condição de pagamento a partir da data do embarque (W6\_DT\_EMB), default definido no parâmetro **MV\_DTB\_APD**.  
Para que o sistema considere a data da emissão da invoice (W9\_DT\_EMIS) como data principal para a condição de pagamento, se faz necessário modificar o parâmetro **MV\_DTB\_APD**, incluindo no conteúdo com o valor: **W9\_DT\_EMIS.**

![MV_DTB_APD.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4407770443159)

**Saiba mais**  
[Cadastro de Condição de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028377912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Cadastro-de-Condi%C3%A7%C3%A3o-de-Pagamento-)
