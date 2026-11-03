---
article_id: 4403736219927
category: Faturamento - Cadastros
content_hash: 9d0381661f285e255a0866f1c8fff45b5488658aa5738bbc838dd6f3960e9501
fetched_at: '2026-06-28T22:38:35.378969+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Faturamento- Campo
  F4_SLDNPT (Sld. Poder 3 na TES)
type: support-article
updated_at: '2021-07-07T11:19:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403736219927-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Faturamento-Campo-F4-SLDNPT-Sld-Poder-3-na-TES
---

**[Remover as instruções entre colchetes]**  
**Dúvida**Existe o campo de Saldo Poder de Terceiros na TES que indica o produto de poder de terceiros disponível para faturamento. Porque o o campo C9\_BLEST continua gravando 02 (bloqueado de estoque) após a liberação do Pedido ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Faturamento - Todas as versões  
  
**Solução**Quando existe quantidade mencionada no campo "Qt. Ter. Ns. Pd." (Quantidade de Terceiro em nosso Poder - B2\_QTNP), este saldo realmente não é liberado em Pedido de Venda do Tipo Normal, pois é de Terceiro, então não poderá ser vendido, pois terá de ser devolvido

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403736210199/mceclip1.png)  
  
O campo F4\_SLDNPT 'Sld. Poder3' não terá influência para o cenário apresentado acima. Como o Help do campo indica, ele está relacionado a 'Saldo nosso em poder de terceiro'; e não, 'Saldo de terceiro em nosso poder'.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403736204055/mceclip0.png)  
  
Se for necessário utilizar o saldo recebido de terceiro (**B2\_QTNP**) para outros faturamentos (venda), informe na TES de venda uma **TES de retorno simbólico através do campo "TES Ret.Sim" (F4\_TESP3).** Esta configuração faz com que, na preparação do Documento de saída, o saldo de terceiro em seu poder (**B6\_SALDO**) seja baixado (indicando que não haverá retorno). E assim, esse saldo é utilizado em sua venda do produto/ material.

**Saiba mais: [FAT0285 - Poder DE/EM Terceiro](https://tdn.totvs.com/x/xyCgGg)**
