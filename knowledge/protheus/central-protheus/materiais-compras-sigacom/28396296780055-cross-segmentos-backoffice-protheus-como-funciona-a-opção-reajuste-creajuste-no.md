---
article_id: 28396296780055
category: Materiais - Compras (SIGACOM)
content_hash: 39eae48ccca7338db9c8d5d4e1e428862bb136a90d31b4f36be0740e2c0b0217
fetched_at: '2026-06-28T22:41:11.838915+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Como funciona a opção reajuste (CREAJUSTE)
  no Contrato Parceria
type: support-article
updated_at: '2024-12-09T19:49:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28396296780055-Cross-Segmentos-Backoffice-Protheus-Como-funciona-a-op%C3%A7%C3%A3o-reajuste-CREAJUSTE-no-Contrato-Parceria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28396296755607) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como funciona o **Reajuste** no **Contrato** **Parceria ?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

A variável apresentada em tela (**CREAJUSTE**) é gravada na tabela **SC3** no campo **C3\_REAJUST**, do **Contrato de Parceria**.

Ao incluir uma autorização de entrega vinculada a este contrato, o campo **C3\_REAJUST** é repassado para o **C7\_REAJUST** da **Autorização de Entrega**.

Tanto na **Autorização de Entrega** quanto no **Pedido de Compra**, o reajuste tem como finalidade reajustar os valores com base em uma fórmula contendo as regras de reajuste do cliente.

Lembrando que o reajuste só é aplicado na inclusão do **Documento de Entrada**, ao vincular o **Pedido de Compra** ou a **Autorização de Entrega**.

Um teste simples para evidenciar o funcionamento do processo é incluir uma fórmula com **M4\_FORMULA** = **SC7**-> **C7\_PRECO\*2**.

Na inclusão do **Documento de Entrada**, ao vincular o **Pedido de Compra** ou a **Autorização de Entrega**, o valor carregado em tela será o dobro do informado.

***Saiba Mais :***

[Reajuste](https://tdn.totvs.com/pages/viewpage.action?pageId=225269018)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
