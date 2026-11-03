---
article_id: 360025674571
category: BI - Business Intelligence - Crystal-Reports
content_hash: 70bfb1cc48051967a0aff1bd1dd504b54c71796011f19b64b65dff807707d916
fetched_at: '2026-06-28T22:40:28.968516+00:00'
product: protheus
section_id: 1500001548282
source: central-protheus
title: ' Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Relatório Crystal
  não funciona via Schedule'
type: support-article
updated_at: '2023-09-15T04:34:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025674571--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Relat%C3%B3rio-Crystal-n%C3%A3o-funciona-via-Schedule
---

![](https://jiratdncdncontent.blob.core.windows.net/tdn/icons/time.png) Tempo aproximado para leitura: **1 minuto****Ocorrência**Erro: Function GetClientDir() doesn't available in JOB.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – Crystal Reports – A partir da versão 12  
  
**Causa**Nos binários anteriores o sistema não fazia validações de componentes visuais nas execuções via **Schedule**, onde só eram gerados eventuais críticas e não **error.log.** Após a expedição da última versão do binário, o sistema está fazendo tal validação. Sendo assim, não será possível executar este relatório via job.  
  
**Solução**Para utilização de relatórios via **Schedule**, sugerimos o desenvolvimento dos mesmos via **ADVPL**. No entanto, será necessário conhecimento da linguagem por parte do desenvolvedor. Do contrário, o cliente precisará do auxílio de um consultor para implementar a solução.
