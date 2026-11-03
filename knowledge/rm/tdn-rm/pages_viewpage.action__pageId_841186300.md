---
content_hash: 8d0b79b1d93d47e18ea2389769c4bc4014f9ed1cfd5f306cb4669d0b38065e26
fetched_at: '2026-06-29T00:11:50.493648+00:00'
page_id: '841186300'
product: rm
source: tdn-rm
title: Diário de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=841186300
version: 41
---

O **Diário de Obra** é uma ferramenta essencial para o gerenciamento eficaz de projetos de construção e obras civis. Ele permite o acompanhamento detalhado do progresso diário, a identificação de problemas em tempo hábil e promove a comunicação eficaz entre as equipes envolvidas.

No TOTVS Construção Obras e Projetos, é possível acessá-lo também através do Portal da Obra, pelo menu lateral:

O Diário da Obra se divide em 5 menus, que serão detalhados nas respectivas abas a seguir:

Diário da ObraFormulários

Assim como no Minhas Inspeções, é possível gerenciar os formulários que serão usados para registro das Anotações do dia, que irão compor o RDO. Dessa maneira, cada tipo de formulário exibirá os respectivos campos a serem preenchidos, conforme necessidade.

O cadastro de um formulário é iniciado no botão Incluir:.

Ao clicar em Incluir, o usuário será direcionado para a tela do Novo Formulário:

Na aba Dados Gerais, deverá informar:

* + **Nome do Formulário:**Nome escolhido para o formulário;
  + **Onde o formulário será aplicado?** Caso a opção selecionada seja **Projeto**, o formulário será aplicado em um projeto, e por isso o usuário que irá preencher a anotação do dia referente ao formulário em questão, deverá informar a que projeto se refere tal anotação. Se **Tarefa**, o formulário será aplicado em uma tarefa a qual será informada no momento que a anotação do dia for respondida;
  + **Roteiro Sequencial:**Caso esteja marcado para utilizar indica que ao responder o questionário não é possível pular perguntas, todas as respostas devem ser respondidas sequencialmente. Caso esteja desmarcado as perguntas do questionário poderão ser respondidas fora de ordem com uma visualização em lista.
  + **Workflows utilizados:** Ao finalizar Anotação do dia, Ao realizar avaliação manual ou disparado no TOTVS Aprovações e Atendimento.

Na aba Itens:

* **Tipo de Item:**É o formato para resposta à pergunta do item em questão. Se data, valor, texto simples, texto formatado...
* **Pergunta:**Texto da pergunta que será visualizado pelo usuário.
* **Item obrigatório:**Caso marcado, o formulário não poderá ser finalizado sem ter essa pergunta respondida.
* **Complementos do Item:**Informações adicionais nas respostas do formulário que também podem ser enviadas. Podem ser obrigatórios ou não
  + **Inserir Evidências:**no momento que o formulário estiver sendo respondido será permitido inserir evidência anexada a resposta do item.
  + **Inserir Observações:**no momento que o formulário estiver sendo respondido será permitido inserir observações anexadas a resposta do item.
* **Questões:**Depois de efetuar o cadastro das questões, elas irão aparecer no canto direito. Ao clicar em uma pergunta, irá habilitar dois botões ou para **Mover para cima** ou para **Mover para a baixo** a determinada questão.
* **Listas:**Se o tipo do item for de lista suspensa ou lista de escolha única, irá ter a opção de alterar a ordem dos itens do mesmo jeito que aparece nas questões, como citado acima.

Para visualizar as questões contidas em cada formulário, basta clicar na respectiva seta, visível no canto direito de cada registro:

Será aberta a visualização do formulário:

Ao selecionar um formulário serão exibidos os botões de **Excluir**, **Editar**. Em processos, será possível transformar em **Rascunho**, **Desativar**, **Clonar** e **Publicar** os formulários cadastrados, dependendo do perfil de acesso do usuário:

* **Formulários Publicados:**Pode ser transformado em rascunho (desde que ainda não tenha sido respondido), ser desativado, ser clonado ou excluído.
* **Formulários Inativos:**Pode ser transformado em publicado, rascunho ou excluído.
* **Formulários Rascunho:**Pode ser publicado, desativado, clonado ou excluído.

Ao clicar em **Gerenciar tabela** o usuário poderá:

* definir quantos registros deseja visualizar por página;
* selecionar quais as colunas deseja visualizar e sua ordenação;
* restaurar a configuração padrão;
* e definir se as colunas poderão ser arrastadas e/ou agrupadas:

IMPORTANTE!

As opções de Assinatura, Código de Barras e QR Code ainda não estão disponíveis para preenchimento no diário de obra; elas serão implementadas posteriormente.

Anotações do dia

As Anotações do dia são os registros diários, feitos para acompanhamento do progresso da obra, clima, registros de problemas, comunicação e etc... dependendo do formulário usado na anotação.

Na visão das Anotações, assim como no cadastro dos Formulários, será possível **Excluir**, **Editar** além das ações de **Ajustar,** **Avaliar** e **Responder**:

IMPORTANTE!

Os botões de **Excluir** e **Editar**, apesar de ficarem visíveis para todos, deverão ser liberados apenas no perfil do usuário Administrador, pois poderão ser usados a qualquer momento, ou seja; para o usuário que tiver esse perfil, será possível editar uma resposta mesmo após a anotação ter sido avaliada ou finalizada, e por isso deve ser liberado apenas em situações muito específicas. O ideal é que o usuário que irá preencher a anotação, faça-a através do processo de **Responder,** ou logo após incluir.

Os status das Anotações são:

**Não avaliado:** Quando a Anotação ainda não foi respondida;

**Aguardando avaliação:** A anotação já foi respondida mas ainda não foi avaliada;

**Conforme:** A anotação foi avaliada como conforme;

**Não conforme:** Após a avaliação, a anotação é considerada não conforme.

Para começar, clique no botão Incluir:

Será direcionado para Criar Anotação do Dia, onde deverá informar:

* **Data de realização:** Virá preenchida com a data do sistema, mas o usuário poderá alterá-la;
* **Projeto:** Virá preenchido com o projeto do contexto, porém o usuário poderá alterá-lo;
* **Formulário:** O formulário que será usado para preenchimento da Anotação, com destaque para a visualização dos Últimos formulários utilizados; um facilitador logo abaixo do campo, que ao clicar, o campo será preenchido automaticamente.

Caso o formulário informado seja aplicado apenas a projeto, o usuário poderá salvar o registro e o mesmo estará disponível para ser respondido:

Caso o formulário seja aplicado a tarefa, será habilitado mais esse campo para que o usuário informe a que tarefa se aplica a anotação antes de salvá-la:

 O usuário poderá salvar e responder ao formulário na sequência, clicando no botão correspondente:

Clicando em salvar e responder, será direcionado para o formulário informado na tela de criação da anotação, onde poderá responder às questões contidas no formulário, salvar o rascunho, ou finalizar a anotação:

Ao finalizar o registro, a Anotação estará disponível para ser avaliada pelo usuário responsável, dependendo o workflow utilizado; e caso utilize esse tipo de validação, será aberta a tela abaixo para que o responsável avalie e finalize a anotação:

Isso fará como que o status da anotação mude para **Conforme** ou **Não conforme** de acordo com a avaliação feita.

**Relatório**

No TOTVS Compartilhamento, foi disponibilizado o relatório do tipo Recursos Smart View TOPREL0077 - Ficha de Verificação(RDO e Minhas Inspeções).TotvsTReports. Este relatório é gerado a partir das Anotações do Dia realizadas, consolidando as respostas fornecidas no formulário de verificação. Cada Anotação do Dia contém uma lista de itens avaliados, incluindo:

* Perguntas do formulário, previamente configuradas.
* Respostas inseridas pelo responsável pela anotação.
* Observações adicionais, quando necessário.
* Anexos (documentos, imagens ou vídeos complementares) com opção de visualização.

**Gerando o relatório utilizando o SmartView:**

Selecione o ID da Ficha na lupa, clique no botão "Enviar" e aguarde a geração do PDF contendo o relatório.

**Exemplo de Relatório**

Abaixo, segue um exemplo do formato gerado:

RDO

A sigla RDO se refere ao Relatório Diário de Obra e traz a compilação de todos os registros feitos no projeto por dia. Ele traz informações não apenas das Anotações do Diário, mas também dos apontamentos de Avanço Físico, Mão de obra, Equipamentos, Inspeções de qualidade e Materiais recebidos.

Para visualização, informe o período, ou data específica, e o projeto. Ao aplicar o filtro, o(s) card(s) contendo o(s) RDO(s) criado(s) no intervalo informado, poderá(ão) ser visualizado(s) conforme tela abaixo:

Importante

* Somente será permitido incluir um RDO por dia em um projeto.
* As opções 'Em Aprovação', 'Aprovado' e 'Reprovado' disponíveis a partir da release 12.1.2510, com integração ao TOTVS Assinatura Eletrônica (TAE); necessitam da mesma parametrização descrita na documentação da .

Para ciar um RDO, basta clicar no sinal  destacado logo abaixo:

Após criado o RDO, é possível visualizá-lo no respectivo card, clicando na opção:

Para isso, foi disponibilizado um recurso do Smart View **TOPREL0076 - Relatorio Diario de Obras-RDO.TotvsTReports**, que pode ser baixado via TOTVS Compartilhamento e deverá ser informado no respectivo .

Um exemplo de RDO pode ser visto logo a seguir, e traz um compilado das Anotações do dia, Avanço Físico, Mão de Obra, Equipamentos, Inspeções e Materiais registrados para o projeto na respectiva data:

   

Caso alguma informação do Diário de Obra seja alterada após a criação do RDO, é possível regerar o mesmo para que o relatório seja atualizado. Basta clicar na opção "Regerar RDO" e em seguida após a confirmação, o novo relatório será gerado.

O RDO criado poderá ser enviado para aprovação através do menu abaixo:

Será exibida a tela seguinte para que seja informado o usuário do TOTVS Assinatura Eletrônica responsável por assinar o relatório. Caso o usuário não apareça na parte inferior da tela, é possível **Adicionar usuário** informando o tipo de envio, demais dados e clicando no botão **Salvar**. Em seguida, ao clicar no botão **Solicitar Assinatura**, o usuário será notificado através do e-mail e direcionado para o site onde poderá visualizar o relatório e assiná-lo.

Após **Solicitar Assinatura** o card do RDO passará para a coluna **Em aprovação:**

E quando assinado, o RDO ficará visível na coluna **Aprovado**:

Workflow 

O workflow definirá o fluxo de trabalho do formulário usado para a Anotação do dia, do Diário da Obra.

Assim como no Minhas Inspeções, durante a criação dos formulários, é necessário definir o fluxo que será usado para as anotações vinculadas a esse formulário. Dependendo das respostas às questões, uma anotação pode ter diversos caminhos a seguir.

No cadastro do workflow é possível criar todo fluxo da Anotação, conforme o exemplo abaixo:

Basta Selecionar a opção de Criar Workflow no Portal, e utilizar as ferramentas de criação.

Será direcionado para tela de cadastro do Workflow cujos campos serão listados na sequência:

* **Nome:**Informe o nome que será dado ao Workflow;
* **Descrição:**Informe a descrição detalhada do Workflow;
* **Início:** Irá determinar o início do fluxo, representada pelo ícone de Circulo Verde;

* **Criar fim:** Da mesma forma, indica o fim para o fluxo, representada pelo ícone de Circulo Vermelho;

* **Criar Condição:**Irá criar uma condição para o fluxo, representada pelo ícone de Losango Amarelo;

* **Criar Ação:**Irá criar uma ação para o fluxo, representada pelo ícone de Quadrado Azul;

* **Excluir:**Selecione um dos ícones representados na tela e clique na opção excluir para excluí-lo;
* **Limpar:**Esta opção exclui todo o fluxo criado;
* **Propriedades:** Abre a Propriedade da condição ou ação selecionada, trazendo opções de Tipo de Condição e Tipo de Ação, esta opção também pode ser acessada com o duplo clique:

Propriedades da Condição: Percentual de Aprovação do Formulário, informando qual o Percentual desejado;

Filtrar por tipo de formulário: Pode ser definido o tipo da categoria para a condição:

É uma funcionalidade empregada quando um mesmo workflow pode ser aplicado a múltiplos tipos de formulários (como Tarefa, Medição de Contrato ou Movimento). Essa opção viabiliza a criação de condições específicas para cada variante de formulário, permitindo uma adaptação mais precisa às particularidades de cada um.

Filtrar por tipo de condição: Inspeção Conforme (avaliação manual) e Inspeção Não Conforme (avaliação manual)

Essas condições devem ser empregadas nos fluxos de trabalho ativados quando uma avaliação manual da anotação é realizada (print abaixo). Isso concede ao usuário a capacidade de definir ações específicas com base na classificação atribuída manualmente à anotação.

Propriedades da Ação: Alterar Conformidade da Anotação, informando o novo status:

Enviar Notificação: Pode ser definido o tipo de formulário:

Após criação do fluxo, utilizando o drag drop, opção de arrastar do mouse, é possível realizar a ligação de um fluxo para o outro, veja;

Ao clicar duas vezes em cima de uma das setas que liga um fluxo ao outro, é possível definir uma **Propriedade da relação entre entidades**que pode ser definida como:

* Indefinido;
* Sim;
* Não;

A criação do fluxo segue algumas regras, veja:

* O **início**só pode ser uma saída (relação entre entidades);
* A **condição** só pode ser duas saídas - sim ou não;
* A **ação**só pode ter uma saída;
* O **fim**não pode ter saídas;

**Tipos de Condições:**

* Condição por pontuação do formulário:
  + Para questões do tipo "Sim ou Não", "lista suspensa" ou "lista de escolha única" para cada item será habilitada o campo de pontuação e criticidade. Será considerada o item de maior valor para a pontuação da questão.
* Condição por criticidade:
  + A quantidade total de questões que serão consideradas, é a soma de questões que podem ter a criticidade preenchida.

O Workflow será disparado quando a anotação for finalizada no App. E, caso o formulário não possua workflow associado, o status da anotação será alterada para "Em avaliação".

**Tipos de ações:**

* Alterar o status de conformidade:
  + Quando a anotação for finalizada, o workflow que estiver associado ao formulário será executado alterando assim o status de conformidade da anotação para uma das opções configuradas: Conforme, Não Conforme ou Indefinido. Caso no formulário não tenha nenhum workflow associado, o status será alterado para Em Avaliação.
* Criar Anotação nova:
  + Utilizando o mesmo Formulário ou um Formulário Específico, destinando a um usuário ou a um grupo de usuário, é possível criar novas anotação segundo o fluxo aplicado para o status da anotação (finalizado).
* Criar Atendimento no Totvs Aprovações:
  + Esta ação, cria um novo atendimento parametrizado no workflow no Totvs Aprovações.
* Enviar notificação:
  + Esta ação permite que seja enviada uma notificação via Push (no celular) ou via e-mail para um usuário ou grupo contendo uma mensagem de texto livre.

Grupo de Usuários

Após a criação da Anotação, será possível enviar uma notificação por e-mail para um usuário ou grupo de usuário para que seja respondida.

Para acessar o cadastro de **Grupo de Usuários** do Diário de Obra,é necessário conceder permissão no perfil do usuário:

No portal será possível criar um **Novo Grupo de Usuário.**

As informações contidas nos **Dados Gerais**do grupo serão:

* **Código do Grupo de Usuários;**
* **Nome do Grupo de Usuários;**

Na aba usuários, será possível informar os usuários que irão receber a inspeção no aplicativo para ser respondido.
