---
article_id: 4414392784279
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7fe0bb766d77114c38465583b6e48067b35efc1a74d8892a73f713d572bb5c9b
fetched_at: '2026-06-28T22:38:43.960960+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus)- SIGAFAT - AJUDA: A240ESTORN
  ao excluir pedido de venda gerado no WMS.'
type: support-article
updated_at: '2021-11-29T17:02:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414392784279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-AJUDA-A240ESTORN-ao-excluir-pedido-de-venda-gerado-no-WMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao realizar a exclusão do pedido de venda gerado pelo WMS, o sistema apresenta o Help: AJUDA: **A240ESTORN** - Está movimentação já foi estornada ou foi originada por um estorno.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414392734359/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Faturamento - Todas as versões  
  
**Solução**

O Help **A240ESTORN** esta localizado no fonte **MATA240**, que é um programa que trata as Movimentações Internas, ele valida os seguintes campos:   
  
If lRet .And. ***(D3\_ESTORNO == "S" .Or. D3\_CF == "499" .Or. D3\_CF == "999")***  
    Help(" ",1,"A240ESTORN")  
    lRet := .F.  
  
Caso a movimentação interna identifique esses conteúdos nos campos o Help será apresentado.
