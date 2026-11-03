---
article_id: 20495450539159
category: Contabilidade Gerencial - Efetivação, Conferência de lançamento
content_hash: b0e013a1c4c0b5bf4bee43500fdca823397ce07d7e147be42f2ca86c46a60202
fetched_at: '2026-06-28T22:40:53.433551+00:00'
product: protheus
section_id: 1500001548622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA350 - Efetivação
  gera help "At, De saldo desligada, MV_CT350SL (L)=F"
type: support-article
updated_at: '2024-01-11T15:08:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20495450539159-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA350-Efetiva%C3%A7%C3%A3o-gera-help-At-De-saldo-desligada-MV-CT350SL-L-F
---

**Dúvida**

Processo de efetivação gerando help "At, De saldo desligada, MV\_CT350SL (L)=F"

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.

**Solução**

Quando o processo de Efetivação gera o help:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20495442581143)

Indica que o parametro MV\_CT350SL esta com o conteúdo = .F..

Desta formas os saldos contábeis não são atualizados de forma automatica.

Sendo necessário realizar o reprocessamento de saldos através da rotina CTBA190, conforme documentação:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA190 - Como realizar o reprocessamento de saldos no SIGACTB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB?source=search)

Pois este parametro é responsável por atualizar os saldos contábeis no processe de efetivação dos lançamentos contábeis, atualizando assim os saldos conforme os lançamentos efetivados.

Caso queira que os saldos dos lançamentos efetivados atualizados no momento da efetivação devera configurar o parametro MV\_CT350SL = .T., desta forma os saldos serão atualizados de forma automatica, e o help não será apresentado.

Saiba mais:

[MV\_CT350SL - Atualização de Saldos na Efetivação](https://tdn.totvs.com/pages/releaseview.action?pageId=6068561)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Documentação - Efetivação CTBA350.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006607172-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Documenta%C3%A7%C3%A3o-Efetiva%C3%A7%C3%A3o-CTBA350-?source=search)
