---
article_id: 18920283371543
category: Financeiro - Aplicação / Emprestimos
content_hash: 400529e6c7156ab04b36d68c4b2a8d43ba5b8d803e496eb253262f134987a240
fetched_at: '2026-06-28T22:37:59.555643+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR820 - Como é composto
  a coluna SALDO no relatório "Demonstrativo de Aplicações" de uma aplicação FAF
type: support-article
updated_at: '2023-11-08T17:45:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18920283371543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR820-Como-%C3%A9-composto-a-coluna-SALDO-no-relat%C3%B3rio-Demonstrativo-de-Aplica%C3%A7%C3%B5es-de-uma-aplica%C3%A7%C3%A3o-FAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18920291748119) Tempo aproximado para leitura: **00:10:00 min****Dúvida**

Como é composto a coluna SALDO no relatório "Demonstrativo de Aplicações" em uma aplicação FAF?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Hoje existem vários tipos de saldo, são eles:

**SALDO** sem o rendimento da aplicação e sem descontar os impostos (ex: **IR / IOF**)

**SALDO** que é soma do rendimento e sem descontar os impostos (ex: **IR / IOF**)

**SALDO** que é soma do rendimento com os descontos dos impostos (ex: **IR / IOF**)

Logo a coluna **SALDO** do relatório **FINR820** seria o "**SALDO** sem o rendimento da aplicação e sem descontar os impostos (ex: **IR / IOF)**"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18920298636311)](https://totvssuporte.zendesk.com/guide-media/01HEQZ9W5K5W0SFSC5KF9BFF04)

Neste relatório também tempos a coluna "**Resgate Líquido**" que seria:

**SALDO** que é soma do rendimento com os descontos dos **impostos** (ex: **IR / IOF**)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18920275281431)](https://totvssuporte.zendesk.com/guide-media/01HEQZFD2AH9Y0GD415MPGR9WJ)

Ou

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18920306572439)](https://totvssuporte.zendesk.com/guide-media/01HEQZKT94NVKDZCB19S97AMKZ)

Ao visualizar na tela da inclusão da aplicação **FAF**, veja que possui um campo chamado "**SALDO**" que seria:

**SALDO** que é soma do rendimento e sem descontar os impostos (ex: **IR / IOF**)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18920298656407)](https://totvssuporte.zendesk.com/guide-media/01HEQZQ70Z64X9XHV58MFX8G27)

No relatório **FINR820** para a coluna **SALDO**, logo se não houver resgate da aplicação, irá demonstrar o mesmo valor inicial da aplicação, pois é:

**SALDO** sem o rendimento da aplicação e sem descontar os impostos (ex: **IR / IOF**)

Logo ao aplicar 75mil, e durante um período não houver resgate, ao emitir o relatório o **saldo** será também será de 75 mil.

**Saiba mais:**

[Demonstrativo de Aplicações (FINR820)](https://tdn.totvs.com/pages/releaseview.action?pageId=676591375)

[Aplicações e Empréstimos - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=392500138)

[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)
