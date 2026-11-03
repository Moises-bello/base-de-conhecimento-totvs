---
article_id: 23926593195287
category: NFe - Nota Fiscal Eletrônica
content_hash: 7eda9bb8d6ecfe1e215c58e85f3cd783b2ad7467eda970b36fffbeb7c2242e2b
fetched_at: '2026-06-28T22:40:00.130382+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2024.002
  ECONF
type: support-article
updated_at: '2025-06-06T18:28:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23926593195287-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2024-002-ECONF
---

**Dúvida**

Quais serão as alterações da Nota Técnica 2024.002?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS

**Solução**

Para a adequação à **Nota Técnica 2024.002 v.1.00.**

O prazo previsto para a **Nota Técnica 2024.002 v.1.00:**

Ambiente de Homologação **(ambiente de teste das empresas): 01/07/2024**

Ambiente de Produção: **02/09/2024**

1. Atualização do ambiente Protheus:

Atualizar o repositório com o último pacote de expedição continua do Protheus disponível no link:

12.1.2210 (Para clientes com garantia estendida): <https://r.totvs.io/p/1163049>

12.1.2310: <https://r.totvs.io/p/1163047>

12.1.2410: <https://r.totvs.io/p/1163050>

2. Atualização do ambiente TSS:

12.1.2210: <https://r.totvs.io/p/1162553>

12.1.2310: <https://r.totvs.io/p/1162554>

12.1.2410: <https://r.totvs.io/p/1162556>

**É necessário atualizar o arquivo tssatuurl.json referente as URLs, também encontrado no pacote da issue DSERTSS1-23539**

Caso tenha dúvidas de como aplicar patch no RPO do TSS:

[MP - TSS - Como aplicar patch no TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24560205471383-MP-TSS-Como-aplicar-patch-no-TSS#:~:text=Clique%20em%20%22Escolher%20Arquivos%22%20item%20%282%29%2C%20navegue%20at%C3%A9,indicar%20os%20arquivos%20que%20foram%20atualizados%20nessa%20patch.)

Caso ocorra o erro Server returned: Duplicated function na aplicação verificar documentação abaixo:

[MP - TSS - Server returned: Duplicated function](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008076022-MP-TSS-Server-returned-Duplicated-function)

Mais informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=865409531>

Para visualizar o passo a passo do envio do evento acessar a documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Evento de Conciliação Financeira - ECONF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26187512116375-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Evento-de-Concilia%C3%A7%C3%A3o-Financeira-ECONF)
