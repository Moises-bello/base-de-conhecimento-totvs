---
content_hash: 192bf3eed9ba8005e41f86078be610b223c4fa799f17dc8eb691bd339dba9f71
fetched_at: '2026-06-28T21:35:30.861157+00:00'
page_id: '862118990'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Início
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862118990
version: 63
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

75%

5.\*ndice

25%

trueIdioma

# Falando de evento Início...

---

O evento **Início** é a etapa inicial de um processo e indica onde o fluxo começa. Ao abrir uma solicitação do processo, essa é a primeira etapa que será executada.

A definição de quem pode abrir solicitações do processo é feita por meio do mecanismo de atribuição do evento. Quem possui permissão, pode abrir solicitações do processo a partir do recurso .

Nesse evento, também é possível configurar algumas características gerais, definir regras de anexo, prazo para conclusão, dentre outras características.

## Ver *tour* guiado do evento Início

---

**100%true5%**

**01.** No  do processo, clique no evento **Início** .

**02.** Na lateral direita, onde foram exibidas as configurações do evento, clique em  **Guia de uso** – localizado na parte inferior.

**03.** Veja a apresentação do recurso destacado.

**04.** Clique em **Próximo** para seguir para a apresentação do próximo recurso.

#f2f2f2#f2f2f2

Quando há recursos anteriores, é possível clicar em **Voltar** para revê-los.

**05.** Ao finalizar o *tour* guiado, clique em **Concluir**.

#f2f2f2#f2f2f2

Se desejar, é possível clicar em **Voltar** para rever os recursos anteriores antes de concluir.

## Configurar evento Início

---

**100%true5%**

**01.** No  do processo, clique no evento **Início** .

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Na aba **Geral**, defina as informações gerais para o evento que representa a primeira etapa do processo, ou seja, a abertura da solicitação.

#f2f2f2#f2f2f2

**Título**  
Nome da primeira etapa ou atividade do processo. É a etapa que será feita por quem irá abrir a solicitação. O nome pode ter até **200** caracteres.

#ebecf0

trueExemplo de uso  
Em um processo de **Solicitação de férias**, o **Início** poderia receber o nome **Solicitar férias**.

**Instruções para atividade**  
Instruções que visam facilitar o entendimento de quem vai abrir a solicitação – ou executar essa etapa novamente caso a solicitação retorne para ela – tais como dados que precisam ser informados para agilizar o entendimento e resolução da solicitação. As instruções são exibidas na aba **Informações** da solicitação.

Dica!

É possível incluir um documento de instruções que está armazenado no recurso . Para isso, basta utilizar o formato **[WD:codigodoc]** substituindo **codigodoc** pelo código numérico do documento.

**Solicitar senha**  
Quando ativada, determina que o solicitante precisa informar sua senha no momento de abrir a solicitação – ou de executar essa etapa novamente caso a solicitação retorne para ela. Se a senha estiver incorreta, é permitido que o solicitante a informe quantas vezes forem necessárias. A abertura da solicitação só será efetivada quando a senha for informada corretamente. A confirmação da senha fica registrada no histórico da solicitação que foi aberta. Se a opção **Confirmar senha** da aba **Segurança** das [configurações](https://tdn.totvs.com/pages/viewpage.action?pageId=860245005#Plataforma%E2%9D%99Editordeprocesso-Definirop%C3%A7%C3%B5esdeseguran%C3%A7aparaoprocessoseguran%C3%A7a-processo) do processo já estiver ativada, essa opção estará desabilitada.

Nota:

Etapas configuradas para solicitar a senha não podem ser automatizadas por *Web services*.

**Transferir responsável**  
Quanto ativada, determina que é possível transferir a responsabilidade para outra pessoa se a solicitação retornar para essa etapa.

**03.** Clique na aba **Atribuição** e defina quem pode abrir solicitações do processo, ou seja, quem pode executar a etapa inicial.

#f2f2f2#f2f2f2

**Tipo de atribuição**  
Como deve ser feita a definição de quem pode abrir solicitações desse processo, ou seja, quem pode executar a etapa inicial do processo. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode abrir solicitações desse processo.

* **Grupo específico**: quando selecionada, determina que apenas as pessoas de um grupo específico podem abrir solicitações desse processo.

* **Papel específico**: quando selecionada, determina que apenas as pessoas que exercem um papel específico podem abrir solicitações desse processo.

* **Pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode abrir solicitações desse processo.

  Nota:

  Se essa pessoa for inativada em algum momento, somente o gestor do processo poderá abrir solicitações em seu lugar.

**Grupo específico**  
Grupo específico de pessoas que podem abrir solicitações desse processo. Esse campo somente é exibido ao selecionar a opção Grupo específico em Tipo de atribuição. Para ver as pessoas que fazem parte do grupo selecionado, basta clicar em **Visualizar**  e, para remover o grupo selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do grupo.

**Papel específico**  
Papel específico exercido pelas pessoas que podem abrir solicitações desse processo. Esse campo somente é exibido ao selecionar a opção Papel específico em Tipo de atribuição. Para ver as pessoas que exercem o papel selecionado, basta clicar em **Visualizar**  e, para remover o papel selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do papel.

**Pessoa específica**  
Pessoa específica que pode abrir solicitações desse processo. Esse campo somente é exibido ao selecionar a opção Pessoa específica em Tipo de atribuição. Para remover a pessoa selecionada, basta clicar em **Remover**  – localizados no lado direito do nome da pessoa.

**04.** Em **Acompanhamento**, assinale as opções que representam quem deve ser notificado quando a solicitação sair dessa etapa ou chegar nessa etapa – caso retorne para ela.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao responsável por essa etapa que, nesse caso, é o próprio solicitante ou a pessoa para a qual a responsabilidade foi transferida, caso a solicitação tenha retornado para essa etapa.

* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao gestor do processo.

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

**05.** Clique na aba **Prazo** e defina as informações relacionadas à conclusão da etapa inicial do processo.

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

**06.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no evento **Início**.

**07.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar mecanismo de atribuição e acompanhamento

---

**01.** No  do processo, clique no evento **Início**  para o qual deseja configurar mecanismo de atribuição e acompanhamento.

**02.** Clique na aba **Atribuição**.

**03.** Defina quem pode abrir solicitações do processo, ou seja, quem pode executar a etapa inicial.

#f2f2f2#f2f2f2

**Tipo de atribuição**  
Como deve ser feita a definição de quem pode abrir solicitações desse processo, ou seja, quem pode executar a etapa inicial do processo. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode abrir solicitações desse processo.

* **Grupo específico**: quando selecionada, determina que apenas as pessoas de um grupo específico podem abrir solicitações desse processo.

* **Papel específico**: quando selecionada, determina que apenas as pessoas que exercem um papel específico podem abrir solicitações desse processo.

* **Pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode abrir solicitações desse processo.

  Nota:

  Se essa pessoa for inativada em algum momento, somente o gestor do processo poderá abrir solicitações em seu lugar.

**Grupo específico**  
Grupo específico de pessoas que podem abrir solicitações desse processo. Esse campo somente é exibido ao selecionar a opção Grupo específico em Tipo de atribuição. Para ver as pessoas que fazem parte do grupo selecionado, basta clicar em **Visualizar**  e, para remover o grupo selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do grupo.

**Papel específico**  
Papel específico exercido pelas pessoas que podem abrir solicitações desse processo. Esse campo somente é exibido ao selecionar a opção Papel específico em Tipo de atribuição. Para ver as pessoas que exercem o papel selecionado, basta clicar em **Visualizar**  e, para remover o papel selecionado, basta clicar em **Remover**  – ambos localizados no lado direito do nome do papel.

**Pessoa específica**  
Pessoa específica que pode abrir solicitações desse processo. Esse campo somente é exibido ao selecionar a opção Pessoa específica em Tipo de atribuição. Para remover a pessoa selecionada, basta clicar em **Remover**  – localizados no lado direito do nome da pessoa.

**04.** Em **Acompanhamento**, assinale as opções que representam quem deve ser notificado quando a solicitação sair dessa etapa ou chegar nessa etapa – caso retorne para ela.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao responsável por essa etapa que, nesse caso, é o próprio solicitante ou a pessoa para a qual a responsabilidade foi transferida, caso a solicitação tenha retornado para essa etapa.

* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao gestor do processo.

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

**05.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no evento **Início**.

**06.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar prazo

---

**01.** No  do processo, clique no evento **Início** para o qual deseja configurar um prazo.

**02.** Clique na aba **Prazo**.

**03.** Defina as informações relacionadas à conclusão da etapa inicial do processo.

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

**04.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no evento **Início**.

**05.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar regras para anexos

---

**100%true5%**

**01.** No  do processo, clique no evento **Início**  para o qual deseja configurar as regras para os anexos das solicitações.

**02.** Na aba **Geral**, clique em **Configurações de anexo** – localizado na parte inferior – para definir as regras para os anexos necessários na etapa inicial do processo, ou seja, a abertura da solicitação.

#f2f2f2#f2f2f2

As regras para anexos não são obrigatórias. Quando não são definidas, é permitido deixar a etapa sem anexos ou adicionar qualquer tipo e qualquer quantidade de anexos, visto que nenhuma validação é feita.

Dica!

para entender como as regras de anexo funcionam antes de configurá-las.

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

É obrigatório adicionar **qualquer tipo**de anexo com a extensão **diferente** de **.zip**. A extensão **.zip** é **proibida**.

→ O anexo deve ser **maior ou igual a 2** com **condição avançada** **\*.pdf|\*.jpg**.

É obrigatório adicionar **pelo menos 2** anexos que tenham uma das extensões permitidas: **.pdf ou .jpg**.

→ O anexo deve ser **igual a 1** com **condição avançada \*fatura\*.pdf.**

É obrigatório adicionar **um** anexo que contenha o termo **fatura** no nome e com a extensão **.pdf**.

Dica!

Veja mais detalhes e mais exemplos de utilização das **regras avançadas** [clicando aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=860252092#Plataforma%E2%9D%99Regrasparaanexosemsolicita%C3%A7%C3%B5es-Regraavan%C3%A7ada).

Para remover as condições definidas para a regra avançada, clique em **Remover**  – localizado no fim da composição da regra.

**11.** Em **Mensagem de erro caso não atenda a regra**, defina uma mensagem ou uma instrução para ajudar o responsável que está executando a etapa inicial quando o anexo que ele adicionou não está atendendo a essa regra.

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

**13.** Ao concluir a configuração de todas as regras desejadas, clique em **Fechar**– localizado no canto superior direito.

**14.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no evento **Início**.

**15.** Na mensagem exibida, clique em **Ok, entendi**.

### Editar regra para anexos

---

**100%true5%**

**01.** No  do processo, clique no evento **Início** do qual deseja editar as regras para os anexos das solicitações.

**02.** Na aba **Geral**, clique em **Configurações de anexo** – localizado na parte inferior.

**03.** Em **Regras criadas**, localize a regra que deseja editar e clique em **Ações**– localizado no lado direito da regra.

**04.** Clique em **Editar**.

**05.** Modifique as condições da regra conforme desejado.

**06.** Clique em **Salvar edição**.

#f2f2f2#f2f2f2

Ao editar uma regra, ela passa a ser exibida por primeiro na listagem de regras, ou seja, a ordem de exibição delas é alterada, elas são exibidas em ordem de edição e depois de criação, da mais recente para a mais antiga.

**07.** Ao concluir a edição de todas as regras desejadas, clique em **Fechar**– localizado no canto superior direito.

**08.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no evento **Início**.

**09.** Na mensagem exibida, clique em **Ok, entendi**.

### Excluir regra para anexos

---

**100%true5%**

**01.** No  do processo, clique no evento **Início**  do qual deseja excluir as regras para os anexos das solicitações.

**02.** Na aba **Geral**, clique em **Configurações de anexo** – localizado na parte inferior.

**03.** Em **Regras criadas**, localize a regra que deseja excluir e clique em **Ações**– localizado no lado direito da regra.

**04.** Clique em **Excluir**.

**05.** Na mensagem de confirmação exibida, clique em **Excluir regra**.

#f2f2f2#f2f2f2

Não é possível restaurar uma regra que foi excluída.

A exclusão de uma regra não altera a ordem de exibição das demais, ou seja, elas continuam sendo exibidas em ordem de edição e depois de criação, da mais recente para a mais antiga.

**06.** Ao concluir a exclusão de todas as regras desejadas, clique em **Fechar**– localizado no canto superior direito.

**07.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no evento **Início**.

**08.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
