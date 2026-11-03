---
article_id: 360044412793
category: NFe - Nota Fiscal Eletrônica
content_hash: 86d84296b8f5f69498dcc5fa8e821d78286e0e97561c4069cd6cf873994c7779
fetched_at: '2026-06-28T22:40:03.180172+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  254 Rejeição:
  NF-e complementar não possui NF referenciada'
type: support-article
updated_at: '2025-06-23T12:06:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044412793-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-254-Rejei%C3%A7%C3%A3o-NF-e-complementar-n%C3%A3o-possui-NF-referenciada
---

**Dúvida**

Como solucionar a rejeição abaixo:

254 Rejeição: NF-e complementar não possui NF referenciada ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

 1- Verificar se a nota foi **referenciada ao documento**de origem corretamente:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986428797719)

D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986404833303)**

**Importante:**

Lembrando que a nota só é **referenciada no XML** caso exista no sistema.

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** .   
  
Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

2- Caso seja **complemento de Exportação ou Devolução de importação:**

Na rotina dos **Livros Fiscais** -> **Atualizações** -> **Movimentos** -> **NF manual de Saída** -> **Outras ações** ->**Complementos** -> **Exportação**  preencha o campo abaixo:

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986428798743)

**CDL\_CHVEXP** com a chave de acesso da **Nota original com 44 posições.**

Além disso a nota de origem deve ser referenciada:

 D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída)**
