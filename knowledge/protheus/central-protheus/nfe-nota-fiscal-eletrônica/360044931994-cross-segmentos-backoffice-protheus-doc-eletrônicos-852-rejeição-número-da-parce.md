---
article_id: 360044931994
category: NFe - Nota Fiscal Eletrônica
content_hash: adaab2f66ef0857a3baa49d402aa15e29f8aa56f723ba719cf6b6cf239930e90
fetched_at: '2026-06-28T22:40:05.397923+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 852 Rejeição :
  Número da parcela inválido ou não informado'
type: support-article
updated_at: '2025-06-18T14:43:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044931994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-852-Rejei%C3%A7%C3%A3o-N%C3%BAmero-da-parcela-inv%C3%A1lido-ou-n%C3%A3o-informado
---

**Dúvida**

Como solucionar a Rejeição 852 : Número da parcela inválido ou não informado

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Deve ser gerado o número da duplica sequencial **001, 002, 003** conforme o exemplo abaixo:

![duplicata.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001071822)

**1. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

    2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

[Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Pacotes de Atualização - Documentos Eletrônicos (NFE | NFSE | MDE | MDFE (FAT))](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

     2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[RDMAKE NFESEFAZ](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

* **Saiba mais:**

[MP - NFE - Como fazer para não gerar duplicata na 4.00 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020374091)

Caso precise gerar duplicata no Protheus, mas **não gerar no XML** basta utilizar o parâmetro abaixo:

**MV\_GRUPCOB = .F. (Para não gerar)**

![20201117_154307.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896580985623)

* **Validação da Sefaz:**

![852_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360102153753)

 

* **Saiba mais:***[Link de todos os artigos da NFe](https://centraldeatendimento.totvs.com/hc/pt-br/sections/207068528-NFe-Nota-Fiscal-Eletr%C3%B4nica)*
