---
content_hash: f2780831573065f6c279033204305d217c7e2d89315b4c9723f98b77a2142c9d
fetched_at: '2026-06-29T00:09:15.338889+00:00'
page_id: '421385351'
product: rm
source: tdn-rm
title: Contrato de Parcela Fixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Contrato+de+Parcela+Fixa
version: 3
---

O contrato de parcela fixa tem como objetivo gerar parcelas com valores iguais, com períodos já medidos, afim de simplificar e dar agilidade ao negócio.   
 A definição do Contrato de Parcela Fixa é feito no cadastro, no campo Finalidade do Contrato.   
 Na aba identificação, é definido o Tipo do contrato, que pode ser "A Pagar" ou "A Receber". Os campos Num. do Contrato, Cod. Cliente Fornecedor, Data Contrato, Data Início, Data Término e Quantidade de Parcelas são obrigatórios. A unidade mínima para o campo Quantidade de Parcelas será de 1 (um) dia, dividindo os dias do contrato pelo o número de parcelas.

Para contratos o tipo "A Receber" ficarão disponíveis as opções Planilha de Atividades e Planilha de Serviços onde suas informações poderão ser utilizadas para execução do projeto.   
Depois de cadastrar e salvar o contrato, não será possível alterar a finalidade e o tipo do contrato, assim como a associação às Planilhas (de Atividades ou de Serviços).   
No Contrato de Parcela Fixa as abas "Fórmula" e "Reajuste" ficam desabilitados.  A aba "Defaults" permanece habilitada, porém o campo "Valores Defaults para Retenção de Contratos" fica desabilitado.  
Associação de itens ao Contrato é efetuada ao clicar no ícone "Associação de itens ao contrato" ou acessando Processos - "Associação de itens ao contrato". Em seguida, o sistema faz uma verificação para que o cálculo do projeto seja efetuado, ela é importante para que os itens não sejam associados com valores desatualizados. Serão apresentados os itens de acordo com a planilha escolhida, Atividades ou Serviços, onde será possível definir os percentuais para associação pelo ícone "Associar quantidade total dos itens selecionados ao contrato" ou definir um percentual pelo ícone "Associação percentual dos itens selecionados". A associação de itens deve ser previamente parametrizada nos Parâmetros do Projeto Parâmetros do Projeto para que o sistema respeite a associação com percentual maior ou igual a 100%. É possível retirar a associação do item ao contrato efetuando o mesmo processo de associação, pelo ícone "Remover associação".    
Ao associar itens, existe um anexo fixo na parte inferior da tela de associação de itens, onde serão exibidos todos os insumos que são recursos da tarefa (itens   do contrato) conforme os insumos presentes na curva ABC. O cálculo do projeto deve ser executado previamente para que os valores da Curva ABC sejam atualizados.

Caso os itens tenham diferentes percentuais de associação, é necessário que cada item seja marcado e definido o percentual, em seguida é necessário remarcar todos os itens que serão associados e só então executar o processo, caso contrário, o sistema só associará o ultimo item marcado.  
A geração de parcelas fixas é efetuada pelo processo "Geração de períodos de contrato com Parcelas Fixas".  Na tela de geração de períodos constam os dados do contrato.  Nessa tela, é possível efetuar uma simulação dos períodos, para verificar datas e valores de cada parcela. Com o ícone "Retorna os períodos para o estado original" é possível desfazer a simulação. Também é possível gerar os períodos como dias úteis, marcando a opção "Somente dias úteis" e considerando os parâmetros do projeto Parâmetros do Projeto.

Os períodos são gerados apenas quando o processo for executado, e estes são gerados com medição. No contrato de Parcela Fixa, não é possível criar períodos complementares e de estorno.

A alteração do número de períodos do contrato poderá ser efetuada alterando o número de parcelas na edição do contrato ou por meio de Aditivo Contratual. No ícone "Aditivos Contratuais" ou em Processos - "Aditivos Contratuais", é possível criar um aditivo de tempo, informando quanto tempo o contrato será expandido e de custo, associando um item ao aditivo. Em ambos os casos é possível simular a geração de Períodos e então executar o processo.

No contrato de Parcela Fixa é possível excluir períodos medidos. Se os períodos estiverem liberados, é necessário cancelar a liberação. Para distribuir o valor do período cancelado, é necessário efetuar a "Geração de períodos de contratos com parcela fixa" no menu Processos. Serão alterados apenas os valores de períodos medidos, os períodos cancelados e liberados não serão alterados.  
No contrato de parcela fixa, é possível cancelar um período através do processo "Cancelar Período". Diferente da exclusão, o valor do período cancelado não será distribuído entre os demais em aberto. Apenas períodos medidos poderão ser cancelados. Os períodos cancelados poderão ser reativados pelo processo "Reativar período".  
No contrato de parcela fixa é possível efetuar o Rateio por produto e por Centro de Custo editando a medição. A grandeza aplicada ao rateio deverá ser a mesma aplicada à medição, ou seja, valor/percentual/quantidade;  
  
O produto a ser rateado será escolhido apenas editando a medição.

É possível liberar os períodos do Contrato de Parcela Fixa para o Totvs Obras e Projetos e para o Financeiro através do ícone "Liberar Período". Nessa tela, a aba Retenções/Deduções ficará desabilitada. Também é possível gerar Integração com Suprimentos /Faturamento.

O cálculo do Contrato de Parcela Fixa irá considerar os valores de períodos cancelados e o cálculo do valor total medido irá considerar apenas períodos ativos.
