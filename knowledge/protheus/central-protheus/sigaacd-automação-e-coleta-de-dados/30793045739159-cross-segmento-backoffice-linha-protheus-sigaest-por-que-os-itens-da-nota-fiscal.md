---
article_id: 30793045739159
category: SIGAACD - Automação e Coleta de Dados
content_hash: 115b85bd418c9efb112c76ab8fa988adfca58243cfd3c9b86272b5f21ae6c02a
fetched_at: '2026-06-28T22:39:13.902878+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Por que os itens da
  nota fiscal (SD1) são excluídos quando faço a conferência da pré-nota?
type: support-article
updated_at: '2025-03-20T18:30:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30793045739159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Por-que-os-itens-da-nota-fiscal-SD1-s%C3%A3o-exclu%C3%ADdos-quando-fa%C3%A7o-a-confer%C3%AAncia-da-pr%C3%A9-nota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30793045732503) Tempo aproximado para leitura: **00:01:08 min** **Dúvida**Por que os itens da nota fiscal (SD1) são excluídos quando faço a conferência da pré-nota?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

A rotina ACDV120 utiliza uma tabela auxiliar – CBE – para gravar as conferências físicas realizadas no recebimento dos materiais. Dessa forma, a cada item lido na SD1, é gravado um correspondente na tabela CBE, porém com as particularidades da conferência, como lote, sublote etc.

Ao final da conferência, todos os itens da SD1 são excluídos e é feita uma leitura da tabela CBE para criação de novos registros na SD1, conforme a ordem que foram gerados na CBE.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
