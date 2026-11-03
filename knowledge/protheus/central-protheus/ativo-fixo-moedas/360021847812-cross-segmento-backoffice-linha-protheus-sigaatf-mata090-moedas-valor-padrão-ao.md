---
article_id: 360021847812
category: Ativo Fixo - Moedas
content_hash: fc716bb879193c465874c7f8fd78041d0a8469a76f79e0f08325736b4b86a8e9
fetched_at: '2026-06-28T22:41:37.792263+00:00'
product: protheus
section_id: 1500001536641
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -SIGAATF- MATA090 - MOEDAS : Valor
  padrão ao iniciar o sistema'
type: support-article
updated_at: '2022-11-07T19:56:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021847812-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-MATA090-MOEDAS-Valor-padr%C3%A3o-ao-iniciar-o-sistema
---

**Dúvida**Há como definir um valor padrão para uma moeda através da rotina **MATA090** na tela de abertura do sistema?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018810651/mceclip0.png)

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – 12.1.17

**Solução**Para trazer os valores do cadastro de moedas na tela de abertura do sistema, a rotina **MATA090**, verifica diretamente no cadastro da moeda(**tabela SM2**) para a data que está logando no sistema, ou seja, o sistema tem por padrão buscar os dados já cadastrados para o dia em questão e oferece ao usuário a oportunidade de alterar a taxa em caso de esteja incorreta.

Caso deseje que de forma automática as moedas venham preenchidas, pode-se realizar a projeção das moedas conforme a seguinte documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=354468911>, assim o sistema irá popular de forma automática a tabela SM2 para um certo período e ao logar no sistema o campo da moeda estará preenchido.

**\*OBS:** Não sugerimos que o cliente efetue customizações neste processo.
