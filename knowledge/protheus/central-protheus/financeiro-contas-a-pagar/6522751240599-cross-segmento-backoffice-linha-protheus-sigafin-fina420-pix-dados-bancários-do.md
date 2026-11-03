---
article_id: 6522751240599
category: Financeiro - Contas a Pagar
content_hash: 24db29ceee3b6b9d3001c6bdfb533809c36ed19f1888ec694daf14c56d338748
fetched_at: '2026-06-28T22:38:07.244409+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA420 - PIX - Dados
  bancários do fornecedor enviados no arquivo de remessa
type: support-article
updated_at: '2022-06-03T21:08:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6522751240599-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA420-PIX-Dados-banc%C3%A1rios-do-fornecedor-enviados-no-arquivo-de-remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**PIX - Quais informações bancárias do fornecedor são enviadas no arquivo de pagamentos?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

O arquivo de remessa leva os dados bancários da conta e chave **PIX do fornecedor**, utiliza os dados do TED, **caso não tenha PIX**, se tiver a chave, considera o pagamento pela chave seguindo o modelo de pagamentos utilizado. 

* **45 - PIX - Transferência**
* **47 - PIX - QR Code**

**Saiba mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=569478747>
