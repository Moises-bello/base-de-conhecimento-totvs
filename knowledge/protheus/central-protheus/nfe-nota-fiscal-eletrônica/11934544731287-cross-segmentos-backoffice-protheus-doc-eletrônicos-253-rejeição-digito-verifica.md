---
article_id: 11934544731287
category: NFe - Nota Fiscal Eletrônica
content_hash: 27af503368f216b0132cf49700e83b69238fe8755784856a7184bab55096f656
fetched_at: '2026-06-28T22:40:03.814720+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 253 Rejeição: Digito
  Verificador da chave de acesso composta inválida'
type: support-article
updated_at: '2025-06-23T12:32:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11934544731287-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-253-Rejei%C3%A7%C3%A3o-Digito-Verificador-da-chave-de-acesso-composta-inv%C3%A1lida
---

**Dúvida**Como corrigir  253 Rejeição: Digito Verificador da chave de acesso composta inválida ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. A chave é gerada de forma automática pelos fontes. Caso ocorra a rejeição realizar atualização do fonte abaixo ***padrão sem customizações:***

**Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

<https://suporte.totvs.com/portal/p/10098/download?e=1152113>

   3. O ambiente deve estar atualizado com **acumulado do fiscal do link abaixo:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11934387876247)
