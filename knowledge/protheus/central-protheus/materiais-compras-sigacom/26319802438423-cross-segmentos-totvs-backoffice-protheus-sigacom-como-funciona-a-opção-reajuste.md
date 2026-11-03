---
article_id: 26319802438423
category: Materiais - Compras (SIGACOM)
content_hash: 8d38b9698a46ceca1028c94b02974d693481c1fd1cfa0b9b155aa9750be06973
fetched_at: '2026-06-28T22:41:15.873444+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como funciona a opção
  reajuste (CREAJUSTE) no Contrato de Parceria?
type: support-article
updated_at: '2024-09-12T11:56:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26319802438423-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-funciona-a-op%C3%A7%C3%A3o-reajuste-CREAJUSTE-no-Contrato-de-Parceria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319833607575) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como funciona a opção reajuste (CREAJUSTE) no Contrato de Parceria?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

A variável apresentada em tela (**CREAJUSTE**) é gravada na tabela **SC3** no campo **C3\_REAJUST**, do **Contrato de Parceria**.

Ao incluir uma autorização de entrega vinculada a este contrato, o campo **C3\_REAJUST** é repassado para o **C7\_REAJUST** da **Autorização de Entrega**.

Tanto na **Autorização de Entrega** quanto no **Pedido de Compra**, o reajuste tem como finalidade reajustar os valores com base em uma fórmula contendo as regras de reajuste do cliente.

Lembrando que o reajuste só é aplicado na inclusão do **Documento de Entrada**, ao vincular o **Pedido de Compra** ou a **Autorização de Entrega**.

Um teste simples para evidenciar o funcionamento do processo é incluir uma fórmula com **M4\_FORMULA = SC7 -> C7\_PRECO\*2**.

Na inclusão do **Documento de Entrada**, ao vincular o **Pedido de Compra** ou a **Autorização de Entrega**, o valor carregado em tela será o dobro do informado.

***Saiba Mais :***

[PCOM08002 - Como funciona a opção reajuste (CREAJUSTE) no Contrato de Parceria?](https://tdn.totvs.com/x/GlVtDQ)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
