---
article_id: 19635492177047
category: TAF - REINF
content_hash: 612879ce8aac589ee7a77aab432fa32821393b74deb278c63208c4db909d6d54
fetched_at: '2026-06-28T22:41:34.663963+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Erro Schemas CompFP
type: support-article
updated_at: '2023-12-07T17:37:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19635492177047-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-Schemas-CompFP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19635487874583) Tempo aproximado para leitura: 00:04:00 min**

**Ocorrência**Ao transmitir o evento da Reinf  ocorre o erro abaixo:

![erro reinf.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19635504605207)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATAF - Todas as versões

**Causa**O problema reportado  está relacionado ao campo **compFP** esse campo tem uma validação especifica de acordo com o layout da Reinf:

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19635476500119)

Assim, se o campo não estiver no formato solicitado pelo layout da Reinf, esse erro pode ocorrer ao transmitir o evento.

**Solução**

Para corrigir este erro, verifique se o campo **Competência** na rotina de Fatura/Recibo **TAFA448** está preenchido de acordo com as validações do layout e efetue os ajustes necessários.

Caso a natureza não pertença ao grupo 10 da tabela 01, o campo competência deve permanecer em branco.

Se o campo **Ind Dec Terceiro** estiver marcado como sim, então o campo competência deve ser preenchido.

![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/19635473320215)
