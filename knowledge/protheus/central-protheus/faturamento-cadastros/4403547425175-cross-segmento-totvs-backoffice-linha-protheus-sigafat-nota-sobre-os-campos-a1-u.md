---
article_id: 4403547425175
category: Faturamento - Cadastros
content_hash: ea22c33d941cc2ef78941c67efd7fe2c9f1528054c051df8d4ae3ee95c566b0a
fetched_at: '2026-06-28T22:38:35.324068+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre
  os Campos A1_ULTCOM e A1_PRICOM '
type: support-article
updated_at: '2022-10-19T18:38:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403547425175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-os-Campos-A1-ULTCOM-e-A1-PRICOM
---

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7734422065431/mceclip1.png)Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Qual o funcionamento dos campos "1a Compra (A1\_PRICOM)" e "Ult. Compra (**A1\_ULTCOM**)", responsável por gravar a data da primeira e última compra do cliente, não esão sendo atualizados ao gerar documentos de saída (faturar).  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**Para atualizar as informações é necessário que na TES o campo "**Gera Dupl. \***" esteja como "**S - Sim**" (gera financeiro).

* F4\_DUPLIC = S - Sim

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7734417543575/mceclip0.png)

Exemplo onde um cliente nunca faturou. Ele então possui os campos A1\_PRICOM e A1\_ULTCOM vazios.

* [A1\_PRICOM =   /  /   ] - "1a Compra" (Primeira compra do cliente)
* [A1\_ULTCOM =   /  /   ] - "Ult. Compra" (Última compra do cliente)

**Etapa 1 - Cliente faz o primeiro faturamento. Nesse instante, é a primeira e última compra do cliente:**

* Database do dia > D2\_EMISSAO = 26/05/2022
* A1\_PRICOM = 26/05/2022
* A1\_ULTCOM = 26/05/2022

**Etapa 2 - Cliente faz o segundo faturamento dois dias depois:**

* Database do dia > D2\_EMISSAO = 28/05/2022
* A1\_PRICOM = 26/05/2022
* A1\_ULTCOM = 28/05/2022

E assim por diante, segue o comportamento do campo. Ele pode ser alterado manualmente. Para seu funcionamento automático como especificado, a TES utilizado no item do pedido de vendas (SC6) do cliente deve gerar financeiro.
