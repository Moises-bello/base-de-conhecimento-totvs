---
article_id: 23392849878551
category: Materiais - Compras (SIGACOM)
content_hash: 59cc86b89e8276c88c0337f32cfaf2f94d7ae2ebf2618f7da161e4fbd64bb6a6
fetched_at: '2026-06-28T22:41:09.075679+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como funciona
  os filtros da Analise de cotação?
type: support-article
updated_at: '2026-03-03T18:02:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23392849878551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-funciona-os-filtros-da-Analise-de-cota%C3%A7%C3%A3o
---

**Dúvida**

Como funciona os filtros da Analise de cotação?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

Quando selecionada a tela de Análise de cotação, temos disponíveis alguns filtros abaixo para apresentar a melhor opção de fornecedor.

![ordenar por.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23392849868695)

**Melhor preço sem Impostos:**

Nessa opção é demonstrando o fornecedor que possui o menor preço da cotação sem calcular os impostos informados.

Validação realizada:

É feita a soma dos seguintes valores Valor Total da Cotação + Valor do Frete + Valor da Despesa + Valor do Seguro + Valor da Embalagem - Valor do Desconto. Caso esteja em outra moeda, é feita a conversão do valor usando a taxa existente no campo C8\_TXMOEDA.

C8\_TOTAL+C8\_VALFRE+C8\_DESPESA+C8\_SEGURO+C8\_VALEMB-C8\_VLDESC

**Melhor preço com Impostos:**

Nessa opção é demonstrando o fornecedor que possui o menor preço da cotação somado com as impostos que foram preenchidos na cotação.

Validação realizada:

É feita o mesmo calculo que no filtro anterior. Porém, neste são somados os valores dos impostos **IPI e ICMS Solidário.** São os dois únicos impostos serão considerados para compor o valor total da cotação.

C8\_TOTAL+C8\_VALFRE+C8\_DESPESA+C8\_SEGURO+C8\_VALEMB-C8\_VLDESC+C8\_VALIPI+C8\_VALSOL

**Menor prazo:**

Nessa opção é demonstrando o fornecedor que possui a menor data de entrega da cotação.

Validação realizada:

É feita a média da Data de Entrega dos itens da cotação **C8\_DATPRF**. É selecionado o menor prazo entre essas médias calculadas.

**Melhor nota:**

Essa nota analisada pelo NFC é referente a nota informado para o fornecedor no cadastro de Produto x Fornecedor. Com base nela o NFC filtra para o fornecedor com a maior nota informada nesse cadastro.

Validação realizada:

É feita a média das notas desse fornecedor para os produtos existentes na cotação. Essas notas ficam no campo **A5\_NOTA.** A média com maior valor será a melhor nota e será a proposta ganhadora. Ou seja, o sistema levará em consideração a nota que foi atribuída na amarração de Produto x Fornecedor, no campo A5\_NOTA. Caso não utilize a amarração de produto x fornecedor não será possível realizar a análise da cotação por meio da nota do produto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26943838365079)

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
