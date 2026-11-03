---
article_id: 360018065972
category: ADVPL - Rotina Automática
content_hash: 3626d96cdac03908fd1764c98c4db8f9bfd4d6e6e8cedc2ddad28a25d8b0f08e
fetched_at: '2026-06-28T22:40:23.933629+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Cannot find function A020AUTOM
type: support-article
updated_at: '2021-12-29T13:39:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018065972-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Cannot-find-function-A020AUTOM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao Executar a ExecAuto da Mata020 apresenta cannot find function A020AUTOM.  
  
**Ambiente**Protheus – ADVPL – A partir da versão 12.1.17  
Com data do fonte MATA020M.PRX  inferior a 05/04/2018  
  
**Causa**Esse incidente ocorre, pois a função não está compilada no RPO.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Aplicar o Patch abaixo.  
[Patch A020AUTOM](https://suporte.totvs.com/portal/p/10098/download?e=679254)

2. Caso aparece o seguinte erro: "variable not an object MODELDEF MATA020MBRA", aplicar o seguinte patch.  
[Patch 2](https://suporte.totvs.com/portal/p/10098/download?e=677927)

Lembrando que se tiver com o ambiente atualizado completo não irá apresentar estes erros.
