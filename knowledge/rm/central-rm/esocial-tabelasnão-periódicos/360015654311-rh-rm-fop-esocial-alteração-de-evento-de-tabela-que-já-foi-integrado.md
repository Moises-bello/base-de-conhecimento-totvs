---
article_id: 360015654311
category: eSocial - Tabelas/Não Periódicos
content_hash: 7adcce9dd315fa87708fd77cbb6cfcf1d50c2199fa21cae50a979f42ac3409e9
fetched_at: '2026-06-28T22:47:10.245799+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Alteração de evento de tabela que já foi integrado
type: support-article
updated_at: '2024-06-27T15:28:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015654311-RH-RM-FOP-eSocial-Altera%C3%A7%C3%A3o-de-evento-de-tabela-que-j%C3%A1-foi-integrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24476801357591)Tempo aproximado para leitura:00:02:00 min  
  
Dúvida**Como realizar uma alteração para evento de tabela que já foi integrado com o TAF ou governo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial- Todas as versões  
  
**Solução**Quando existe um evento de tabela na fila de eventos com status igual a **3 - Enviado para o TAF**, **4 - Aceito TAF** ou **10 - Aceito RET** e o registro é alterado no RM, será gerado um novo gatilho na fila de eventos.

1. Vamos utilizar como exemplo o evento S-1005. Abaixo é possível verificar a existência de um evento S-1005 para a seção 03 com status **4 - Aceito TAF**. 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041409874)

2. Ao editar a seção 03 alterando determinada informação registrada no S-1005, é gerado um novo gatilho com tipo de operação **Alteração** e status **Pendente.**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042248793)**

3. Se o gatilho foi excluído indevidamente da fila de eventos, será necessário a inclusão manual deste registro para transmissão ao eSocial. O **Tipo de Operação** deverá ser **Alteração** (assim como gerado no gatilho automático)e a **Competência** deve corresponder ao mês da devida alteração.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041410814)

4. Se o evento tiver sido transmitido para o governo com informações incorretas, deve-se retificá-lo incluindo manualmente um gatilho com **Tipo de Operação** como **Retificação** e **Competência** igual a informada no XML do evento de inclusão/alteração.
