---
content_hash: 9829e1894b7145169247a8806d5dfed348b7d33ce4136d1bf9fe3fc84b8c85c4
fetched_at: '2026-06-28T21:35:31.410969+00:00'
page_id: '919050491'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Atividade de serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=919050491
version: 59
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

3.\*ndice

# Falando de componente Atividade de serviço...

---

O componente **Atividade de serviço** representa um ponto do processo onde será feita uma consulta aos dados de um serviço externo repassando esses dados para o processo.

A principal característica desse componente é sua capacidade de automatizar a execução de tarefas, facilitando a integração com sistemas externos e promovendo a eficiência do processo.

Ao configurar esse componente, é necessário selecionar um serviço já cadastrado na plataforma e editar um *script* JavaScript que fará o acesso aos métodos e dados desse serviço.

Dica!

Os serviços são cadastrados no recurso  do Painel de controle.

Com o uso das APIs hAPI e um formulário, é possível passar os dados obtidos na consulta do serviço para o processo.

Uma atividade de serviço pode ter apenas um fluxo de saída e deve ter um evento intermediário de captura de erro para onde a solicitação será enviada se ocorrer alguma inconsistência na execução do *script*.

Importante!

A etapa posterior à captura de erro não é atribuída automaticamente a quem enviou a solicitação para a etapa correspondente à atividade de serviço. Por isso, é importante definir quem será a pessoa responsável pela etapa de tratamento do erro. Se não for definido um responsável, a etapa é enviada automaticamente para a primeira pessoa encontrada na lista de pessoas com [cadastro](https://tdn.totvs.com/pages/viewpage.action?pageId=234455411) ativo na plataforma em ordem alfabética, mesmo que essa pessoa não tenha nenhuma participação ou envolvimento no processo em questão.

Esse componente permite utilizar dois tipos de execução da consulta aos dados do serviço externo: a execução **Automatizada** e a execução **Imediata**, que são detalhadas a seguir.

#ebecf0

trueExemplo de uso  
Em um processo de **Aprovação de contrato**, o solicitante preenche um formulário solicitando a criação do contrato com informações como o nome do fornecedor, o tipo e o número do contrato, a validade do contrato, dentre outras. Em seguida, o contrato passa por algumas etapas de aprovação e, depois de aprovado, precisa ser armazenado no recurso . É nesse ponto que pode ser incluído o componente atividade de serviço, para que uma pasta seja criada automaticamente para armazenar o contrato e os documentos relacionados.

Desta forma, quando a última etapa de aprovação for concluída, a solicitação seguirá para uma atividade de serviço que, utilizando as APIs da plataforma, criará a pasta no recurso Documentos com base nas informações fornecidas e nas permissões de acesso definidas no formulário, garantindo que a pasta será única para cada contrato.

Um exemplo de código que poderia ser utilizado como *script* na atividade de serviço é:

Importante!

Esse é um exemplo que fica disponível no repositório [SAMPLES](https://git.fluig.com/projects/SAMPLES) e, por isso, ele pode ser atualizado lá a qualquer momento. Para ver sua versão mais recente e sempre atualizada, acesso-o a partir do repositório **[clicando aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/create-advanced-folder/workflow/scripts/sample-create-advanced-folder.servicetask9.js)**.

js

## Execução automatizada

---

A execução automatizada determina que a execução do *script* será feita de forma assíncrona e sem a necessidade de uma interação manual de uma pessoa. Nesse tipo de execução, é possível definir o número de tentativas de execução e uma mensagem de sucesso que será exibida quando a execução for concluída sem inconsistências.

Quando a solicitação chega em uma atividade de serviço com execução automatizada, ela fica parada nesse ponto até que o *scritp* seja executado com sucesso ou até que ele seja executado o número de vezes definido como tentativas de execução.

Se o *script* for executado com sucesso, a atividade de serviço é considerada concluída e a solicitação segue o seu fluxo de saída padrão. Porém, se o número de tentativas for atingido sem que haja uma execução do *script* com sucesso, a solicitação é movimentada para o evento intermediário de captura de erro que, por sua vez, movimentará a solicitação para o fluxo correspondente à etapa de tratamento do erro.

Em atividades de serviço com a forma de execução automatizada, é obrigatório o uso do evento intermediário de captura de erro anexado a ela, bem como um fluxo de saída deste evento, para permitir que o processo seja desviado quando o *script* de integração não for executado com sucesso em nenhuma das tentativas feitas.

O *script* da próxima execução – depois de uma execução com inconsistência – pode receber a quantidade de tentativas de execução e a mensagem da última execução como parâmetros, podendo ser utilizados dentro do *script*. Dessa forma, o *script* ficaria conforme o exemplo abaixo:

js

Tanto a mensagem de sucesso quanto as mensagens de inconsistências são salvas no histórico da solicitação como complementos, podendo ser vistas por quem tiver acesso à solicitação.

trueGreenIndicação de uso  
A execução automatizada deve ser utilizada quando a execução não necessita de um retorno imediato sobre a operação ter sido ou não executada com êxito. Essa execução é mais indicada para integração com serviços que podem ficar indisponíveis ou externos e que, necessariamente, devem ser assíncronos, fornecendo um fluxo de contingência quando a integração não for concluída com sucesso em nenhuma tentativa por qualquer motivo.

O fluxo de contingência é criado anexando um evento intermediário de captura de erro à atividade de serviço (o evento deve ser colocado em cima da atividade). Esse fluxo de saída será utilizando quando todas as tentativas de integração falharem.

## Execução imediata

---

A execução imediata determina que a execução do *script* será feita de forma síncrona, logo depois do evento *afterStateEntry* do processo em questão, ou seja, será executado no momento em que a solicitação chegar na atividade de serviço.

Quando o *script* for executado com sucesso, a solicitação é enviada imediatamente da atividade de serviço para a próxima etapa, dando continuidade ao fluxo de saída padrão. Porém, se ocorrer alguma inconsistência, esta forma de execução apenas retornará a inconsistência encontrada, mantendo a solicitação parada até que uma pessoa interaja na solicitação para averiguar e corrigir as inconsistências que ocorreram.

Esse é um exemplo de código para iniciar a integração com o serviço configurado no componente:

js

trueGreenIndicação de uso  
A execução imediata deve ser utilizada quando a execução necessita de um retorno imediato sobre a operação para que o processo possa seguir adiante.

Nota:

Atualmente, o tipo de execução imediata não é muito recomendado por ter seu desempenho reduzido.

## *Headers* headers

---

No contexto do componente Atividade de serviço, os ***headers*** (cabeçalhos) representam **informações adicionais** ou **metadados** que são enviados junto com a requisição de um serviço. Eles são usados para fornecer contexto ou parâmetros extras que o serviço ou a operação que está sendo chamada pode precisar para processar a requisição.

Os *headers* são frequentemente usados em chamadas de APIs REST ou SOAP e permitem adicionar informações cruciais para a comunicação entre sistemas. Cada chave/valor tem um propósito específico e a definição correta desses *headers* pode ser fundamental para o sucesso da integração com o serviço. Eles permitem personalizar ou configurar as requisições e, muitas vezes, podem ser obrigatórios para que o serviço funcione corretamente.

Esses *headers* podem ser usados para várias finalidades, dependendo do tipo de serviço e da operação. Alguns exemplos comuns de *headers* são:

* **Autenticação e autorização**: pode ser um *token* de autenticação, uma chave de API ou credenciais de um usuário.

  #ebecf0

  ```
  trueExemplo
  ```

  **Chave**: `Authorization`

  **Valor**: `Bearer token_de_acesso`
* **Informações de rastreio**: dados sobre a requisição que podem ser usados para monitoramento ou rastreamento da chamada do serviço.

  #ebecf0

  trueExemplo

  **Chave**: `X-Request-ID`

  **Valor**: `12345`
* **Informações de contexto**: dados que definem o contexto da requisição, tais como o idioma, a localidade ou a versão da API.

  #ebecf0

  trueExemplo

  **Chave**: `Accept-Language`

  **Valor**: `pt-BR`
* **Formato dos dados**: definição sobre como os dados devem ser interpretados ou enviados, como o tipo de conteúdo (*Content-Type*) ou a versão da API.

  #ebecf0

  trueExemplo

  **Chave**: `Content-Type`

  **Valor**: `application/json`

## Parâmetros parametros

---

No contexto do componente Atividade de serviço, os **parâmetros** são **valores** ou **variáveis** que o método/operação precisa receber para funcionar corretamente. Cada método/operação de um serviço geralmente tem uma lista de parâmetros que precisam ser fornecidos para que a execução da ação seja bem-sucedida. Sendo assim, o objetivo de configurar esses parâmetros é fornecer as informações necessárias para que o método/operação seja executado.

Esses parâmetros podem ser de diversos tipos, como números, textos, datas ou até mesmo objetos, que são uma estrutura de dados mais complexa.

#ebecf0

trueExemplo 1  
Ao chamar um método/operação para criar um usuário, é necessário passar o **nome**, o ***e-mail*** e uma **senha** provisória para o novo usuário como parâmetros de entrada.

**Nome**: `Angelina Reek`

***E-mail***: `angelina.reek@email.com`

**Senha**: `senha123@45`

#ebecf0

trueExemplo 2  
Ao chamar um método/operação para criar um pedido de compra, é necessário passar o **identificador (ID)** do cliente, os **itens do pedido** e o **valor total** como parâmetros de entrada.

**ID do cliente**: `78956`

**Itens do pedido**: `monitor; mouse; teclado; fone de ouvido`

**Valor total**: `1800`

Além de fornecer os dados essenciais para a execução do método/operação, outros objetivos da configuração dos parâmetros podem envolver:

* **a definição do contexto da execução**: os parâmetros podem determinar o contexto no qual a operação será executada.

  #ebecf0

  trueExemplo  
  Um parâmetro de "idioma" pode ser usado para alterar o idioma de uma resposta ou para personalizar a resposta do serviço com base na localização do usuário.
* **a comunicação eficiente entre sistemas**: quando diferentes sistemas estão interagindo, é essencial que os parâmetros estejam corretamente configurados para que a comunicação e o entendimento entre eles se estabeleça corretamente.

  #ebecf0

  trueExemplo  
  Se um serviço externo precisa de um código de produto para retornar informações sobre ele, esse código precisa ser passado corretamente como um parâmetro.
* **o mapeamento de dados**: permite mapear valores provenientes de outras etapas do processo.

  #ebecf0

  trueExemplo  
  Um parâmetro pode ser alimentado com o valor presente no formulário do processo preenchido em uma etapa anterior, como um número de pedido ou o ID de um cliente.

Por isso, a configuração dos parâmetros do método/operação é essencial para a correta execução da ação e comunicação entre os sistemas envolvidos.

## Retorno retorno

---

No contexto do componente Atividade de serviço, o **retorno** são os dados que a operação retorna depois de ser executada. Ao chamar um método/operação dentro de uma atividade de serviço, em muitos casos, a operação não só executa uma ação, mas também retorna um ou mais valores que podem ser usados em outras partes do processo. Esse retorno pode ser uma resposta simples – como um código de *status* ou uma mensagem – ou dados mais complexos – como um objeto JSON, uma lista ou um valor calculado.

Quando o método/operação é chamado, ele processa os dados de entrada, que são os . Durante sua execução, o método/operação pode realizar cálculos, consultas a um banco de dados ou algum outro processamento de dados. Depois de processar os parâmetros e realizar suas funções internas, o serviço gera um retorno. Esse retorno pode ser algo simples – como um código de sucesso – ou pode ser um conjunto de dados mais complexo – como o resultado de uma busca ou a confirmação de que uma ação foi realizada.

O retorno do serviço pode ser utilizado de várias formas no processo:

* **de forma condicional**: se o retorno for um código de *status* que indica sucesso ou falha, por exemplo, é possível direcionar o fluxo para diferentes caminhos dependendo do valor desse retorno;

* **como entrada para outras etapas**: pode "alimentar" outra etapa do processo, como o ID de um pedido retornado por um serviço Criar pedido, que pode ser passado para uma etapa/atividade Enviar notificação;

* **ser armazenado para uso futuro**: pode ser armazenado em variáveis ou campos de formulário para ser utilizado em uma fase posterior, como um ID de usuário gerado após sua criação.

Alguns exemplos de retorno de uma operação são:

* **criação de um registro**:

  #ebecf0

  trueExemplo  
  Ao chamar um método/operação para criar o cadastro de um novo usuário, o retorno pode ser o identificador (ID) do usuário gerado pelo sistema.

  **Retorno da execução**: `78956`
* **resposta de sucesso ou falha**:

  #ebecf0

  trueExemplo  
  Em operações simples, o retorno pode ser apenas um *status* – como sucesso ou falha – ou um código que indica o resultado da execução.

  **Retorno da execução**: `sucesso`
* **dados complexos**:

  #ebecf0

  trueExemplo  
  Se o objetivo de uma operação é buscar informações de um usuário, o retorno pode ser um objeto complexo com vários campos.

  **Retorno da execução**: `{ "id": 12345, "nome": "Alonso da Cunha", "email": "alonso.cunha@email.com" }`

* **valor calculado**:

  #ebecf0

  trueExemplo  
  Uma operação pode realizar cálculos e retornar um valor como resultado, como o preço final de um pedido com base em itens, descontos e impostos, onde o retorno pode ser o valor total.

  **Retorno da execução**: `5000`

Dessa forma, o retorno de uma operação é essencial para capturar os resultados de um serviço e usá-los de maneira eficaz dentro do fluxo do processo. Ele pode ser utilizado para tomar decisões, realizar ações subsequentes ou simplesmente para fornecer informações úteis para a continuação do processo.

## Configurar componente Atividade de serviço – REST rest

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade de serviço**  que deseja configurar com um serviço do tipo REST.

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Na aba **Geral**, defina as informações gerais para o componente que representa a execução de um serviço externo.

#f2f2f2#f2f2f2

**Título**  
Nome da etapa que representa a execução de um serviço externo. O nome também pode ser alterado diretamente no componente, clicando sobre seu nome atual e depois em **Editar**– localizado no lado direito.

#ebecf0

trueExemplo de uso  
Em um processo de **Aprovação de contrato**, o componente poderia receber o nome **Criar pasta e armazenar contrato**, visto que ele servirá para criar uma pasta específica para armazenar esse contrato no recurso .

**Selecione o serviço**  
Serviço externo que será utilizado para executar alguma ação. É possível selecionar serviços do tipo **REST** que já existem no recurso  do Painel de controle.

Nota:

Esse campo não é exibido quando o *script* da atividade de serviço foi criado por desenvolvimento, ou seja pelo Fluig Studio ou outra ferramenta externa à plataforma. Neste caso, para acessar as configurações do *script*, clique em **Acessar *script* de integração** – localizado na parte inferior.

**Tipo de execução**  
Forma como a requisição do serviço externo será executada. As opções disponíveis são:

* **Automatizado**: a requisição é executada de forma assíncrona. Deve ser utilizado quando a execução não necessita de um retorno imediato sobre a operação ter sido ou não executada com êxito;

* **Imediato**: a requisição é executada de forma síncrona. Deve ser utilizado quando a execução necessita de um retorno imediato sobre a operação para que o processo possa seguir adiante.

Dica!

Saiba mais sobre os tipos de execução em Integração assíncrona via processos *workflow*.

**Tentativas**  
Número de vezes que o componente deve tentar executar a operação do serviço antes que seja encaminhado para o evento intermediário de captura de erro. Esse campo somente é exibido ao selecionar o tipo de execução **Automatizado**.

**A cada**Intervalo que o componente deve considerar entre uma tentativa e outra de execução. Esse campo somente é exibido ao selecionar o tipo de execução **Automatizado**.

**Frequência**Unidade de tempo que o componente deve considerar para fazer os intervalos e as tentativas de execução. Esse campo somente é exibido ao selecionar o tipo de execução **Automatizado**. As opções disponíveis são:

* **Minuto**;
* **Hora**;
* **Dia**.

#ebecf0

trueExemplo de configuração de tentativas  
→ O componente deve tentar executar o *script* por **10** vezes, tentando **1** vez  a cada **hora**. Sendo assim, a configuração deve ser feita como:

| Tentativas | A cada | Frequência |
| --- | --- | --- |
| 10 | 1 | Hora |

**Mensagem**  
Mensagem que será exibida na conclusão da execução da operação do serviço.

**03.** Clique em **Configurar integração**.

**04.** Na aba **Geral**, defina as informações solicitadas para configurar a execução do serviço.

#f2f2f2#f2f2f2

**Selecione a ação (operação)**  
Método do serviço correspondente à ação que será feita a partir da integração.

**Defina o tempo de resposta**Tempo que a requisição pode aguardar para obter resposta sobre a execução da operação do serviço.

**Ativar conexão segura (SSL)**Quando ativada, determina que a comunicação com o serviço será segura e evitará que terceiros acessem os dados trocados durante a integração.

**05.** Em ***Header***, clique em **Adicionar *header*** para adicionar informações adicionais à requisição do serviço.

#f2f2f2#f2f2f2

Os *headers* ou cabeçalhos são informações adicionais ou metadados que são enviados juntos com a requisição do serviço para que a integração funcione corretamente. Mais detalhes e exemplos podem ser obtidos em *Headers*.

**06.** Informe os dados necessários para cada *header*.

#f2f2f2#f2f2f2

**Chave**  
Chave de identificação do parâmetro.

**Valor**  
Valor que deve ser atribuído ao parâmetro.

#ebecf0

trueExemplo

**Chave**: `Content-Type`

**Valor**: `application/json`

Veja mais exemplos em *Headers*.

Para excluir o *header* adicionado, basta clicar em **Excluir *header*** – localizado no lado direito.

**07.** Clique na aba **Parâmetros** para configurar os parâmetros do método/operação do serviço.

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem ao método/operação que foi selecionado em **Selecione a ação (operação)** na aba **Geral**.

Esses parâmetros são os dados que o método/operação precisa receber para ser executado. Mais detalhes e exemplos podem ser obtidos em .

**08.** Na coluna **Origem do valor** de cada parâmetro, selecione de onde será obtido o valor que será passado para esse parâmetro do método/operação.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Campo de formulário**: quando selecionada, determina que o valor que será passado para o parâmetro será obtido de um campo do formulário do processo. Essa opção somente é exibida quando existe um formulário vinculado ao processo e não é exibida para parâmetros do tipo lista ou objeto;

* **Variável**: quando selecionada, determina que o valor que será passado para o parâmetro será obtido de uma variável padrão existente no contexto do processo. Essa opção não é exibida para parâmetros do tipo lista ou objeto;

* **Nulo**: quando selecionada, determina que nenhum valor será passado para esse parâmetro;

* **Fixo**: quando selecionada, determina que o valor que será passado para o parâmetro é um valor fixo que será informado no componente.

**09.** Na coluna **Valor** de cada parâmetro, selecione ou insira o valor que será passado de acordo com a origem selecionada.

#f2f2f2#f2f2f2

Se a origem selecionada foi:

* **Campo de formulário**: selecione o campo do formulário do processo do qual será obtido o valor que será passado para o parâmetro. São exibidos todos os campos que pertencem ao formulário vinculado ao processo;

  Nota:

  Quando o campo do parâmetro é do tipo byte[] e o dado inserido no campo do formulário for em base64, esse valor será convertido para byte[] na execução do *script*.  
  Para os demais tipos de valor, não será feita nenhuma conversão, ou seja, será considerado o tipo do valor vindo do campo do formulário – numérico, *string*, booleano etc.

* **Variável**: selecione a variável padrão do contexto do processo da qual será obtido o valor que será passado para o parâmetro. As variáveis disponíveis são:
  + WKCompany;
  + WKUser;
  + WKCardId;
  + WKCurrentState;
  + WKDef;
  + WKFormId;
  + WKNextState;
  + WKNumProcess;
  + WKNumState;
  + WKUserComment;

* **Fixo**: informe o valor fixo que será passado para o parâmetro.

**10.** Se um dos parâmetros for do tipo objeto, na coluna **Ação**, clique em **Editar objeto**  para configurar os parâmetros do objeto.

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem ao objeto em questão. É possível configurar todos os parâmetros do objeto da mesma forma que é feito para os demais parâmetros.

Se um dos parâmetros do objeto também for do tipo objeto, é possível configurar seus respectivos parâmetros da mesma forma, clicando em **Editar objeto**  e configurando os respectivos valores para cada parâmetro. E assim sucessivamente para cada parâmetro que for do tipo objeto.

Se um dos parâmetros do objeto for do tipo lista, é possível configurar seus parâmetros clicando em **Adicionar via lista**  e configurando os respectivos valores para cada parâmetro da lista.

**11.** Ao finalizar a configuração dos parâmetros do objeto, clique em **Salvar**, para voltar para a aba **Parâmetros**.

**12.** Se um dos parâmetros for do tipo lista, na coluna **Ação**, clique em **Adicionar via lista**  para adicionar os valores para os parâmetros da lista.

**13.** Clique em **Adicionar valor** .

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem à lista em questão. É possível configurar todos os parâmetros da lista da mesma forma que é feito para os demais parâmetros.

Se um dos parâmetros da lista for do tipo objeto, é possível configurar seus parâmetros clicando em **Editar objeto**  e configurando os respectivos valores para cada parâmetro do objeto. E assim sucessivamente para cada parâmetro que for do tipo objeto.

Para excluir um valor adicionado, basta clicar em **Excluir** – localizado na coluna **Ação**.

**14.** Ao finalizar a configuração dos parâmetros da lista, clique em **Salvar**, para voltar para a aba **Parâmetros**.

**15.** Para os tipos de parâmetros Objeto ou Map, é possível adicionar atributos clicando em **Adicionar atributos**  – localizado ao lado do parâmetro.

**16.** Clique em **Adicionar atributos** .

**17.** Na coluna **Chave**, insira uma chave para identificar o atributo.

**18.** Na coluna **Atribuição**, selecione como será a atribuição de valor para o atributo.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Campo de formulário**: quando selecionada, determina que o valor para esse atributo será obtido de um campo do formulário do processo. Essa opção somente é exibida quando existe um formulário vinculado ao processo;

* **Variável**: quando selecionada, determina que o valor para esse atributo será obtido de uma variável padrão existente no contexto do processo;

* **Fixo**: quando selecionada, determina que o valor para esse atributo é um valor fixo que será informado no componente.

**19.** Na coluna **Valor**, selecione ou insira o valor para o atributo de acordo com a origem selecionada.

#f2f2f2#f2f2f2

Se a origem selecionada foi:

* **Campo de formulário**: selecione o campo do formulário do processo do qual será obtido o valor para o atributo. São exibidos todos os campos que pertencem ao formulário vinculado ao processo;

  Nota:

  Quando o campo do parâmetro é do tipo byte[] e o dado inserido no campo do formulário for em base64, esse valor será convertido para byte[] na execução do *script*.  
  Para os demais tipos de valor, não será feita nenhuma conversão, ou seja, será considerado o tipo do valor vindo do campo do formulário – numérico, *string*, booleano etc.

* **Variável**: selecione a variável padrão do contexto do processo da qual será obtido o valor para o atributo. As variáveis disponíveis são:
  + WKCompany;
  + WKUser;
  + WKCardId;
  + WKCurrentState;
  + WKDef;
  + WKFormId;
  + WKNextState;
  + WKNumProcess;
  + WKNumState;
  + WKUserComment;

* **Fixo**: informe o valor fixo para o atributo.

**20.** Ao finalizar a configuração dos atributos, clique em **Salvar** até voltar para a aba **Parâmetros**.

**21.** Clique na aba **Retorno** para configurar o destino dos dados retornados pelo método/operação.

#f2f2f2#f2f2f2

Os dados de retorno exibidos são os que pertencem ao método/operação que foi selecionado em **Selecione a ação (operação)** na aba **Geral**.

Eles são os dados que a operação retorna depois de ser executada. Mais detalhes e exemplos podem ser obtidos em .

**22.** Na coluna **Atribuição** de cada retorno, selecione para onde o dado retornado pelo método/operação deve ser enviado ou armazenado para ser usado no processo.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Descartar**: quando selecionada, determina que o valor que será retornado por esse parâmetro do método/operação não será utilizado em nenhum momento no processo e, por isso, pode ser descartado. Essa opção somente é exibida quando existe um formulário vinculado ao processo;

* **Formulário**: quando selecionada, determina que o valor que será retornado por esse parâmetro do método/operação deve ser armazenado em um campo do formulário do processo. Essa opção somente é exibida quando existe um formulário vinculado ao processo.

**23.** Na coluna **Valor** de cada retorno, defina onde o dado retornado deve ser armazenado ou utilizado, de acordo com o destino selecionado.

#f2f2f2#f2f2f2

Se o destino selecionado foi:

* **Formulário**: selecione o campo do formulário do processo no qual o valor retornado pelo método/operação deve ser armazenado. São exibidos todos os campos que pertencem ao formulário vinculado ao processo.

**24.** Se um dos parâmetros de retorno for do tipo complexo, como objeto ou lista, na coluna **Ação**, clique em **Editar objeto**  para configurar o destino dos valores de retorno.

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem ao objeto retornado em questão. É possível configurar todos os parâmetros do objeto retornado da mesma forma que é feito para os demais parâmetros de retorno.

Se um dos parâmetros do objeto retornado também for do tipo complexo, como objeto ou lista, é possível configurar seus respectivos parâmetros da mesma forma, clicando em **Editar objeto** . E assim sucessivamente para cada parâmetro do objeto retornado que for do tipo complexo, como objeto ou lista.

**25.** Ao finalizar a configuração dos parâmetros do objeto retornado, clique em **Salvar**, para voltar para a aba **Retorno**.

**26.** Clique em **Salvar** para salvar todas as configurações feitas para o serviço, operação, parâmetros e retorno.

**27.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Atividade de serviço**.

**28.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar componente Atividade de serviço – SOAP soap

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade de serviço**  que deseja configurar com um serviço do tipo SOAP.

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Na aba **Geral**, defina as informações gerais para o componente que representa a execução de um serviço externo.

#f2f2f2#f2f2f2

**Título**  
Nome da etapa que representa a execução de um serviço externo. O nome também pode ser alterado diretamente no componente, clicando sobre seu nome atual e depois em **Editar**– localizado no lado direito.

#ebecf0

trueExemplo de uso  
Em um processo de **Aprovação de crédito**, o componente poderia receber o nome **Consultar crédito**, visto que ele servirá para consultar o serviço de crédito do cliente para que a compra liberada.

**Selecione o serviço**  
Serviço externo que será utilizado para executar alguma ação. É possível selecionar serviços do tipo **SOAP**que já existem no recurso  do Painel de controle.

Nota:

Esse campo não é exibido quando o *script* da atividade de serviço foi criado por desenvolvimento, ou seja pelo Fluig Studio ou outra ferramenta externa à plataforma. Neste caso, para acessar as configurações do *script*, clique em **Acessar *script* de integração** – localizado na parte inferior.

**Tipo de execução**  
Forma como a requisição do serviço externo será executada. As opções disponíveis são:

* **Automatizado**: a requisição é executada de forma assíncrona. Deve ser utilizado quando a execução não necessita de um retorno imediato sobre a operação ter sido ou não executada com êxito;

* **Imediato**: a requisição é executada de forma síncrona. Deve ser utilizado quando a execução necessita de um retorno imediato sobre a operação para que o processo possa seguir adiante.

Dica!

Saiba mais sobre os tipos de execução em Integração assíncrona via processos *workflow*.

**Tentativas**  
Número de vezes que o componente deve tentar executar a operação do serviço antes que seja encaminhado para o evento intermediário de captura de erro. Esse campo somente é exibido ao selecionar o tipo de execução **Automatizado**.

**A cada**Intervalo que o componente deve considerar entre uma tentativa e outra de execução. Esse campo somente é exibido ao selecionar o tipo de execução **Automatizado**.

**Frequência**Unidade de tempo que o componente deve considerar para fazer os intervalos e as tentativas de execução. Esse campo somente é exibido ao selecionar o tipo de execução **Automatizado**. As opções disponíveis são:

* **Minuto**;
* **Hora**;
* **Dia**.

#ebecf0

trueExemplo de configuração de tentativas  
→ O componente deve tentar executar o *script* por **10** vezes, tentando **1** vez  a cada **hora**. Sendo assim, a configuração deve ser feita como:

| Tentativas | A cada | Frequência |
| --- | --- | --- |
| 10 | 1 | Hora |

**Mensagem**  
Mensagem que será exibida na conclusão da execução da operação do serviço.

**03.** Clique em **Configurar integração**.

**04.** Na aba **Geral**, defina as informações solicitadas para configurar a execução do serviço.

#f2f2f2#f2f2f2

**Selecione a ação (operação)**  
Método do serviço correspondente à ação que será feita a partir da integração.

**Defina o tempo de resposta**Tempo que a requisição pode aguardar para obter resposta sobre a execução da operação do serviço.

**Ativar conexão segura (SSL)**Quando ativada, determina que a comunicação com o serviço será segura e evitará que terceiros acessem os dados trocados durante a integração.

**Ativar *Chunking***  
Quando ativada, determina que a resposta do serviço será dividida em partes menores, evitando que o processo fique pesado ou apresente inconsistências.

**05.** Em ***Header***, clique em **Adicionar *header*** para adicionar informações adicionais à requisição do serviço.

#f2f2f2#f2f2f2

Os *headers* ou cabeçalhos são informações adicionais ou metadados que são enviados juntos com a requisição do serviço para que a integração funcione corretamente. Mais detalhes e exemplos podem ser obtidos em *Headers*.

**06.** Informe os dados necessários para cada *header*.

#f2f2f2#f2f2f2

**Nome do *header***  
Nome para identificação do *header* que será adicionado.

**Objeto**  
Objeto do serviço que possui informações que precisam ser enviadas junto com a requisição. São exibidos para seleção apenas os objetos que possuem campos.

**07.** Na coluna **Valor** de cada propriedade do objeto, insira o valor que será enviado para essa propriedade na requisição do serviço.

**08.** Ao finalizar a configuração das propriedades do objeto do *header*, clique em **Salvar**.

#f2f2f2#f2f2f2

Para editar as configurações do *header* adicionado, basta clicar em **Editar *header*** – localizado no lado direito.

Também é possível excluir o *header* adicionado clicando em **Excluir *header*** .

**09.** Clique na aba **Parâmetros** para configurar os parâmetros do método/operação do serviço.

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem ao método/operação que foi selecionado em **Selecione a ação (operação)** na aba **Geral**.

Esses parâmetros são os dados que o método/operação precisa receber para ser executado. Mais detalhes e exemplos podem ser obtidos em .

**10.** Na coluna **Origem do valor** de cada parâmetro, selecione de onde será obtido o valor que será passado para esse parâmetro do método/operação.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Campo de formulário**: quando selecionada, determina que o valor que será passado para o parâmetro será obtido de um campo do formulário do processo. Essa opção somente é exibida quando existe um formulário vinculado ao processo e não é exibida para parâmetros do tipo lista ou objeto;

* **Variável**: quando selecionada, determina que o valor que será passado para o parâmetro será obtido de uma variável padrão existente no contexto do processo. Essa opção não é exibida para parâmetros do tipo lista ou objeto;

* **Nulo**: quando selecionada, determina que nenhum valor será passado para esse parâmetro;

* **Fixo**: quando selecionada, determina que o valor que será passado para o parâmetro é um valor fixo que será informado no componente.

**11.** Na coluna **Valor** de cada parâmetro, selecione ou insira o valor que será passado de acordo com a origem selecionada.

#f2f2f2#f2f2f2

Se a origem selecionada foi:

* **Campo de formulário**: selecione o campo do formulário do processo do qual será obtido o valor que será passado para o parâmetro. São exibidos todos os campos que pertencem ao formulário vinculado ao processo;

  Nota:

  Quando o campo do parâmetro é do tipo byte[] e o dado inserido no campo do formulário for em base64, esse valor será convertido para byte[] na execução do *script*.  
  Para os demais tipos de valor, não será feita nenhuma conversão, ou seja, será considerado o tipo do valor vindo do campo do formulário – numérico, *string*, booleano etc.

* **Variável**: selecione a variável padrão do contexto do processo da qual será obtido o valor que será passado para o parâmetro. As variáveis disponíveis são:
  + WKCompany;
  + WKUser;
  + WKCardId;
  + WKCurrentState;
  + WKDef;
  + WKFormId;
  + WKNextState;
  + WKNumProcess;
  + WKNumState;
  + WKUserComment;

* **Fixo**: informe o valor fixo que será passado para o parâmetro.

**12.** Se um dos parâmetros for do tipo objeto, na coluna **Ação**, clique em **Editar objeto**  para configurar os parâmetros do objeto.

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem ao objeto em questão. É possível configurar todos os parâmetros do objeto da mesma forma que é feito para os demais parâmetros.

Se um dos parâmetros do objeto também for do tipo objeto, é possível configurar seus respectivos parâmetros da mesma forma, clicando em **Editar objeto**  e configurando os respectivos valores para cada parâmetro. E assim sucessivamente para cada parâmetro que for do tipo objeto.

Se um dos parâmetros do objeto for do tipo lista, é possível configurar seus parâmetros clicando em **Adicionar via lista**  e configurando os respectivos valores para cada parâmetro da lista.

**13.** Ao finalizar a configuração dos parâmetros do objeto, clique em **Salvar**, para voltar para a aba **Parâmetros**.

**14.** Se um dos parâmetros for do tipo lista, na coluna **Ação**, clique em **Adicionar via lista**  para adicionar os valores para os parâmetros da lista.

**15.** Clique em **Adicionar valor** .

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem à lista em questão. É possível configurar todos os parâmetros da lista da mesma forma que é feito para os demais parâmetros.

Se um dos parâmetros da lista for do tipo objeto, é possível configurar seus parâmetros clicando em **Editar objeto**  e configurando os respectivos valores para cada parâmetro do objeto. E assim sucessivamente para cada parâmetro que for do tipo objeto.

Para excluir um valor adicionado, basta clicar em **Excluir** – localizado na coluna **Ação**.

**16.** Ao finalizar a configuração dos parâmetros da lista, clique em **Salvar**, para voltar para a aba **Parâmetros**.

**17.** Para os tipos de parâmetros Objeto ou Map, é possível adicionar atributos clicando em **Adicionar atributos**  – localizado ao lado do parâmetro.

**18.** Clique em **Adicionar atributos** .

**19.** Na coluna **Chave**, insira uma chave para identificar o atributo.

**20.** Na coluna **Atribuição**, selecione como será a atribuição de valor para o atributo.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Campo de formulário**: quando selecionada, determina que o valor para esse atributo será obtido de um campo do formulário do processo. Essa opção somente é exibida quando existe um formulário vinculado ao processo;

* **Variável**: quando selecionada, determina que o valor para esse atributo será obtido de uma variável padrão existente no contexto do processo;

* **Fixo**: quando selecionada, determina que o valor para esse atributo é um valor fixo que será informado no componente.

**21.** Na coluna **Valor**, selecione ou insira o valor para o atributo de acordo com a origem selecionada.

#f2f2f2#f2f2f2

Se a origem selecionada foi:

* **Campo de formulário**: selecione o campo do formulário do processo do qual será obtido o valor para o atributo. São exibidos todos os campos que pertencem ao formulário vinculado ao processo;

  Nota:

  Quando o campo do parâmetro é do tipo byte[] e o dado inserido no campo do formulário for em base64, esse valor será convertido para byte[] na execução do *script*.  
  Para os demais tipos de valor, não será feita nenhuma conversão, ou seja, será considerado o tipo do valor vindo do campo do formulário – numérico, *string*, booleano etc.

* **Variável**: selecione a variável padrão do contexto do processo da qual será obtido o valor para o atributo. As variáveis disponíveis são:
  + WKCompany;
  + WKUser;
  + WKCardId;
  + WKCurrentState;
  + WKDef;
  + WKFormId;
  + WKNextState;
  + WKNumProcess;
  + WKNumState;
  + WKUserComment;

* **Fixo**: informe o valor fixo para o atributo.

**22.** Ao finalizar a configuração dos atributos, clique em **Salvar** até voltar para a aba **Parâmetros**.

**23.** Clique na aba **Retorno** para configurar o destino dos dados retornados pelo método/operação.

#f2f2f2#f2f2f2

Os dados de retorno exibidos são os que pertencem ao método/operação que foi selecionado em **Selecione a ação (operação)** na aba **Geral**.

Eles são os dados que a operação retorna depois de ser executada. Mais detalhes e exemplos podem ser obtidos em .

**24.** Na coluna **Atribuição** de cada retorno, selecione para onde o dado retornado pelo método/operação deve ser enviado ou armazenado para ser usado no processo.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Descartar**: quando selecionada, determina que o valor que será retornado por esse parâmetro do método/operação não será utilizado em nenhum momento no processo e, por isso, pode ser descartado. Essa opção somente é exibida quando existe um formulário vinculado ao processo;

* **Formulário**: quando selecionada, determina que o valor que será retornado por esse parâmetro do método/operação deve ser armazenado em um campo do formulário do processo. Essa opção somente é exibida quando existe um formulário vinculado ao processo.

**25.** Na coluna **Valor** de cada retorno, defina onde o dado retornado deve ser armazenado ou utilizado, de acordo com o destino selecionado.

#f2f2f2#f2f2f2

Se o destino selecionado foi:

* **Formulário**: selecione o campo do formulário do processo no qual o valor retornado pelo método/operação deve ser armazenado. São exibidos todos os campos que pertencem ao formulário vinculado ao processo.

**26.** Se um dos parâmetros de retorno for do tipo complexo, como objeto ou lista, na coluna **Ação**, clique em **Editar objeto**  para configurar o destino dos valores de retorno.

#f2f2f2#f2f2f2

Os parâmetros exibidos são os que pertencem ao objeto retornado em questão. É possível configurar todos os parâmetros do objeto retornado da mesma forma que é feito para os demais parâmetros de retorno.

Se um dos parâmetros do objeto retornado também for do tipo complexo, como objeto ou lista, é possível configurar seus respectivos parâmetros da mesma forma, clicando em **Editar objeto** . E assim sucessivamente para cada parâmetro do objeto retornado que for do tipo complexo, como objeto ou lista.

**27.** Ao finalizar a configuração dos parâmetros do objeto retornado, clique em **Salvar**, para voltar para a aba **Retorno**.

**28.** Clique em **Salvar** para salvar todas as configurações feitas para o serviço, operação, parâmetros e retorno.

**29.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Atividade de serviço**.

**30.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar integração

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade de serviço**  para o qual deseja configurar a integração depois de selecionar o serviço desejado.

**02.** Clique em **Configurar integração**.

**03.** Defina as configurações desejadas para a integração nas abas **Geral**, **Parâmetros** e **Retorno**, de acordo com o tipo de serviço selecionado.

#f2f2f2#f2f2f2

Obtenha informações detalhadas sobre as opções disponíveis de configuração para cada serviço em  e .

**04.** Depois de definir todas as configurações desejadas em cada aba, clique em **Salvar**.

**05.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Atividade de serviço**.

**06.** Na mensagem exibida, clique em **Ok, entendi**.

### Editar integração

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade de serviço**  para o qual deseja editar as configurações da integração.

**02.** Clique em **Editar**  – localizado no quadro da integração configurada.

**03.** Edite as configurações desejadas para a integração nas abas **Geral**, **Parâmetros** e **Retorno**, de acordo com o tipo de serviço selecionado.

#f2f2f2#f2f2f2

Obtenha informações detalhadas sobre as opções disponíveis de configuração para cada serviço em  e .

**04.** Depois de editar todas as configurações desejadas em cada aba, clique em **Salvar**.

**05.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Atividade de serviço**.

**06.** Na mensagem exibida, clique em **Ok, entendi**.

### Excluir integração

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade de serviço**  do qual deseja excluir a integração configurada.

**02.** Clique em **Excluir**  – localizado no quadro da integração configurada.

**03.** Na mensagem exibida, clique em **Excluir** para confirmar a exclusão da integração.

**04.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Atividade de serviço**.

**05.** Na mensagem exibida, clique em **Ok, entendi**.

## Dúvidas frequentes

---

Confira aqui algumas dúvidas frequentes sobre o componente Atividade de serviço.

(function() {
function toggleAreas(isExpand, $parent) {
var $items = $parent.find('.panel');
$.each($items, function(idx, el) {
var $arrow = $(el).find('span.cloakToggle').find('span');
var $content = $(el).find('span.cloak');
if (isExpand) {
$arrow.removeClass('cloakDefaultOpen').addClass('cloakDefaultClose');
$content.show();
} else {
$arrow.addClass('cloakDefaultOpen').removeClass('cloakDefaultClose');
$content.hide();
}
});
}
$(document).on('click', '#toggleAll-3', function(ev) {
ev.preventDefault();
var isExpand = $(this).data('expand');
var $parent = $(this).nextAll('.sectionColumnWrapper').first();
toggleAreas(isExpand, $parent);
$(this).data('expand', !isExpand);
});
})();
[Abrir/fechar todas as dúvidas](#)]]>#ebecf0

#### @saiba-mais-1 Quando se deve usar uma atividade de serviço?

@saiba-mais-1

---

A atividade de serviço é indicada quando o processo depende de dados externos oriundos de uma ação automatizada que pode ser executada sem a necessidade de interação direta de uma pessoa, tais como uma consulta a um banco de dados, uma chamada a uma API externa ou um cálculo automatizado.

#ebecf0

#### @saiba-mais-2 Qual é a diferença da atividade de serviço e o evento de mensagem?

@saiba-mais-2

---

A principal diferença entre esses dois componentes é o papel de cada um. Enquanto a atividade de serviço executa uma ação específica – como uma consulta a um sistema externos – o evento de mensagem envia ou recebe uma mensagem durante o andamento do processo, o que pode desencadear uma ação em outro processo ou sistema.

Sendo assim, pode-se dizer que o evento de mensagem é mais voltado para a comunicação entre processos ou sistemas e a atividade de serviço tem como objetivo automatizar uma ação dentro do processo.

#ebecf0

#### @saiba-mais-3 O que acontece se uma atividade de serviço falhar ou gerar um erro?

@saiba-mais-3

---

Se a atividade de serviço foi configurada com a execução **automatizada**, é obrigatório que ela contenha um evento intermediário de captura de erro e um fluxo alternativo para onde a solicitação será direcionada em caso de falhas. Desta forma, quando a execução da atividade de serviço falhar, a solicitação será direcionada para o evento de captura de erro e, posteriormente, para o fluxo alternativo que direciona para uma etapa de tratamento da falha. Depois que a falha for solucionada, a solicitação volta para a atividade de serviço de origem e, assim que ela for executada com sucesso, segue o fluxo principal de saída.

Se a atividade de serviço foi configurada com a execução **imediata**, quando o *script* for executado com sucesso, a solicitação é enviada imediatamente da atividade de serviço para a próxima etapa, dando continuidade ao fluxo de saída padrão. Porém, se ocorrer alguma inconsistência, ela apenas retornará a inconsistência encontrada, mantendo a solicitação parada até que uma pessoa interaja na solicitação para averiguar e corrigir as inconsistências que ocorreram.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
