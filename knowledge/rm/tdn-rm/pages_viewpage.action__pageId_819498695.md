---
content_hash: 51f847f4bddea42471014bcef2c6312a33dc05792671198bc337ec530799c31a
fetched_at: '2026-06-29T00:11:45.137632+00:00'
page_id: '819498695'
product: rm
source: tdn-rm
title: Mão de Obra - TCOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819498695
version: 8
---

Através do cadastro de Mão de Obra é possível inserir e editar os dados referentes às mãos de obra necessárias para execução das ordens de serviços, bem como identificar através do Parque de Máquinas, quais os objetos foram instalados por tais mãos de obra.

Estarão disponíveis para o cadastro de mão de obra, funcionários e/ou pessoas previamente cadastrados. Através do parâmetro "Listar Somente Funcionários" será possível listar somente pessoas cadastradas como funcionários ativos. O cadastro de Funcionários pode ser realizado no aplicativo RM Officina ou no RM Labore e o cadastro de Pessoas no RM Vitae. Caso a empresa não possua o aplicativo RM Vitae, somente funcionários estarão disponíveis para o cadastro de mãos-de-obra.

**Observação:** Toda vez que for cadastrada uma nova mão-de-obra para uma determinada coligada, será dada ao usuário a opção de escolher em quais Tipos de Objetos de Manutenção este funcionário terá permissão para trabalhar. Será apresentada uma janela perguntando ao usuário se ele deseja associar a mão de obra a algum tipo de objeto. Caso a resposta seja sim, ele poderá escolher o(s) tipo(s) de objeto(s) que será(ao) associado(s) ao funcionário. Se for inserido um funcionário como mão de obra que esteja com status demitido, a mesma não aparecerá para ser alocada no momento de alocar mão de obra na Ordem de Serviço.

Caso o funcionário não possua serviço alocado, será apresentada a última data e hora de atualização (clicando no botão Atualiza Previsão de Disponibilidade). Caso o funcionário esteja executando algum serviço ou tenha serviços já alocados (o que é possível verificar em Mão-de-Obra | Cronograma Pessoal | Visão de Cronograma Pessoal), o campo apresentará data e hora em que o funcionário terminará o último serviço e poderá começar outro.

**Recalculo do Custo da Mão de Obra**

Esta funcionalidade permite recalcular o valor de um item da ordem de serviço de acordo com o valor do custo da mão de obra que esta alocada para ele.  
Para que essa funcionalidade possa ser acessada no sistema o usuário deverá marcar o parâmetro "Somar Custo da Mão de Obra ao Custo Financeiro da OS" em Opções | Parâmetros | Sistema | Aba – Ordem de serviço, ao marca-lo o botão Recalcular Custo será exibido na tela de visão da ordem de serviço.  
Para realizar o recalculo o usuário deverá clicar no botão "Recalcular Custo" e selecionar o serviço que se deseja realizar o recalculo. Ao finalizar o recalculo será exibido um log de atualização dentro da tela do WIZARD e os campos "Preço Unitário" e "Valor Total do item" que fica dentro do item da OS serão atualizados com o novos valores recalculados. Exemplo: Por exemplo, se para o serviço A houve apontamento da mão-de-obra H nos intervalos de 08:00 às 12:29 e 14:18 às 17:51, as horas efetivas dessa mão-de-obra no serviço A são 8 horas e 2 minutos. Logo, supondo que o custo/hora da mão-de-obra cadastrado para a mão de obra em questão é R$ 5,66, tem-se que 8,03 X 5,66 = R$45,45

Então R$ 45,45 (quarenta e cinco reais e quarenta e cinco centavos) será o valor adicionado ao preço unitário do serviço.  
Se o preço do serviço for R$ 15,00, o seu preço unitário será atualizado para R$ 60,45 pois será contabilizado a ele o preço do custo da mão de obra que foi de 8 horas.

Ao final do processo de recalculo do custo será exibido um log de atualização dentro do WIZARD, esse log pode ser visualizado em bloco de notas clicando no botão "Bloco de notas".

**Anexos - Mão de Obra**

**Tipo de Objeto por Mão-de-Obra**

Nesta janela é possível associar as pessoas habilitadas para execução dos serviços para cada Tipo de Objeto de Manutenção. Nas ordens de serviços com status 'Em Andamento' a Mão-de-obra. Selecionada será alocada de acordo com sua disponibilidade, quando esta se tratar de funcionários da própria empresa.

Para associar Pessoas (terceiros) como Mão-de-Obra na execução de serviços no RM Officina é necessário a integração deste aplicativo com o aplicativo RM Vitae onde é realizado todo o cadastro de pessoas. Caso você não possua o aplicativo RM Vitae, toda Mão-de-Obra alocada será proveniente do castrado de funcionários, realizado no RM Officina com integração com o aplicativo RM Labore.

**Modelo por Mão de Obra**

Nesta janela é possível associar as pessoas habilitadas para execução dos serviços para cada Modelo. Nas ordens de serviços com status 'Em Andamento' a Mão-de-obra selecionada será alocada de acordo com sua disponibilidade, quando esta se tratar de funcionários da própria empresa.

**Sub-Modelo por Mão de Obra**

Nesta janela é possível associar as pessoas habilitadas para execução dos serviços para cada Sub-Modelo. Nas ordens de serviços com status 'Em Andamento' a Mão-de-obra selecionada será alocada de acordo com sua disponibilidade, quando esta se tratar de funcionários da própria empresa.

**Objeto de Manutenção**

Este anexo irá exibir diretamente na tela da visão, as informações sobre o Objeto de Manutenção, tais como Data da Instalação, Identificador do Objeto, Local da Instalação e Histórico.

**Histórico de custo de mão-de-obra**

Este anexo permite ao usuário visualizar e editar o histórico de todos os custos já vinculados a esta mão de obra em cada mês.

O custo no anexo "Histórico de Custo da Mão de Obra" será utilizado no recalculo da ordem de serviço quando o usuário rodar o processo "Recalcular Custo" que se encontra na tela de visão da ordem de serviço.

**Processos - Mão de Obra**

**Atualização do Custo da Mão de Obra**

Através do processo "Atualização de custo" é possível atualizar o custo que é visualizado no histórico de custo da mão de obra. O usuário poderá atualizar o custo importando de uma planilha que esteja cadastrada na base do CorporeRM.

Para acessar o processo de "Atualização de Custo" basta acessar Manutenção de equipamentos | Mão de Obra | Processos | Atualização de custo e selecionar pelo menos uma mão de obra. Será aberto um WIZARD onde o usuário terá que preencher os dados e Executar onde será atualizado o custo da mão de obra.

Após marcar "Definir Planilha" o usuário deverá informar o nome da planilha, a coluna Identificadora (Coluna da planilha onde se encontra o código da mão de obra) e a coluna Custo/hora (Coluna da planilha onde se encontra o custo da mão de obra), ao preencher esses dados deverá clicar em Executar, será realizada a importação dos dados da planilha cujo os dados foram informados no passo anterior.

Caso a Planilha não seja definida manualmente com o parâmetro "Definir Planilha", os dados do cadastro da Mão de Obra serão considerados para o cálculo do custo dos registros selecionados. Os dados utilizados no momento do cadastro da Mão de Obra devem ter sido previamente informados a partir de uma planilha cadastrada no sistema.

Exemplo:

| Id. Planilha | Planilha de custo |
| --- | --- |
| Coluna Identificadora | A |
| Coluna Custo/Hora | B |

Marcando a opção "Visualizar", ao clicar no botão "Calcular" a planilha será aberta para que o usuário possa alterar algum dado nela antes de importa-los para o histórico.

Se os dados da planilha não forem informados corretamente em Mão de obra, aba "Planilha de Calculo" da mão de obra, o sistema exibirá um erro e não fará a importação dos dados.As planilhas são cadastradas no menu Gestão| Planilha Net.

**Agendamento de Mão-de-Obra**

O agendamento técnico da OS tem como objetivo o controle de agenda do técnico que irá realizar os serviços nas OS. Com esse controle poderá ser definido a data para agendamento da execução do serviço pelo técnico no momento de alocação de mão de obra no serviço.  
   
**Parametrização**

Para que esta funcionalidade possa ser utilizada é necessário marcar o parâmetro "Controla Agendamento de Mão de Obra" que se encontra no menu Manutenção | Parâmetros | aba Ordem de Serviço.  
Para que este parâmetro fique visível para o usuário marcá-lo, será necessário marcar também o parâmetro "Controla Alocação de Mão de obra".   
Além de marcar o parâmetro o usuário deverá ter permissão de acesso para Inserir, editar e excluir um agendamento, e a Agenda Técnica da Mão de Obra do Serviço,  permissão é dada no modulo de Serviços Globais | menu Segurança | Perfil escolhendo o perfil do usuário.

**Processo de Agendamento Técnico**

Para realizar um agendamento técnico basta acessar a tela de alocação de mão de obra, selecionar a mão de obra e clicar no ícone na parte superior "Agendamento de Mão Obra".   
O sistema irá abrir um WIZARD. Na primeira tela serão exibidos na grid os agendamentos realizados para a mão de obra selecionada, clique em avançar.   
Na próxima tela será feito o agendamento. Selecione uma data inicial e uma data final e preencha o campo observação.   
O sistema irá calcular a data final de acordo com o tempo previsto para a realização do serviço cadastrado na aba Integração, no campo "Tempo de serviço" no cadastro de produtos/serviços.  
Se o usuário não quiser seguir o tempo calculado pelo sistema com base no tempo de realização do serviço ele poderá alterar esse tempo no momento de inserir os dados do agendamento.  
Depois que o agendamento é criado ele pode ser visualizado através do menu Mão de Obra | Agenda Técnica da Mão de Obra do Serviço.   
Ao clicar nesse menu será aberto uma grid com todos os agendamentos realizados. É possível visualizar o numero da OS, a data de início e fim do agendamento, o serviço dentre outros dados. Selecionando o agendamento e clicando em Anexo é possível visualizar o item da OS e clicando no anexo do item da OS é possível também iniciar, interromper, terminar os apontamentos e efetuar desconto/despesa para o item da OS.

Caso já exista um agendamento de serviço para o técnico na data informada, o sistema irá exibir mensagem ao usuário informando que já existe um agendamento naquela data.  
A data inicial do agendamento deverá ser maior que a data de emissão da OS.  
A data final do agendamento deverá ser maior que a data inicial.  
Ao excluir a alocação de mão de obra o sistema irá verificar se existe agendamento para o técnico e caso exista o mesmo será excluído.  
Ao excluir a OS o sistema irá verificar se existe agendamento para o técnico e caso exista o mesmo será excluído. Não poderão existir registros de agendamento sem que aja uma OS para este agendamento.

**Iniciar Apontamento para Serviços ou Mão-de-obra**

Os apontamentos de serviços podem ser feitos de duas formas:

1. A primeira é através da visão de itens da Ordem de Serviço, ao clicar em Processos, "Iniciar apontamento do serviço". Nesta opção será possível iniciar o apontamento para um ou mais serviços;
2. ou através da edição do item de serviço, pasta mão-de-obra ao clicar no botão "Incluir". Nesta opção só é possível iniciar o apontamento para o serviço que foi selecionado.

* + Ao **iniciar** um apontamento, o serviço ficará com status "Em Andamento";
  + Ao **interromper** um apontamento, o serviço ficará com status "Interrompido";
  + Ao **terminar** um apontamento, o serviço ficará com status "Terminado".

O apontamento é feito apenas para itens do tipo serviços e mão de obra ativa.  
A data e hora de início do apontamento não poderão ser maiores que a data atual.  
A data e hora de início não poderão ser menores que a data e hora de emissão da ordem de serviço.  
A data e hora de término não podem ser maiores do que a atual.  
A data e hora de término não podem ser menores ou iguais à data e hora de inicio.  
Ao incluir vários apontamentos para uma mão-de-obra em um mesmo serviço, a data e hora de início do novo apontamento não poderão ser menores que data e hora do término do último apontamento.No cadastro de Produtos/Serviços, anexos "Produto – Informações de manutenção", ao marcar o parâmetro "Permite abertura simultânea para mesma mão-de-obra", o sistema permite fazer apontamentos simultâneos para uma mesma mão de obra.   
Através do menu Cadastro | Segurança | Perfis | edição, pasta "Acesso à Menus", é possível remover as permissões de acesso aos botões iniciar, interromper e terminar apontamento de mão-de-obra, para determinado perfil de usuários.   
Faça o logout/login no sistema para que as alterações sejam validadas.
