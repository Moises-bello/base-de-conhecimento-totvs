---
article_id: 360004943552
category: NFe - Nota Fiscal Eletrônica
content_hash: aa91012a1f7929f2f4bb6b123d3bf4868e38746f7dde7a532b370876885f18b7
fetched_at: '2026-06-28T22:39:59.910331+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 379 Rejeição :
  Grupo de Encerrante na NF-e (modelo 55) para CFOP diferente de venda de combustível
  para consumidor final '
type: support-article
updated_at: '2021-07-20T13:03:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004943552--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-379-Rejei%C3%A7%C3%A3o-Grupo-de-Encerrante-na-NF-e-modelo-55-para-CFOP-diferente-de-venda-de-combust%C3%ADvel-para-consumidor-final
---

**Dúvida**Como solucionar a rejeição 379 Grupo de Encerrante na NF-e (modelo 55) para CFOP diferente de venda de combustível para consumidor final?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O  grupo de encerrante  só deve ser informado com os **CFOPS 5656 e 5657.**  
  
Diferente disso os campos **não devem ser preenchidos no complemento de Combustível** nos Livros Fiscais.

1- Acesse a rotina **Livros Fiscais** -> **Atualizações** -> **Movimentos** -> **NF manual de Saída** -> **Outras ações** ->**Complementos** -> **Exportação**

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099707813/20201117_103818.gif)

2- Refaça a nota sem preencher os  **campos abaixo:**

CD6\_BICO, CD6\_BOMBA, CD6\_ENCFIN, CD6\_ENCFIN, CD6\_TANQUE

3- Caso o grupo precise ser gerado o grupo de encerrante  altere o CFOP da nota para **5656 e 5657** no TES no campo **Cod. Fiscal "F4\_CF":**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060423754/mceclip1.png)

4 - Após isso, **exclua a nota** e gere novamente.
