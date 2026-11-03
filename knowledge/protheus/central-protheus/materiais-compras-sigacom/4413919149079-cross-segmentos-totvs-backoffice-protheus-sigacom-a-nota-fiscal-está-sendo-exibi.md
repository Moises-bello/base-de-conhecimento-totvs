---
article_id: 4413919149079
category: Materiais - Compras (SIGACOM)
content_hash: 33c307b10fef7a82e0168caa7825aba10f15277fb5c514e075fef1efd07b5f46
fetched_at: '2026-06-28T22:41:13.076652+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - A nota fiscal está
  sendo exibida para retorno, mesmo após ter sido devolvida
type: support-article
updated_at: '2024-12-11T20:20:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413919149079-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-A-nota-fiscal-est%C3%A1-sendo-exibida-para-retorno-mesmo-ap%C3%B3s-ter-sido-devolvida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16596512676887) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Qual o conceito do campo f2\_flagdev na Devolução de Compras?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

O parâmetro MV\_FLAGDEV por padrão esta desativado. Com isso se o cliente tem um volume muito alto de devoluções a performance do vinculo com o documento de origem demore um pouco na carga. Definindo o parâmetro como ativado no padrão, ao realizar as devoluções, caso totalize a quantidade da nota de origem é gravado o F2\_FLAGDEV com o conteúdo = '1'.

![flag.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413938134295)

Esta nota não será mais apresentada no vínculo com documento de origem, ao tentar devolver a nota sem saldo, o help é gerado :

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413931806871)

**Saiba mais em :**

* [Conteúdo default do parâmetro MV\_FLAGDEV](https://tdn.totvs.com/x/daHaFQ)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
