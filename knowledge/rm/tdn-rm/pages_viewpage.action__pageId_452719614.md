---
content_hash: 7f94f6232d47cbc94b2604d55d8d01b0b441ba948da3da556fe4e0e04d7af492
fetched_at: '2026-06-29T00:10:08.962057+00:00'
page_id: '452719614'
product: rm
source: tdn-rm
title: Pasta Identificação - Requisição de Aumento de Quadro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719614
version: 2
---

**Pasta Identificação - Requisição de Aumento de Quadro**

Na pasta Identificação os seguintes dados devem ser informados:

**Número -** Gerado automaticamente e com valor único.

**Status -** Será apresentado logo após a abertura da requisição como  "Pendente". Este campo será alterado a medida que a requisição for avançando no fluxo de aprovações assumindo os valores parametrizados para cada etapa.

Para verificar a parametrização acesse: Configurações | Tipos de Requisições.

Os status que poderão ser definidos pelo fluxo de aprovação são "Em Andamento", "Aprovado" e "Reprovado". Os status "Suspenso" e "Cancelado" serão definidos conforme a utilização do processo "Suspender requisição " e "Cancelar Requisição" respectivamente.

O status "Concluído" será determinado quando todas as vagas aprovadas na requisição forem utilizadas, seja nos processos relacionados a efetivação da admissão de candidatos ou nas alterações dos dados funcionais de funcionário(s).

Quando a requisição adquirir o status "Aprovado" significa que a mesma ficará disponível para utilização no Totvs Gestão de Pessoas, nos processos relacionados à Seleção de Pessoal e Admissão, conforme utilização do parâmetro relacionado à requisição.

Os status das requisições são representados pelas cores:

Aprovada – cor verde

Cancelada – cor preta

Concluída – cor roxa

Em Andamento – cor amarela

Pendente – cor laranja

Reprovada – cor vermelha Suspensa – cor azul

**Nome do Aprovador Atual -** Este campo não é editável e apresentará o nome do aprovador atual da requisição, ou seja, o responsável atual pela requisição, conforme definição do fluxo de aprovações.

**Requisitante -** Somente podem ser selecionados chefes da coligada na qual o usuário do Totvs Gestão de Pessoas esteja logado. Esta informação poderá ser modificada enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Caso a requisição seja aberta pelo "Totvs RM Portal" este campo exibirá o nome do usuário logado não podendo ser modificado.

**Previsão -** Deverá ser informada a data prevista para a contratação solicitada, não podendo receber um valor inferior à data atual (data do dia). Este campo poderá ser alterado enquanto a requisição estiver pendente ou em andamento, e caso a requisição esteja pendente, apenas se nenhum parecer tiver sido cadastrado.

**Vagas solicitadas -** Deverá ser informado o número de vagas solicitadas para atender o aumento de quadro. Este campo poderá ser alterado enquanto a requisição estiver pendente ou em andamento, e caso a requisição esteja pendente, apenas se nenhum parecer tiver sido cadastrado.

**Justificativa -** Ao solicitar um aumento de quadro deverá ser informada uma justificativa para tal solicitação. Este campo poderá ser alterado enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado.

**Filial -** Após o preenchimento do campo "Requisitante", este campo ficará habilitado permitindo que seja selecionada a filial de destino da requisição de aumento de quadro, ou seja, aonde se deseja realizar a contratação. Neste campo, serão exibidas apenas as filiais onde o requisitante seja chefe de alguma seção e a filial pertencer à coligada em que o usuário está logado, sendo que esta informação poderá ser alterada enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Se houver alteração do requisitante, o conteúdo deste campo será apagado e o usuário deverá preenchê-lo novamente.

**Seção -** Após o preenchimento do campo "Filial", este campo ficará habilitado permitindo que seja selecionada a seção de destino da requisição de aumento de quadro, ou seja, aonde se deseja realizar a contratação. Somente poderá ser selecionada uma seção pertencente à filial que tiver sido selecionada, sendo que esta informação poderá ser alterada enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Se houver alteração da "Filial", o conteúdo deste campo será apagado e o usuário deverá preenchê-lo novamente.

**Função -** Após o preenchimento do campo "Seção", este campo ficará habilitado permitindo que seja selecionada a função de destino da requisição de aumento de quadro, ou seja, aonde se deseja realizar a contratação. Somente poderá ser selecionada a função que tenha cadastrada em seu quadro de lotação a seção selecionada anteriormente. Não existindo registros no quadro de lotação da função, TODAS as funções cadastradas no sistema devem ser exibidas.

Este campo poderá ser alterado enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Se houver alteração da "Seção", o conteúdo deste campo será apagado e o usuário deverá preenchê-lo novamente.

**Tabela -** Caso esteja configurada a utilização das tabelas salariais será exibido, neste campo, o nome da tabela associada à seção e função, previamente selecionadas. Para verificar esta configuração acesse: Configurações | Parametrizador | Gerais | Validações | "Remuneração".

**Nível e Faixa -** Após o preenchimento dos campos "Seção" e "Função" e se o parâmetro "Considerar os salários das tabelas salariais" estiver marcado, serão apresentados os níveis e as faixas da tabela vinculada à seção/função ou ao quadro de lotação. Estes campos poderão ser alterados enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Se houver alteração da "Seção" o conteúdo dos campos "Nível" e "Faixa" serão apagados e o usuário deverá preenchê-los novamente. Para saber como funciona a vinculação de tabelas acesse: Valorização | Tabelas Salariais/Vinculação.

**Salário -** Com a utilização de tabela salarial, o salário proposto será automaticamente preenchido com base no nível e faixa salarial selecionados. O campo salário será habilitado se a empresa não trabalhar com tabelas salariais e, neste caso, o valor do salário deverá ser informado diretamente neste campo, ou, caso seja parametrizada a utilização das tabelas salariais, o parâmetro "Não permitir alterar diretamente o salário" deverá estar desmarcado, para que este campo permita alterações.

Este campo poderá ser alterado enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Se houver alteração do nível salarial, da faixa salarial, da seção ou da função o conteúdo deste campo será apagado e o usuário deverá preenchê-lo novamente.

**Observações**

Enquanto a requisição estiver com status "Pendente" os dados desta pasta poderão ser alterados, caso o status seja "Em andamento" as alterações somente poderão ser feitas através da inclusão de pareceres.

Ao editar uma requisição que esteja com status "Em andamento", o sistema exibe, no lugar dos dados originais da requisição, os dados correspondentes ao último parecer registrado de modo a posicionar o aprovador atual sobre as mudanças mais recentes. Somente se não existir nenhum parecer anterior, o sistema exibirá os dados originais da requisição.  
Requisições em andamento, suspensas, canceladas, aprovadas, reprovadas ou concluídas não podem ser excluídas. Apenas requisições pendentes poderão ser excluídas!
