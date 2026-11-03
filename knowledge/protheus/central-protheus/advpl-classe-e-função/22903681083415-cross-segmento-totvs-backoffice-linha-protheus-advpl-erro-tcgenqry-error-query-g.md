---
article_id: 22903681083415
category: ADVPL - Classe e Função
content_hash: 1c73d143e4bacc9209e0780010c8c0968e21f9a2d2953c98c10ffe9a8903cb1e
fetched_at: '2026-06-28T22:40:20.710360+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: TCGenQry
  Error - Query greater than 31960 bytes.'
type: support-article
updated_at: '2024-04-18T19:09:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22903681083415-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-TCGenQry-Error-Query-greater-than-31960-bytes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22903710458263)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao utilizar a classe TCGenQry é apresentado o erro: TCGenQry Error - Query greater than 31960 bytes.  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**O limite máximo é 65536 bytes, caso a query ultrapasse este limite o responsável por seu desenvolvimento deverá reavaliar a mesma a fim de reduzir o seu tamanho, buscando alternativas que não usem queries tão longas.

**Solução**

Realizar ajuste no tamanho máximo da configuração MaxQuerySize.

```
[General]  
MaxQuerySize=65536
```

Obs: Esta configuração pode ser especificada diretamente na seção do ambiente (environment) em uso, atuando unicamente sobre ele.

**Saiba mais**

[MaxQuerySize](https://tdn.totvs.com/display/tec/MaxQuerySize)

[Filter greater than 2000 bytes](https://tdn.totvs.com/display/tec/Filter+greater+than+2000+bytes)
