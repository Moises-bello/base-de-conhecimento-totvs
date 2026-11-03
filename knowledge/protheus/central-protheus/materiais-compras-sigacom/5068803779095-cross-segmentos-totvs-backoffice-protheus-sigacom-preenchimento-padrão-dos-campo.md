---
article_id: 5068803779095
category: Materiais - Compras (SIGACOM)
content_hash: 0fd6a9478b5b687642fdd9921cc5e98e98a7126bb1ac9e45384a6d9a9c16de43
fetched_at: '2026-06-28T22:41:24.061323+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Preenchimento padrão
  dos campos no Documento de Entrada - D1_CONTA / D1_CC / D1_ITEMCTA / D1_CLVL e D1_TES
type: support-article
updated_at: '2022-03-28T13:41:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5068803779095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Preenchimento-padr%C3%A3o-dos-campos-no-Documento-de-Entrada-D1-CONTA-D1-CC-D1-ITEMCTA-D1-CLVL-e-D1-TES
---

**Dúvida**Ao alterar o código de um produto, o sistema não limpa os dados do código do produto anterior nos campos **D1****\_CC**, **D1\_CONTA** e **D1****\_ITEMCTA**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras- Todas as versões  
  
**Solução**O preenchimento padrão dos campos no item da Nota Fiscal obedece as seguintes regras:

1) Se o campo estiver vazio, ele é preenchido com o conteúdo do campo do cadastro de Produto.

2) Se já estiver preenchido, ao alterar o produto do item da nota, o conteúdo dos campos descritos é mantido conforme o que já estava preenchido, exceto para o campo **D1\_CONTA**. No caso do campo **D1\_CONTA**, o padrão de preenchimento é sempre sobrescrever o conteúdo do campo com àquele que corresponde ao cadastro de Produtos.

Assim, se o ponto de entrada **MT103CPO** estiver compilado e alguma posição do vetor de retorno possuir algum campo da nota, dentre os descritos, o conteúdo será preenchido conforme o cadastro de Produto, porém, no caso específico do campo **D1\_CONTA**, se ele for informado no vetor de retorno, não será carregado o conteúdo do cadastro de Produto.

Mais informações : [MT103CPO](https://tdn.totvs.com/pages/viewpage.action?pageId=6085731)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DO](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)[COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[Preenchimento padrão dos campos D1\_CC, D1\_ITEMCTA, D1\_CLVL e D1\_TES](https://tdn.totvs.com/pages/viewpage.action?pageId=6085731)
