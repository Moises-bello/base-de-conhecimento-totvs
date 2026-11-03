---
article_id: 360018813791
category: Materiais - Compras (SIGACOM)
content_hash: 71317499700708ad50ff1086e3259135dc297ba1ea97bd18a040d1009f243db7
fetched_at: '2026-06-28T22:41:09.049731+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não altera TES ao mudar
  o produto na inclusão do Documento de Entrada
type: support-article
updated_at: '2022-05-13T11:41:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018813791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-altera-TES-ao-mudar-o-produto-na-inclus%C3%A3o-do-Documento-de-Entrada
---

**Dúvida**

Não altera TES ao mudar o produto na inclusão do Documento de Entrada

Ao informar produto que possui vínculo com a TES sistema gatilha no campo D1\_TES, porém se alterado o produto que possui outra TES no campo B1\_TE o sistema não altera, mantendo a TES do primeiro produto.

**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
  
**Solução**

O preenchimento padrão dos campos no item da Nota Fiscal obedece as seguintes regras:

1) Se o campo estiver vazio, ele é preenchido com o conteúdo do campo do cadastro de Produto.  
2) Se já estiver preenchido, ao alterar o produto do item da nota, o conteúdo dos campos descritos serão mantidos conforme o que já estava preenchido, exceto para o campo D1\_CONTA.

Diante da necessidade de alteração poderá utilizar o ponto de entrada MT103CPO.   
<http://tdn.totvs.com/pages/releaseview.action?pageId=6085731>

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
