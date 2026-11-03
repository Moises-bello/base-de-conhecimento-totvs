---
article_id: 23441589408279
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: 14a37b06b3bf96bb8cc69c528c7b3fd705191662353c6e2d246a4074bc177474
fetched_at: '2026-06-28T22:36:57.358355+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Geração da Nota
  de Crédito ao cliente
type: support-article
updated_at: '2024-05-14T12:11:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23441589408279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Gera%C3%A7%C3%A3o-da-Nota-de-Cr%C3%A9dito-ao-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23441618500503) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Geração da Nota de Crédito ao cliente.  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Export Control – A partir da versão  12.1.33.

**Solução**

No *Easy Export Control* - **SIGAEEC** - rotina de Adiantamentos de Clientes - permite a escolha do usuário pela manutenção de adiantamentos entre os eventos **605 - Adiantamento do cliente e 606 - Crédito do cliente** na manutenção de adiantamentos bem como a vinculação destes adiantamentos aos adiantamentos de Pedido ou ao Adiantamento de Embarque.

Na integração do módulo **SIGAEEC** com o módulo financeiro - **SIGAFIN** - a inclusão e liquidação de adiantamento de tipo **(605 - Adiantamento do cliente)** permanecerá integrando o referente título financeiro com o tipo **"RA" - Registro de Adiantamento** - que gera movimentação bancária enquanto para o adiantamento de tipo **(606 - Crédito do cliente)** integrará o referente título financeiro com o tipo "**NCC**" - Nota de crédito ao cliente - que não gera movimentação bancária.

**Saiba mais:**[Nota de Crédito ao cliente](https://tdn.totvs.com/pages/releaseview.action?pageId=501468425)  
[Inclusão do RA por Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045568153-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Inclus%C3%A3o-do-RA-por-Cliente)  
[Inclusão do RA por Pedido de Exportação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045029634-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Inclus%C3%A3o-do-RA-por-Pedido-de-Exporta%C3%A7%C3%A3o)
