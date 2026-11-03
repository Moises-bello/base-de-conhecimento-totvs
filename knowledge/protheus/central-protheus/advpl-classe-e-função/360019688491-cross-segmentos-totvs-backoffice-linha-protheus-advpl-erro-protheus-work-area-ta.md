---
article_id: 360019688491
category: ADVPL - Classe e Função
content_hash: 3a9ad2b21b01208ad5fb20113a2ed4dbba179f597a25566ad2fb6e33a2d7501d
fetched_at: '2026-06-28T22:40:19.249518+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro: protheus
  work area table full (max=1024)'
type: support-article
updated_at: '2024-10-15T18:41:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019688491-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-protheus-work-area-table-full-max-1024
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao executar processos que manipulam diversas tabelas, o erro abaixo é exibido:

```
Protheus Work area table full (Max= 1024) 
```

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Este erro acontece quando são abertas mais de 1024 tabelas ao mesmo tempo e não são fechadas após cada manipulação (comumente presente na execução de uma rotina automática por diversas vezes).  
  
**Solução**Adaptar a customização para verificar as tabelas que estão sendo abertas e fechá-las após a execução de cada inserção por meio da rotina automática ou procedimento realizado na customização.
