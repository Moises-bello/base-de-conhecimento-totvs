---
content_hash: d13815bf3c522f0fe687d466352faa34970b36dfb31e7da283fc10d02f0c64da
fetched_at: '2026-06-29T00:09:26.185766+00:00'
page_id: '423938295'
product: rm
source: tdn-rm
title: Análise
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938295
version: 12
---

O recurso de Análise de Ressuprimento é responsável por dimensionar os níveis de estoque e gerar, caso necessário, sugestões de compra. Ao executar o recurso selecionando os produtos que se deseja analisar o consumo, o sistema exibe os produtos organizados conforme o nível de gestão(Coligada, Filial ou Por Local). Estes produtos são classificados de duas formas:

Não é necessário realizar análise de compra, pois o saldo é maior que o ponto de reposição.

O produto deve ser analisado, pois existe uma sugestão de compra a ser gerada, o saldo é menor que o ponto de reposição.

A identificação de um produto, no processo de Análise de Ressuprimento, é feito pelo código, descrição, data de cadastramento, unidade e até mesmo por tabelas de classificação.   
Além destes dados, são exibidos os tempos de estoque máximo, estoque mínimo, reposição, fornecimento, compra e consumo médio teórico. Todos estes registros são buscados do cadastro de produto.  
Os valores do estoque máximo, estoque mínimo, ponto de reposição, lote econômico de compras, consumo médio prático e classificação ABC, são calculados e atualizados nestes campos informados.  
Com o produto selecionado, o usuário também pode verificar informações como Tipo de aplicação, fornecedores, consumo, saldos e sugestões de compra deste produto.  
O tipo de aplicação e fornecedores exibidos na análise são aqueles definidos no próprio cadastro do produto.  
Para facilitar a análise de consumo do produto, este dado é exibido em forma de gráfico.  
Os saldos definidos na pasta sugestão e tipos de movimentos parametrizados como “[x]Saldo” referente ao módulo de Ressuprimento são os dados referentes a Saldos.  
Após ter calculado o atributo "[x] Sugestão de Compra" do Processo de Ressuprimento e o sistema ter gerado uma sugestão de compra para o produto em questão, é possível visualizar a sugestão por meio da Análise de Ressuprimento.  
As sugestões de compra geradas podem possuir as seguintes classificações:

 Sugestão de Compra não analisada.

Sugestão de Compra analisada que gerou uma solicitação de compras.

 Sugestão de Compra rejeitada.

 Sugestão de Compra forçada.

***Atenção!***Quando a sugestão de compra está classificada como “Sugestão de Compra Forçada” quer dizer que o sistema não identificou necessidade de gerar uma sugestão de compra para o produto, classificando-o como “  Não é necessário realizar análise de compra”, mas mesmo assim o usuário optou por gerar uma análise de compra deste produto.
