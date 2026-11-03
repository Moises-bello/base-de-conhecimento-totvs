---
content_hash: 6bea2e3357358e1786b82e01392cd07333a8e9f7913f56e78b8da34a3488ec8a
fetched_at: '2026-06-29T00:09:27.150303+00:00'
page_id: '423938441'
product: rm
source: tdn-rm
title: Histórico de custo de mão-de-obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938441
version: 2
---

Este anexo permite o usuário lançar/cadastrar um novo custo para a mão de obra além de fornecer um histórico de todos os custos que já foram vinculados a esta mão de obra em cada mês.   
O custo informado no anexo "Histórico de Custo da Mão de Obra" será utilizado no recalculo da ordem de serviço quando o usuário rodar o processo "Recalcular Custo" que se encontra na tela de visão da ordem de serviço.   
Para lançar um novo custo para a mão de obra basta acessar o anexo "Histórico do Custo da Mão de Obra" que se encontra no caminho Cadastro | Mão de Obra | Anexo | Histórico do Custo da Mão de Obra e clicar em Incluir.   
Ao clicar em Incluir será aberta uma tela onde o usuário poderá informar manualmente o custo para a mão de obra no campo "Custo/Hora" ou importar de uma planilha cadastrada na base do CorporeRM clicando no botão "Calcular pela planilha".   
Se o usuário preferir importar os dados de uma planilha esta mesma terá que ser previamente cadastrada e informada dentro do cadastro de mão de obra no caminho Cadastro | Mão de obra, editando a mão de obra e acessando a aba "Planilha de Calculo".   
Dentro desta aba o usuário terá que informar o nome da planilha no campo Id. Planilha (selecionar uma dentre as que existem cadastradas no sistema), a célula Identificadora (Célula da planilha onde se encontra o código da mão de obra) e a célula Custo/hora (Célula da planilha onde se encontra o custo da mão de obra)..Exemplo:

| Id. Planilha | Planilha de custo |
| --- | --- |
| Célula Identificadora | $A$5 |
| Célula Custo/Hora | $B$5 |

***Atenção!*** A célula deverá ser delimitada pelo carácter "$" como mostrado no exemplo acima.  
  
Após realizar o processo descrito acima basta clicar no botão "Calcular pela planilha", escolher o mês e o ano que será lançado o custo e o sistema atualizará o campo "Custo/Hora" com o dado contido na planilha.   
Marcando a opção "Visualizar/Editar", ao clicar no botão "Calcular pela Planilha" a planilha será aberta para que o usuário possa alterar algum dado nela antes de importa-los para o histórico.  
***Atenção!***Se os dados da planilha não forem informados corretamente em Cadastro | Mão de obra, aba "Planilha de Calculo" da mão de obra, o sistema não fará a importação dos dados.   
***Observação***: As planilhas são cadastradas no menu Relatórios | Planilha.
