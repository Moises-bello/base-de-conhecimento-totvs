---
article_id: 360000459807
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 86dd1f83062c3a3a7d1e50adabd2fec4d1b8b41a85121f3cad06b8022702b6ff
fetched_at: '2026-06-28T22:41:43.279386+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - Cálculo Mensal não
  calcula depreciação do bens e preenche o campo N3_FIMDEPR '
type: support-article
updated_at: '2022-05-09T15:16:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000459807-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-C%C3%A1lculo-Mensal-n%C3%A3o-calcula-deprecia%C3%A7%C3%A3o-do-bens-e-preenche-o-campo-N3-FIMDEPR
---

**Ocorrência**Ao calcular a depreciação ATFA050, alguns bens não estão sendo depreciados

**Ambiente**  
Protheus – Ativo Fixo – A partir da versão 12.1.17  
  
**Causa**

Esse incidente ocorre, pois o sistema  preenchendo o campo N3\_FIMDEPR .  
  
**Solução**

1. Deve-se  avaliar o valor origem do bem campo N3\_VORIG1  e comparar como o valor d depreciação acumulada do bem campo N3\_VRDACM1, quando os dois campos possuem o mesmo valor, entende-se o vem foi totalmente depreciado.
