---
article_id: 4412594862231
category: NFe - Nota Fiscal Eletrônica
content_hash: caec8ae796143fa9f3394b18c97b7c17485e7f6e272295cf2ba4ff11ede01078
fetched_at: '2026-06-28T22:40:00.259260+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  790 Rejeição:
  Operação com Exterior para destinatário Contribuinte de ICMS'
type: support-article
updated_at: '2021-11-12T18:36:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412594862231--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-790-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-Exterior-para-destinat%C3%A1rio-Contribuinte-de-ICMS
---

**Dúvida**Como solucionar a rejeição 790 Rejeição: Operação com Exterior para destinatário Contribuinte de ICMS ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Verifique se o CFOP tem finalidade de exportação para este documento, **caso não** tenha altere no TES  no campo **Cod. Fiscal "F4\_CF"**para um CFOP de finalidade de **operação interestadual ou interna iniciado por 1, 2, 5 ou 6.**

**![F4_CF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412594787479/F4_CF.gif)**

2 - Após isso, exclua a **nota e gere novamente.**

3 - Se operação for com **exterior (idDest=3) deve ser gerado como não contribuinte preencher** no cadastro de cliente o campo **Contribuinte "A1\_CONTRIB = 2 - Não"**

![A1_CON.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412670078743/A1_CON.gif)

4- Se operação for com **exterior (idDest=3) deve ser gerado como não contribuinte preencher no** cadastro de fornecedor o campo **Contribuinte "A2\_CONTRIB = 2- Não"**

**![A2_CONTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412669999127/A2_CONTRIB.gif)**

5 - Após isso, **exclua a nota e gere** novamente.

* **Validação da Sefaz:**

![790.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4412589551255/790.JPG)
