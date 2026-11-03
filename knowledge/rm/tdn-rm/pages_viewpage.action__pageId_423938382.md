---
content_hash: b5988196857d4f4a0491f02f33a29191c392d62a3a6725f4603b2b785ad010f5
fetched_at: '2026-06-29T00:09:26.716972+00:00'
page_id: '423938382'
product: rm
source: tdn-rm
title: Requisição de Material
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938382
version: 2
---

O processo de Requisição de Material permite gerar movimentos do tipo Requisição de Material no aplicativo TOTVS Gestão de Estoque, Compras e Faturamento dos produtos e serviços necessários para execução da Ordem de serviço caso não exista os produtos em estoque.   
Através desse processo será possível gerar uma solicitação de compra ou uma ordem de compra para o sistema TOTVS Gestão de Estoque, Compras e Faturamento.

**Parametrização**

Antes de acessar o processo de requisição de material pela primeira vez é necessário que o usuário parametrize o movimento que será usado para realizar a requisição. A parametrização é feita acessando o sistema TOTVS Gestão de Estoque, Compras e Faturamento em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento, escolhendo o tipo de movimento.  
Após parametrizar o movimento no sistema TOTVS Gestão de Estoque, Compras e Faturamento é preciso também acessar o sistema TOTVS Manutenção no menu Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento, na aba movimentos e informar o movimento no campo "Requisição de Material".   
Após fazer isso sistema estará parametrizado para gerar movimentos de Requisição de Material.

**Processo**

Para gerar um movimento de Requisição de Material basta acessar a visão de OS, selecionar uma ordem de serviço e clicar no menu Movimentação | Requisição de material. Feito isso irá ser aberto o Wizard do processo.   
Atenção! Não é possível gerar requisição de material para OS's com status "Aguardando Análise".  
   
Na primeira tela do Wizard o usuário irá preencher os campos Tipo de movimento, filial, local de estoque, cliente, centro de custo e condição de pagamento.  
***Atenção!*** Alguns campos desta primeira tela podem não se usados, para isto basta parametrizar no tipo de movimento acessando o sistema TOTVS Gestão de Estoque, Compras e Faturamento.

Na segunda tela do Wizard o usuário irá editar os itens da ordem de serviço que serão incluídos na requisição a ser gerada.   
Para editar o item o usuário deverá marcar um item por vez e clicar no botão editar, ao clicar o sistema exibirá a tela com três abas: identificação com os dados do item, aba classificação onde é preenchido a classificação do item e o departamento (parametrizado no tipo de movimento par ser editável ou não) e por ultimo a aba histórico.   
O campo histórico retorna o conteúdo do campo histórico do item da ordem de serviço na aba histórico que se encontra na edição do item da OS.   
A aba histórico pode ser parametrizada para não ser editável, se isso for feito a mesma não ficará visível.  
O usuário poderá escolher a quantidade do produto que ele quer requisitar, para fazer isso basta clicar no campo "Qtde a Requisitar" na grid e informar a quantidade a se requisitada para item.   
Depois de informar a quantidade é necessário selecionar os itens que irão ser inclusos na requisição e clicar em avançar para que o Wizard vá para o próximo passo.  
***Atenção!*** Somente os itens marcados serão inclusos no processo de requisição.

A quantidade a requisitar não poderá ser maior que a quantidade necessária e nem maior que a quantidade requisitada.  
No próximo passo do wizard o usuário o usuário irá preencher os campos de classificação do movimento e o departamento.  
***Atenção!*** Esses campos podem ser parametrizados para não serem usados, se isso acontecer com todos os campos, o passo do Wizard será ocultado e o sistema levará o usuário para o passo seguinte.  
   
No próximo passo o usuário irá preencher os datas do movimento (data de digitação e data de entrega), os valores financeiros e o frete.  
***Atenção***: Esses campos também podem ser parametrizados para não serem usados, se isso acontecer com todos os campos, o passo do Wizard será ocultado e o sistema levará o usuário para o passo seguinte.  
É obrigatório que o usuário informe um valor para os campos frete (CIF, FOB e Terceiro). É possível parametrizar esses campos para assumirem valores default ficando isso a critério do usuário.

No ultimo passo o usuário irá preencher os campos livres se eles estiverem parametrizados para serem usados. Após preenche-los e clicar em avançar o processo chega ao fim e basta o usuário clicar em executar para gerar o movimento de requisição de material.
