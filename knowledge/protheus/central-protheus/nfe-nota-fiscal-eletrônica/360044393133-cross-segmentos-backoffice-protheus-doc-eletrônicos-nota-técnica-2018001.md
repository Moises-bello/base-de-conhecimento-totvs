---
article_id: 360044393133
category: NFe - Nota Fiscal Eletrônica
content_hash: defc8f31f4f5fd08b39fe384dfa3728ca8724cbd9eadafeaa0192f6c8afc3a4c
fetched_at: '2026-06-28T22:40:06.942917+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2018.001
type: support-article
updated_at: '2025-06-23T11:59:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044393133-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2018-001
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2018.001 ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

 O Protheus  já atende a **Nota Técnica 2018.001\_V\_1.10.**

Para o funcionamento correto é necessário que os fontes estejam atualizados.

**1. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

**Saiba Mais:** [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

2.**Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

<https://suporte.totvs.com/portal/p/10098/download?e=1152113>

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.
