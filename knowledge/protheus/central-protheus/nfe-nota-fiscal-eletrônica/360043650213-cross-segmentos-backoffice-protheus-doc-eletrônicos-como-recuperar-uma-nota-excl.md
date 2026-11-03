---
article_id: 360043650213
category: NFe - Nota Fiscal Eletrônica
content_hash: 208ee00cef1e3ed7f2f061e69d0cdb0eb69c9647e33cde7c2291454fbd298a55
fetched_at: '2026-06-28T22:40:01.802678+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como recuperar
  uma nota excluída que está autorizada na Sefaz ?'
type: support-article
updated_at: '2021-10-11T17:09:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043650213--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-recuperar-uma-nota-exclu%C3%ADda-que-est%C3%A1-autorizada-na-Sefaz
---

**Dúvida**Como recuperar uma nota excluída que está autorizada na Sefaz ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Para voltar a nota no sistema a mesma deve ser incluída em **data base retroativa** ou seja incluída no mesmo dia em que foi **incluída anteriormente.**

2- Após isso, na rotina de transmissão de nota selecione a nota em **Outras ações -> Monitor -> Consulta NF**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058287234/mceclip1.png)

3- **A nota não deve** ser transmitida após isso, será preenchidas a chave e o conteúdo correto nas tabelas do TSS assim a nota estará normal no sistema.

* **Saiba mais:**

Para que não seja necessário realizar esse procedimento **existe o FATJOBNFE** que exclui a nota do sistema apenas ao ter o cancelamento realizado na Sefaz:

[MP-FAT-Configuração do FATJOBNFE para mais de uma empresa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037817733)
