---
article_id: 360014258812
category: Ativo Fixo - Bens X Manutenção de ativo
content_hash: 74a7c702f70163a26bb7cba7e37749a24a2ddce5f35555146f008395adffbd8a
fetched_at: '2026-06-28T22:41:50.916106+00:00'
product: protheus
section_id: 1500001536141
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Exclusão do Bem vinculado
  ao SIGAMNT
type: support-article
updated_at: '2023-11-21T13:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014258812-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Exclus%C3%A3o-do-Bem-vinculado-ao-SIGAMNT
---

**Ocorrência**

Ao tentar excluir um **Ativo** pela rotina **ATFA012**(Cadastro de Ativo) é apresentado a seguinte mensagem:

Help : FWFORMCANCEL

Problema : Violação de Integridade. Foi encontrada referencia de Bem MNT (N1\_CODBEM) na tabela ST9 - Bem Formulário SN1MASTER

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009699771)

**Ambiente**

Protheus – Ativo Fixo – A partir versão 12.

**Causa**

Esta mensagem é apresentada devido ao **bem no Ativo Fixo estar vinculado a um bem no módulo SIGAMNT**(Manutenção de Ativos).

A **integração** é definida pelo parâmetro [**MV\_NGMNTAT**](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=606099816) com as seguintes opções:

**0 = Não existe integração**

**1 = Integrado com réplica a partir do SIGAATF**

**2 = Integrado com réplica à partir do SIGAMNT**

**3 = Integrado com réplica nos dois sentidos**

**Solução**

Para prosseguir com a exclusão do bem **o vinculo entre os módulos não deve existir**, ou seja, **deve-se excluir o ativo primeiramente da tabela ST9** onde o mesmo se encontra amarrado para depois tentar excluí-lo no módulo de **Ativo** **Fixo**.
