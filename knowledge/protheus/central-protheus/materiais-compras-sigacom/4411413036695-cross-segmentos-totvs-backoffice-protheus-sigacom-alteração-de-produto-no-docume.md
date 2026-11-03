---
article_id: 4411413036695
category: Materiais - Compras (SIGACOM)
content_hash: ba9463dff9bb866750da44b0ca5db5d1ec84dc32d27484943355793cd83739fe
fetched_at: '2026-06-28T22:41:12.826984+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus  - SIGACOM - Alteração de Produto
  no Documento de Entrada Não Altera Todas as Entidades Contábeis
type: support-article
updated_at: '2022-08-08T11:37:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411413036695-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Altera%C3%A7%C3%A3o-de-Produto-no-Documento-de-Entrada-N%C3%A3o-Altera-Todas-as-Entidades-Cont%C3%A1beis
---

**Dúvida**Por que ao efetuar a alteração de um produto que contém as entidades contábeis cadastradas em seu cadastro, o sistema só atualiza o campo de conta contábil ( ***D1\_CONTA*** ) no documento de entrada ?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões]  
  
**Solução**Por padrão, somente o campo ***D1\_CONTA*** é alterado conforme o código do produto informado no documento de entrada.

Mesmo que no cadastro do produto haja outras entidades contábeis cadastradas, como centro de custo, etc, quando há a alteração de um produto no documento de entrada somente a conta contábil é atualizada conforme o novo produto informado.

Caso haja a necessidade de que as demais entidades contábeis sejam alteradas, poderão ser efetuadas através da utilização do ponto de entrada MT103CPO.

Abaixo as documentações :

[PCOM12028 - Preenchimento padrão dos campos D1\_CC, D1\_ITEMCTA, D1\_CLVL e D1\_TES](https://tdn.totvs.com/pages/releaseview.action?pageId=267795777)  
[MT103CPO - Gatilho do código de produto](https://tdn.totvs.com/pages/releaseview.action?pageId=6085731)

***Saiba Mais :***

*[PCOM12028 - Preenchimento padrão dos campos D1\_CC, D1\_ITEMCTA, D1\_CLVL e D1\_TES](https://tdn.totvs.com/pages/releaseview.action?pageId=267795777)  
[MT103CPO - Gatilho do código de produto](https://tdn.totvs.com/pages/releaseview.action?pageId=6085731)*

*[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*
