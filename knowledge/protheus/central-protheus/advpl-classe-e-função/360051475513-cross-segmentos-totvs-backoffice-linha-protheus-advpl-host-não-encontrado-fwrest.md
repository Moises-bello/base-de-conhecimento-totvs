---
article_id: 360051475513
category: ADVPL - Classe e Função
content_hash: e12dbfd4c90fcbcc5e523e12edf1d402fe9aa38c8016002c3dcec7451776fe85
fetched_at: '2026-06-28T22:40:19.568628+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Host não encontrado
  FwRest
type: support-article
updated_at: '2022-01-11T18:13:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051475513-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Host-n%C3%A3o-encontrado-FwRest
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Estou utilizando a Classe **FwRest()**, porém retorna erro:

```
Host não encontrado
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**esse erro significa que causou um problema no recurso interno utilizado para identificar os valores dos **headers**. Como os **headers** também fazem parte da requisição, é preferível cancelar todo o processo, do que permitir seguir.  
Como sempre, os casos que envolvem ferramentas de terceiros (**Postman**, **Insomnia**, **SoapUi**, **curl**, etc) precisam ter sua relevância reconsiderada pois eles implementam serviços e tratamentos que podem não fazer sentido para funções do **ERP**.  
  
 **Solução**Como alternativa, utilize a função **HTTPGET**, para realizar a requisição, pois ela não valida o **header****Saiba mais**[HttpGet](https://tdn.totvs.com/display/tec/HTTPGet)
