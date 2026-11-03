---
content_hash: 8dcf2b5a0044fc20282ba4c680c3089c317e69c5f65d16e38856cf8c0800e917
fetched_at: '2026-06-29T00:10:09.900905+00:00'
page_id: '452719725'
product: rm
source: tdn-rm
title: Bloqueio/Desbloqueio do Recálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719725
version: 3
---

O controle de bloqueio e o desbloqueio do recálculo serão feitos para que o movimento do funcionário não tenha alteração em caso de um recálculo geral.   
   
A opção Período permite bloquear todos os períodos, ou um período único. Depois da seleção do período a ser bloqueado/calculado, o usuário deverá escolher a opção bloqueio ou desbloqueio do recálculo.  
   
**Exemplo:**  
O período 02 foi selecionado para manter apenas rescisões. Todas as rescisões foram calculadas e pagas. Neste caso a empresa não deseja que este determinado período sofra um recálculo. Para que este processo seja efetuado com sucesso, o usuário deverá marcar o período a bloquear e depois clicar no botão bloqueia. Também no caso de desbloqueio, basta clicar no botão desbloqueia.   
   
O bloqueio será realizado por completo para todos os funcionários ou parcialmente através da chapa do funcionário, do código de quebra ou da seleção de funcionários.  
   
Quando houver necessidade de bloqueio do período completo o status do período mudará para "Totalmente Bloqueado" após confirmação do bloqueio e na pasta "Funcionários" não haverá informação de quais funcionários estão travados porque todos no período estarão bloqueados e somente poderão ser desbloqueados juntos. Para desbloqueio deverá ser selecionado o período e pressionar o botão "Desbloquear". O Status do período passará para "Livre", após confirmação do desbloqueio.   
   
Para o "Bloqueio Parcial" deverá ser selecionado o período, marcar o parâmetro "Bloqueio Parcial", informar a chapa ou "código de quebra" ou selecionar funcionários e pressionar o botão "Bloquear". O status do período mudará para "Parcialmente Bloqueado". Na opção "Funcionários" serão apresentados todos os funcionários com movimentação no período travados ou destravado conforme o filtro de seleção. Nesta opção poderá ser feito o bloqueio ou desbloqueio de determinado funcionário acionando os botões a direita da tela.   
   
Para desbloqueio, o usuário deverá selecionar o período e clicar no botão "Desbloquear" para que o período volte para o status "Livre". O usuário também poderá marcar o parâmetro "Bloqueio Parcial" e desbloquear parte dos funcionários informando a chapa ou código da quebra ou selecionar funcionário.  
   
A ordenação inicial dos funcionários poderá ser feita por qualquer coluna da visão bastando clicar na coluna desejada.  
   
**Atenção:**  
O desbloqueio parcial somente poderá ser utilizado se a coluna "Status" do Período selecionado estiver igual a "Parcialmente Bloqueado". Caso seja utilizada estando a coluna "Status" igual a "Totalmente Bloqueado", mesmo que selecione determinado grupo de funcionários serão desbloqueados todos os funcionários.

O usuário poderá efetuar o bloqueio e desbloqueio dos funcionários de acordo com as permissões de filtro de usuário cadastrados.
