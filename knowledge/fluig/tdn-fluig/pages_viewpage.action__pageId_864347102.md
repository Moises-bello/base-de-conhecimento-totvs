---
content_hash: b59c62e5155a443cc2c4217a0772ddbb63e03a402f059f4efa952070239c5bb9
fetched_at: '2026-06-28T21:35:30.953326+00:00'
page_id: '864347102'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Fluxos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864347102
version: 36
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

75%

5.\*ndice

25%

trueIdioma

# Falando de fluxos...

---

Os fluxos são os mecanismos que definem para qual atividade a solicitação deve seguir. São eles que determinam o caminho que a solicitação percorrerá conforme as etapas ou atividades vão sendo concluídas.

Os fluxos são representados por setas que indicam o sentido da movimentação, que pode ser apenas de ida – da atividade de origem para a atividade destino – ou de retorno – da atividade destino para a atividade de origem.

Os tipos de fluxos disponíveis para utilização são detalhados a seguir.

## Fluxo comum

---

O fluxo comum é o fluxo padrão para movimentação da solicitação entre as atividades. É o fluxo mais utilizado, que permite movimentar a solicitação de uma atividade para outra sem a possibilidade de retornar para a atividade anterior.

O fluxo comum é representado por uma seta que indica a direção para onde a solicitação será movimentada.

## Fluxo automático

---

O fluxo automático movimenta a solicitação automaticamente para a atividade destino quando o prazo da atividade de origem foi atingido e ela ainda não foi concluída, ou seja, a solicitação ainda não foi movimentada para a próxima etapa.

O fluxo automático é representado por um relógio no meio da seta que indica a direção para onde a solicitação será movimentada.

Para que o fluxo automático funcione corretamente, é necessário que:

* a atividade de origem tenha um **prazo** definido;

* exista um agendamento do tipo **Fluxo automático** no , determinando um intervalo de tempo a partir do qual são verificadas e movimentadas as solicitações que estão paradas em atividades com fluxo automático.

Notas:

→ Como o fluxo automático somente movimenta a solicitação depois que o prazo da atividade de origem foi atingido, **é necessário configurar também um fluxo comum** na atividade de origem para permitir a movimentação convencional, ou seja, para permitir que a solicitação seja movimentada antes de atingir o prazo de conclusão da atividade de origem.

→ Durante a execução de um fluxo automático, **não há um usuário autenticado realizando a movimentação**. Portanto, eventos que utilizam o usuário autenticado por meio de APIs devem considerar esse fato para evitar inconsistências na execução.

#ebecf0

trueExemplo de uso  
Em um processo de **Abertura de chamado** para o suporte técnico, o solicitante tem um **prazo definido** para avaliar a solução proposta e retornar positiva ou negativamente, ou seja, informar se a solução atendeu ou não a sua necessidade. Se ele não retornar dentro desse prazo, o chamado será automaticamente encerrado. Neste caso, é recomendado utilizar um **fluxo automático** entre a etapa **Avaliar solução** – de responsabilidade do solicitante – e a etapa **Finalizar chamado**, que é o fim do processo. Assim, evita-se que existam muitos chamados pendentes ainda abertos por falta de retorno dos solicitantes.

## Fluxo de retorno

---

O fluxo de retorno permite voltar a solicitação somente para a atividade de origem, ou seja, a última atividade que foi executada no processo.

Quando a solicitação é movimentada da atividade de origem para a atividade destino por meio de um fluxo que permite retorno, ao concluir a atividade destino, será permitido retornar a solicitação para a atividade anterior, ou seja, a de origem.

O responsável que receberá a solicitação será a mesma pessoa que concluiu a atividade de origem anteriormente, ou seja, que a movimentou para a atividade destino pela última vez.

O fluxo de retorno é representado por uma seta partindo da atividade destino e direcionando para a atividade de origem.

Fluxos automáticos também podem ser configurados para permitir retorno. Neste caso, sua representação também terá um relógio no meio da seta, da seguinte forma: .

Nota:

O fluxo de retorno somente pode ser utilizado na versão do processo na qual a solicitação se encontra durante a movimentação. Por isso, se a solicitação é convertida para outra versão do processo, **na sua primeira movimentação depois da conversão, ela não pode retornar para a atividade anterior**, visto que haverá uma movimentação que representa a conversão e, portanto, perderá a possibilidade de retorno imediato.

#ebecf0

trueExemplo de uso  
Em um processo de **Solicitação de férias**, ao enviar a solicitação para a aprovação do gestor, pode ser que ele solicite **algum ajuste** na data de início ou na quantidade de dias solicitados. Nesse caso, é recomendado utilizar o **fluxo de retorno** para permitir que o gestor **retorne** a solicitação para o colaborador **ajustar os dados** e enviar a solicitação para aprovação novamente. Assim, evita-se que o gestor tenha que reprovar a solicitação e o colaborador tenha que abrir uma nova com os ajustes solicitados.

### Como o fluxo de retorno funciona na prática

---

O fluxo de retorno funciona da mesma forma que o botão **Voltar** de um navegador de internet: ele enxerga apenas a última atividade de onde a solicitação veio.

Em um processo simples, como o exemplificado abaixo, onde a solicitação passará apenas uma vez pela atividade de destino, a atividade de origem será sempre exibida como opção para retornar a solicitação.

Neste caso, temos um fluxo de retorno entre as atividades Início (**origem**) e Aprovação do gestor (**destino**).

→ Quando a solicitação for enviada do Início para a Aprovação do gestor, ao finalizar a atividade Aprovação do gestor (**destino**) e movimentar a solicitação, ao olhar para trás, a atividade Início (**origem**) será vista como a última executada, por isso, ela será exibida como opção para retornar a solicitação.

Porém, em processos mais complexos, como o abaixo, o resultado obtido pode ser diferente do esperado.

Aqui, temos um fluxo de retorno entre as atividades Ajustar contrato (**origem**) e Revisar contrato (**destino**).

→ Quando a solicitação for enviada da atividade Ajustar contrato para a Revisar contrato pela primeira vez, ao finalizar a atividade Revisar contrato (**destino**) e movimentar a solicitação, ao olhar para trás, a atividade Ajustar contrato (**origem**) será vista como a última executada, por isso, ela é exibida como opção para retornar a solicitação.

→ Já quando a solicitação avança e vai para a atividade Aprovar contrato, passa pela decisão de aprovação (*gateway* Exclusivo) e é reprovada, ela volta para a atividade Revisar contrato. Porém, nesse momento, a última atividade que foi executada (**origem**) foi a etapa de aprovação (*gateway* Exclusivo) e não mais a atividade Ajustar contrato. Como o histórico imediato da atividade de origem mudou, a atividade Ajustar contrato não é mais exibida como opção para retornar a solicitação.

Neste caso, se for desejado que a atividade Ajustar contrato seja exibida como opção para retornar a solicitação, mesmo após ela ter passado por outras atividades adiante, uma alternativa é remover o fluxo de retorno e adicionar dois fluxos comuns entre as atividades Ajustar contrato e Revisar contrato, um que vai e outro que volta. Dessa forma, sempre que a solicitação estiver na atividade Revisar contrato, a atividade Ajustar contrato será exibida como opção para enviar a solicitação, funcionando como um **retorno**, conforme exemplificado abaixo.

## Mensagem dos fluxos

---

Os fluxos possuem mensagens pré-definidas que são exibidas no momento da movimentação da solicitação da atividade de origem para a atividade destino. Porém, essas mensagens podem ser personalizadas, de acordo com o processo ou etapa.

#ebecf0

trueExemplo de uso  
Em um processo de **Abertura de chamado** para o suporte técnico, a mensagem de movimentação do **Início** para a **Segunda etapa** pode ser definida como "**Seu chamado foi aberto com sucesso!**" ao invés de manter a mensagem padrão "**Solicitação 999 iniciada com sucesso.**".

## Configurar fluxo

---

**100%true5%**

**01.** No  do processo, clique no componente **Fluxo** que deseja configurar.

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Na aba **Tipo de fluxo**, defina as informações gerais do fluxo.

#f2f2f2#f2f2f2

**Tipo de fluxo**  
Tipo de fluxo que será utilizado entre as duas atividades ou etapas do processo. As opções disponíveis são:

* **Fluxo comum**: quando selecionada, determina que o fluxo será comum, ou seja, é necessário movimentar a solicitação da atividade origem para a atividade destino.

* **Fluxo automático**: quando selecionada, determina que o fluxo será automático, ou seja, a solicitação será movimentada automaticamente da atividade origem para a atividade destino quando o prazo de conclusão da atividade de origem vencer.

  Importante!

  Para que o fluxo automático funcione corretamente, é necessário criar um agendamento do tipo **Fluxo automático** no .

**Título do fluxo comum**  
Nome para identificação do fluxo. Esse nome é exibido acima do fluxo no  do processo.

#ebecf0

trueExemplo de uso  
Em um processo de **Solicitação de pagamento**, o fluxo entre a etapa **Solicitar pagamento** e a etapa **Aprovação** **do gestor** poderia se chamar **Enviar para aprovação**.

**Fluxo de retorno**  
Quando ativada, determina que é permitido retornar a solicitação da atividade destino para a atividade de origem.

**Título do fluxo de retorno**  
Nome para identificação do fluxo de retorno. Esse nome é exibido abaixo do fluxo no  do processo.

#ebecf0

trueExemplo de uso  
Em um processo de **Solicitação de férias**, o fluxo de retorno entre a etapa **Aprovação do gestor** e a etapa **Solicitar férias** poderia se chamar **Ajustar datas**.

**03.** Clique na aba **Mensagem do fluxo** para personalizar a mensagem exibida quando a solicitação passar por esse fluxo.

#f2f2f2#f2f2f2

A mensagem do fluxo é exibida ao concluir a movimentação da solicitação da atividade de origem para a atividade destino. Essas mensagens já existem por padrão, porém, é possível personalizá-las se desejado.

Dica!

É possível inserir o número da solicitação em qualquer parte da mensagem, seja no **título**, na **descrição** ou no texto do ***link***. Para isso:

**01.** Insira o caractere **@**.

**02**. Clique em **nº solicitação**.

**03.** Ao clicar, o **nº solicitação** será substituído por **[request:id]**.

→ Quando a mensagem for exibida, no lugar de **@[request:id]** será exibido o número da solicitação em questão.

@personalizada trueClique aqui e veja um exemplo de mensagem personalizada

@personalizada#ebecf0

**Sua solicitação de férias foi enviada para aprovação!**

O número da sua solicitação é **999**. Clique no *link* abaixo e acompanhe o andamento.

[Acompanhar solicitação](http://Acompanhar solicitação).

**Título**  
Título da mensagem de movimentação da solicitação. O título pode ter até 70 caracteres. Se nenhum título for inserido, será exibido o padrão.

@titulo-padrao trueClique aqui e veja o título padrão

@titulo-padrao#ebecf0

Ao **abrir** a solicitação:  
**→ Solicitação 999 iniciada com sucesso.**

Ao **enviar** a solicitação de uma etapa para outra:  
**→ Solicitação 999 movimentada com sucesso.**

**Descrição**  
Mensagem de movimentação da solicitação. A mensagem pode ter até 255 caracteres. Se nenhuma mensagem for inserida, será exibida a padrão.

@descricao-padrao trueClique aqui e veja a descrição padrão

@descricao-padrao#ebecf0

→ Você pode acessar os detalhes, os anexos e os complementos desta sua solicitação.

**Texto do *link* da solicitação**  
Texto que será exibido no *link* que permite acessar a solicitação. O texto pode ter até 70 caracteres. Se nenhum texto for inserido, será exibido o padrão.

@link-padrao trueClique aqui e veja o link padrão

@link-padrao#ebecf0

→ [Acessar solicitação #999](http://Acessar solicitação #999).

**04.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Fluxo**.

**05.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
