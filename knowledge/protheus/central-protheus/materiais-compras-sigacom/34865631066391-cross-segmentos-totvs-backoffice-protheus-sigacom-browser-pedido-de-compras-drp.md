---
article_id: 34865631066391
category: Materiais - Compras (SIGACOM)
content_hash: b9098b28c8a1e2cbf6a66760f645d9ea0b8008bd8681a4d510850f67c9fd83fd
fetched_at: '2026-06-28T22:41:14.268148+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Browser Pedido de Compras
  - DRP Neogrid
type: support-article
updated_at: '2025-09-11T18:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34865631066391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Browser-Pedido-de-Compras-DRP-Neogrid
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34865631042839) Tempo aproximado para leitura: **00:02:SS min**  
  
**Dúvida**

No Browser do Pedido de Compras aparece a coluna DRP Neogrid  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras  - Versão 12

**Solução**

A coluna DRP Neogrid esta sendo apresentada no browser devido o campo C7\_DRPIMP, estar marcado no browse, campo que relacionado a Neogrid.

Para desabilitar a coluna, seguir os procedimentos á seguir;

Acesse o CFG -> Vá até a tabela SC7 e no campo C7\_DRPIMP, e desmarque a opção Browser como usado;

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34865642953623)

Após alterações o campo não estará disponível no Browser;

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34865631046423)

Saiba mais 

[DT MV\_LJDRP](https://tdn-homolog.totvs.com/display/public/PROT/DT+MV_LJDRP)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
