---
article_id: 22658426125847
category: NFe - Nota Fiscal Eletrônica
content_hash: 3b45869ae035387984eadb9413cd54b3e44d09dedf4f93f6db59bafaca9aba4f
fetched_at: '2026-06-28T22:40:07.145282+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 769 - Obrigatório
  o preenchimento da Quantidade tributada retida anteriormente
type: support-article
updated_at: '2026-02-19T13:22:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22658426125847-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-769-Obrigat%C3%B3rio-o-preenchimento-da-Quantidade-tributada-retida-anteriormente
---

**Dúvida**Como solucionar a rejeição abaixo:

Rejeição 769 - Obrigatório o preenchimento da Quantidade tributada retida anteriormente ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A rejeição ocorre quando esta emitindo nota usando CST 61 com ST MONO e não gerar o valor da tag qBCMonoRet

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22658956554135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22658426111127)

Informações retidas da NT 2023.001– Tributação Monofásica sobre Combustíveis

As informações que geram o grupo da tag ICMS61 são retiradas da tabela CD2 na linha STMONO.

![](https://totvssuporte.zendesk.com/attachments/token/biHukxm1QDmAleQDSVhYYAWDz/?name=image.png)

Para a gravação da tabela CD2 com o grupo STMONO verifique a documentação abaixo:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - COMO GERAR O STMONO 61 NO FISA170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15741756726423-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-COMO-GERAR-O-STMONO-61-NO-FISA170?source=search)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - MP FIS Como gerar a Devolução do CST61 STMONO ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17500823205143-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-gerar-a-Devolu%C3%A7%C3%A3o-do-CST61-STMONO?source=search)

Atualizações necessárias do Protheus e TSS para o correto funcionamento estão na documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2023.001](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12928311594903-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2023-001?source=search)

Informações relevantes:

<https://tdn.totvs.com/pages/releaseview.action?pageId=765332384>
