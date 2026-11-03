---
article_id: 360059760933
category: NFe - Nota Fiscal Eletrônica
content_hash: 4bd3ff807c68788a2bd36c7a3060aecb76eb3d4b500a2df79ad8be00931a91bc
fetched_at: '2026-06-28T22:40:00.378257+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na Tag cprodanvisa '
type: support-article
updated_at: '2021-07-19T17:26:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059760933--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-cprodanvisa
---

**Dúvida**Como solucionar a falha de Schema na TAG  cprodanvisa  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Se houver conteúdo nas TAGS **<xMotivoIsencao> e / ou <vPMC>** é obrigatório ter conteúdo na TAG **<cProdANVISA>**

**![TABELA_cd7.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360098154714/TABELA_cd7.JPG)**

1- Preencha os campos no módulo dos **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos.**

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098154874/20201117_103818.gif)

* **Na opção Medicamento:**

![MEDICAMENTO.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360100410073/MEDICAMENTO.JPG)

2- Preencher os campos abaixo:

* **CD7\_PRECO**
* **CD7\_CODANV**

**O campo não** é obrigatório **CD7\_MOTISE**

3- Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

Para gerar o conteúdo dos campos de forma automática verificar o artigo:

[MP - NFE - Como gerar as TAGs rastro e med (Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004922252)
