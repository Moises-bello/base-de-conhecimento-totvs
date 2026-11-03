---
content_hash: ccc6ac3ae09805450dc06abd1a304462f24a1f81810425fb03c00a07b96705b5
fetched_at: '2026-06-29T00:10:42.964956+00:00'
page_id: '547880159'
product: rm
source: tdn-rm
title: Orcamento Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Orcamento+Folha+de+Pagamento
version: 9
---

## Descrição

Através do Totvs Folha de Pagamento, o usuário pode criar e gerar orçamentos, possibilitando fazer previsões de custos futuros.

## Procedimento para Utilização

O usuário pode simular o cálculo de uma folha fazendo admissões, demissões, transferências, reajuste de salário, cálculo de férias, entre outros.

**Parâmetros de Orçamento**

Definições de parâmetros gerais do orçamento para efetuar, dentre outras operações, processos em lote. Essas definições são por coligada.  
  
**Parâmetros Default**

Na tela abaixo, estão definidos os parâmetros default para admissão, demissão, transferência e promoção. Estes parâmetros tem a finalidade de facilitar o cadastro já preenchendo os dados default ao inserir um novo registro. Caso os parâmetros default não sejam cadastrados, o usuário ao cadastrar um novo registro de admissão, demissão, transferência ou promoção tem que preencher as informações manualmente.

Este cadastro está disponível no Parametrizador.

**Parâmetros de Admissão**

*Lookup – Motivo da Admissão*

*****Lookup*–*Tipo de Funcionário (normal, autônimo, diretor, estagiário, etc)***

*Lookup – Sindicato*

**Lookup – Horário**

*Lookup – Letra (índice inicial do horário)   
Jornada*

***Melhorias no perfil de admissão:*** O campo Chapa Base era utilizado apenas para preenchimento de dados no cadastro do perfil. O cadastro foi alterado para o campo ser gravado na base e foi criada a função de fórmula CHAPABASE para recuperar a chapa informada.  
Desta forma, é possível criar fórmulas para recuperar demais informações do funcionário base.

No step de admissão também foi criado o campo Chapa Base. Desta forma mesmo não utilizando um Perfil de Admissão é possível informar uma chapa base.  
Após selecionar a chapa base os campos Seção, Função, Tipo de Funcionário, Tipo de Recebimento, Sindicato, Horário, Faixa e Nível salarial serão preenchidos com os dados do funcionário base.  
É possível utilizar o perfil ou a chapa base. Ao selecionar um perfil o campo chapa base ficará desabilitado. O mesmo acontecerá ao selecionar uma chapa base, neste caso o campo perfil será desabilitado.

***Campos Complementares***  
Foi criado um cadastro para Campos Complementares de Orçamento. Estes campos são utilizados apenas para admissões feitas no orçamento.  
Os valores destes campos poderão ser informados no Step de Admissão. Foi criada a função de fórmula TABCOMPLORC para retornar o valor de um campo complementar de orçamento.  
Para os funcionários já existentes na base, ao executar o cálculo do orçamento onde existam fórmulas que utilizem valores de campos complementares, os valores serão recuperados dos campos complementares atuais do funcionário (PFCOMPL), ou seja, não será possível fazer a edição dos campos complementares no módulo de orçamento.

*Cadastro Campos Complementares de Orçamento*

*Campos Complementares no step de Admissão*

***Observação: Para que os dados complementares da admissão sejam gravados, será necessário avançar até o Finalizar processo e utilizado os botões "Salvar" ou "Salvar e Executar" para que os dados sejam persistidos na base.***

***Melhorias Itens de Orçamento***

Foi criado um cadastro para Itens de Orçamento. Neste cadastro são informados um código, uma descrição e os eventos que compõe o item de orçamento.  
Sua finalidade é funcionar com um agrupador de eventos para gerar relatórios e informações gerenciais.

*Item de Orçamento*

****Parâmetros de Demissão****

*- Tipo da Demissão (“2 - Inic.Empregador sem justa causa” e “4 - Inic.Empregado sem justa causa”)*

*- Motivo da Demissão*

*- Tem Aviso Prévio Indenizado* 

*- Desconta Aviso Prévio (Campo deve ficar habilitado caso o tipo de demissão for igual a 4 e o campo “Tem Aviso Prévio Indenizado” não estiver marcado.)*

*- Dias de Aviso (Deve ficar habilitado se os campos “Têm Aviso Prévio Indenizado” ou “Desconta Aviso Prévio” estiverem marcados. Valor default: 30)*

**Parâmetros de Transferência**

*Lookup – Tipo de Transferência (com Ônus ou sem Ônus)*

*Lookup – Motivo da**Transferência*

******Parâmetros de Promoção******

*Lookup – Motivo da Promoção*

********Perfil de Admissão********

Neste módulo são cadastrados os perfis de funcionário.  
Estas informações são utilizadas como default para admissão de novos funcionários.   
Ao cadastrar um novo perfil, é possível selecionar um funcionário já existente na base para fazer a cópia das informações. **Obs: O lookup para seleção do funcionário base deve respeitar o filtro de perfil.**É possível cadastrar apenas um perfil para uma mesma seção, função e tipo de recebimento que serão a chave primária da tabela.

**Anexo I – Eventos Fixos**

Eventos que são lançados para o funcionário em toda a competência da folha. O usuário deverá selecionar o evento e determinar o seu valor, seja de origem monetária, horas ou referência.

O processo para a carga inicial de perfis faz uma leitura dos funcionários atuais na base de acordo com a seleção definida, agrupando por seção, função e tipo de recebimento, e cria um perfil para cada grupo.  
O salário é calculado de acordo com o parâmetro selecionado: menor valor, valor médio, maior valor ou piso salarial (piso salarial somente ficará disponível se utilizar tabela salarial).

A descrição dos perfis é composta por descrição da seção + descrição da função + forma de recebimento.  
Caso durante a geração o sistema encontre na base perfis com mesma chave e o parâmetro “Atualizar perfis já existentes com a mesma chave” estiver marcado o sistema irá fazer a atualização dos mesmos, caso contrário os mesmos serão ignorados.

Este processo está disponível nos Processos da visão de Perfil de Amissão:

****Lotação de Pessoal****

Neste passo o usuário configura os filtros que elegem os funcionários participantes do processo.  
A base para este filtro é a tela de seleção de funcionários padrão da folha de pagamento e a quebra de seção.  
O usuário pode montar várias configurações para o orçamento.  
Tem a visão para visualizar os funcionários selecionados.  
O cadastro da lotação é visível em todas as coligadas. Dessa forma poderemos, mesmo com orçamentos por coligada, ter a transferência de um funcionário de uma coligada que irá alterar a lotação da coligada destino.

  

|  |  |
| --- | --- |
| Lotação | Código da Lotação definido pelo usuário. |
| Descrição | Descrição da Lotação. |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a lotação. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a lotação. |

******Informações Iniciais******

**Dados do Orçamento**

Neste passo o usuário irá cadastrar as informações básicas do orçamento como o código, a descrição, as datas de início e fim do orçamento, a competência base, lookup para seleção da lotação e um campo para observações e informações adicionais.  
O cadastro de orçamento deve ser separado por coligada.

|  |  |
| --- | --- |
| Código | Código do Orçamento definido pelo usuário. |
| Data Início | Competência inicial do orçamento. |
| Data Fim | Competência final do orçamento. |
| Lotação de pessoal | Selecionar a lotação para o orçamento. |
| Competência base | Competência para a carga inicial das informações e serve como base para seleção dos eventos referente movimento anterior. |
| Informações adicionais | Informações adicionais sobre o orçamento. |

**Manutenção da Lotação**

**Admissão**

Neste passo o usuário irá informar os dados para admissão de novos funcionários.  
Como facilitador, o sistema  preenche a tela automaticamente com os parâmetros default de admissão e dados do perfil selecionado. Estes dados poderão ser modificados pelo usuário.

Obs.: o gestor pode utilizar o Quadro de Vagas para inserir informações de admissão.

|  |  |
| --- | --- |
| Data de Admissão | A data de admissão deve ser preenchida com data igual ou superior ao período inicial do orçamento e igual ou inferior ao período final do orçamento. |
| Código Perfil | Código do Perfil de Admissão. Após selecionar o perfil, deve preencher os campos função, seção, tipo de recebimento e salário. |
| Função | Função da vaga preenchida pelo perfil. |
| Seção | Seção em que a vaga será alocada  - Lookup exibe apenas as seções que compõe a lotação. |
| Tipo de Recebimento | Tipo de recebimento da vaga.  - Lookup exibe apenas os tipos de recebimento que compõe a lotação. |
| Tipo de Funcionário | Tipo de funcionário da vaga. Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.1).  - Lookup exibe apenas os tipos de funcionário que compõe a lotação. |
| Motivo da Admissão | Informar motivo da admissão. Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.1). |
| Sindicato | Informar o sindicato. Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.1). |
| Horário | Informar o horário do funcionário. Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.1). |
| Letra | Informar o índice inicial do horário. Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.1). |
| Salário | Informar o salário do funcionário |
| Jornada | Informar a jornada do funcionário. Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.1). |
| Salário hora | Será calculado pelo sistema de acordo com o salário e jornada informados. |
| Quantidade | Quantidade de funcionários a serem admitidos com os mesmos parâmetros. |

******Promoção******

Neste passo o usuário informa as promoções dos funcionários.  
Para cadastrar uma promoção é necessário informar a nova função e o novo salário do funcionário. Nos casos onde apenas o salário será alterado deve-se utilizar o processo de Reajuste Salarial.  
A alteração terá efeito na competência da alteração e posteriores.

Obs.: o gestor pode utilizar o Quadro de Vagas para inserir informações de promoção.

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Data da Promoção | A data da promoção deve ser preenchida com data igual ou superior ao período inicial do orçamento e igual ou inferior ao período final do orçamento. |
| Motivo da Promoção | Informar motivo da promoção. Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.4). |
| Nova Função | Informar a nova função do funcionário. |
| Novo Tipo de Recebimento | Informar o novo tipo de recebimento do funcionário. |
| Tipo Alteração Salário | Selecionar o tipo da alteração de salário:  - Fórmula: alteração através de uma fórmula;  - Percentual: alteração através de um percentual aplicado em cima do salário atual do funcionário;  - Piso Salarial: Somente poderá ser utilizado se o sistema estiver parametrizado para utilizar tabela salarial. Marcando esta opção, o sistema deve verificar o valor do salário da função selecionada e preencher o campo “Salário”.  - Valor Informado: usuário informa o valor do salário.    **Obs: A opção “Piso Salarial” não será implementada na primeira versão do módulo de orçamento.** |
| Fórmula | Campo somente deve ficar ativo caso seja selecionada a opção “Fórmula” no campo “Tipo Alteração Salário”.  Usuário deve selecionar a fórmula para alteração do salário do funcionário. |
| Permite redução de salário | Campo somente deve ficar ativo caso seja selecionada a opção “Fórmula” no campo “Tipo Alteração Salário”.  Com esse parâmetro marcado, se a fórmula de alteração salarial resultar, para um ou mais funcionários, em um valor menor que o salário nominal dos mesmos, o sistema irá proceder com a alteração salarial. Esse parâmetro foi criado para empresas que, por meio legal, possam reduzir o salário dos funcionários. |
| Percentual | Campo somente deve ficar ativo caso seja selecionada a opção “Percentual” no campo “Tipo Alteração Salário”.  Usuário deve informar o percentual para o ajuste salarial. |
| Salário | Campo somente deve ficar ativo caso seja selecionada a opção “Valor Informado” no campo “Tipo Alteração Salário”.  Usuário deve informar o valor do salário. |
| Quantidade | Informando um valor maior que 0 (zero) neste campo, o sistema irá ignorar a seleção de funcionários e o usuário deverá clicar na botão “Sugerir” para fazer a inclusão da promoção. |
| Sugerir | Ao clicar no botão, o sistema irá selecionar aleatoriamente a quantidade informada de funcionários da seção informada no campo código de quebra, e irá abrir uma tela informando os funcionários selecionados onde o usuário poderá alterar a seleção ou confirmar. Após a confirmação o sistema irá incluir no grid uma linha de promoção para cada funcionário selecionado.    Obs: Se a quantidade informada for maior que o total de funcionários, o sistema deve exibir a mensagem “A quantidade de funcionários solicitada é maior que a quantidade disponível: x”. |

**Transferência**

Neste passo o usuário informa as transferências de funcionários para outra filial ou coligada.

A transferência de coligada representa o desligamento do colaborador na coligada de origem e a geração de um novo cadastro na coligada de destino, com a interferência na vaga do quadro da coligada de origem e também na vaga do quadro da coligada de destino. Somente é possível fazer transferência para as coligadas e seções que fazem parte da mesma lotação do orçamento.

Todos os campos devem ser preenchidos da forma mais apropriada à transferência. Contudo, o Tipo de Demissão deverá necessariamente conter um dos seguintes valores.

“5” - Transferência sem ônus para cedente: Significa que o cedente do funcionário, ou seja, a empresa, filial ou seção de onde o funcionário está sendo transferido, não arcará com o pagamento das verbas rescisórias. Neste caso não haverá cálculo da rescisão, a nova empresa assumirá todas as obrigações trabalhistas do contrato de origem, portanto deve cadastrar um novo colaborador para a outra empresa, onde a data de admissão será a data do cadastro de origem. Neste caso o quadro de vagas será atualizado (redução do quadro) na própria competência da transferência, visto que o colaborador não será orçado nesta competência. Serão transferidas as programações de férias (individual e coletiva) para o novo contrato, visto que esta empresa assumiu todas as obrigações trabalhistas, porém, serão levadas somente as programações com data de início maior ou igual à data da transferência. Sendo que, sempre gravará como programação de férias coletivas, mesmo que seja programação individual. Isto deve-se ao fato da inexistência do período aquisitivo para o novo colaborador na nova empresa.

“6” - Transferência com ônus para cedente: Inversamente ao caso anterior, neste tipo de transferência o cedente do funcionário arcará com o pagamento das verbas rescisórias. O sistema fará o cálculo da rescisão. Neste caso, o quadro de vagas de origem será atualizado (redução do quadro) somente no mês seguinte à transferência, visto que o colaborador deve ser orçado nesta competência. Não deve levar a programação de férias para o novo contrato, visto que o direito de férias foi quitado.  

Caso o tipo de demissão tenha sido "5" (Transferência sem ônus para o cedente) o tipo de admissão deverá ser necessariamente "T" (Entrada por transferência sem ônus para o cedente). Caso o tipo de demissão tenha sido "6" (Transferência com ônus para o cedente) o tipo de admissão correspondente será o "E" (Entrada por transferência com ônus para o cedente). Estas combinações: 5-T e 6-E, são importantes para o perfeito funcionamento do sistema.

Ao excluir uma transferência de empresa, a atualização do quadro de vagas será feita conforme o valor definido no campo "Sem Ônus" (Grid de Saídas): se for uma transferência sem ônus, as vagas liberadas serão adicionadas na mesma competência. Se for com ônus, as vagas serão adicionadas na competência seguinte.

Obs.: o gestor pode utilizar o Quadro de Vagas para inserir informações de transferência.

|  |  |  |
| --- | --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |  |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |  |
| Data da Alteração | A data da alteração deve ser preenchida com data igual ou superior ao período inicial do orçamento e igual ou inferior ao período final do orçamento. |  |
| Motivo da Alteração | Informar o motivo da alteração.  Este campo deve ser carregado com o valor default dos parâmetros (vide item 1.1.3). |  |
| Nova Seção | Informar a seção para qual o funcionário será transferido.   - Lookup exibe apenas as seções que compõe a lotação. | |
| Alteração através de fórmula | Marque este campo para fazer a alteração através de fórmula.  Marcando este campo deve limpar e desabilitar o campo “Nova Seção”. |  |
| Fórmula | Informar a fórmula para alteração de seção. |  |
| Quantidade | Informando um valor maior que 0 (zero) neste campo, o sistema irá ignorar a seleção de funcionários e o usuário deverá clicar na botão “Sugerir” para fazer a inclusão da alteração. |  |
| Sugerir | Ao clicar no botão, o sistema irá selecionar aleatoriamente a quantidade informada de funcionários da seção informada no campo código de quebra, e irá abrir uma tela informando os funcionários selecionados onde o usuário poderá alterar a seleção ou confirmar. Após a confirmação o sistema irá incluir no grid uma linha de alteração para cada funcionário selecionado.    Obs: Se a quantidade informada for maior que o total de funcionários, o sistema deve exibir a mensagem “A quantidade de funcionários solicitada é maior que a quantidade disponível: x”. |  |

******Quadro de Vagas******

Neste passo será exibida uma tabela com o número de funcionários em cada função por competência para a seção e ano base selecionados.

Para fazer o cálculo, o sistema deve carregar as informações da lotação considerando as alterações feitas nos steps de Admissão, Promoção, Transferência, Demissão e Alteração de Seção.  
A tabela de manutenção do quadro de vagas **não permitirá alterar** a quantidade de vagas manualmente, pois serão gerenciadas pelas telas de Transferência Coletiva, Admissão Coletiva, Promoção Coletiva e Demissão Coletiva, porém permitirá incluir novas funções para a seção.

**Exemplo:** Ao fazer a leitura da lotação no ano base 2012, na competência 09/2012 e seção “Departamento de Vendas” existiam alocados 3 funcionários com a função Assistente Comercial. No mês 10/2012 foi demitido 1 funcionário e no mês de dezembro foram admitidos mais 2. Neste caso o quadro de vagas ficaria assim:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Função | Descrição | Jan | Fev | Mar | Abr | Mai | Jun | Jun | Jul | Ago | Set | Out | Nov | Dez |
| 0001 | Assist. Comercial | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 2 | 4 |

Esta tela pode ser acessada por fora do Wizard de orçamento, onde os gerentes de cada seção poderão fazer admissões, promoções, transferências, demissões e alteração de seção. 

|  |  |  |
| --- | --- | --- |
| Orçamento | Campo deve ser preenchido com os dados do orçamento atual e não permitir a edição. Ao acessar o Quando de vagas por fora do wizard de orçamento, este campo de ficar habilitado para o usuário selecionar o orçamento. |  |
| Ano Base | Deve ficar disponível para seleção somente os anos que compõe o período do orçamento. |  |
| Seção | Usuário deve selecionar a seção para a montagem do quadro de vagas.  - Lookup exibe apenas as seções que compõe a lotação. |  |
| Admissão | Chama a tela de **“Admissão”**, preenchendo os campos “Data da Admissão” (primeiro dia da competência), “Função”, “Seção” e “Tipo de Recebimento” de acordo com a célula selecionada no grid ao pressionar o botão.  Sistema deve verificar se existe perfil cadastrado para a função, seção e tipo de recebimento preenchendo o campo “Cod. Perfil” e “Salário”. Caso não encontre um perfil deve exibir a mensagem para o usuário “Não foi encontrado perfil cadastrado para a Função, seção e Tipo de Recebimento. O valor do salário deverá ser informado manualmente.”  Os campos “Motivo da Admissão”, “Tipo de Funcionário”, “Sindicato”, “Horário”, “Letra” e “Jornada” devem ser preenchidos com os valores default de admissão, devendo o usuário determinar o número de funcionários que serão admitidos. Processo deve aumentar o número de vagas também para as competências subseqüentes, gerando admissão de funcionários temporários. |  |
| Demissão | Chama a tela de **“Demissão”**, preenchendo os campos “Data da Demissão” e “Data de Pagamento” (primeiro dia da competência), “Função”, “Seção” e “Tipo de Recebimento” (seleção de funcionários) de acordo com a célula selecionada no grid ao pressionar o botão.  Os campos “Tipo de Demissão”, “Motivo da Demissão” e Aviso Prévio devem ser preenchidos com os valores default de demissão, devendo o usuário determinar o número de funcionários que serão demitidos.    Obs: se o valor da célula selecionada for 0 (zero), o sistema deve apresentar a mensagem “Não há funcionários para realizar o processo.”. | |
| Transferência | Chama a tela de **“Transferência”**, preenchendo os campos “Data da Transferência” (primeiro dia da competência), “Função”, “Seção” e “Tipo de Recebimento” (seleção de funcionários) de acordo com a célula selecionada no grid ao pressionar o botão.  Os campos “Tipo da Transferência” e “Motivo da Transferência” devem ser preenchidos com os valores default de transferência, e os campos “Sindicato”, “Horário”, “Letra” e “Jornada” com os valores default de admissão.  Após selecionar a nova seção e a nova função, o sistema deve verificar se existe perfil cadastrado para a função, seção e tipo de recebimento preenchendo o campo “Salário”.  Caso não encontre um perfil deve exibir a mensagem para o usuário “Não foi encontrado perfil cadastrado para a Função, seção e Tipo de Recebimento. O valor do salário deverá ser informado manualmente.”.    Obs: se o valor da célula selecionada for 0 (zero), o sistema deve apresentar a mensagem “Não há funcionários para realizar o processo.”. |  |
| Promoção | Chama a tela de **“Promoção”**, preenchendo os campos “Data da Promoção” (primeiro dia da competência), “Função”, “Seção” e “Tipo de Recebimento” (seleção de funcionários) de acordo com a célula selecionada no grid ao pressionar o botão.  O campo “Motivo da Promoção” deve ser preenchido com o valor default de promoção.  Após selecionar a nova função e o novo tipo de recebimento, o sistema deve verificar se existe perfil cadastrado para a função, seção e tipo de recebimento selecionando no campo “Tipo de Alteração Salarial” a opção “Piso Salarial” e preenchendo o campo “Salário” com o valor do perfil.  Caso não encontre um perfil deve exibir a mensagem para o usuário “Não foi encontrado perfil cadastrado para a Função, seção e Tipo de Recebimento. O valor do salário deverá ser informado manualmente.” E selecionar no campo “Tipo de Alteração Salarial” a opção “Valor Informado”.    Obs: se o valor da célula selecionada for 0 (zero), o sistema deve apresentar a mensagem “Não há funcionários para realizar o processo.”. |  |
| Alteração de Seção | Chama a tela de **“Alteração de Seção”**, preenchendo os campos “Data da Alteração” (primeiro dia da competência), “Função”, “Seção” e “Tipo de Recebimento” (seleção de funcionários) de acordo com a célula selecionada no grid ao pressionar o botão.  O campo “Motivo da Alteração” deve ser preenchido com o valor default de transferência.    Obs: se o valor da célula selecionada for 0 (zero), o sistema deve apresentar a mensagem “Não há funcionários para realizar o processo.”. |  |
| Nova Função | Permite incluir uma nova função para a seção selecionada. Todos os dados virão zerados. |  |
| Atualizar | Recalcula o número de funcionários e atualiza o grid. |  |
| Total Geral de Vagas da Seção | Apresenta o total geral das vagas para a seção. |  |

******Reajustes******

******Reajuste Salarial******

Neste passo o usuário informa as alterações de salário dos funcionários que não utilizam salário composto.  
O reajuste pode ser feita por piso salarial, por percentual, por fórmula ou valor informado.

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Data da Mudança | A data da mudança deve ser preenchida com data igual ou superior ao período inicial do orçamento e igual ou inferior ao período final do orçamento. |
| Motivo | Informar motivo da mudança. |
| Tipo Alteração Salário | Selecionar o tipo da alteração de salário:  - Fórmula: alteração através de uma fórmula;  - Percentual: alteração através de um percentual aplicado em cima do salário atual do funcionário;  - Piso Salarial: Somente poderá ser utilizado se o sistema estiver parametrizado para utilizar tabela salarial. Marcando esta opção, o sistema deve verificar o valor do salário da função selecionada e preencher o campo “Salário”.  - Valor Informado: usuário informa o valor do salário.  ***Obs: A opção “Piso Salarial” não será implementada na primeira versão do módulo de orçamento.*** |
| Fórmula | Campo somente deve ficar ativo caso seja selecionada a opção “Fórmula” no campo “Tipo Alteração Salário”.  Usuário deve selecionar a fórmula para alteração do salário do funcionário. |
| Permite redução de salário | Campo somente deve ficar ativo caso seja selecionada a opção “Fórmula” no campo “Tipo Alteração Salário”.  Com esse parâmetro marcado, se a fórmula de alteração salarial resultar, para um ou mais funcionários, em um valor menor que o salário nominal dos mesmos, o sistema irá proceder com a alteração salarial. Esse parâmetro foi criado para empresas que, por meio legal, possam reduzir o salário dos funcionários. |
| Percentual | Campo somente deve ficar ativo caso seja selecionada a opção “Percentual” no campo “Tipo Alteração Salário”.  Usuário deve informar o percentual para o ajuste salarial. |
| Salário | Campo somente deve ficar ativo caso seja selecionada a opção “Valor Informado” no campo “Tipo Alteração Salário”.  Usuário deve informar o valor do salário. |
| Fórmula para alteração da jornada | Selecione a fórmula que será utilizada para realização da alteração da jornada.  O parâmetro Alterar jornada mantendo salário hora para horistas será habilitado se for informada fórmula exclusivamente no campo Fórmula de Alteração de Jornada.  Obs: A fórmula para alteração da jornada deverá ser expressa em minutos. |
| Alterar jornada mantendo salário hora para horistas | Marque este parâmetro para alterar a jornada do funcionário mantendo o salário hora.  **Exemplo:**  Salário Mensal: R$ 2.200,00  Jornada (horas): 220  Salário Hora: R$ 10,00  Para este exemplo utilizou no campo Fórmula de Alteração de Jornada, a fórmula que retorna 6600 minutos (6600 minutos é igual a 110 horas).  Após o processamento da alteração de jornada, para os funcionários que possuem a Forma de Recebimento "H - Horista" o resultado será o seguinte:  **- Com parâmetro marcado:**  Salário Mensal: R$1.100,00  Jornada (horas): 110  Salário Hora: R$ 10,00  O salário hora foi mantido, alterada a jornada (de 220 para 110) e salário mensal calculado em relação ao salário hora e a nova jornada (R$10,00 x 110 = 1.100,00).  **- Com parâmetro desmarcado:**  Salário Mensal: R$2.200,00  Jornada (horas): 110  Salário Hora: R$ 20,00  A jornada foi reduzida (de 220 para 110), o salário mensal se manteve (R$2.200,00) e o salário hora em relação ao salário mensal e a nova jornada foi alterado (R$20,00 = R$2.200,00 / 110). |

******Folha de Pagamento******

******Grupo de eventos******

Neste passo o usuário configura os grupos de eventos que são lançados na movimentação dos funcionários e perfis.

|  |  |
| --- | --- |
| Grupo de eventos | Selecionar o Grupo de Eventos que será lançado. |
| Competência | Informar em quais competências que o grupo de eventos será lançado.  A competência inicial ser preenchida com data igual ou superior ao período inicial do orçamento e a competência final igual ou inferior ao período final do orçamento. |
| Período | Informar o período que o grupo de eventos deve ser lançado. |
| Dia | Informar o dia do pagamento |
| Mês | Selecionar uma das opções:  - Mês corrente: se o pagamento for no mesmo mês de competência.  - Próximo mês: se o pagamento for no mês posterior ao da competência. |

 

******Eventos Adicionais******

Neste passo o usuário pode definir eventos que serão lançados na movimentação além dos grupos de eventos.

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Código Evento | Selecionar o evento que será lançado. |
| Hora | Informar o valor hora.  Campo somente deve ficar habilitado se o evento selecionado for do tipo Hora. |
| Referência | Informar o valor referência. Quando o evento for do tipo Dia, este campo deverá ficar habilitado, enquanto os campos Hora e Valor deverão ficar inabilitados. |
| Valor | Informar o valor. |
| Competência | Informar em quais competências que o evento será lançado.  A competência inicial ser preenchida com data igual ou superior ao período inicial do orçamento e a competência final igual ou inferior ao período final do orçamento. |
| Período | Informar o período que evento deve ser lançado. |
| Dia | Informar o dia do pagamento |
| Mês | Selecionar uma das opções:  - Mês corrente: se o pagamento for no mesmo mês de competência.  - Próximo mês: se o pagamento for no mês posterior ao da competência. |

********Eventos movimento anterior********

Neste passo é possível fazer o lançamento e a manutenção de eventos baseados no movimento anterior.

**Lançamento de eventos do movimento anterior**

Primeiro deve-se executar o processo de lançamento de eventos do movimento anterior, onde o sistema irá preencher a grid de valores realizados (competências anteriores calculadas pela folha).  
Este processo deve buscar os eventos selecionados (hora extra, adicional noturno, etc) na ficha financeira e totalizar o valor de cada evento (evento do tipo Hora totalizar o valor hora, evento do tipo Referência totalizar o valor referência), separando por funcionário e competência.  
Na grid de valores realizados os valores devem ser agrupados por função.  
O período de busca será realizado considerando a competência base do orçamento da seguinte forma: no período de 01/2008 a 12/2008, com competência base do orçamento em 10/2007, a busca inicia em ordem decrescente a partir do mês da competência base, ou seja, a primeira busca é feita no período de 10/2007 (equivalente ao período de 10/2008), a segunda em 09/2007, assim sucessivamente, até chegar ao início do período indicado (01/2008, ou seja, busca em 01/2007). Para os meses que estão após a competência base (11/2008 e 12/2008), a busca será feita em 11/2006 e 12/2006 respectivamente.

|  |  |
| --- | --- |
| Seção | Selecionar a seção para a qual se deseja fazer o lançamento.  - Lookup exibe apenas as seções que compõe a lotação.    Caso não seja informado serão considerados todas as Seções da lotação. |
| Função | Selecionar a função para a qual se deseja fazer o lançamento.  Caso não seja informado função, serão considerados todas. |
| Competência | Informar o período para o qual devem ser gerados lançamentos.  O competência inicial e final devem estar dentro do período permitido conforme regra acima. |
| Gerar Eventos Previstos | Definir se deseja copiar automaticamente os eventos para a grid de eventos Previstos, ou seja, se marcado o sistema irá lançar os eventos gerados também para a grid de eventos previstos. |
| Eventos para geração | Informar os eventos a serem gerados. |

**********Manutenção dos eventos**********

Após a execução deste processo, é possível fazer o lançamento do realizado (competências anteriores calculadas pela folha) para o previsto (competências compreendidas pelo orçamento).  
A grid de Previsto permite cadastrar ou dar manutenção nos itens gerados.  
Alterando o valor de um evento, a diferença deve ser rateada para os funcionários na mesma proporção dos valores previstos.

**Obs: Não será possível selecionar um funcionário específico para alteração. A alteração afetará todos os funcionários que compõe o valor previsto.**

**Exemplo:**

**Valor realizado:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evento | Descrição | Jan | Fev | Mar | Abr | Mai | Jun | Jun | Jul | Ago | Set | Out | Nov | Dez |
| 0082 | Hora Extra 50% | **320:00** | 0 | 0 | 400:00 | 0 | 0 | 0 | 0 | 0 | 350:00 | 200:00 | 0 | 323:00 |

**Valor previsto:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evento | Descrição | Jan | Fev | Mar | Abr | Mai | Jun | Jun | Jul | Ago | Set | Out | Nov | Dez |
| 0082 | Hora Extra 50% | **500:00** | 0 | 0 | 400:00 | 0 | 0 | 0 | 0 | 0 | 350:00 | 200:00 | 0 | 323:00 |

 

Realizado Janeiro: 320:00  
Composição:  
Funcionário 00030: 100:00 – 31,25%  
Funcionário 00045:   20:00 – 6,25%  
Funcionário 00052: 200:00 – 62,5%  
Previsto Janeiro: 500:00 (diferença = +180:00)

Composição:  
Funcionário 00030: 100:00 + 31,25% de 180:00 =  156:15  
Funcionário 00045:   20:00 +   6,25% de 180:00 =    31:15  
Funcionário 00052: 200:00 + 62,50% de 180:00 =  312:30

|  |  |
| --- | --- |
| Seção | Selecionar a seção para a qual se deseja fazer o lançamento.  - Lookup exibe apenas as seções que compõe a lotação. |
| Função | Selecionar a função para a qual se deseja fazer o lançamento. |
| Lançar eventos movimento anterior | Executa o processo de lançamento de eventos do movimento anterior. |
| Realizado | São apresentados os eventos da folha que foram gerados através do processo “Lançar eventos movimento anterior”. São apresentadas uma coluna para cada mês, de acordo com os meses utilizados para busca de informações (conforme a competência base). Essa grid é apenas para consulta, ou seja, não é possível efetuar alterações nos itens. |
| Copiar Realizado / Previsto | Faz a cópia do evento selecionado no grid Realizado para o grid Previsto. |
| Previsto | São apresentados os eventos da folha previstos. As colunas são mostradas conforme o período do orçamento (mostrado acima da grid de realizados). Esta grid permite inserção/alteração de itens/valores. |

**Férias**

**********Cálculo de Férias**********

Neste passo o usuário cadastra a programação de férias para os funcionários.  
O sistema considera as férias já marcadas para os funcionários no período do orçamento, e não irá permitir que seja calculado as férias, em caso de intercessão entre datas.  
Caso algum funcionário já tenha férias marcadas no intervalo informado, na visualização do log de cálculo o sistema irá avisar que "O período de ferias de na "data informada" não poderá ser considerado, porque o funcionário  já possui o período de naquela data cadastrado com dias em interseção".

ex:

Durante o cálculo do orçamento o sistema irá simular a abertura e o fechamento dos períodos aquisitivos dos funcionários. Desta forma, quando o usuário informar um número de dias de férias superior ao de direito do funcionário, o sistema irá automaticamente abrir o próximo período aquisitivo.

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Data inicial | Informe a data inicial de gozo das ferias. |
| Data final | Informe a data final das Férias |
| Dias de férias | Neste campo, o sistema preencherá o número de dias de férias. Pode também informar a data inicial e o número de dias das férias para que o Sistema preencha a data de final de gozo automaticamente. |
| Substituir Férias em meses posteriores | Se você marcar este campo o sistema lança a data informada para as Férias Coletivas até mesmo para os funcionários com a data de férias já cadastradas em meses posteriores, ou seja, para funcionários com datas de férias cadastradas nos meses anteriores que ainda não foram liberadas, e no mês atual não serão substituídas. No caso em que não for marcado, o Sistema lança a data informada somente para os funcionários que não têm data de férias cadastradas. |
| Férias Coletivas | O default deste parâmetro é estar marcado, desta forma o sistema realizará o cadastramento das Férias Coletivas para os funcionários.  Desmarcando este parâmetro o sistema efetuará o cadastro das férias normais de forma global para os funcionários. |
| Pagar 1º parcela de 13º Salário | Se este parâmetro for marcado o sistema calcula a primeira parcela do 13 º Salário junto com as férias. |
| Verifica faltas funcionário >1 ano | Quando o parâmetro estiver marcado e o funcionário possuir faltas, será verificado o parâmetro sindical "Ignora faltas em férias" para considerar ou não as faltas. Caso contrário, as faltas não serão consideradas.     Exemplo:  O funcionário tem 30 dias de direito de férias, porém teve 10 dias de faltas neste período aquisitivo e no sindicato esta parametrizado para considerar as faltas.  Ao cadastrar as ferias coletivas ou globais com o parâmetro marcado o sistema irá lançar 24 dias de férias, caso contrário, as faltas serão ignoradas e serão lançados 30 dias de férias.    Observação:  - O objetivo deste parâmetro nas Férias Coletivas, é para atender os clientes que consideram as faltas no gozo das férias normais e não consideram as faltas no gozo das férias coletivas.  - O objetivo deste parâmetro nas Férias Globais, é devida a impossibilidade de interromper o processo para alertar o usuário que o funcionário tem menos dias de direito de férias do que o cadastrado devido às faltas, como ocorre atualmente no cadastro individual de férias. |

**Diferença de Férias**

O usuário pode efetuar o cálculo da diferença de valores referente às férias, ocasionado por algum aumento salarial. Esta diferença será calculada verificando a data do aumento salarial (existente no histórico) e todos os períodos de gozo constantes no histórico de férias, posteriores à esta data.  
Os funcionários afetados são aqueles com férias partidas que tiveram aumento salarial no mês subseqüente ao do pagamento das férias.

Como é feito o cálculo:

1 - Recalcula as férias novamente, desconsiderando o cálculo já efetuado;

2 - Fará a comparação do valor encontrado com o valor já lançado;

3 - Se o valor encontrado for maior que o valor já calculado, o Sistema lançará a diferença;

4 –Os valores serão dispostos em eventos específicos da diferença e lançados automaticamente para o envelope.

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Competência | Informar em qual competência que o cálculo da diferença será realizado.   A competência inicial ser preenchida com data igual ou superior ao período inicial do orçamento e a competência final igual ou inferior ao período final do orçamento. |
| Período | Informe o período para lançamento da diferença. |
| Período de Início de Gozo | Informe um intervalo de datas para que o Sistema calcule a diferença de férias somente dos funcionários com início de férias nesse período. |
| 13º Pago nas Férias | Informe o evento de Diferença de 13º Salário com Código de Cálculo 09- 1º Parcela de 13º Salário para calcular o valor da Diferença da 1ª Parcela de 13º Salário pago nas férias. |
| Calcula diferença para funcionários demitidos | Marque esta opção para que o sistema calcule diferença de férias para funcionários demitidos. |
| Dados do dissídio/Convenção/acordo coletivo | Em caso de diferença por dissídio, selecionar dos dados do acordo coletivo. |

**13º Salário**

Neste passo o usuário informa as parametrizações para o cálculo do 13º salário

 

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Primeira Parcela | Marque esta opção para o pagamento da primeira parcela. O sistema executará o código de cálculo 009 (1ª Parcela do 13º Salário). |
| Ajusta 1º Parcela | Este campo ficará marcado como padrão, caso a primeira parcela esteja sendo lançada. Este parâmetro funciona da seguinte forma:    Suponhamos que a folha de pagamento esteja sendo processada em 11/1999 e que determinado funcionário tenha um aumento de seu salário R$ 1000,00 para R$1500,00 neste período.    Se este funcionário já tiver tido a primeira parcela do 13º salário lançada em 06/1999, que no caso foi de R$ 500,00 (o parâmetro "Utiliza Salário Atual para 1ª Parcela" está marcado), quando a primeira parcela for lançada novamente, ou seja, para que o ajuste referente ao aumento salarial seja efetuado, o parâmetro "Ajustar 1ª Parcela" deve estar marcado. Sendo assim, os seguintes eventos referentes a 13º serão lançados:    - 1ª Parcela de 13º Salário (Código de Cálculo 9) R$ 750,00 (Provento)  - Adiantamento de 13º Salário (Código de Cálculo 35) R$ 500,00 (Desconto)  Onde a diferença referente ao aumento salarial corresponde a R$ 250,00    Se este parâmetro não estiver marcado, o sistema irá verificar que o evento de 1ª Parcela de 13º Salário já foi lançado (Código de Cálculo 009) e não irá lançar o ajuste.    Obs: Campo deve ficar habilitado somente se “Primeira Parcela” estiver marcado. |
| Mês lanc. 1ª Parcela | Informar o mês para o lançamento da primeira parcela. Valor inicial do campo deve ser 11.  Obs: Campo deve ficar habilitado somente se “Primeira Parcela” estiver marcado. |
| Período 1ª Parcela | Informar o período para o lançamento da primeira parcela.  Obs: Campo deve ficar habilitado somente se “Primeira Parcela” estiver marcado. |
| Segunda Parcela | Marque esta opção se pretender lançar o pagamento da segunda parcela do 13º salário. |
| Mês lançamento 2ª Parcela | Informar o mês para o lançamento da Segunda Parcela. Valor inicial do campo deve ser 12.  Obs: Campo deve ficar habilitado somente se “Segunda Parcela” estiver marcado. |
| Período 2ª Parcela | Informar o período para o lançamento da segunda parcela.  Obs: Campo deve ficar habilitado somente se “Segunda Parcela” estiver marcado. |
| Lança Códigos Fixos | Marque este campo para que os códigos fixos relacionados ao 13º salário sejam lançados no movimento de 2ª parcela de 13º salário. |
| Lança Eventos Programados | Marque este campo para que os eventos programados relacionados ao 13º salário sejam lançados no movimento de 2ª parcela de 13º salário. |

**Provisões**

Neste passo o usuário configura a geração das provisões mensais (férias e 13º salário) .  
O histórico de provisões é gerado e armazenado mensalmente. Desta forma é possível obter o valor acumulado e o valor mensal.

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Competência | Informar em quais competências que o Histórico de Provisões será gerado.  A competência inicial ser preenchida com data igual ou superior ao período inicial do orçamento e a competência final igual ou inferior ao período final do orçamento. |
| 13º Salário | Selecione esta opção caso deseje gerar o histórico de provisão de 13º Salário.  No processo do cálculo da provisão de 13º Salário o sistema irá considerar:  - Avos de direito até o último dia da competência atual ou até a data de demissão (incluindo aviso prévio indenizado);  - Médias;  - Faltas e afastamentos ocorridos no ano atual;  - Parâmetros de 13º Salário existentes no Parametrizador.  - Parâmetros de 13º Salário existentes no cadastro do sindicato do funcionário;  - Eventos que incidem salário.  Atenção:  Caso o evento com código de cálculo 102-2a PARCELA 13o SALARIO tenha fórmula valor, o cálculo da provisão de 13º Salário será baseado nesta fórmula. |
| Férias | Selecione esta opção caso deseje gerar o histórico de provisão de Férias.  No processo do cálculo da provisão de Férias o sistema irá considerar:  - Avos de direito até o último dia da competência atual ou até a data de demissão (incluindo aviso prévio indenizado) para férias as férias vencidas e proporcionais e cadastro de férias;  - Médias;  - Faltas e afastamentos ocorridos no ano atual;  - Parâmetros de Férias existentes no Parametrizador.  - Parâmetros de Férias existentes no cadastro do sindicato do funcionário;  - Eventos que incidem salário.    Observações:  - Caso o evento com código de cálculo 38-Férias tenha fórmula valor, o cálculo da provisão de Férias será baseado nesta fórmula.  - Se o funcionário for demitido no mês com o tipo de rescisão =1 (iniciativa do empregador por justa causa) será provisionado apenas as férias Vencidas deste funcionário. |
| Gerar provisão com valor zero para demitidos no mês | Marcando este parâmetro no mês da demissão do funcionário o sistema irá gerar a provisão zerada. |
| Permite valores negativos | Com este parâmetro desmarcado o sistema irá calcular zero para o funcionário que antecipar o gozo das férias, ou seja, tiver avos negativos. Caso contrário será calculado o valor negativo. Exemplo:    O funcionário tem o período aquisitivo em aberto de: 04/2006 a 04/2007 e gozou 20 dias de férias no mês 10/2006.    **Com o parâmetro desmarcado o sistema fazer o seguinte cálculo:**  Funcionário: NOME DO FUNCIONÁRIO  Salário: 440,00 Dt.Admissão: 26/04/2004 Dt.Venc.Férias: 25/04/2007  Proporção por faltas : 0,00 / 30 \* 30 = 0,00 Número de faltas: 5  Adicional sobre férias : (0,00 + 0,00) \* 0,33 = 0,00  Total das Férias : 0,00 + 0,00 + 0,00 = 0,00    **Com o parâmetro marcado o sistema fazer o seguinte cálculo:**  Funcionário: NOME DO FUNCIONÁRIO  Salário: 440,00 Dt.Admissão: 26/04/2004 Dt.Venc.Férias: 25/04/2007  Proporção por faltas : 0,00 / 30 \* 30 = 0,00 Número de faltas: 5  Férias Proporcionais : ((440,00 + 0,00 + 222,61) / 12 \* -2,0) + 0,00 = -110,44  Dias de direito : -5,0  Adicional sobre férias : (0,00 + -110,44) \* 0,33 = -36,81  Total das Férias : 0,00 + -110,44 + -36,81 = -147,25 |
| Abate o valor das férias do mês | Com este parâmetro marcado no momento do cálculo da provisão de férias o sistema irá abater o valor das férias gozadas no mês atual. Exemplo:  O funcionário possui férias vencidas mais 3/12 avos de férias proporcionais e está em gozo de férias no mês de competência.  Com o parâmetro marcado o valor integral das férias gozadas no mês será abatido na provisão, ou seja, será calculado apenas 3/12 avos de férias proporcionais. |
| Abate o valor das férias na rescisão do mês | Com este parâmetro marcado no momento do cálculo da provisão de férias o sistema irá abater o valor das férias pagas na rescisão no mês atual. |

Na tela de Análise do Orçamento é possível acessar uma view para visualização e edição dos históricos gerados.  
Nesta view é possível fazer agrupamentos para melhor visualização dos registros. Para isto basta arrastar as colunas desejadas para o agrupamento.

Exemplo: agrupando por Nome e Ano.

**Encargos**

Neste passo o usuário informa as parametrizações para a geração dos encargos da folha de pagamento.   
É possível selecionar o mesmos encargos cadastrados que são utilizados na folha de pagamento.

|  |  |
| --- | --- |
| Quebra de Seção | Código de quebra para seleção das seções que irão compor a seleção. |
| Seleção de Funcionários | Parâmetros para a seleção dos funcionários que irão compor a seleção. |
| Período | Informe o período de competência que serão gerado os encargos.  **- Todos:** Opte por este campo se você desejar utilizar todos os períodos.  **- Períodos:** Opte por este campo se você desejar contabilizar um ou mais de um período selecionado. Digite no campo a seguir os períodos selecionados, separando–os por vírgula.  Exemplo: 1,2,3. |
| Permite valores negativos para fórmulas | Este parâmetro não permite que o sistema gere encargos valores negativos gerados por fórmula. Isto é válido somente para os encargos, cujo o tipo é A (Valor calculado através de fórmula). |
| Seleção dos Códigos de encargos ativos | Selecionar quais os grupos de encargos (código de encargos ativos) devem ser processados. |

Na tela de Análise do Orçamento será possível acessar uma view para visualização e edição dos encargos gerados:

****Cálculo do Orçamento****

Nesta tela o usuário salva os parâmetros do orçamento e dispara o cálculo.  
Obs: Antes de disparar o cálculo, o sistema  verifica a existência das tabelas de cálculos (INSS, IRRF) com vigência para o período do orçamento.

****Análise do orçamento****

O Totvs Folha de Pagamento tem uma tela para verificação das informações geradas no cálculo do Orçamento.  
Os dados não podem ser alterados nesta tela. Se necessário, os ajustes devem ser realizados nas etapas anteriores, e o orçamento recalculado.  
Esta tela deve permitir visualizar as informações totalizadas seção e função, e também os valores individuais por funcionário.  
Serão listadas todas as seções do orçamento, exibindo as funções de cada seção e os funcionários de cada função. Haverá um grid com os eventos totalizados por competência e por função, e outro grid com os eventos totalizados por competência e por funcionário.  
Através desta tela também é possível acessar as views de Histórico de Provisões e Histórico de Encargos.

**Análise Realizado x Previsto**

Será disponibilizado em Versões futuras!
