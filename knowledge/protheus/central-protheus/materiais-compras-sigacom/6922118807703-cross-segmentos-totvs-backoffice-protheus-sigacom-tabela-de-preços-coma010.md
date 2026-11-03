---
article_id: 6922118807703
category: Materiais - Compras (SIGACOM)
content_hash: 0af2804d4182b9da832d848659c93c4c4fa10f92a1f04b9b8e947f10890dfa20
fetched_at: '2026-06-28T22:41:25.347850+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Tabela de Preços (COMA010)
type: support-article
updated_at: '2025-04-04T13:15:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6922118807703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Tabela-de-Pre%C3%A7os-COMA010
---

**Dúvida**Como configurar a Tabela de Preços (**COMA010**) e para que serve esse cadastro?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões.  
  
**Solução**Permite cadastrar as tabelas de preços dos fornecedores que atendem à empresa.

Neste cadastro podem ser informados os preços e a condição de pagamento a serem praticados. Quando informada a condição de pagamento, o Sistema não permitirá que outra condição seja utilizada nos processos de compras (cotações e pedidos).

A Tabela de Preços pode ser utilizada nas rotinas [Pedidos de Compras](https://tdn.totvs.com/pages/createpage.action?spaceKey=PROT&title=Pedido+de+Compra+%28MATA121+-+SIGAGCP%29&linkCreation=true&fromPageId=312158061), [Gera Cotações](https://tdn.totvs.com/pages/viewpage.action?pageId=312157887), [Atualiza Cotações](https://tdn.totvs.com/pages/viewpage.action?pageId=312157074) e [Produto x Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=306857135).

O prazo de validade da Tabela de Preços é determinado por meio dos campos "Dt. Vld. Ini." e "Dt. Vld. Final".

As Tabelas de Preços são sinalizadas por uma legenda, sendo:

Tabela Inativa - a tabela se torna inativa, quando o prazo de validade for ultrapassado.

Tabela Ativa - as tabelas ativas são aquelas que estão dentro do prazo de validade.

**Procedimentos:**

Para cadastrar tabelas de preços dos fornecedores:

1. Na janela de manutenção da rotina Tabela de Preços, clique em **"Incluir"**.

A janela "Manutenção da Tabela de Preços - Incluir" é exibida, dividida em áreas.

* Cabeçalho

Nesta área, são informados: código/loja do fornecedor, código da tabela de preço, data de validade, condição de pagamento, etc.

* Itens

Nesta área, são informados: produto, preço unitário, faixa, vigência, frete, código do produto no fornecedor, etc.

2. Na área "Cabeçalho", preencha os dados conforme orientação do help de campo.

Observe, os campos "Dt. Vld. Ini." e Dt. Vld. Final, pois estes irão determinar o prazo de validade da tabela de preço.

3. Em seguida, posicione o cursor na área "Itens" e preencha os dados conforme orientação do help de campo.

Observe o campo "Vigência", que determina a partir de qual data o preço para determinado produto entrará em vigor.

***Importante:***

Para cadastrar duas ou mais vigências para um mesmo produto, é necessário inclui-las, sempre, de forma decrescente, ou seja da data de vigência maior para a data de vigência menor. Desta forma, ao utilizar a este cadastro em outras rotinas, o Sistema dará prioridade ao valor cadastrado com a data de vigência mais próxima à data atual.

Exemplo:

Produto A - Preço R$ 10,00 - Data de Vigência 15/10/08.

Produto A - Preço R$ 5,00 - Data de vigência 01/10/08

Ao efetuar o cadastro deste produto na Tabela de Preços, e cadastre primeiramente o produto e preço com data de vigência a partir de 15/10/08 e em seguida, cadastre o produto e preço com data de vigência a partir de 01/10/08.

O Sistema apresentará, até o dia 14/10/08, a Tabela de Preços com o valor de R$ 5,00 e a partir desta  data, apresentará a Tabela de Preços com valor de R$ 10,00.

***Obs:***

Por padrão mesmo que uma tabela de preços seja chamada no item do Pedido de compras trazendo o Valor Unitário, o sistema permite a alteração do valor unitário, não havendo disponível uma parametrização/configuração para impedir a alteração do valor trazido.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como carregar a Tabela de Preços no Pedido de Compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5745230677783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-carregar-a-Tabela-de-Pre%C3%A7os-no-Pedido-de-Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
