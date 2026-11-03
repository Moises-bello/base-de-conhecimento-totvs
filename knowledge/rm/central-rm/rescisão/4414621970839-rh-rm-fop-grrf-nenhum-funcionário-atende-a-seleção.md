---
article_id: 4414621970839
category: Rescisão
content_hash: a996c996f73139dc1c502d1e0fa92e58ed50b39d327954623219ec102de31958
fetched_at: '2026-06-28T22:46:54.439370+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH- RM - FOP - GRRF: Nenhum funcionário atende a seleção'
type: support-article
updated_at: '2025-01-21T18:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414621970839-RH-RM-FOP-GRRF-Nenhum-funcion%C3%A1rio-atende-a-sele%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:06 min****Ocorrência**No módulo Folha de Pagamento, ao gerar a GRRF para funcionário com o tipo de demissão 8- Falecimento está apresentando a seguinte mensagem: **Nenhum funcionário atende a seleção**.   
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois para rescisão do tipo **8 -Falecimento** e tipo **4 - Iniciativa do empregado sem justa causa** não há recolhimento de multa do FGTS.  
  
**Solução**Para a rescisão com o tipo de demissão **8 -Falecimento** não há recolhimento de multa do FGTS. Portanto, não é necessário gerar a Guia de Recolhimento Rescisório do FGTS.  
  
A GRRF será gerada apenas para os tipos:

* **2-** Iniciativa Empregador sem justa causa
* **T-** Término de contrato de trabalho
* **V-** Comum acordo

**Saiba Mais** [Geração GRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=311065074)  
[GRRF - Guia de Recolhimento Rescisório do FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=452719518)
