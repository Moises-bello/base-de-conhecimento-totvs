---
content_hash: f1da48767da93cec2ae58fb260dbb3fdae4bc8d41eac23e8ed045c3e29e151a9
fetched_at: '2026-06-29T00:09:14.211092+00:00'
page_id: '421385156'
product: rm
source: tdn-rm
title: Contrato Marco Contratual
type: documentation
url: https://tdn.totvs.com/display/LRM/Contrato+Marco+Contratual
version: 3
---

O contrato do tipo Marco contratual foi criado possibilitando estabelecer metas a serem cumpridas para cada atividade do projeto. A sua utilização será na tela de cadastro de contratos, sendo um tipo a ser definido como Marco Contratual. Após a criação do contrato, deverá ser definido o(s) marco(s) contratual(is), este processo estará disponível na opção "Associação de itens ao contrato".

Ao associar itens, existe um anexo fixo na parte inferior da tela de associação de itens, onde serão exibidos todos os insumos que são recursos da tarefa (itens   do contrato) conforme os insumos presentes na curva ABC. O cálculo do projeto deve ser executado previamente para que os valores da Curva ABC sejam atualizados.

Caso a opção "Rateio automático dos produtos associados" seja marcada, o processo irá ratear os produtos de acordo com os valores informados no detalhamento da tarefa.

Os processos de Liberação do Contrato para o Totvs Obras e Projetos e para o Financeiro e Gerar Integração com Suprimentos\Faturamento continuam disponíveis, mesmo que o projeto utilize o detalhamento de itens.   
Logo após o cadastro do(s) marco(s) o usuário poderá realizar a associação de metas ao marco cadastrado. Esta associação estará disponível no anexo de itens de contrato. Contratos do tipo marco contratual, não irá utilizar medições, e sim liberação de um marco contratual alcançado. A visualização se uma meta foi alcançada, ou não, será através do cronograma realizado ou do Pert.

Para realizar o cadastro de um contrato do tipo Marco Contratual: Acesse o menu Cadastros - Contrato - Ao incluir um novo contrato, o sistema habilita uma opção de tipo do contrato, deverá ser informado Marco Contratual.(Este tipo de contrato não utilizará periodicidade, pois o marco alcançado no projeto não necessita de uma data pré-definida).

Para contratos com finalidade Marco Contratual do tipo "A Receber" ficarão disponíveis as opções Planilha de Atividades e Planilha de Serviço, onde suas informações poderão ser utilizadas para execução do projeto.   
Após cadastrar e salvar um contrato com finalidade Marco Contratual, o sistema não possibilita a alteração da finalidade do contrato.  
As abas Fórmula, Reajuste e Default não sofrerão nenhuma alteração em relação aos demais contratos.  
Todo novo contrato do tipo marco contratual, terá o seu status EM ANDAMENTO, como já é realizado nos outros contratos, se necessário alterar o default do status do contrato, acesse o Parâmetros do Projeto - Contratos.  
O cadastro de marco contratual utilizará a tela de "associação de Itens ao contrato" e todas as consistências deste processo seguiram a estrutura usada no contrato de serviço.

É sugerido que o usuário use tarefas do tipo marco, inserindo "quantidade" igual a 1, e o valor na coluna "valor unitário contratado".  
A Associação de metas as tarefas: Metas são as tarefas contidas na Planilha de Atividades ou Planilha de Serviço que farão parte do marco, contendo um percentual de conclusão. Assim para realizar a funcionalidade de associação de metas ao marco contratual, será utilizado o anexo "itens de contrato", nesta visão serão mostrados o(s) marco(s) cadastrado(s) e ao editar um marco contratual, será disponibilizado no menu anexos, uma nova opção chamada "metas", esta opção estará disponível apenas para contratos do tipo marco contratual. Poderá ser inserido uma ou mais metas ao marco selecionado. Quando o percentual informado da meta for atingido, o marco contratual já esta pronto a ser liberado pelo usuário, caso um marco não possua metas associadas, este marco contratual poderá ser liberado em qualquer momento. Não poderá ser associadas metas com percentual de conclusão nulo, menor ou igual a zero ou maiores que cem. Será disponibilizada a opção de exclusão da meta associada ao marco contratual, ela apenas poderá ser executada, caso algum dos processos abaixo não estiver sido realizado: - Marco Liberado; - Status do contrato igual a Concluído, Cancelado, Paralisado;  
Poderá ser inserido uma ou mais metas ao item de contrato, ou seja, é possível inserir várias tarefas a uma meta, não sendo possível repeti-las. Quando o percentual informado da meta for atingido, o marco contratual já esta pronto a ser liberado pelo usuário, caso um marco não possua metas associadas, este marco contratual poderá ser liberado em qualquer momento. Não poderá ser associadas metas com percentual de conclusão nulo, menor ou igual a zero ou maiores que cem. Será disponibilizada a opção de exclusão da meta associada ao marco contratual, ela apenas poderá ser executada, caso algum dos processos abaixo não estiver sido realizado: - Marco Liberado; - Status do contrato igual a Concluído, Cancelado, Paralisado;

Se o marco já foi liberado para o lançamento (baixado pelo faturamento da liberação), não será permitida a sua exclusão, da mesma forma que é realizada nos outros contratos.
