---
content_hash: 859ac0a47222aa6c21eb0371f75487cca50fee40379161718e93ad455e1ac83b
fetched_at: '2026-06-29T00:06:25.858952+00:00'
page_id: '224448994'
product: rm
source: tdn-rm
title: ER_Gestão_Hierarquia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224448994
version: 23
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | Gestão Organizacional |
| **Segmento Executor** | RM | | |
| **Projeto1** | WBS\_R\_RHU007 | **IRM1** | PCREQ-6306 |
| **Requisito1** | PCREQ-6309 | **Subtarefa1** | PDR\_RHU\_RHU007-92 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## 

## Objetivo

 O objetivo deste projeto é definir um novo modelo de hierarquia a ser utilizado pelos sistemas de Recursos Humanos da Linha RM.

O modelo tem como base a hierarquia de seções, porém permite maior flexibilidade para os clientes e melhor usabilidade para os usuários.

A definição de chefes/subordinados utilizada pelos sistemas de RH passa a respeitar o modelo de posições.

## Definição da Regra de Negócio

**História:** *RHUAGIL-58 - Gestão de Hierarquia por Posição*

**Como:** Analista de recursos humanos

**Eu preciso:** Cadastrar gestões de hierarquia, definindo nome, descrição e visualizando se a gestão está ativa.

**Para conseguir:** Aplicar uma gestão à empresa e assim definir as regras de hierarquia que serão utilizadas.

**Critérios de aceitação:**

* Deve ser possível cadastrar e editar gestões de hierarquia;
* Deve ser possível excluir gestões que não estejam ativas;
* O campo “Ativa” não pode ser editado pelo usuário por meio do cadastro.
* Ao cadastrar uma Gestão de Hierarquia, o usuário deve poder escolher se deseja utilizar a estrutura de seções atual ou se deseja utilizar uma Proposta de Reestruturação de Seções. Se utilizar Proposta de Reestruturação, deve ser obrigado informar qual proposta. Somente poderão ser utilizadas propostas do tipo “Reimplantação da Estrutura de Seções” e que estejam com o status “Definida”.
* Não deve ser permitido mudar o tipo de estrutura numa gestão se existir pelo menos uma posição associada a uma seção (posição física). (Informação na tela e validação no salvar/server)
* Não deve ser permitido mudar a Proposta de Reestruturação de Seção escolhida para uma gestão se existir pelo menos uma posição associada a uma seção (posição física). (Informação na tela e validação no salvar/server)
* Se for escolhida numa Gestão de Hierarquia uma Proposta de Reestruturação de Seção que já está sendo utilizada em outra Gestão de Hierarquia, deve ser dada uma mensagem de alerta ao usuário, informando o ocorrido. Isto não impede que a proposta seja utilizada.
* Uma Gestão ativa nunca poderá ser alterada para apontar para uma proposta de reestruturação.

**Tela:**

**História:** *RHUAGIL-59 - Times de gestões de hierarquia por posições*

**Como:** Analista de recursos humanos

**Eu preciso:** Dentro de uma gestão por posições tenho que cadastrar times e seus participantes (funcionários e externos).

**Para conseguir:** Agrupar de maneira flexível e rápida, funcionários e externos de acordo com os critérios que a empresa quiser levar em conta.

**Critérios de aceitação:**

* Cadastrar, editar e excluir times;
* Somente times que não tenham vínculo com posição podem ser excluídos;
* Deve ser possível excluir participantes de um time;
* Não pode ser incluído num time um participante que esteja ocupando uma posição na gestão. Auxiliares podem ser incluídos normalmente.
* Deve haver um processo para inclusão de funcionários ou externos. O processo deve conter apenas uma etapa, onde o usuário escolher se quer incluir funcionário ou externo e uma listagem para escolher as pessoas.

**Tela:**

**História:** *RHUAGIL-60 - Painel de Hierarquia*

**Como:** Analista de RH

**Eu preciso:** Acessar um painel que possua quatro áreas para exibição de informações e que no 1º quadrante possua um campo para escolher uma gestão de hierarquia.

**Para conseguir:** Escolher a gestão de hierarquia que desejo visualizar.

**Critérios de aceitação:**

* Deve possuir um campo de busca da gestão de hierarquia, que por padrão trará carregada a gestão de hierarquia que estiver ativa, se houver.
* Ao lado do campo de busca da gestão de hierarquia, deve haver um campo que demonstre se a gestão está ativa ou não.

***Sincronismo entre quadrantes e a*** **árvore de posições*:***

* Informações de líder deve obedecer ao foco. Se estiver trocando posição na árvore de posições, deve respeitar a árvore de posições.
* Ao incluir, editar ou excluir posição, deve atualizar a árvore de posições, somente incluindo ou excluindo o node, e não recarregando.

**Tela:**

**História:** *RHUAGIL-61 - Árvore de posições* (*Treeview) de hierarquia no Painel de Hierarquia*

**Como:** Analista de RH

**Eu preciso:** visualizar no Painel de Hierarquia (no 2º quadrante) uma árvore de posições que represente a estrutura hierárquica de posições da Gestão de Hierarquia que estiver selecionada no 1º quadrante.

**Para conseguir:** ter uma visão rápida e centralizada da hierarquia de posições.

**Critérios de aceitação:**

* A árvore de posições deve ser carregada automaticamente após uma Gestão de Hierarquia ter sido selecionada no 1º quadrante.
* Cada nó da árvore de posições deve exibir o nome da posição.
* A árvore de posições deve ser exibida expandida.
* Na árvore de posições só deve mostrar líderes ativos
* Líder ativo demitido, deve ser exibido em vermelho

**História:** *RHUAGIL-62 - Opções de visualização da árvore de posições* (*treeview)*

**Como:** Analista de RH

**Eu preciso:** ter a opção de visualizar na árvore de posições os nomes dos líderes das posições e ter botões para expandir e recolher a árvore de posições.

**Para conseguir:** ter uma visão rápida

* Deve haver botões para expandir e para recolher toda a árvore de posições.
* Deve haver um parâmetro que, quando marcado, altera a montagem da árvore de posições de modo que seja exibido um nó contendo o nome do líder atual abaixo de cada posição. Se não houver líder, não exibirá o nó específico para o nome do líder. Ao ser desmarcado a árvore de posições volta a exibir somente as posições. Sempre que for trocada esta opção a árvore de posições é expandida automaticamente.
* Deve existir um parâmetro para apresentar Cód. da Seção no painel de hierarquia em frente ao nome da posição (se for uma posição física).

**História:** *RHUAGIL-64 - Legenda e formatação da árvore de posições* (*treeview)*

**Como:** Analista de RH

**Eu preciso:** ter uma legenda que explique as cores de fontes e ícones usados na árvore de posições, e ter a árvore de posições representando corretamente ícones e fontes esperados.

**Para conseguir:** entender o que está sendo demonstrado na árvore de posições.

**Critérios de aceitação:**

* A legenda deve ser localizada na posição direita superior do 1º quadrante.
* A legenda deve ser retrátil, ou seja, permitir ser expandida e recolhida, conforme necessidade do usuário.
* A legenda deve conter os ícones utilizados na árvore de posições e também as cores de fontes que sejam utilizadas para demonstrar os status das posições.
* Os ícones e fontes demonstrados na legenda devem ser aplicados à árvore de posições.
* Deve haver um ícone para representar posições físicas (ligadas a uma seção) e outro para posições lógicas.
* Deve haver um ícone para representar líderes, quando exibidos na árvore de posições.
* Para posições que possuam mais de um líder vigente ou nenhum, ou que o líder esteja com a situação “Demitido”, o nome da posição deve ser exibido na cor vermelha.

**Tela:**

**História:** *RHUAGIL-65 - Informações do líder*

**Como:** Analista de RH

**Eu preciso:** visualizar foto e informações do líder de uma posição.

**Para conseguir:** obter detalhes do participante.

**Critérios de aceitação:**

* Quando escolher uma posição na árvore de posições, as informações do líder devem ser apresentadas no 3º quadrante.
* Se for escolhida uma posição sem líder, esse quadrante deve exibir um informativo sobre a ausência de líder.
* Deve ser exibida a foto do participante redimensionada.
* Para funcionário, devem ser exibidos: chapa, nome, tipo (funcionário), função e seção.
* Para externo, devem ser exibidos: código de externo, nome, tipo (externo), função e seção.
* Se for escolhida uma posição, ou um líder de posição com mais de um líder, ao clicar na posição deve dar um alerta informando que há mais de um líder.
* Deve exibir código e descrição de função e seção.
* Os funcionários e externos devem ter um link para abrir seus cadastros.
* Os campos de seção devem estar sendo mencionados como função atual e seção atual.
* Nas informações do líder de posição de uma gestão vinculada a uma reestruturação de seções, devem ser exibidos código e descrição da seção proposta, e não da seção que o líder esteja lotado atualmente.

**Tela:**

**História:** *RHUAGIL-66 - Detalhes da Posição*

**Como**: Analista de RH

**Eu preciso:** visualizar informações de uma posição.

**Critérios de aceitação:**

* Deve haver no 4º quadrante uma coleção de abas, cuja primeira aba “Posição”, exibe informações da posição escolhida na árvore de posições.
* Devem ser exibidos: código da posição, descrição, posição pai, código e descrição da seção (se houver).

**Tela:**

**História:** *RHUAGIL-67 - Times da posição*

**Como:** Analista de RH

**Eu preciso:** visualizar os times vinculados a uma posição, incluir e excluir vínculos, e incluir e editar times existente.

**Critérios de aceitação:**

* Deve ser incluído na aba Times, do 4º quadrante do Painel de Hierarquia, uma listagem capaz de incluir e excluir vínculos. O funcionamento da listagem deve permitir, que novos times sejam incluídos a partir da tela de pesquisa.
* Ao incluir um time pela listagem, ao salvar, já deve vincular com a posição selecionada.
* Ao excluir o vínculo, o time continua existindo.
* Ao trocar a posição, é necessário atualizar a listagem somente se a aba de times estiver sendo visualizada.
* Ao trocar o líder da árvore de posições, mas não trocar a posição, não é necessário atualizar a listagem.

**Tela:**

**História:** *RHUAGIL-72 - Liderança da posição*

**Como:** Analista de RH

**Eu preciso:** de uma lista de participantes que exercem liderança na posição escolhida.

**Para conseguir:** visualizar os líderes das posições hierárquicas.

**Critérios de aceitação:**

***Listagem***

* Deve haver no 4º quadrante, a terceira aba “Liderança”, para listar e acessar líderes vinculados à posição selecionada na árvore de posições.
* Na listagem devem ser exibidos chapa, código de externo, nome, vigência e tipo dos líderes da posição, ordenados em ordem decrescente de data de início da vigência.

***Cadastro de líder:***

* Ao incluir um participante numa posição, é necessário estabelecer:
* Coligada: coligada do participante.
* Chapa: chapa do funcionário que ocupa a posição, se for funcionário.
* Código de externo: código do externo que ocupa a posição, se for externo.
* Data inicial: data inicial da ocupação da posição pelo funcionário. Campo obrigatório.
* Data final: data final da ocupação da posição pelo funcionário. Se não informada, entende-se que não há data final de vigência dessa ocupação.
* Tipo: direta ou indireta.
* Auxiliar/Temporário: indica se é um ocupante auxiliar ou temporário.
  + Somente participantes que não participam de um time podem ocupar posições de liderança. Ao tentar vincular um participante a uma posição, se ele pertencer a um time, deve ser perguntado ao usuário se ele deseja remover o participante do time e alocá-lo na posição. Neste caso o participante é removido do time que pertence e passa a ocupar a posição.

***Editar líder***:

* Ao clicar no botão “Editar”, se não houver um, e apenas um líder selecionado, deve ser exibida a mensagem “Por favor selecione o líder que deseja editar”.
* Ao clicar no botão “Editar”, se só tiver um líder selecionado, deve ser a exibida a tela de edição de líderes, descrita na história “Liderança da posição – Incluir novo líder”. O líder que estava selecionado será carregado para edição.
* Não é permitido alterar o participante após salvar o registro. Este campo passa a ser somente para leitura.

***Excluir líder:***

* Ao clicar no botão deve ter uma mensagem de confirmação da ação solicitada.

***Regras da Tela:***

* Na Inclusão de líder a data final não fica disponível.
* Na Inclusão de auxiliar a data final fica disponível e é obrigatória.
* Ao preencher a data final de vigência de um chefe e salvar, deve ser dada uma mensagem de confirmação "Ao salvar você estará finalizando a vigência. Deseja prosseguir?". Se o usuário confirmar a data final será gravada no banco.
* É possível editar o registro de um líder apagando sua data final de vigência, desde que não haja outro chefe com a data final não preenchida.
* Para auxiliares, não deve ser informado o Tipo de ligação (direta/indireta) com posição acima. Esta informação deverá ficar desabilitada e desmarcada.
* Para auxiliares, não deve haver validação de interseção de períodos. Data de início e fim são sempre obrigatórias. Consequentemente, ao validar a vigência, só devem ser considerados os líderes que não são auxiliares.
* Não pode ser incluído num time um participante que seja chefe vigente numa posição

**Tela:**

**História:** *RHUAGIL-76 - Validação de vigência de liderança*

**Como:** Analista de RH

**Eu preciso:** ter regras de consistência de vigência de liderança.

**Para conseguir:** integridade na definição de líderes.

**Critérios de aceitação:**

* Os campos Data Inicial e Data Final indicam o período de vigência da ocupação da posição. A Data Final pode ser deixada em branco se não houver previsão de final da ocupação da posição, porém não deve existir mais de um ocupante para uma posição com data final indefinida.
* Não pode haver conflito entre a vigência de ocupantes de uma posição. Isso significa que, para definir um novo ocupante ou alterar a vigência, é necessário respeitar as datas já definidas, de modo que não exista interseção entre as vigências dos ocupantes de uma posição.
* Não pode existir interseções no futuro: se houver um período sem data final não pode permitir incluir uma liderança num período futuro em relação a ele.

**História:** *RHUAGIL-77 - Validação de liderança direta e indireta*

**Como:** Analista de RH

**Eu preciso:** ter regras de consistência de tipos de liderança e assim conseguir identificar quem é o chefe direto de um participante que ocupe mais de uma posição na hierarquia da empresa.

**Para conseguir:** integridade na definição de líderes.

**Critérios de aceitação:**

* Ao definir um participante como ocupante de uma posição, ao selecionar o participante, se ele não for ocupante de uma posição, o tipo “Direta” deverá ser selecionado automaticamente e não permitir que seja “Indireta”. Se ele já é ocupante direto de uma posição, o tipo indireto será marcado automaticamente. O usuário poderá alterar posteriormente se assim desejar.
* Para registros existentes, quando alterar o tipo de Indireto para Direto, deve ser dado um aviso ao usuário informando que a posição que atualmente é a Direta passará a ser indireta. Caso o usuário confirme, deverá prosseguir com a ação.
* Para registros existentes, quando alterar o tipo de Direto para Indireto, deve ser exibido um campo para que o usuário escolha a posição que passará a ser do tipo Direta. Essa informação é obrigatória. Caso não haja posições indiretas para que o usuário possa escolher, o usuário não conseguirá salvar a alteração.
* Caso seja necessário trocar ou remover um participante que ocupa uma posição Direta e ele ocupe uma ou mais posições do tipo “Indireta”, deve haver o seguinte tratamento:
* Se tiver apenas uma posição Indireta: alerta ao usuário informando que a posição Indireta deve passar a ser Direta. Caso o usuário aceite a sugestão, o sistema prossegue com essa alteração de tipo na posição que restou.
* Se tiver mais de uma posição Indireta: alerta para o usuário informando que ele deve definir uma nova posição Direta para este participante antes de removê-lo da posição.

**História:** *RHUAGIL-78 - Cadastro de Posições*

**Como:** Analista de RH

**Eu preciso:** Incluir e editar as posições que formam a hierarquia organizacional de uma empresa.

**Para conseguir:** Representar no sistema a hierarquia de chefia.

**Critérios de aceitação:**

* Na primeira aba do 4º quadrante do Painel de Hierarquia, deve haver um botão “Nova Posição”. Este botão, ao ser clicado, deverá acionar a tela de cadastro de posição.
* Também deve ser exibido o botão “Editar Posição”. Ao ser clicado abre a tela de cadastro de posição com o registro que está selecionado na árvore de posições para sua edição.
* Se houver mais de uma posição cadastrada sem posição pai, ao visualizar a tela de edição desses registros deve haver um informativo com os dizeres: “Há mais de uma posição cadastrada sem posição pai. Favor verificar.”.
* A seção pode ser informada se a posição se referir a uma seção física existente na empresa. A mesma seção não pode estar vinculada a mais de uma posição. O usuário pode escolher uma seção que já está vinculada, porém ao salvar o sistema irá informar que já está vinculada a outra, e que não pode prosseguir. Na mensagem, deve mostrar a posição a qual está vinculada.
* A validação de seção será realizada caso no cadastro de gestão de hierarquia estiver selecionado a opção "Validação de Seção no cadastro de Posições", caso não esteja selecionado o sistema só realizará a validação se a seção está cadastrada em outras posições.
  + Ao preencher a seção de uma posição, deve ser validado se não há nas posições acima, seções que sejam inferiores à seção informada. Também não podem existir nas posições abaixo seções superiores à seção informada. Isso deve garantir que a estrutura de posições não entre em conflito com a estrutura de seções.
  + A validação de seção deve ser feita através da máscara, e não somente pelo nível hierárquico.
* Na inclusão, sugerir automaticamente a posição-pai como sendo a posição que estava selecionada na árvore de posições. O usuário poderá alterar esse campo ou até mesmo deixá-la em branco.

**História:** *RHUAGIL-79 - Excluir Posição*

**Como:** Analista de RH

**Eu preciso:** Excluir uma posição da gestão de hierarquia.

**Para conseguir:** Revisar a hierarquia que foi definida previamente.

**Critérios de aceitação:**

* Na primeira aba do 4º quadrante do Painel de Hierarquia, deve haver um botão “Excluir Posição”. Este botão, ao ser clicado, deverá exibir uma mensagem de confirmação da ação.
* Ao tentar remover uma posição que seja pai de outra posição, deve ser exibida a mensagem “Não é possível remover uma posição que seja pai de outras posições”. A remoção não será efetuada.
* Ao tentar remover uma posição que tenha times vinculados, deve ser exibida a mensagem “Os times vinculados a esta posição serão mantidos no cadastro. Deseja prosseguir com a exclusão?”. A remoção será efetuada se o usuário confirmar a operação.
* Ao tentar remover uma posição que tenha líderes vinculados, deve ser exibida a mensagem “Os registros de líderes vinculados a esta posição também serão excluídos. Deseja prosseguir com a exclusão?”. A remoção será efetuada se o usuário confirmar a operação.

**Tela:**

**História:** *RHUAGIL-98 - Alertas da gestão*

**Como:** Analista de RH

**Preciso:** ter uma funcionalidade que me mostre o total de alertas de inconsistência de uma gestão de hierarquia.

**Para conseguir:** estar ciente e agir nas inconsistências, eliminando-as.

**Critérios de aceitação:**

* A tela deve ser acionada a partir de um item de menu.
* Deve ser possível escolher a gestão que eu desejo validar, sendo que a gestão ativa será carregada por padrão.
* A análise só será feita após o usuário solicitar. Uma barra de progresso deverá exibir o andamento da análise.
* Deve ser exibida uma lista com todos os tipos de inconsistências que serão validadas (numa história futura).
* Deve existir um botão “Ver detalhes” que permita abrir uma visão com os itens inconsistentes de um determinado item escolhido na lista. Só habilita o botão se a quantidade de ocorrências do item escolhido for maior que zero.
* Devem ser exibidas na tela de alertas a quantidade de ocorrências de cada um dos tipos de inconsistências abaixo:
  + Posições sem posição-pai: são posições que não possuam posição-pai preenchida nos seus cadastros. A existência de mais de um registro nestas condições caracteriza uma provável inconsistência na estrutura de posições. Só é inconsistência se houver mais de uma posição sem pai.
  + Posições sem líder na data atual: são posições que não possuem um “líder” vigente na data atual.
  + Posições com líder na situação “Demitido”: são posições cujo líder atual encontra-se com a situação “Demitido”.
  + Times sem participantes: são times que não possuem nenhum participante.
  + Times não ligados a uma posição: são times que não estão ligados a nenhuma posição. Os possíveis participantes destes times logicamente não possuem liderança.
  + Funcionários sem liderança: são funcionários que não possuem chefe, seja porque não pertencem a um time, seja porque o time não está ligado a uma posição, seja ainda porque a seção que ele está lotado não está vinculada a uma posição. Quando validando Gestão ligada a uma reestruturação, deve olhar para as seções da reestruturação, e não da estrutura atual.
  + Externos sem liderança: são externos que não possuem chefe, seja porque não pertencem a um time, seja porque o time não está ligado a uma posição, seja ainda porque a seção que ele está lotado não está vinculada a uma posição.
  + Participantes que estejam em mais de um time: são participantes que estão vinculados a mais de um time.
  + Existência de participantes de times que ocupem posições: são participantes que são líderes em posições e que estão vinculados a pelo menos um time.
  + Existência de times que estejam vinculados a mais de uma posição: são times que estão vinculados a mais de uma posição.
  + O líder está definido como Direto em mais de uma posição: são líderes que estão cadastrados com ligação do tipo “Direta” em mais de uma posição da Gestão.
  + Mais de um time ativo em uma posição.
  + Líder da posição pertence a uma coligada onde o tipo de gestão hierárquica é por seção.
  + Externo é líder em outra coligada onde o tipo de gestão hierárquica é por seção.
  + Funcionário é líder em outra coligada onde o tipo de gestão hierárquica é por seção.
* Ao clicar no botão “Ver detalhes”, se houver alertas para o item selecionado, deverá ser carregada uma visão padrão RM com uma lista das posições, com código e descrição, que contêm as inconsistências do tipo escolhido.

**Tela:**

**História:** *RHUAGIL-80 - Ativar gestão de posição e histórico*

**Como:** Analista de RH

**Eu preciso:** ter um assistente que me permita ativar uma gestão de posição. Ao ativar uma gestão, se houver outra ativa, ela deverá ser desativada. Este assistente deverá validar a gestão escolhida e exibir uma lista das possíveis inconsistências (reutilizando rotinas da visão de alertas). Deve ser informado um motivo para ativar uma gestão, e deve gerar histórico, tanto da ativação da gestão quanto da possível desativação de uma gestão que estava ativa.

**Para conseguir:** ter a garantia de ter apenas uma gestão ativa, válida e devidamente registrado o motivo e o responsável pela ativação.

**Critérios de aceitação:**

* O processo só pode ser acionado se uma única gestão estiver selecionada na visão de gestões, e apenas a partir de uma gestão que não esteja ativa.
* Ao ser iniciado, o assistente deverá validar a gestão, exibindo um resumo das validações existentes na visão de alertas de gestão, descritas na história “História: Alertas da gestão”. Deve-se reutilizar os métodos existentes.
* A partir das informações de validação exibidas, o usuário poderá decidir se prossegue com a ativação ou se vai revisá-la. As informações exibidas até este ponto não impedem a execução do processo.
* Após verificar as validações citadas anteriormente, será exibida ao usuário uma lista de validações que impedem a ativação da gestão. Caso sejam encontradas devem ser informadas ao usuário para que, antes de ativar, ele atue eliminando-as. São as seguintes condições:
* Existência de participantes que estejam em mais de um time.
* Existência de participantes de times que ocupem posições.
* Existência de times que estejam vinculados a mais de uma posição.
* Existência de líder direto em mais de uma posição.
  + Se o usuário avançar a etapa, deverá informar o motivo da ativação. Este campo é de preenchimento obrigatório, sem validação do seu conteúdo.
  + Se neste momento a parametrização vigente no sistema não for de Gestão por Posições, o assistente exibirá um alerta na tela com os seguintes dizeres: “O Tipo de Hierarquia parametrizado no sistema não é Gestão por Posições. A Gestão que está prestes a ser ativada só será considerada pelas demais funcionalidades do sistema a partir do momento que a parametrização for realizada. A parametrização está disponível no caminho: Configurações > Parametrizador > Gestão por Posições”.
  + A execução do processo desativa a gestão vigente, se houver, e em seguida ativa a nova gestão.
  + É gravado um histórico da operação, gerando um registro para a gestão desativada (se houver) e um registro para a gestão ativada.
  + Um controle de transações deverá garantir que a ativação só ocorra se a desativação tiver ocorrido.

**Tela:**

**História:** *RHUAGIL-81 - Histórico de ativação*

**Como:** Analista de RH

**Eu preciso:** ter um histórico, tanto da ativação da gestão quanto da desativação de uma gestão que estava ativa.

**Para conseguir:** visualizar o histórico das ativações gestões.

**Critérios de aceitação:**

* Os registros de histórico devem conter informações que identifiquem a gestão, ação realizada (ativação/desativação), motivo, usuário responsável, data e hora. Essas informações podem ser visualizadas em Gestões de Hierarquia > Anexos > Histórico de Ativação/Desativação.

**Tela:**

**História:** *RHUAGIL-96 - Assistente de montagem de gestão de hierarquia a partir da estrutura de seções*

**Como:** Analista de RH

**Preciso:** Ter um assistente que pode ser utilizado para uma gestão de hierarquia, que me auxilie a montar uma estrutura hierárquica a partir da estrutura de seções existente no sistema.

**Para conseguir:** Montar com facilidade e fidelidade a hierarquia.

**Critérios de aceitação:**

* O assistente só pode ser executado se não houver posições e times cadastrados para a gestão.
* O assistente só pode ser executado se a gestão não estiver vigente.
* O assistente deverá, para cada seção da coligada do contexto, criar uma posição “física” e, montar a estrutura de posições seguindo a estrutura de seções.
* Os chefes definidos para as seções deverão ser aplicados como ocupantes das posições criadas para as seções. Os chefes serão incluídos com o tipo de ligação “Direta”. E somente neste momento um participante que esteja num time poderá assumir uma posição.
* Cada supervisor definido no cadastro de chefes/supervisores deve originar uma posição “lógica”. Devem ser vinculados à essa posição times gerados a partir das equipes que esses supervisores atendem. Somente neste momento times podem ser vinculados à mais de uma posição. Também neste momento pode ser que um time seja criado com participantes que ocupem posições.
* Deve existir um parâmetro no assistente de montagem para "Desconsiderar estrutura de supervisores".
* Deve existir um parâmetro no assistente de montagem para “Desconsiderar seções desativadas”.
* Deve haver uma descrição explicando que chefes não vigentes não serão migrados.

**Tela****:**

**História:** *RHUAGIL-147 - Parametrização de tipo de hierarquia*

**Como:** Administrador do sistema

**Eu preciso:** ter a possibilidade de parametrizar no sistema (Parametrizador / Configurações / Gerais / Preferências) se desejo utilizar hierarquia de gestão de posição ou hierarquia de seção. Isso refletirá em todo o sistema a forma de buscar chefes e subordinados. Só deve ser possível parametrizar a hierarquia para gestão por posição se houver uma gestão ativa cadastrada.

**Para conseguir:** escolher o tipo de sistema de hierarquia e ativar a gestão por posição.

**Critérios de aceitação:**

* Se o usuário marcar a segunda opção e não houver uma Gestão de Hierarquia ativa no sistema, deverá ser exibido um alerta com a mensagem: “Não é possível ativar a Gestão de Hierarquia enquanto não houver um cadastro de Gestão de Hierarquia com o status ‘Ativa’. Favor verificar”.
* Por padrão, a opção que deverá estar marcada será “Por Seção”.
* Ao trocar o tipo de hierarquia, o sistema deverá verificar se há requisições em andamento, suspensas ou pendentes para a coligada atual. Se houver, deverá ser dado um aviso ao usuário informando a quantidade de requisições e que, a partir do momento da confirmação, as ações que envolvem fluxos passarão a respeitar a nova regra de hierarquia. (Semelhante à validação existente ao habilitar centro de custos em requisições).
* O parâmetro só deve estar visível mediante execução de script de inserção de “ParamLinha”, onde NOMECOLUNA = ‘HABILITARPARAMETROHIERARQUIA’ e VALORINT = 1. Caso o parâmetro ‘HABILITARPARAMETROHIERARQUIA’ não exista ou tenha VALORINT=0, o Parametrizador não deverá sequer exibir as opções de configuração de hierarquia e nenhuma outra funcionalidade da gestão (Cadastro, Painel, Alertas e Processos).
* Se houver alertas, apresentaremos uma mensagem se tiverem alertas de gestão, para que o usuário confirme que deseja seguir mesmo assim.

**História:** *RHUAGIL-236 - Gestão de hierarquia para proposta de reestruturação de seções*

**Como:** Analista de RH

**Eu preciso:** montar uma Gestão de Hierarquia a partir de uma estrutura de seções que esteja sendo proposta por meio de uma “Proposta de reestruturação de seções” ou a partir da estrutura de seções atual da coligada.

**Para conseguir:** planejar hierarquia conforme uma proposta de reestruturação de seções para aplicação futura na empresa.

**Critérios de aceitação:**

* O cadastro de posições deve permitir associar a posição a seções da estrutura atual ou de uma proposta de reestruturação, de acordo com o definido na Gestão.
* As validações de seções (posições físicas) deverão considerar estrutura atual ou proposta de reestruturação, de acordo com a Gestão.
* O assistente de ativação de gestão de hierarquia só pode ser executado para gestões que não estejam vinculadas a propostas de reestruturação de seções. Para este caso, haverá um processo específico de ativação a ser definido posteriormente.

**História:** *RHUAGIL-237 - FOP - Aplicar Proposta de Reestruturação de Seção*

**Como:** Analista de RH

**Eu preciso:** aplicar uma proposta de reestruturação vinculada a uma gestão de hierarquia.

**Para conseguir**: aplicar todo o planejamento realizado e ver toda a estrutura atual ser atualizada.

**Critérios de aceitação:**

* Ao optar por “Reparametrizar” uma proposta de reestruturação que esteja vinculada a uma Gestão de Hierarquia, deve ser dado um alerta ao usuário informando que ele deverá refazer a Gestão de Hierarquia e que as definições feitas até o momento nesta gestão serão perdidas. Se o usuário prosseguir, todas as posições, líderes e times da gestão serão excluídos, sendo mantido apenas o cadastro da gestão.
* Ao optar por “Executar proposta” de reestruturação que esteja vinculada a uma Gestão de Hierarquia, deve ser chamada a validação da Gestão e verificar se não há nenhum alerta impeditivo de ativação. Exibir numa etapa os alertas encontrados. Se houver impeditivo, não deixar prosseguir. Se o tipo de hierarquia parametrizada no Vitae não for “hierarquia”, deve ser exibido um alerta informando que a somente após alterada a parametrização a hierarquia será considerada (igual existe na ativação).
* Se houver mais de uma Gestão de Hierarquia vinculadas à proposta de reestruturação, no assistente de execução da proposta deve haver um campo de busca da Gestão da qual deseja aplicar.
* Deve haver um controle de transações que garanta a atomicidade do processo todo: aplicação da reestruturação e ativação da hierarquia.
* Se houver mais de uma gestão de hierarquia vinculadas à proposta, todas serão alteradas para apontar para a estrutura atual de seções e não mais a uma proposta, porém somente a escolhida pelo usuário será ativada.
* Será gerado histórico de ativação da gestão, informando que a ativação foi feita a partir da execução de uma proposta de reestruturação, e qual foi a proposta. Se houver uma gestão que estava ativa anteriormente, ela será desativada e também terá um registro no histórico.

**História:** *RHUAGIL-241 - Assistente de Montagem de Hierarquia de Proposta de Reestruturação*

**Como:** Analista de RH

**Eu preciso:** Montar uma hierarquia a partir de uma proposta de reestruturação de seção definida no Labore.

**Para conseguir:** Ter a hierarquia que respeite o que já foi definido anteriormente em seções físicas numa proposta de reimplantação.

**Critérios de aceitação:**

* O assistente de montagem de hierarquia deve estar apto a ser executado utilizando como insumo uma proposta de reestruturação de seção. Quando executado para uma gestão ligada a uma reestruturação, as seções físicas que serão criadas devem ser as que estiverem na proposta. Os chefes, supervisores e equipes deverão ser lidos de acordo com a tabela De/Para, e deste modo respeitarem as preferências de reestruturação propostas. Este assistente só pode ser executado se a proposta estiver com status “Definida”.
* Todo líder criado deverá ser do tipo Direto.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
