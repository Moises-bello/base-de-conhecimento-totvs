---
article_id: 360027154371
category: Comércio Exterior - Easy Import Control - Entreposto
content_hash: 3d3220dabc267ffa9ead0d839658f2c7494f726c19f60c3ea1ee9c43af25e543
fetched_at: '2026-06-28T22:39:46.038374+00:00'
product: protheus
section_id: 1500001549622
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem nota
  fiscal não pode ser gerada, processo refere-se a uma D.A.
type: support-article
updated_at: '2024-06-03T12:11:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027154371-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-nota-fiscal-n%C3%A3o-pode-ser-gerada-processo-refere-se-a-uma-D-A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23439579265175)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual o procedimento a ser feito quando apresentar a mensagem "Nota Fiscal não pode ser gerada, processo refere-se a uma D.A"?   
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus– *Easy Import Control* – A partir da versão 11.80  
  
**Solução**Se o processo for de Entreposto Aduaneiro, deve ser preenchido o campo **W6\_TIPODES** "Tipo de Declaração" com o código **"14 - NACIONALIZAÇÃO DE ENTREPOSTO ADUANEIRO"** .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027307691)

Caso seja um processo de consumo preencha com campo **W6\_TIPODES "Tipo de Declaração"** com o código **"01 - CONSUMO"** , ou deixar o campo em branco.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027307731)

**Saiba mais**[Entreposto aduaneiro](http://tdn.totvs.com/display/public/PROT/EIC0012_Entreposto)
