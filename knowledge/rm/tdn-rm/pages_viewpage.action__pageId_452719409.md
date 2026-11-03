---
content_hash: 7737a077a373f009f946a2656b704a1135e206e7fccc5a22855d0174ae585921
fetched_at: '2026-06-29T00:10:07.349819+00:00'
page_id: '452719409'
product: rm
source: tdn-rm
title: Pasta Identificação - Requisição de Substituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719409
version: 2
---

**Pasta Identificação - Requisição de Substituição**

Na pasta Identificação os seguintes dados devem ser informados:

**Número -** Gerado automaticamente e com valor único.

**Status -** Será apresentado logo após a abertura da requisição como "Em Andamento". Este campo será alterado a medida que a requisição for avançando no fluxo de aprovações assumindo os valores parametrizados e definidos para cada etapa.

Para verificar a parametrização acesse: Configurações | Tipos de Requisições.

Os status que poderão ser definidos pelo fluxo de aprovação são "Em Andamento", "Aprovado" e "Reprovado". Os status "Suspenso" e "Cancelado" e serão definidos conforme a utilização do processo "Suspender requisição " e "Cancelar Requisição" respectivamente.

O status "Concluído" será determinado quando todas as vagas aprovadas na requisição forem utilizadas, seja nos processos relacionados a efetivação da admissão de candidatos ou nas alterações dos dados funcionais de funcionário(s).

Quando a requisição adquirir o status "Aprovado" significa que a mesma ficará disponível para utilização no Totvs Gestão de Pessoas, nos processos relacionados à Seleção de Pessoal e Admissão, conforme utilização do parâmetro relacionado à requisição.

**Os status das requisições são representados pelas cores:**

Aprovada – cor verde

Cancelada – cor preta

Concluída – cor roxa

Em Andamento – cor amarela

Pendente – cor laranja

Reprovada – cor vermelha

Suspensa – cor azul

**Nome do Aprovador Atual -** Este campo não é editável e apresentará o nome do aprovador atual da requisição, ou seja, o responsável atual pela requisição, conforme definição do fluxo de aprovações.

**Conclusão -** Irá apresentar a data que a requisição foi concluída.

**Requisitante -** Exibirá o mesmo nome do requisitante da requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Previsão -** Exibirá a mesma data prevista da requisição pai que está vinculada à requisição de substituição. Este campo poderá ser alterado enquanto a requisição estiver pendente ou em andamento, e caso a requisição esteja pendente, apenas se nenhum parecer tiver sido cadastrado.

**Requisição Vinculada (PAI) -** Exibirá o código e o tipo da requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Substituição de -** Exibirá o nome do funcionário ou ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Substituto -** Exibirá o nome da pessoa que foi admitida ou realocada para atender à requisição de substituição. Este campo é visível somente nas requisições com status "Concluída" e não é editável.

**Filial -** Exibirá a mesma filial da lotação do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Seção -** Exibirá a mesma seção da lotação do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Função -** Exibirá a mesma função do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Tabela -** Caso esteja configurada a utilização das tabelas salariais será exibido, neste campo, o nome da tabela associada à seção e função, previamente selecionadas.

**Nível e Faixa -** Se o parâmetro "Considerar os salários das tabelas salariais" estiver marcado, serão apresentados o nível e a faixa salarial do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Estes campos poderão ser alterados enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado.

**Salário -** Com a utilização de tabela salarial, o salário proposto será automaticamente preenchido com base no nível e faixa salarial selecionada. O campo salário será habilitado se a empresa não trabalhar com tabelas salariais e, neste caso, o valor do salário deverá ser informado diretamente neste campo, ou, caso seja parametrizada a utilização das tabelas salariais, o parâmetro "Não permitir alterar diretamente o salário" deverá estar desmarcado, para que este campo permita alterações. Este campo poderá ser alterado enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Se houver alteração do nível ou da faixa salarial este campo também sofrerá alterações,  assumindo o valor referente à Tabela Salarial.

**Observações**

Enquanto a requisição estiver com status "Pendente" os dados desta pasta poderão ser alterados, caso o status seja "Em andamento" as alterações somente poderão ser feitas através da inclusão de pareceres.

Ao editar uma requisição que esteja com status "Em andamento", o sistema exibe, no lugar dos dados originais da requisição, os dados correspondentes ao último parecer registrado de modo a posicionar o aprovador atual sobre as mudanças mais recentes.

Somente se não existir nenhum parecer anterior, o sistema exibirá os dados originais da requisição. Requisições em andamento, suspensas, canceladas, aprovadas, reprovadas ou concluídas não podem ser excluídas. Apenas requisições pendentes poderão ser excluídas!
