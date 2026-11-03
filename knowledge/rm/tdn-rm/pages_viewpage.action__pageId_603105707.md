---
content_hash: 28504cebad672fc8b1c8fae271d086d4696b0ef75174947ebe736c7e7f2e4c31
fetched_at: '2026-06-29T00:10:58.075636+00:00'
page_id: '603105707'
product: rm
source: tdn-rm
title: Acelerador de Implantação - App Minha Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=603105707
version: 118
---

Esta funcionalidade do TOTVS Construção Obras e Projetos está disponível a partir da versão 12.1.32 e possibilita que a configuração do ambiente de Integração com app Minha Obra seja realizado de forma simples e rápida.

Para acessar basta navegar através do menu principal: Aba Projetos/Grupo Parâmetros/Aceleradores de Implantação/Aceleradores de Implantação Minha Obra:

Mas antes, é necessário conceder permissão de acesso ao usuário:

Após dada permissão, o usuário deverá acessar o projeto por onde deseja começar, pois o assistente usa o projeto do contexto para configuração:

**Iniciando a implantação do App Minha Obra**

Será exibida a tela principal do wizard de implantação do App Minha Obra contendo algumas orientações:

Na próxima etapa do wizard será possível escolher qual funcionalidade deseja configurar .

Ao selecionar o checkbox "configurar" , iniciará os passos do wizard da opção selecionada.

O link "**Saiba Mais**"  direcionará para a documentação da funcionalidade caso queira consultá-la.

Exemplo: Selecionando a configuração da funcionalidade Avanço Físico o wizard direciona a página geral da documentação no tdn [App Minha Obra](https://tdn.totvs.com/pages/viewpage.action?pageId=607612027)

(Para detalhes da funcionalidade selecionada nesse exemplo basta navegar no menu de opções : App Minha Obra\ Funcionalidade\ Avanço Físico )

Quando a funcionalidade já estiver configurada ela não aparecerá mais no wizard como opção para ser configurada.

**Passo 1:** Informe quais as funcionalidades deseja configurar:

**Passo 2:** Após selecionar as funcionalidades que deseja configurar, o usuário será direcionado para a tela dos parâmetros gerais e globais conforme abaixo:

Nesse momento o usuário implantador deve informar:

* se utilizará mais de um projeto por coletor móvel (trata-se de um parâmetro geral e valerá para todos os projetos e coletores cadastrados);

* se utilizará mais de um coletor por usuário (também se trata de um parâmetro geral e assim como o primeiro, uma vez definido e cadastrado mais de um, não será permitido alterá-lo);

* e a chave de acesso para o Google Maps (opcional).
* Ao acessar o link de documentação "Porque utilizar essa chave e como ativa-la" navegue na opção "[Parametrização do Mapa](https://tdn.totvs.com/pages/releaseview.action?pageId=506373365#Portal--2120820397)".

**Passo 3:** Na tela seguinte, deverá informar quais usuários terão acesso a quais funcionalidades no App:

Após aplicar, será apresentada a tela abaixo, possibilitando ao implantador cadastrar vários usuários com diferentes permissões; ou avançar, dando continuidade na implantação do App:

**Passo 4:** Após informar os usuários, será necessário cadastrar os coletores, para então associá-los aos usuários cadastrados no passo anterior:

**IMPORTANTE:** O Identificador do coletor pode ser visualizado na tela inicial do [App Minha Obra](https://tdn.totvs.com/pages/viewpage.action?pageId=607612027) ou ao selecionar o tipo de configuração manual; por isso, é necessário ter o dispositivo com o App instalado. 

Da mesma forma que o cadastro de usuários, será possível informar vários coletores nesse passo:

A partir desse momento, as telas serão apresentadas de acordo com as funcionalidades selecionadas no Passo 1. Clique na funcionalidade desejada para expandir o conteúdo e conhecer a respeito:

Mão de Obra

Selecionando essa funcionalidade serão exibidas as seguintes telas:

Selecionando que não deseja utilizar folha tarefa, será exibida a tela para que possa selecionar um filtro para exibição das tarefas:

Ao aplicar o filtro será exibida a tela abaixo, onde o usuário poderá além de inserir filtro para outro coletor, editar o mesmo, ou avançar.

Caso o usuário tenha optado por usar folha tarefa, será exibida a tela abaixo, onde o usuário poderá optar por usar ou não uma periodicidade padrão:

Ao avançar, deverá informar se irá utilizar a revaloração de mão de obra no projeto corrente, através da integração com o TOTVS Folha de Pagamento. Assim como nas telas anteriores, o assistente dispõe o link do documento de referência do processo para apoiar o usuário caso tenha alguma dúvida:

Saiba mais detalhes em: [Rateio e Revaloração de Mão de Obra](https://tdn.totvs.com/pages/releaseview.action?pageId=421385566)

Na sequência, será exibida a tela de Rateio de horas de improdutividade.

Essa tela permite habilitar ou não o rateio de horas improdutivas para as tarefas de mão de obra.

Caso escolha sim é necessário definir também qual tarefa padrão e o motivo de improdutividade default. [Motivos de Improdutividade](https://tdn.totvs.com/pages/viewpage.action?pageId=607612064#tudo-sobre-funcionalidades-interfaces)

Ao habilitar sim só é possível avançar no processo se informar a tarefa e motivo de improdutividade.

Na próxima tela será disponibilizada a opção de utilizar ou não alocação de Mão de Obra.

No TCOP existe um parâmetro que permite controlar a capacidade da equipe na alocação de mão de obra. Saiba mais em: [Alocação de mão de obra da equipe](https://tdn.totvs.com/pages/releaseview.action?pageId=421385139)

A próxima tela é possível definir se vai utilizar ou não apontamento avulso de mão de obra e  como será a sincronização dos membros da equipe.

No próximo passo segue a tela de criação de equipe de mobilidade.

Nesse passo é necessário informar o nome da equipe , marcar o checkbox de ativa , informar o responsável da equipe e seu tipo (se é funcionário ou terceiro).  Veja mais detalhes em: [Equipes](https://tdn.totvs.com/display/LRM/Equipe+de+Mobilidade)

Na sequência é exibida a tela de inclusão de membos na equipe.

Para incluir basta:

* Selecionar no campo Equipe a que deseja vincular o membro
* Definir o tipo de membro (funcionário ou terceiro)
* ativa-lo (opcional)
* Marcar se esse membro atuará em mais de uma equipe (opcional) .

Após informar os campos basta aplicar e avançar

Para mais detalhes acesse: [Inclusão de Membro de Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=421385443)e [Membros de Equipe](https://tdn.totvs.com/display/LRM/Membro%28s%29+da+Equipe+Projeto)

Avanço Físico

Na funcionalidade de Avanço Físico, o primeiro passo e definir qual a forma de utilização da funcionalidade, sendo Progresso da Tarefa ou Trabalho  Realizado no Apontamento.

Para saber mais sobre as duas formas de utilização clique [aqui](https://tdn.totvs.com/x/KtUdGQ).                  

                           

Se esta funcionalidade tiver sido selecionada no Passo 1, então na próxima tela o implantador deverá informar se deseja utilizar Folha Tarefa:

Os links em azul direcionam para a documentação da folha tarefa e da associação de projeto ao coletor, assim o implantador poderá entender melhor o que é, e sua utilização.

Ao selecionar que Não deseja utilizar folha tarefa, é apresentada a tela abaixo:

Assim como na tela anterior, o link auxilia o usuário caso tenha alguma dúvida sobre a seleção do filtro para exibição das tarefas no coletor. Basta informar o coletor, criar/informar um filtro existente e aplicar. Será exibida mensagem confirmando:

Caso não queira informar algum filtro para outros coletores, basta clicar em avançar. Será exibida tela abaixo, onde deverá responder se deseja atualizar o PERT/Cronograma automaticamente:

* Clicando em Sim, quando os apontamentos forem sincronizados e recebidos pelo TCOP, as informações da coluna Percentual Concluído do PERT serão atualizadas conforme o apontamento lançado. Caso esse projeto não utilize o PERT a atualização se dará no cronograma realizado.

* Clicando em Não, a atualização dos dados apontados não será automática e poderá ser feita posteriormente.

Em caso de ter optado por usar folha tarefa (na primeira tela da funcionalidade), será apresentada a tela para seleção da periodicidade padrão para as folhas tarefas: 

Caso decida por informar uma periodicidade padrão, clicando em Sim, serão habilitados os campos da periodicidade e para o dia da semana que deverão iniciar os apontamentos:

Em seguida, será exibida a tela abaixo, onde deverá responder se deseja atualizar o PERT/Cronograma automaticamente ao sincronizar, e se deseja considerar o saldo da tarefa:

* Clicando em Sim, para atualizar o Pert/Cronograma, quando os apontamentos forem sincronizados e recebidos pelo TCOP, as informações da coluna Percentual Concluído do PERT serão atualizadas conforme o apontamento lançado. Caso esse projeto não utilize o PERT a atualização se dará no cronograma realizado.

* Clicando em Não, a atualização dos dados apontados não será automática e poderá ser feita posteriormente.

Com relação ao saldo da tarefa:

* Clicando em sim, o saldo da tarefa será considerado, ou seja, não será permitido que tarefas que  não possuem saldo sejam associadas à folha tarefa, ou que sejam  realizadas associações que ultrapassem o saldo disponível da tarefa.

* Clicando em não, o saldo não será considerado em nenhuma rotina do App Minha Obra, sendo permitida a associação à folha tarefa para tarefas que não tenham saldo, bem como que sejam realizadas associações que ultrapassem o saldo disponível da tarefa.

As parametrizações de Avanço Físico foram concluídas com sucesso:

Equipamento

Selecionando essa funcionalidade serão exibidas as seguintes telas:

A tela para definir custos indiretos será exibida quando integrado com o backoffice Protheus.

A tela para vinculação de equipamentos ao projeto tem a necessidade de ao menos um equipamento vinculado para poder avançar.

Clicando no botão Vincular Equipamentos será exibido o processo.

Selecione quais equipamentos irão ser vinculados ao projeto, podendo filtrar por somente equipamentos da filial do mesmo.

Após selecionado, execute o processo:

Ao finalizar o processo, a tabela de Equipamentos Associados ao Projeto listará os novos registros.

A coluna Operador de Equipamento é editável, podendo atribuir ou remover a permissão de operador.

**Observação: A tela de Operadores de Equipamento só é apresentada caso exista ao menos uma equipe de mobilidade cadastrada.**

Ao carregar a etapa de atribuição de equipamento ao operador a tabela Equipamentos Associados ao Usuário exibi todos os equipamentos associados a usuários. Podendo ser filtrada através do campo Dados Usuário, informando um usuário específico para a associação.

**Observação: A tela de Atribuição de Equipamento por Operador só é apresentada caso exista ao menos uma equipe de mobilidade cadastrada.**

Com o filtro de Dados de Usuário:

Ao clicar no botão Associar Equipamentos irá iniciar o processo de Associar Equipamentos ao Usuário que foi selecionado no campo Dados do Usuário:

Selecione quais equipamentos serão associados e execute o processo:

Após, será atualizada a tabela com os novos registros:

Ciclo de Transporte

Selecionando essa funcionalidade será exibida a tela que informa sobre o parâmetro de distância fixa padrão entre os marcadores do ciclo de distância percorrida:

Após, será exibida a tela para cadastro dos seus ciclos de transporte, na qual você irá informar:

**Tipos de Ciclo de Transporte**

**Distância Pré-Definida:**Distância fixa definida no cadastro do Ciclo que será usada como base entre o ponto de Carga e Descarga.

**Distância Percorrida:**Busca distância entre os marcadores de Carga e Descarga definida em **Parâmetros de Projeto → Mobilidade → Ciclo de Transporte**. O cálculo da distância entre os marcadores é realizado no App Minha Obra, após realizar o apontamento da descarga.

Para saber mais sobre o Ciclo de Transporte e os Tipos de Ciclo de Transporte clique [aqui](https://tdn.totvs.com/display/MOBILE/Guia+de+Uso+-+Minha+Obra#tudo-sobre-funcionalidades-interfaces).

Movimentações de Produto

Selecionando essa funcionalidade será exibida a seguinte tela:

Caso o sistema esteja integrado com o backoffice Protheus, a tela será apresentada da seguinte forma:

Ao final das parametrizações, caso tenha optado por utilizar folha tarefa, o usuário terá a opção de cadastrar uma folha tarefa para o projeto corrente:

Optando por cadastrar deverá preencher as seguintes informações:

Ao clicar em avançar será apresentada tela para associar as tarefas que irão constar na folha tarefa:

Em seguida deverá associar à folha tarefa que está sendo cadastrada, um coletor:

Selecionar a equipe e as tarefas caso queira :

Após executar, o processo de criação de folha tarefa será concluído:

Retornando para a tela do assistente, ao avançar, será exibida a tela abaixo:

Clicando em "Gerar QR Code", após preenchimento dos campos, é exibido o QR Code para configuração automática dos dispositivos:

Na tela seguinte, será possível enviar a todos os usuários de coletores, para que estes possam efetuar a correta configuração do App nos dispositivos:

Pronto! A implantação do App Minha Obra foi concluída!
