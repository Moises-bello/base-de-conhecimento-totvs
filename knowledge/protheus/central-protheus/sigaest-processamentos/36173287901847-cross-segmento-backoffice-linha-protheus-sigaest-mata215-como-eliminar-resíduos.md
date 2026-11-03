---
article_id: 36173287901847
category: SIGAEST - PROCESSAMENTOS
content_hash: 110689ced77c7e77ad771109cbe594cf643dc0f4f9368b3ac012d4eacc363707
fetched_at: '2026-06-28T22:39:04.910084+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Como eliminar
  resíduos de Solicitação ao Armazém e Pré-Requisição
type: support-article
updated_at: '2025-11-07T12:15:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36173287901847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Como-eliminar-res%C3%ADduos-de-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-e-Pr%C3%A9-Requisi%C3%A7%C3%A3o
---

Para eliminar resíduos de Solicitação ao Armazém (S.A) e Pré-Requisição no Protheus, execute a rotina "Refaz Acumulado" para recalcular acumulados e ajustar divergências. Verifique o campo "Qtd. Empenhada por S.A" para identificar quantidades empenhadas. Se o empenho não for mais utilizado, encerre a S.A na rotina MATA185, devolvendo o empenho ao saldo disponível para novas requisições.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36173287894935) Tempo aproximado para leitura: 00:02:00 min  
  
**Dúvida**  
Como eliminar resíduos de Solicitação ao Armazém e Pré-Requisição no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Para eliminar resíduos de Solicitação ao Armazém (S.A) e Pré-Requisição, siga conforme o caso:

1. **Quando houver resíduos de movimentação:**

* Execute a rotina **Refaz Acumulado** (Miscelânea > Processamento > Refaz Acumulado).
* Essa rotina recalcula os acumulados do módulo, ajustando possíveis divergências e eliminando resíduos pendentes.
* Verifique o campo **“Qtd. Empenhada por S.A” (B2\_QEMPSA)** conforme descrito no artigo da TOTVS para identificar quantidades ainda empenhadas por S.A.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo "Qtd. Empenhada por SA" (B2\_QEMPSA) no F4 do Produto dentro da rotina MATA010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021553532-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-Qtd-Empenhada-por-SA-B2-QEMPSA-no-F4-do-Produto-dentro-da-rotina-MATA010)

**2. Quando se tratar de empenho que não será mais utilizado:**

* Acesse a rotina **MATA185 – Solicitação ao Armazém**.
* Localize a S.A. e **encerre** o documento.
* Ao encerrar, o sistema **devolve o empenho ao saldo disponível**, permitindo o uso em novas requisições.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Lentidão ou Travamento no Processamento Refaz Acumulados/Empenhos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8891836908311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Lentid%C3%A3o-ou-Travamento-no-Processamento-Refaz-Acumulados-Empenhos)
