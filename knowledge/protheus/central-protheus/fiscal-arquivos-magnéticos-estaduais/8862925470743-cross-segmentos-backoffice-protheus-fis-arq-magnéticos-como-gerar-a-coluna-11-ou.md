---
article_id: 8862925470743
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7c4aaddd93aa9aca4a75ce640c2cc578152fed5c88cb44c9ec24b1554d68ed8b
fetched_at: '2026-06-28T22:42:08.908983+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a coluna 11 - Outras  da DAPIMG?
type: support-article
updated_at: '2022-09-14T12:16:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8862925470743-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-coluna-11-Outras-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar a coluna **11 - Outras** da **DAPIMG**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12

**Solução**

Para gerar a **Coluna 11 - Outras** da **DAPI MG,** o **Protheus** valida os documentos fiscais escriturados com cadastro de **TES** em que a **Situação Tributária do ICMS** seja **90 - Outras.**Dessa forma, o campo **Sit.Trib.ICM - F4\_SITTRIB** deve ser configurado como **90 - Outras**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8862832018327/mceclip0.png)

**Importante**:

Quando o campo **Sit.Trib.ICM - F4\_SITTRIB = Outras** o campo **L.Fisc. ICMS - F4\_LFICM** deve ser configurado como **Outros** para correta geração dos valores nas respectivas **colunas**.

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8862902521367/mceclip1.png)**
