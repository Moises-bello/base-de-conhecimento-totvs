---
article_id: 360021074152
category: ADVPL - Ponto de Entrada
content_hash: c3c63a0105c0e4c42cebc63f337fc50cebf04505a021e6c0e4216425c1df354c
fetched_at: '2026-06-28T22:40:12.799805+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de entrada
  MT130COL e MT130HED não são chamados na MATA131
type: support-article
updated_at: '2021-12-30T17:00:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021074152-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pontos-de-entrada-MT130COL-e-MT130HED-n%C3%A3o-s%C3%A3o-chamados-na-MATA131
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Utilização dos pontos de entrada **MT130COL** e **MT130HED** na versão 12

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**Os pontos de entrada **MT130COL** e **MT130HED** existentes no fonte **MATA130**, não existem mais no fonte **MATA131**, os pontos de entrada citados não foram migrados para o **MATA131** e não é possível fazer da maneira que eles foram construídos, pois o **MATA131** esta em **MVC** e não tem mais o **aHeader** e o **aCols** para serem passados via parâmetro para o ponto de entrada.
