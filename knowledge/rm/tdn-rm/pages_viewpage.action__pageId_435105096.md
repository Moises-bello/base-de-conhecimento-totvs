---
content_hash: 710086e4f5a94da6eabb86ce9e117db8d258766fc8914450ea1acc503d8fd3cf
fetched_at: '2026-06-29T00:09:47.904854+00:00'
page_id: '435105096'
product: rm
source: tdn-rm
title: Aditivo - Troca de Subunidade (Apartamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105096
version: 8
---

Esse aditivo possibilita a troca da subunidade associada ao contrato de vendas por outra.

Novidade!

A partir do Release 12.1.2502 ao efetivar um aditivo de troca de subunidade para um contrato de vendas com [origem no *Portal do Imóveis*](https://tdn.totvs.com/display/LRM/Atualizar+Venda+no+backoffice), o sistema trocará também a subunidade associada à proposta que originou esta venda.

Após a ação acima, será necessário executar o [*sincronismo do Portal de Imóveis*](https://tdn.totvs.com/pages/viewpage.action?pageId=794362068) para que a situação das subunidades envolvidas, seja atualizada no *[Mapa de Disponibilidade](https://tdn.totvs.com/display/LRM/Empreendimento+-+Mapa+de+disponibilidade)* deste portal.

Os campos a serem preenchidos são:   
   
**Tipo de troca:** Indica qual tipo de troca de Apto será realizada. Possui as seguintes opções:

* **Por subunidades disponíveis para venda:** Nesta opção será possível realizar troca de subunidades que estão disponíveis no Empreendimento da subunidade a ser trocada;
* **Por subunidades vendidas/alugadas:** Nesta opção será possível realizar a troca de subunidades que estão vendidas ou alugadas no Empreendimento da subunidade a ser trocada. Dessa forma os 2 contratos envolvidos, terão suas subunidades trocadas;

**De:** Campos da subunidade a ser trocada:

* **Empreendimento:** Empreendimento da subunidade a ser trocada, campo preenchido automaticamente;
* **Bloco:** Bloco da subunidade a ser trocada, campo preenchido automaticamente;
* **Subunidade:** Subunidade a ser trocada, campo preenchido automaticamente;
* **Numero da tabela de preço:** Número da tabela de preço vinculada a subunidade a ser trocada, campo preenchido automaticamente;
* **Valor do item:** Valor da subunidade a ser trocada, campo preenchido automaticamente
* **Valor acréscimo**: Valor de acréscimo da subunidade a ser trocada, campo preenchido automaticamente;
* **Desconto item:** Valor de desconto da subunidade a ser trocada, campo preenchido automaticamente.

**Para:** Campos da nova subunidade da venda:

* **Empreendimento:** Empreendimento da nova subunidade da venda, campo preenchido automaticamente;
* **Bloco:** Bloco da nova subunidade da venda;
* **Subunidade:** Subunidade da venda, campo preenchido automaticamente;
* **Numero da tabela de preço:** Número da tabela de preço vinculada da nova subunidade da venda, campo preenchido automaticamente;
* **Valor do item:** Valor da nova subunidade da venda;
* **Valor acréscimo:** Valor de acréscimo da nova subunidade ;
* **Desconto item:** Valor de desconto da nova subunidade.

Caso exista proposta e venda aditivada essa informação será apresentada na impressão da minuta no Portal de Imóveis.

Advertimos que caso a nova subunidade associada ao contrato por meio deste aditivo, tenha um valor diferente da subunidade original associada por meio da proposta, o sistema não atualizará esta informação na proposta. Neste cenário, ao efetivar este aditivo, o sistema exibirá o alerta abaixo na efetivação:

*No aditivo [#] da venda [#] existe uma diferença de valores entre as subunidades relacionadas.*  
*\*Talvez seja necessário realizar um aditivo de renegociação para corrigir a diferença de [R$ ##,##].*

**Venda/Aluguel:** Venda que possui a nova subunidade da venda, caso esteja associada;  
O aditivo de troca de Apto ou subunidade apesar de não ter alteração em valores de parcelas, poderá ser contabilizado. Esta contabilização geralmente é utilizada em conjunto com a apuração de resultado contábil pelo POC, mas poderá ser utilizada livremente de acordo com a necessidade.

false

Veja Também

---
