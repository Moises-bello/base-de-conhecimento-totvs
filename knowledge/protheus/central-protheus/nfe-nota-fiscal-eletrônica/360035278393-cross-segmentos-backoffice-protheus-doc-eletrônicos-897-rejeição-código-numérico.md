---
article_id: 360035278393
category: NFe - Nota Fiscal Eletrônica
content_hash: 46eee140df18d29f8e04df665925e1a05a9b10afb1b042d377f562d546b69e03
fetched_at: '2026-06-28T22:40:05.488940+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 897 - Rejeição:
  Código numérico em formato inválido'
type: support-article
updated_at: '2025-06-06T19:12:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035278393-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-897-Rejei%C3%A7%C3%A3o-C%C3%B3digo-num%C3%A9rico-em-formato-inv%C3%A1lido
---

**Dúvida**Como corrigir a rejeição abaixo:

897 Rejeição: Código numérico em formato inválido?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Conforme a nota técnica **2019.001\_v\_1.50 do link abaixo:**

[Nota Técnica 2019.001 - v.1.50 - Publicada em 08/04/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=UDWXVR/WXxw=)

A Sefaz **não permite** mais que as TAGS **cNF e nNF tenham o mesmo conteúdo.**

Além disso,  a TAG **cNF não pode ser igual:**

00000000, 11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999, 12345678, 23456789, 34567890, 45678901, 56789012, 67890123, 78901234, 89012345, 90123456, 01234567.

* Exemplo de como ***não pode gerar:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046070273)

1. Caso ocorra a rejeição realizar atualização do fonte abaixo ***padrão sem customizações:***

**Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)

3. O ambiente deve estar atualizado com **acumulado do fiscal do link abaixo:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525823851)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046077613)**
