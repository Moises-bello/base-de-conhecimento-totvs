---
content_hash: adbacb39b305929b402a56ae0045e821a64d34345db68b1194b70461569de42b
fetched_at: '2026-06-29T00:11:03.437687+00:00'
page_id: '622512467'
product: rm
source: tdn-rm
title: Minhas Inspeções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=622512467
version: 120
---

App Minhas InspeçõesGuia de Uso APP

A documentação relacionada ao uso do APP está disponível em:  
[APP Minhas Inspeções](https://tdn.totvs.com.br/pages/releaseview.action?pageId=645237708)

Portal WebWebConfiguração

* **Configurações do RM.Host/RM.Host.Service**

Nas configurações do RM.Host/RM.Host.Service devem estar informadas as chaves **DefaultDB** e **ApiPort**.

**DefaultDB:** Chave necessária para que o Host encontre no arquivo Alias.dat qual alias de base de dados será utilizada.

**ApiPort:** Porta de conexão de API do host.

Em alguns casos a chave pode não estar preenchida no arquivo de configuração do host mas por padrão caso a tag não estiver preenchida, o valor para a chave ApiPort é 8051

A porta informada no ApiPort deve estar liberada nas regras de firewall do servidor/máquina para que a comunicação via api funcione corretamente no host.

**WebServiceCulture:**A tag WebServiceCulture é utilizada para alterar a cultura de leitura e conversão dos dados recebidos pelo WebService.

    Para o que a comunicação via api funcione corretamente o valor a ser inserido na chave deve ser "Invariant".

PortalPortalGeralGeral

O **Minhas Inspeções** oferece uma solução **multi-coligada** para a gestão de inspeções, permitindo o compartilhamento de recursos e a centralização de dados. Isso otimiza processos e proporciona uma visão unificada dos projetos. Os cadastros de formulários e grupos de usuários podem ser utilizados por todas as coligadas, e na visão de inspeções e no dashboard, o usuário poderá visualizar informações de todos os projetos e coligadas.

DashboardDashboard

O Dashboard apresenta indicadores representados através de gráficos referente as Inspeções, separados por Fichas de Inspeções, Fornecedores e Usuários.

**Fichas de Inspeções**

Para tal, basta selecionar o(s) Projeto(s) que deseja extrair as informações, na tela será permitido selecionar no máximo 5 Projetos.

Selecione também o período (data início e fata final) e o status de conformidade, Todos, Não Avaliado, Conforme e Não Conforme.

Uma vez selecionado, o gráfico irá atualizar de forma automática apresentando os dados conforme selecionado acima, o primeiro gráfico irá apresentar um Panorama das Inspeções pelos projetos e parâmetros selecionados.

Abaixo irá apresentar um gráfico separado por status, Conforme, Não Conforme, Aguardando Avaliação, Não Avaliados. Este gráfico possui hiperlinks, caso o usuário clique em um destes status o sistema irá direcionar para a tela de Inspeções com filtros aplicados dentro do valor selecionado.

**Fornecedores**

Para tal, basta selecionar o(s) Projeto(s) que deseja extrair as informações, na tela será permitido selecionar no máximo 5 Projetos.

E também, selecionar os Fornecedores que deseja extrair as informações, será permitido selecionar no máximo 5 Fornecedores.

Selecione também o período (data início e fata final) e o status de conformidade, Todos, Não Avaliado, Conforme e Não Conforme.

Uma vez selecionado, o gráfico irá atualizar de forma automática apresentando os dados conforme selecionado acima, o primeiro gráfico irá apresentar um Panorama das Inspeções pelos projetos e parâmetros selecionados.

Abaixo irá apresentar um gráfico separado por status, Conforme, Não Conforme, Aguardando Avaliação, Não Avaliados. Este gráfico possui hiperlinks, caso o usuário clique em um destes status o sistema irá direcionar para a tela de Inspeções com filtros aplicados dentro do valor selecionado.

FormuláriosFormulários

No portal da Obra ou no link direto do Minhas Inspeções, é possível gerenciar os formulários que serão exibidos no app.

No menu Formulários, serão exibidos os formulários já cadastrados e os formulários modelo (com questionário já pronto).

* **Formulários Publicados:**Poderão ser transformados em Rascunhos, Desativados, serem Clonados ou excluídos.
* **Formulários Desativados:** Poderão ser transformados em Publicados, Rascunhos ou excluídos.
* **Formulários Rascunho:**Poderão ser publicados, Inativados, Clonados ou excluídos.

Através das Ações relacionadas, é possível voltar um formulário para Rascunho, Desativar, Clonar, e Publicar, os formulários cadastrados. Ao selecionar um formulário, os botões de Excluir e Editar ficam visíveis:

O cadastro de um novo formulário é iniciado no botão Incluir, em azul na tela acima. Ao clicar o usuário será direcionado para a tela a seguir, onde deverá informar os dados descritos logo na sequência:

* **Dados Gerais**
  + **Nome do Formulário:**Nome do formulário
  + **Onde o formulário será aplicado?:**
    - Caso a opção selecionada for **Projeto**, o formulário será aplicado em um projeto,
    - Se **Tarefa**, o formulário será aplicado em tarefas e
    - Caso a opção selecionada seja **Medição de Contrato,**o formulário será aplicado em medições contratuais.
  + **Roteiro Sequencial:**Caso esteja marcado para utilizar indica que ao responder o questionário não é possível pular perguntas, todas as respostas devem ser respondidas sequencialmente. Caso esteja desmarcado as perguntas do questionário poderão ser respondidas fora de ordem com uma visualização em lista.
  + **Workflow disparado ao finalizar a Inspeção:**
  + **Workflow disparado ao realizar a avaliação a Inspeção:**
  + **Workflow disparado no TOTVS Aprovações e Atendimentos:** Informe o Workflow criado previamente para ser disparado no TAA

Na aba seguinte:

* **Itens**
  + **Tipo de Item:** É o formato para resposta à pergunta do item que será criado no formulário. Se data, valor, texto simples, texto formatado...
  + **Pergunta:**Texto da pergunta
  + **Item obrigatório:**Caso marcado, o formulário não poderá ser finalizado sem ter essa pergunta respondida.
  + **Complementos do Item:**Informações adicionais nas respostas do formulário que também podem ser enviadas. Podem ser obrigatórios ou não
    - **Inserir Evidências:** no momento que o formulário estiver sendo respondido será permitido inserir evidência anexada a resposta do item.
    - **Inserir Observações:**no momento que o formulário estiver sendo respondido será permitido inserir observações anexadas a resposta do item.
  + **Questões:**Depois de efetuar o cadastro das questões, elas irão aparecer no canto direito. Ao clicar em uma pergunta, irá habilitar dois botões ou para **Mover para cima** ou para **Mover para a baixo** a determinada questão.
  + **Listas:** Se o tipo do item for de lista suspensa ou lista de escolha única, irá ter a opção de alterar a ordem dos itens do mesmo jeito que aparece nas questões, como citado acima.

769pxAo criar, na opção de Visualizar formulário, é possível ter uma pré-visualização do formulário e seus itens, exibindo também informações de obrigatoriedade, criticidade e pontuação dos itens do formulário. No canto superior direito possui um botão que permite o usuário alterar o workflow que está associado ao formulário selecionado.

Inspeções

Inspeções

Nesta tela serão listados todas as inspeções criadas com o status de conformidade:

* Conforme
* Não conforme
* Não avaliado
* Aguardando avaliação

O usuário poderá visualizar as questões respondidas no App "Minhas Inspeções" e o total de pontuação:

É possível ainda, visualizar as respostas da inspeção respondida, basta clicar nos três pontinhos ao lado da inspeção que deseja e clicar em visualizar.

Caso a inspeção ainda não tenha um status de conformidade, irá exibir um botão "Resolver" para que seja avaliado como Conforme ou não conforme assim como a justificativa para a alteração do mesmo.

Através do botão , é possível incluir uma nova inspeção, onde as seguintes características são consideradas:

* **Título:** Representa a descrição da nova inspeção
* **Projeto:** Representa a descrição do local da nova inspeção e também é utilizado como filtro para seleção de Tarefas ou Medições
* **Formulário:** Formulários já publicados, onde a partir dessa informação é definido o objeto da inspeção, podendo ser Medição ou Tarefa
* **Medição:** Medições do projeto selecionado
* **Tarefa:** Tarefas do projeto selecionado, onde somente é possível selecionar tarefas do tipo serviço
* **Grupo ou Usuário Específico:** Pode ser selecionado um usuário específico para receber a inspeção ou um grupo de usuários
* **Data de Realização:** Representa a data de prazo para a conclusão da inspeção

Após salvar a nova inspeção, os usuários de destino envolvidos, receberão as notificações nos dispositivos.

**Relatório**

No TOTVS Compartilhamento, foi disponibilizado o relatório do tipo Recursos Smart View TOPREL0077 - Ficha de Verificação(RDO e Minhas Inspeções).TotvsTReports. Este relatório é gerado a partir das inspeções realizadas, consolidando as respostas fornecidas no formulário de verificação. Cada inspeção contém uma lista de itens avaliados, incluindo:

* Perguntas do formulário, previamente configuradas.
* Respostas inseridas pelo responsável pela inspeção.
* Observações adicionais, quando necessário.
* Anexos (documentos, imagens ou vídeos complementares) com opção de visualização.

**Gerando o relatório utilizando o SmartView:**

Selecione o ID da Ficha na lupa, clique no botão "Enviar" e aguarde a geração do PDF contendo o relatório.

**Exemplo de Relatório**

Abaixo, segue um exemplo do formato gerado:

Workflow

Entendendo ainda que, após a criação de Formulários e Inspeções, o resultado da inspeção pode ter diversos caminhos a seguir - fluxos - foi criado a opção de Criação de WorkFlow. Nele é possível criar todo fluxo da Inspeção conforme o exemplo abaixo.

Basta Selecionar a opção de Criar Workflow no Portal, e utilizar as ferramentas de criação.

* **Nome:**Informe o nome do Workflow;
* **Descrição:**Informe a Descrição do Workflow;
* **Criar início:**Irá criar um início do fluxo, representada pelo ícone de Circulo Verde;
* **Criar fim:**Irá criar um fim para o fluxo, representada pelo ícone de Circulo Vermelho;
* **Criar Condição:**Irá criar uma condição para o fluxo, representada pelo ícone de Losango Amarelo;
* **Criar Ação:**Irá criar uma ação para o fluxo, representada pelo ícone de Quadrado Azul;
* **Excluir:**Selecione um dos ícones representados na tela e clique na opção excluir para excluí-lo;
* **Limpar:**Esta opção exclui todo o fluxo criado;
* **Propriedades:**Abre a Propriedade da condição e ação, desde que selecionadas, trazendo opções de Tipo de Condição e Tipo de Ação, esta opção também pode ser acessada com o duplo clique:
  + Propriedades da Condição: Percentual de Aprovação do Formulário, informando qual o Percentual desejado;
  + Filtrar por tipo de formulário: Pode ser definido o tipo da categoria para a condição:

É uma funcionalidade empregada quando um mesmo workflow pode ser aplicado a múltiplos tipos de formulários (como Tarefa, Medição de Contrato ou Movimento). Essa opção viabiliza a criação de condições específicas para cada variante de formulário, permitindo uma adaptação mais precisa às particularidades de cada um. OBS: Para ter compatibilidade em determinado formulário, tipo da ação do workflow deve ser o mesmo informado no formulário, ou marcar 'todos'.

* + - Filtrar por tipo de condição: Inspeção Conforme (avaliação manual) e Inspeção Não Conforme (avaliação manual)

Essas condições devem ser empregadas nos fluxos de trabalho ativados quando uma avaliação manual da inspeção é realizada (Print abaixo). Isso concede ao usuário a capacidade de definir ações específicas com base na classificação de qualidade atribuída manualmente à inspeção.

* + - Propriedades da Ação: Alterar Conformidade do Formulário, informando o novo status: Pendente, Conforme, Não Conforme;
    - Filtrar por tipo de formulário: Pode ser definido o tipo da categoria para a condição:

Após criação do fluxo, utilizando o drag drop, opção de arrastar do mouse, é possível realizar a ligação de um fluxo para o outro, veja;

Ao clicar duas vezes em cima de uma das setas que liga um fluxo ao outro, é possível definir uma **Propriedade da relação entre entidades**que pode ser definida como:

* Indefinido;
* Sim;
* Não;

A criação do fluxo segue algumas regras, veja:

* O **início**só pode ser uma saída (relação entre entidades);
* A **condição** só pode ser duas saídas - sim ou não;
* A **ação**só pode ter uma saída;
* O **fim**não pode ter saídas;

**Tipos de Condições:**

* Condição por pontuação do formulário: 
  + Para questões do tipo "Sim ou Não", "lista suspensa" ou "lista de escolha única" para cada item será habilitada o campo de pontuação e criticidade. Será considerada o item de maior valor para a pontuação da questão.
* Condição por criticidade:
  + A quantidade total de questões que serão consideradas, é a soma de questões que podem ter a criticidade preenchida.

O Workflow será disparado quando a inspeção for finalizada no App. E, caso o formulário não possua workflow associado, o status da inspeção será alterada para "Em avaliação".

**Tipos de ações:**

* Alterar o status de conformidade:
  + Quando a inspeção for finalizada e sincronizada com o sistema via aplicativo, o workflow que estiver associado ao formulário será executado alterando assim o status de conformidade da inspeção para uma das opções configuradas: Conforme, Não Conforme ou Indefinido. Caso no formulário não tenha nenhum workflow associado, o status será alterado para Em Avaliação.
* Criar Inspeção nova:
  + Utilizando o mesmo Formulário ou um Formulário Específico, destinando a um usuário ou a um grupo de usuário, é possível criar novas inspeções segundo o fluxo aplicado para o status da inspeção (finalizado).
* Criar Atendimento no Totvs Aprovações:
  + Esta ação, cria um novo atendimento parametrizado no workflow no Totvs Aprovações.
* Enviar notificação:
  + Esta ação permite que seja enviada uma notificação via Push (no celular) ou via e-mail para um usuário ou grupo contendo uma mensagem de texto livre.
Grupo de Usuários

Após a criação do das Inspeções, será feito o envio da mesma para um usuário ou grupo de usuário no aplicativo para que seja respondida a Inspeção.

Para acessar o cadastro de **Grupo de Usuários**é necessário conceder permissão por usuário.

No portal será possível criar um **Novo Grupo de Usuário.**

As informações contidas nos **Dados Gerais**do grupo serão:

* **Código do Grupo de Usuários;**
* **Nome do Grupo de Usuários;**

Na aba usuários, será possível informar os usuários que irão receber a inspeção no aplicativo para ser respondido.

BIM

**BIM**Assim como no aplicativo, temos no portal o item de menu "BIM" com as mesmas opções conhecidas da funcionalidade:

Dentro do BIM temos a inspeção para mostrar os objetos a serem inspecionados no modelo 3D através do projeto e da tarefa associada a inspeção.

Temos também, a opção de Inspeção, onde podemos buscar as inspeções por:

* Criado em
* Realizado em
* Data inicial e final
* Não avaliado
* Conforme
* Não conforme

Obs: Check-box Adaptativo melhora a visualização de modelos grandes e pesados.

filtro de objeto podemos selecionar todos os objetos referente ao modelo 3D ou selecionar por partes.

Integração com o TOTVS Aprovações e Atendimento

No WorkFlow do Minhas Inspeções, existe a opção de criar um atendimento no TOTVS Aprovações e Atendimento. Recentemente, foi adicionada uma nova funcionalidade que permite que o atendimento criado pelo WorkFlow do Minhas Inspeções se comunique com o próprio aplicativo, informando se uma determinada inspeção está ou não em conformidade, e também dispara um fluxo de trabalho específico no Minhas Inspeções.

**1 Passo: Configurando o TOTVS Aprovações e Atendimento:**

Primeiramente é necessário criar um novo tipo de atendimento e associar o serviço do tipo **27 - Serviços do Minhas Inspeções.**

Agora é preciso criar as etapas necessárias para seu projeto e o fluxo dessas determinadas etapas:

É necessário configurar uma ação no ultimo fluxo de etapa do tipo de atendimento no TAA na aba **Ações Visíveis:**

**2 Passo: Configurando o Portal Minhas Inspeções:**

O primeiro workflow será disparado ao finalizar uma inspeção no aplicativo.  
O segundo workflow será disparado ao realizar a avaliação manual através do portal Minhas Inspeções.  
O terceiro workflow será disparado ao executar uma ação avançando uma etapa no atendimento selecionado no TAA.

Atenção

Para que a integração funcione é necessário que o atendimento do TAA tenha sido criado pelo workflow do Minhas Inspeções, com o mesmo tipo de atendimento criado acima.

[Voltar](https://tdn.totvs.com/pages/viewpage.action?pageId=203766343)
