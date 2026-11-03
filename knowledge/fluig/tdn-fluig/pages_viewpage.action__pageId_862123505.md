---
content_hash: cb05ad5afdbee28a5133ebbfde2fab54088c54a1b4c32a374b9546f1145c7499
fetched_at: '2026-06-28T21:35:30.905523+00:00'
page_id: '862123505'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Atividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862123505
version: 80
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

75%

5.\*ndice

25%

trueIdioma

# Falando de componente Atividade...

---

O componente **Atividade** é a unidade básica de separação de um processo em etapas, ou seja, uma atividade comum. Ele indica que uma tarefa ou ação deve ser realizada nesta etapa do fluxo do processo.

É uma etapa que precisa ser executada por uma pessoa para que a solicitação possa ser enviada adiante.

A definição de quem pode executar essa etapa do processo é feita por meio do mecanismo de atribuição do componente.

Nesse componente, também é possível configurar algumas características gerais, definir regras de anexo, prazo para conclusão, dentre outras características.

## Ver *tour* guiado do componente Atividade

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade** .

**02.** Na lateral direita, onde foram exibidas as configurações do componente, clique em  **Guia de uso** – localizado na parte inferior.

**03.** Veja a apresentação do recurso destacado.

**04.** Clique em **Próximo** para seguir para a apresentação do próximo recurso.

#f2f2f2#f2f2f2

Quando há recursos anteriores, é possível clicar em **Voltar** para revê-los.

**05.** Ao finalizar o *tour* guiado, clique em **Concluir**.

#f2f2f2#f2f2f2

Se desejar, é possível clicar em **Voltar** para rever os recursos anteriores antes de concluir.

## Configurar componente Atividade

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade**  que deseja configurar.

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Na aba **Geral**, defina as informações gerais para o componente que representa uma etapa do processo.

#f2f2f2#f2f2f2

**Título**  
Nome da etapa ou atividade do processo. O nome também pode ser alterado diretamente no componente, clicando sobre ele e depois em **Editar**– localizado no canto superior direito.

#ebecf0

trueExemplo de uso  
Em um processo de **Solicitação de férias**, essa etapa poderia receber o nome **Aprovar férias** e ser de responsabilidade de um gestor.

**Instruções para atividade**  
Instruções que visam facilitar o entendimento de quem vai executar essa etapa, tais como dados que precisam ser informados para agilizar o entendimento e resolução da solicitação. As instruções são exibidas na aba **Informações** da solicitação.

Dica!

Ao preparar as instruções de uma etapa, é comum precisar buscar informações de outros documentos ou *sites*. A plataforma possui o conceito de *hiperlink*, que permite incluir um documento de instruções armazenado no recurso , evitando a replicação de informações e facilitando a navegação. Para isso, basta utilizar o formato **[WD:codigodoc]**, substituindo **codigodoc** pelo código numérico do documento.

**Solicitar senha**  
Quando ativada, determina que o responsável precisa informar sua senha no momento de executar essa etapa. Se a senha estiver incorreta, é permitido que o solicitante a informe quantas vezes forem necessárias. A solicitação somente poderá ser enviada para a próxima etapa quando a senha for informada corretamente. A confirmação da senha fica registrada no histórico da solicitação. Se a opção **Confirmar senha** da aba **Segurança** das [configurações](https://tdn.totvs.com/pages/viewpage.action?pageId=860245005#Plataforma%E2%9D%99Editordeprocesso-Definirop%C3%A7%C3%B5esdeseguran%C3%A7aparaoprocessoseguran%C3%A7a-processo) do processo já estiver ativada, essa opção estará desabilitada.

Nota:

Etapas configuradas para solicitar a senha não podem ser automatizadas por *Web services*.

**Transferir responsável**  
Quando ativada, determina que é possível transferir a responsabilidade por executar essa etapa para outra pessoa.

**03.** Clique na aba **Atribuição** e defina como deve ser a atribuição do responsável pela solicitação quando ela chegar nessa etapa.

#f2f2f2#f2f2f2

**Tipo de atribuição**  
Como deve ser feita a definição do responsável por essa etapa do processo, ou seja, quem pode receber essa etapa quando a solicitação for movimentada para ela. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode receber e executar essa etapa, ou seja, ao movimentar a solicitação para essa etapa, é possível selecionar qualquer pessoa existente na plataforma para recebê-la.

* **Grupo específico**: quando selecionada, determina que apenas as pessoas de um grupo específico podem receber e executar essa etapa. É possível definir se a etapa será individual – executada por uma única pessoa do grupo – ou se ela será conjunta – executada por mais de uma pessoa do grupo. Essa definição é feita selecionando uma das opções Atividade individual ou Atividade conjunta.

* **Papel específico**: quando selecionada, determina que apenas as pessoas que exercem um papel específico podem receber e executar essa etapa. É possível definir se a etapa será individual – executada por uma única pessoa que exerce esse papel – ou se ela será conjunta – executada por mais de uma pessoa que exerce papel. Essa definição é feita selecionando uma das opções Atividade individual ou Atividade conjunta.

* **Campo de formulário**: quando selecionada, determina que apenas a pessoa informada em um campo do formulário da solicitação em alguma etapa anterior pode receber e executar essa etapa, ou seja, ao movimentar a solicitação para essa etapa, ela será enviada automaticamente para essa pessoa.

* **Pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode receber e executar essa etapa, ou seja, ao movimentar a solicitação para essa etapa, ela será enviada automaticamente para essa pessoa.

  Nota:

  Se essa pessoa for inativada em algum momento, somente o gestor do processo poderá movimentar a solicitação em seu lugar.

**Grupo específico**  
Grupo específico de pessoas que podem receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Grupo específico em Tipo de atribuição. Para ver as pessoas que fazem parte do grupo selecionado, basta clicar em **Visualizar**  e, para remover o grupo selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do grupo.

**Papel específico**  
Papel específico exercido pelas pessoas que podem receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Papel específico em Tipo de atribuição. Para ver as pessoas que exercem o papel selecionado, basta clicar em **Visualizar**  e, para remover o papel selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do papel.

**Selecione um campo**  
Campo do formulário no qual foi informada a pessoa que pode receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Campo de formulário em Tipo de atribuição. Para remover o campo selecionado, basta clicar em **Remover**  – localizado no lado direito do nome do campo.

**Pessoa específica**  
Pessoa específica que pode receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Pessoa específica em Tipo de atribuição. Para remover a pessoa selecionada, basta clicar em **Remover**  – localizado no lado direito do nome da pessoa.

**04.** Ainda na aba **Atribuição**, se o tipo de atribuição escolhido foi **Grupo específico** ou **Papel específico**, defina como deve ser a execução dessa etapa, se individual ou conjunta.

#f2f2f2#f2f2f2

**Atividade individual**Quando selecionada, determina que a etapa deve ser executada por uma única pessoa. Neste caso, é possível definir se apenas uma pessoa do grupo ou que exerce o papel pode ser selecionada para receber a solicitação quando ela for movimentada ou se a solicitação deve ser enviada para todas as pessoas do grupo ou que exercem o papel e a primeira que a assumir se torna a responsável por executar essa etapa. Essa opção somente é exibida quando o tipo de atribuição escolhido for Grupo específico ou Papel específico.

**Atividade conjunta conjunta**Quando selecionada, determina que a etapa deve ser executada por mais de uma pessoa. Desta forma, somente será possível concluir a etapa e movimentar a solicitação para a próxima quando o percentual de consenso de conclusão definido for atingido. Essa opção também permite definir se várias pessoas do grupo ou que exercem o papel podem ser selecionadas para receber a solicitação quando ela for movimentada ou se a solicitação deve ser enviada para todas as pessoas do grupo ou que exercem o papel para que possa ser executada por quaisquer pessoas até que o percentual de consenso seja atingido. Essa opção somente é exibida quando o tipo de atribuição escolhido for Grupo específico ou Papel específico.

**Movimentação da atividade**  
Como deve ser a definição do responsável pela etapa quando a solicitação for movimentada para ela, de acordo com a forma de execução escolhida: individual ou conjunta.  
Para atividade **individual**, as opções disponíveis são:

* **Seleção de uma pessoa do grupo**: quando selecionada, determina que será necessário selecionar uma pessoa do grupo ou do papel ao movimentar a solicitação para essa etapa.

* **Envio para todos do grupo/papel (*pool*)**: quando selecionada, determina que ao movimentar a solicitação para essa etapa, ela será automaticamente enviada para todas as pessoas do grupo ou que exercem o papel e a primeira que a assumir se torna a responsável por executar essa etapa.

Para atividade **conjunta**, as opções disponíveis são:

* **Seleção de múltiplas pessoas**: quando selecionada, determina que será necessário selecionar mais de uma pessoa do grupo ou que exerce o papel ao movimentar a solicitação para essa etapa.

* **Atribuição para todos do grupo/papel**: quando selecionada, determina que ao movimentar a solicitação para essa etapa, ela será automaticamente enviada para todas as pessoas do grupo ou que exercem o papel para que a etapa possa ser executada por quaisquer pessoas até que o percentual de consenso seja atingido.

**Consenso para conclusão**  
Percentual de consenso que é necessário atingir para que a etapa seja considerada concluída, ou seja, percentual de pessoas que devem assumir a etapa e tomar a mesma decisão para que a solicitação possa ser movimentada para a próxima. Por padrão, o consenso é definido em 100%. Esse campo somente é exibido ao selecionar a opção Atividade conjunta.

**05.** Em **Acompanhamento**, assinale as opções que representam quem deve ser notificado quando a solicitação chegar ou sair dessa etapa.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início dessa etapa será enviada ao responsável por ela.

* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre o início dessa etapa será enviada ao solicitante.

* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início dessa etapa será enviada ao gestor do processo.

Importante!

Independentemente das opções assinaladas, a notificação não é enviada para quem realizou a ação.

#ebecf0

trueExemplo 1  
Uma pessoa movimenta a solicitação para uma etapa na qual ela mesma é a responsável. Mesmo que a opção **Notificar responsável** esteja assinalada, ela não receberá a notificação, visto que a ação foi feita por ela mesma.

#ebecf0

trueExemplo 2  
O gestor do processo movimenta a solicitação (como responsável ou gestor) para uma etapa na qual a opção **Notificar gestor** está assinalada. Neste caso, ele não receberá a notificação, apenas os outros gestores do processo receberão.

O mesmo ocorre para todos os tipos de notificação, incluindo a de substituto.

#ebecf0

trueExemplo  
Se a pessoa A é substituta da pessoa B e movimenta a solicitação para uma etapa onde a pessoa B é responsável, a pessoa A (substituta) não será notificada. Apenas a pessoa B e outras pessoas substitutas dela serão notificadas.

Nota:

As notificações podem ser enviadas na  ou por *e-mail*, dependendo de como foi feita a  das opções de envio no perfil pessoal, bem como quais opções estão disponíveis para uso na empresa, que podem ter sido configuradas de forma  – para todas as empresas – ou por .

**06.** Clique na aba **Prazo** e defina as informações relacionadas à conclusão dessa etapa do processo.

#f2f2f2#f2f2f2

**Expediente**  
Expediente que será considerado na execução dessa etapa. O expediente é utilizado nos cálculos de prazo final e atraso da etapa. São exibidos para seleção os expedientes que existem no recurso .

**Prazo por tempo**  
Tempo, em horas, dentro do qual essa etapa precisa ser concluída. Essas horas, juntamente com o expediente selecionado, também são consideradas para determinar o prazo final de conclusão da etapa. Esse tempo começa a ser contado a partir do momento no qual a solicitação chega nessa etapa.

#ebecf0

trueExemplo de cálculo  
→ O expediente selecionado está configurado como: de **Segunda à Sexta das 8:00 às 18:00**.  
→ O tempo para conclusão da etapa é **1 hora**.  
→ A solicitação chegou nessa etapa às **17:30** de uma **Terça-feira**.  
→ Sendo assim, o prazo final de conclusão da etapa será **Quarta-feira** às **8:30**. Depois das 08:30, a etapa será considerada atrasada.

**07.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Atividade**.

**08.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar mecanismo de atribuição e acompanhamento

---

**01.** No  do processo, clique no componente **Atividade**  para o qual deseja configurar mecanismo de atribuição e acompanhamento.

**02.** Clique na aba **Atribuição**.

**03.** Defina como deve ser a atribuição do responsável pela solicitação quando ela chegar nessa etapa.

#f2f2f2#f2f2f2

**Tipo de atribuição**  
Como deve ser feita a definição do responsável por essa etapa do processo, ou seja, quem pode receber essa etapa quando a solicitação for movimentada para ela. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode receber e executar essa etapa, ou seja, ao movimentar a solicitação para essa etapa, é possível selecionar qualquer pessoa existente na plataforma para recebê-la.

* **Grupo específico**: quando selecionada, determina que apenas as pessoas de um grupo específico podem receber e executar essa etapa. É possível definir se a etapa será individual – executada por uma única pessoa do grupo – ou se ela será conjunta – executada por mais de uma pessoa do grupo. Essa definição é feita selecionando uma das opções Atividade individual ou Atividade conjunta.

* **Papel específico**: quando selecionada, determina que apenas as pessoas que exercem um papel específico podem receber e executar essa etapa. É possível definir se a etapa será individual – executada por uma única pessoa que exerce esse papel – ou se ela será conjunta – executada por mais de uma pessoa que exerce papel. Essa definição é feita selecionando uma das opções Atividade individual ou Atividade conjunta.

* **Campo de formulário**: quando selecionada, determina que apenas a pessoa informada em um campo do formulário da solicitação em alguma etapa anterior pode receber e executar essa etapa, ou seja, ao movimentar a solicitação para essa etapa, ela será enviada automaticamente para essa pessoa.

* **Pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode receber e executar essa etapa, ou seja, ao movimentar a solicitação para essa etapa, ela será enviada automaticamente para essa pessoa.

  Nota:

  Se essa pessoa for inativada em algum momento, somente o gestor do processo poderá movimentar a solicitação em seu lugar.

**Grupo específico**  
Grupo específico de pessoas que podem receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Grupo específico em Tipo de atribuição. Para ver as pessoas que fazem parte do grupo selecionado, basta clicar em **Visualizar**  e, para remover o grupo selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do grupo.

**Papel específico**  
Papel específico exercido pelas pessoas que podem receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Papel específico em Tipo de atribuição. Para ver as pessoas que exercem o papel selecionado, basta clicar em **Visualizar**  e, para remover o papel selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do papel.

**Selecione um campo**  
Campo do formulário no qual foi informada a pessoa que pode receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Campo de formulário em Tipo de atribuição. Para remover o campo selecionado, basta clicar em **Remover**  – localizado no lado direito do nome do campo.

**Pessoa específica**  
Pessoa específica que pode receber essa etapa quando a solicitação for movimentada para ela. Esse campo somente é exibido ao selecionar a opção Pessoa específica em Tipo de atribuição. Para remover a pessoa selecionada, basta clicar em **Remover**  – localizado no lado direito do nome da pessoa.

**04.** Ainda na aba **Atribuição**, se o tipo de atribuição escolhido foi **Grupo específico** ou **Papel específico**, defina como deve ser a execução dessa etapa, se individual ou conjunta.

#f2f2f2#f2f2f2

**Atividade individual**Quando selecionada, determina que a etapa deve ser executada por uma única pessoa. Neste caso, é possível definir se apenas uma pessoa do grupo ou que exerce o papel pode ser selecionada para receber a solicitação quando ela for movimentada ou se a solicitação deve ser enviada para todas as pessoas do grupo ou que exercem o papel e a primeira que a assumir se torna a responsável por executar essa etapa. Essa opção somente é exibida quando o tipo de atribuição escolhido for Grupo específico ou Papel específico.

**Atividade conjunta**Quando selecionada, determina que a etapa deve ser executada por mais de uma pessoa. Desta forma, somente será possível concluir a etapa e movimentar a solicitação para a próxima quando o percentual de consenso de conclusão definido for atingido. Essa opção também permite definir se várias pessoas do grupo ou que exercem o papel podem ser selecionadas para receber a solicitação quando ela for movimentada ou se a solicitação deve ser enviada para todas as pessoas do grupo ou que exercem o papel para que possa ser executada por quaisquer pessoas até que o percentual de consenso seja atingido. Essa opção somente é exibida quando o tipo de atribuição escolhido for Grupo específico ou Papel específico.

**Movimentação da atividade**  
Como deve ser a definição do responsável pela etapa quando a solicitação for movimentada para ela, de acordo com a forma de execução escolhida: individual ou conjunta.  
Para atividade **individual**, as opções disponíveis são:

* **Seleção de uma pessoa do grupo**: quando selecionada, determina que será necessário selecionar uma pessoa do grupo ou do papel ao movimentar a solicitação para essa etapa.

* **Envio para todos do grupo/papel (*pool*)**: quando selecionada, determina que ao movimentar a solicitação para essa etapa, ela será automaticamente enviada para todas as pessoas do grupo ou que exercem o papel e a primeira que a assumir se torna a responsável por executar essa etapa.

Para atividade **conjunta**, as opções disponíveis são:

* **Seleção de múltiplas pessoas**: quando selecionada, determina que será necessário selecionar mais de uma pessoa do grupo ou que exerce o papel ao movimentar a solicitação para essa etapa.

* **Atribuição para todos do grupo/papel**: quando selecionada, determina que ao movimentar a solicitação para essa etapa, ela será automaticamente enviada para todas as pessoas do grupo ou que exercem o papel para que a etapa possa ser executada por quaisquer pessoas até que o percentual de consenso seja atingido.

**Consenso para conclusão**  
Percentual de consenso que é necessário atingir para que a etapa seja considerada concluída, ou seja, percentual de pessoas que devem assumir a etapa e tomar a mesma decisão para que a solicitação possa ser movimentada para a próxima. Por padrão, o consenso é definido em 100%. Esse campo somente é exibido ao selecionar a opção Atividade conjunta.

**05.** Em **Acompanhamento**, assinale as opções que representam quem deve ser notificado quando a solicitação chegar ou sair dessa etapa.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início dessa etapa será enviada ao responsável por ela.

* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre o início dessa etapa será enviada ao solicitante.

* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início dessa etapa será enviada ao gestor do processo.

Importante!

Independentemente das opções assinaladas, a notificação não é enviada para quem realizou a ação.

#ebecf0

trueExemplo 1  
Uma pessoa movimenta a solicitação para uma etapa na qual ela mesma é a responsável. Mesmo que a opção **Notificar responsável** esteja assinalada, ela não receberá a notificação, visto que a ação foi feita por ela mesma.

#ebecf0

trueExemplo 2  
O gestor do processo movimenta a solicitação (como responsável ou gestor) para uma etapa na qual a opção **Notificar gestor** está assinalada. Neste caso, ele não receberá a notificação, apenas os outros gestores do processo receberão.

O mesmo ocorre para todos os tipos de notificação, incluindo a de substituto.

#ebecf0

trueExemplo  
Se a pessoa A é substituta da pessoa B e movimenta a solicitação para uma etapa onde a pessoa B é responsável, a pessoa A (substituta) não será notificada. Apenas a pessoa B e outras pessoas substitutas dela serão notificadas.

Nota:

As notificações podem ser enviadas na  ou por *e-mail*, dependendo de como foi feita a  das opções de envio no perfil pessoal, bem como quais opções estão disponíveis para uso na empresa, que podem ter sido configuradas de forma  – para todas as empresas – ou por .

**06.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Atividade**.

**07.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar prazo

---

**01.** No  do processo, clique no componente **Atividade**  para o qual deseja configurar um prazo.

**02.** Clique na aba **Prazo**.

**03.** Defina as informações relacionadas à conclusão dessa etapa do processo.

#f2f2f2#f2f2f2

**Expediente**  
Expediente que será considerado na execução dessa etapa. O expediente é utilizado nos cálculos de prazo final e atraso da etapa. São exibidos para seleção os expedientes que existem no recurso .

**Prazo por tempo**  
Tempo, em horas, dentro do qual essa etapa precisa ser concluída. Essas horas, juntamente com o expediente selecionado, também são consideradas para determinar o prazo final de conclusão da etapa. Esse tempo começa a ser contado a partir do momento no qual a solicitação chega nessa etapa.

#ebecf0

trueExemplo de cálculo  
→ O expediente selecionado está configurado como: de **Segunda à Sexta das 8:00 às 18:00**.  
→ O tempo para conclusão da etapa é **1 hora**.  
→ A solicitação chegou nessa etapa às **17:30** de uma **Terça-feira**.  
→ Sendo assim, o prazo final de conclusão da etapa será **Quarta-feira** às **8:30**. Depois das 08:30, a etapa será considerada atrasada.

**04.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Atividade**.

**05.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar regras para anexos

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade** para o qual deseja configurar as regras para os anexos das solicitações.

**02.** Na aba **Geral**, clique em **Configurações de anexo**  – localizado na parte inferior – para definir as regras para os anexos necessários nessa etapa do processo.

#f2f2f2#f2f2f2

As regras para anexos não são obrigatórias. Quando não são definidas, é permitido deixar a etapa sem anexos ou adicionar qualquer tipo e qualquer quantidade de anexos, visto que nenhuma validação é feita.

Dica!

para entender como as regras para anexos funcionam antes de configurá-las.

**03.** Para definir que a etapa não deve receber anexos, ative a opção **Proibir anexos**.

#f2f2f2#f2f2f2

**Proibir anexos**  
Quando ativada, determina que não é permitido anexar nenhum arquivo nessa etapa.

**04.** Se a etapa permitirá anexos, clique em  **Adicionar regra de anexo na atividade** para definir a regra.

**05.** Em **Regra geral**, escolha como o anexo deve ser, selecionando uma **condição** e informando uma **quantidade**, caso a condição permita.

#f2f2f2#f2f2f2

As condições disponíveis são:

* **igual a**;
* **maior que**;
* **maior ou igual a**;
* **menor que**;
* **menor ou igual a**;
* **qualquer um**.

@gerais-2 trueClique aqui e veja alguns Exemplos

@gerais-2#ebecf0

→ O anexo dever ser **maior ou igual a** **2**.

Significa que é **obrigatório** anexar **pelo menos dois** anexos – podendo adicionar **mais** – nessa etapa.

→ O anexo dever ser **menor que 4**.

Significa que é permitido adicionar **até três** anexos nessa etapa ou deixá-la sem anexo.

→ O anexo deve ser **qualquer um**.

Significa que é permitido adicionar **qualquer tipo** e **quantidade** de anexo nessa etapa ou deixá-la sem anexo.

Dica!

Veja mais exemplos de utilização das **regras gerais** [clicando aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=860252092#Plataforma%E2%9D%99Regrasparaanexosemsolicita%C3%A7%C3%B5es-Regrageral).

**06.** Se desejar, clique em **Adicionar regra específica** para determinar algumas características exigidas para o anexo.

**07.** Escolha a **característica** do anexo para compor a regra específica.

#f2f2f2#f2f2f2

As condições disponíveis são:

* **a extensão**;
* **o nome do arquivo**;
* **o nome e a extensão**;
* **condição avançada:** quando selecionada, é necessário criar a regra a partir de uma expressão que utiliza os caracteres **\*** (**asterisco**), **|** (***pipe***) e **!** (**exclamação**). Mais detalhes sobre essa opção podem ser obtidos no .

**08.** Agora, escolha a **condição** que essa característica precisa atender.

#f2f2f2#f2f2f2

As condições disponíveis são:

* **igual a**;
* **diferente de**;
* **contendo**.

Se a condição selecionada for **contendo**, ainda é possível escolher:

* **início**;
* **meio**;
* **fim**.

**09.** Por fim, informe os **termos** que precisam ou não constar no nome ou na extensão do anexo, de acordo com a **característica** e a **condição** selecionadas.

#f2f2f2#f2f2f2

@especificas-2 trueClique aqui e veja alguns Exemplos

@especificas-2#ebecf0

→ O anexo deve ser **qualquer um** com **a extensão igual a** **.zip**.

Significa que é obrigatório adicionar qualquer anexo que tenha a extensão **.zip**.

→ O anexo deve ser **maior ou igual a 0** com **a extensão igual a** **.log**.

Significa que é permitido adicionar **um** ou **mais** anexos com a extensão **.log** ou deixar a etapa sem anexos.

→ O anexo deve ser **igual a 1** com **o nome e extensão contendo** no nome o termo **boleto** no **início** e na extensão o termo **.pdf** no **fim**.

Significa que é obrigatório adicionar **um** anexo que tenha o termo **boleto** no **início** do seu **nome** e que seja um documento do tipo **PDF**.

Dica!

Veja mais exemplos de utilização das **regras específicas** [clicando aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=860252092#Plataforma%E2%9D%99Regrasparaanexosemsolicita%C3%A7%C3%B5es-Regraespec%C3%ADfica).

Para remover as condições selecionadas para a regra específica, clique em **Remover**  – localizado no fim da composição da regra.

**10.** Se a opção selecionada para a regra específica for **condição avançada**, é possível definir a regra utilizando uma expressão que pode conter os caracteres **\*** (**asterisco**), **|** (***pipe***) e **!** (**exclamação**). condição-avançada-10

#f2f2f2#f2f2f2

* **\*** (**asterisco**): permite deixar livre para ter ou não quaisquer caracteres antes ou depois dele.

* **|** (***pipe***): significa "**ou**" e permite definir múltiplos padrões.

* **!** (**exclamação**): significa "**diferente de**" ou "**proibido**" e permite barrar um padrão.

@avancadas-2 trueClique aqui e veja alguns Exemplos

@avancadas-2#ebecf0

→ O anexo deve ser **qualquer um** com **condição avançada** **!\*.zip**.

É permitido adicionar **qualquer tipo**de anexo com a extensão **diferente** de **.zip** ou deixar a etapa sem anexos. A extensão **.zip** é **proibida**.

→ O anexo deve ser **maior ou igual a 2** com **condição avançada** **\*.pdf|\*.jpg**.

É obrigatório adicionar **pelo menos 2** anexos que tenham uma das extensões permitidas: **.pdf ou .jpg**.

→ O anexo deve ser **igual a 1** com **condição avançada \*fatura\*.pdf.**

É obrigatório adicionar **um** anexo que contenha o termo **fatura** no nome e com a extensão **.pdf**.

Dica!

Veja mais detalhes e mais exemplos de utilização das **regras avançadas** [clicando aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=860252092#Plataforma%E2%9D%99Regrasparaanexosemsolicita%C3%A7%C3%B5es-Regraavan%C3%A7ada).

Para remover as condições definidas para a regra avançada, clique em **Remover**  – localizado no fim da composição da regra.

**11.** Em **Mensagem de erro caso não atenda a regra**, defina uma mensagem ou uma instrução para ajudar o responsável que está executando essa etapa quando o anexo que ele adicionou não está atendendo a essa regra.

#f2f2f2#f2f2f2

@mensagens-2 trueClique aqui e veja alguns Exemplos

@mensagens-2#ebecf0

→ **Se a regra for**: O anexo deve ser **maior ou igual a 1**.

**A mensagem pode ser**: Você precisa anexar pelo menos 1 arquivo de qualquer tipo. Se desejar, pode anexar mais de 1.

→ **Se a regra for**: O anexo deve ser **igual a 2**.

**A mensagem pode ser**: Você precisa anexar 2 arquivos de qualquer tipo. Não é permitido adicionar mais de 2.

→ **Se a regra for**: O anexo deve ser **maior ou igual a 3** com **a extensão igual a** **.pdf**.

**A mensagem pode ser**: Você precisa anexar pelo menos 3 documentos do tipo PDF. Se desejar, pode anexar mais de 3.

**12.** Clique em **Salvar**.

#f2f2f2#f2f2f2

Ao salvar, a regra passa a ser exibida em **Regras criadas**. As regras são exibidas em ordem de criação, da mais recente para a mais antiga.

É possível editar ou remover as regras criadas clicando em **Ações**– localizado no lado direito da regra – e, em seguida, em **Editar** ou **Excluir**. Ao editar uma regra, a ordem de exibição é alterada, ou seja, a regra editada passa a ser exibida por primeiro. Já ao excluir uma regra, a ordem de exibição não é alterada, continuam sendo exibidas em ordem de edição e depois de criação, da mais recente para a mais antiga.

Para adicionar mais regras, clique em  **Adicionar regra de anexo na atividade**.

**13.** Ao concluir a configuração de todas as regras desejadas, clique em **Fechar**– localizado no canto superior direito.

**14.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Atividade**.

**15.** Na mensagem exibida, clique em **Ok, entendi**.

### Editar regra para anexos

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade**  do qual deseja editar as regras para os anexos das solicitações.

**02.** Na aba **Geral**, clique em **Configurações de anexo**  – localizado na parte inferior.

**03.** Em **Regras criadas**, localize a regra que deseja editar e clique em **Ações**– localizado no lado direito da regra.

**04.** Clique em **Editar**.

**05.** Modifique as condições da regra conforme desejado.

**06.** Clique em **Salvar edição**.

#f2f2f2#f2f2f2

Ao editar uma regra, ela passa a ser exibida por primeiro na listagem de regras, ou seja, a ordem de exibição delas é alterada, elas são exibidas em ordem de edição e depois de criação, da mais recente para a mais antiga.

**07.** Ao concluir a edição de todas as regras desejadas, clique em **Fechar**– localizado no canto superior direito.

**08.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Atividade**.

**09.** Na mensagem exibida, clique em **Ok, entendi**.

### Excluir regra para anexos

---

**100%true5%**

**01.** No  do processo, clique no componente **Atividade**  do qual deseja excluir as regras para os anexos das solicitações.

**02.** Na aba **Geral**, clique em **Configurações de anexo**  – localizado na parte inferior.

**03.** Em **Regras criadas**, localize a regra que deseja excluir e clique em **Ações**– localizado no lado direito da regra.

**04.** Clique em **Excluir**.

**05.** Na mensagem de confirmação exibida, clique em **Excluir regra**.

#f2f2f2#f2f2f2

Não é possível restaurar uma regra que foi excluída.

A exclusão de uma regra não altera a ordem de exibição das demais, ou seja, elas continuam sendo exibidas em ordem de edição e depois de criação, da mais recente para a mais antiga.

**06.** Ao concluir a exclusão de todas as regras desejadas, clique em **Fechar**– localizado no canto superior direito.

**07.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Atividade**.

**08.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar atividade para ser aprovada pelo My Approval

---

É necessário ter um formulário vinculado ao processo para configurar a aprovação para o aplicativo.

**100%true5%**

**01.** No  do processo, clique no componente **Atividade** que deseja configurar para ser aprovada pelo aplicativo .

**02.** Na aba **Geral**, clique em **App My Approval**  – localizado na parte inferior – para definir as configurações desejadas.

**03.** Informe ou configure as informações solicitadas.

#f2f2f2#f2f2f2

**Título**Nome da solicitação que aparecerá no aplicativo. É possível inserir um nome ou selecionar um campo do formulário para ser o nome. Se não for definido um nome para a solicitação, a descrição do processo será exibida por padrão.

**Destaque**  
Informação que será exibida como destaque da solicitação no aplicativo. É possível inserir uma informação ou selecionar um campo do formulário para ser o destaque. Essa informação não pode ser muito extensa. Se não for definida uma informação para ser exibida em destaque, o nome da atividade em questão será exibido por padrão.

**Descrição**  
Breve descrição da solicitação que será exibida no aplicativo. É possível inserir uma descrição ou selecionar um campo do formulário para ser a descrição. Se não for definida uma descrição, a instrução do processo e da atividade e o identificar da solicitação serão exibidos por padrão.

**Se rejeitada**Atividade de destino para a qual a solicitação será enviada se ela for rejeitada pelo aplicativo. É possível selecionar as atividades posteriores à atividade em questão ou a opção **Desabilitar**, que significa que o responsável não poderá rejeitar a solicitação pelo aplicativo, apenas aprová-la – se a opção estiver habilitada – ou escolher outra ação em Mais ações.

**Se aprovada**Atividade de destino para a qual a solicitação será enviada se ela for aprovada pelo aplicativo. É possível selecionar as atividades posteriores à atividade em questão ou a opção **Desabilitar**, que significa que o responsável não poderá aprovar a solicitação pelo aplicativo, apenas rejeitá-la – se a opção estiver habilitada – ou escolher outra ação em Mais ações.

**Mais ações**  
Demais atividades que existem no processo e que não foram selecionadas nos campos Se aprovada e Se rejeitada. Essas atividades podem ser selecionadas no aplicativo no momento da tomada de decisão para enviar a solicitação para outra etapa específica que não sejam as que estão configuradas nos campos Se aprovada e Se rejeitada.

**Solicitar observação para rejeitadas**  
Quando ativado, o responsável precisará adicionar uma observação ao rejeitar a solicitação pelo aplicativo.

**Solicitar observação para aprovadas**  
Quando ativado, o responsável precisará adicionar uma observação ao aprovar a solicitação pelo aplicativo.

**04.** Ao concluir as configurações, clique em **Salvar**.

**05.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Atividade**.

**06.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
