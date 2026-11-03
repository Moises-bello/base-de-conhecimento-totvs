---
article_id: 23940229501207
category: NFe - Nota Fiscal Eletrônica
content_hash: fd4757ba4c0ee8c6203b46573dd53aec527ef3c7b56b33186cd4f8f101cd96b8
fetched_at: '2026-06-28T22:40:07.171119+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 965: Valor
  do troco acima do permitido'
type: support-article
updated_at: '2024-06-04T14:45:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23940229501207-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-965-Valor-do-troco-acima-do-permitido
---

**Dúvida**Como corrigir a Rejeição 965: Valor do troco acima do permitido?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

**Solução**

A regra de validação da Sefaz, diz o seguinte:

Valor do troco (id:YA09, tag:vTroco) superior a R$ 1.000,00

![](https://atendimento.tecnospeed.com.br/hc/article_attachments/22108734901527)

A Rejeição 965 pode ocorrer quando uma NF-e for emitida com a tag vTroco\_YA09 superior a R$ 1.000,00

Como Resolver:

Para resolver a Rejeição 965: Valor do troco acima do permitido, verifique se o grupo de cartões foi informado para um tipo de pagamento diferente de 03, 04, 10, 11, 12, 13, 15, 17 e 18, caso sim, o mesmo deverá ser removido.

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Conceito das Condições de Pagamento:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG tPag (forma de pagamento / duplicata / fatura)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-tPag-forma-de-pagamento-duplicata-fatura)

* [Nota Técnica 2023.004 -v.1.10 - Publicada em 02/02/2024](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=#:~:text=Nota%20T%C3%A9cnica%202023.004%20%2Dv.1.10%20%2D%20Publicada%20em%2002/02/2024)
