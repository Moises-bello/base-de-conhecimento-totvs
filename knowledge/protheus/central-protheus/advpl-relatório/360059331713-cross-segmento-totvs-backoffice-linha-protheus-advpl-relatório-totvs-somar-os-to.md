---
article_id: 360059331713
category: ADVPL - Relatório
content_hash: d7d257993dbe39f13701e8f83b1e140606e3f02f323d88714905afc4ff277a6f
fetched_at: '2026-06-28T22:40:22.953801+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Relatório Totvs:
  Somar os totais das seções no Total Geral'
type: support-article
updated_at: '2023-01-20T18:39:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059331713-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Relat%C3%B3rio-Totvs-Somar-os-totais-das-se%C3%A7%C3%B5es-no-Total-Geral
---

**Dúvida**Como configurar no relatório Protheus para o Total Geral sair uma linha somando os totais das seções?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões

**Solução**O **Total Geral** não realiza a somatória de duas ou mais **seções** na opção **Relatório Totvs**, o **Total Geral** é responsável apenas por listar todos os totalizadores das seções disponíveis no relatório.  
Caso você queira realizar um totalizador geral envolvendo as seções é necessário criar um fonte codificando o relatório utilizando as classes do **TReport**, onde será possível criar o totalizador por seção de acordo com sua necessidade e no final do relatório você pode criar o seu total geral pegando os valores dos outros totalizadores das seções que você precisa.

**Layout padrão para o exemplo citado.**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099734693/mceclip0.png)

**Saiba Mais  
[TReport](https://tdn.totvs.com/display/public/PROT/TReport)**
