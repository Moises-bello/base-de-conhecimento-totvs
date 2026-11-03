---
article_id: 360020161711
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: eec2283a7c46cb24e42c27de9e0f2dd11c4c244b7d181bb16792b485ef5304cb
fetched_at: '2026-06-28T22:38:28.651198+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Principais Pontos
  de Entrada que permitem tratar a Numeração do Documento de Saída
type: support-article
updated_at: '2021-08-30T18:51:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020161711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Principais-Pontos-de-Entrada-que-permitem-tratar-a-Numera%C3%A7%C3%A3o-do-Documento-de-Sa%C3%ADda
---

**Dúvida**

Quais os principais pontos de entrada para tratamento de controle de numeração de nota?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Segue a lista abaixo dos principais pontos de entrada que permitem tratar a Numeração da Nota de Saída:

**- M467FILT** - Filtrar séries a serem mostradas (não é válido para o módulo SIGALOJA): <https://tdn.totvs.com/x/5IRn>

**- SX5NOTA** - Validação das séries que deseja considerar no momento da geração da NF: [https://tdn.totvs.com/x/wIVn](http://tdn.totvs.com/pages/releaseview.action?pageId=6784448)

**- M460NUM** - Seleção da série - Executado após a seleção da série para permitir a troca através de customização local: <https://tdn.totvs.com/x/wYRn>

**- M461SER** - Série e Número Nota Fiscal Saída: <https://tdn.totvs.com/x/DgS-Ag>

**- M468ASER** - Chamado durante o processamento da nota fiscal, para a obtenção da série da NF: <https://tdn.totvs.com/x/54Rn>

**- MA461NNF** - Visualização do número da nota gerada pelo SD9: <https://tdn.totvs.com/x/YIZn>
