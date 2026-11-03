---
article_id: 8192661227415
category: Comércio Exterior - Easy - Financing
content_hash: c6ceca624504db6c02fbbefb9d8caa01238d98ac522ff752b68fdf0f3dcfefe2
fetched_at: '2026-06-28T22:39:52.969910+00:00'
product: protheus
section_id: 1500001538101
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEFF - Cálculo do evento
  Provisão de juros ACC
type: support-article
updated_at: '2022-08-15T20:24:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8192661227415-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEFF-C%C3%A1lculo-do-evento-Provis%C3%A3o-de-juros-ACC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como é realizado o cálculo do evento Provisão de juros ACC (520/521) ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Financing- Todas as versões  
  
**Solução**Provisão de juros ACC (520) contendo o valor dos juros devidos da data de Início de juros até a data da vinculação da invoice, o cálculo será feito da seguinte maneira:  
**VV** = Valor Vinculado (na moeda do contrato)  
**DI** = Data de Início de Juros  
**DV** = Data de Vinculação  
**QD** = Quantidade de Dias  
**TX** = Taxa Diária de Juros  
**PJ** = Provisão de Juros (na moeda do contrato)  
  
Formula:

```
QD = ( DV – DI ) + 1
```

```
Exemplo:   
QD = (05/06/06 – 01/06/06) + 1  
QD = 5
```

Formula:

```
PJ = VV * QD * TX
```

```
Exemplo:  
PJ = 1.000,00 * 5 * 0,05%  
PJ = 2,50
```

O código do evento depende do tipo de juros a que se refere, por exemplo:

|  |  |
| --- | --- |
| **TIPO DE JUROS** | **EVENTO** |
| 0 | 520 |
| 1 | 521 |
