---
article_id: 360028775811
category: Escrita Fiscal - CIAP
content_hash: 3e34a9b39cb1f55c0337bced5447c41c54345c12c60cdd69de99c201a988bf19
fetched_at: '2026-06-28T22:39:33.950627+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Quais são as configurações
  para emissão de Nota Fiscal de crédito CIAP? '
type: support-article
updated_at: '2022-05-16T17:45:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028775811-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Quais-s%C3%A3o-as-configura%C3%A7%C3%B5es-para-emiss%C3%A3o-de-Nota-Fiscal-de-cr%C3%A9dito-CIAP
---

**Dúvida**

Quais são as configurações para emissão de Nota Fiscal de crédito CIAP?   
  
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**

Para emissão da Nota Fiscal, que deve ser um documento de entrada com formulário próprio e tipo Complemento de ICMS, utilize as seguintes configurações:

* **Calcula ICMS (F4\_ICM)** = Sim
* **L.Fisc.ICMS(F4\_LFICM)** = Tributado
* **Agrega Valor (F4\_AGREG)** = Não
* **Ajuste CIAP (F4\_AJUSTE)** = Sim – para transmitir Nf-e
* **Formula (F4\_FORMULA)** = "COMPLEMENTO DE ICMS"

Na emissão da Nota Fiscal, por ser complemento de ICMS, informe no campo **Docto. Orig. (D1\_NFORI)** a palavra **CIAP**, pode também ser acrescentado mês/2019.

exemplo: **CIAP052019**.

O campo **Ajuste CIAP (F4\_AJUSTE)**  permite que a nota fiscal seja transmitida mesmo que não conste o número da nota fiscal de origem.

**Exemplo do Danfe:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046679513/mceclip0.png)**

**Exemplo do XML:**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046681553/mceclip4.png)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045820274/mceclip1.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045820474/mceclip2.png)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046680013/mceclip3.png)**

**Segue em anexo o vídeo do processo:**
