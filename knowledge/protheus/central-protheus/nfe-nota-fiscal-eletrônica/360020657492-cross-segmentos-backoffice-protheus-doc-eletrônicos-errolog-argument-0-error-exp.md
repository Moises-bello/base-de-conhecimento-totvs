---
article_id: 360020657492
category: NFe - Nota Fiscal Eletrônica
content_hash: 3d3f3eb26034578314dd7d4edc9b5af977531251aa35b709a0603f3e11b98e5d
fetched_at: '2026-06-28T22:40:01.842775+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Erro.log  argument
  #0 error, expected C->U, function XmlParser '
type: support-article
updated_at: '2021-10-11T14:26:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020657492--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Erro-log-argument-0-error-expected-C-U-function-XmlParser
---

**Dúvida**Como corrigir o  erro.log **argument #0 error, expected C->U, function XmlParser ?**  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O erro ocorre, no momento da transmissão devido a **existência de carácter especial no conteúdo da nota.**  
  
 É necessário revisar os cadastros utilizados e **remover os caracteres especiais,** geralmente esses caracteres ficam no cadastro do cliente/fornecedor, nome do produto e informações complementares.  
  
Após remover os caracteres a NFe deve ser refeita para gerar um novo XML com as **informações corretas.**
