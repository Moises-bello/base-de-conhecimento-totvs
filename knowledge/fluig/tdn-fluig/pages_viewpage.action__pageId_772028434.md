---
content_hash: 8baaa6430ee2bcfbe74781506e3eac82c33b71561f6549e44320f3bc448693ee
fetched_at: '2026-06-28T21:35:29.880867+00:00'
page_id: '772028434'
product: fluig
source: tdn-fluig
title: Flows | Solicitação de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772028434
version: 28
---

.\*ndice

# Falando de solicitação de pagamento...

---

O *flow* de solicitação de pagamento registra a necessidade de um pagamento avulso, seja para um fornecedor, colaborador, prestador de serviço ou outro. O usuário solicita aprovação de acordo com as regras definidas e encaminha a notificação para o responsável liberar o pagamento.

Depois de adquirido, instalado e configurado, ele cria um processo igual a qualquer outro processo padrão da plataforma, ou seja, a abertura de solicitações é a partir do recurso .

#ebf8ff#ebf8ff
.flows \* {
-webkit-box-sizing: border-box;
-moz-box-sizing: border-box;
box-sizing: border-box;
}
.flows-text-center {
text-align: center;
}
.flows-full-height {
height: 100%;
}
/\* Component flows Callout \*/
.flows-callout {
border: none;
padding: 0px;
display: -moz-box;
-moz-flex-flow: row wrap;
-moz-justify-content: center;
-moz-align-items: center;
display: -ms-flexbox;
-ms-flex-flow: row wrap;
-ms-justify-content: center;
-ms-align-items: center;
display: -webkit-flex;
display: -webkit-box;
-webkit-flex-flow: row wrap;
-webkit-justify-content: center;
-webkit-align-items: center;
display: flex;
flex-flow: row wrap;
justify-content: center;
align-items: center;
}
.flows-callout .flows-callout-image {
width: 24px;
}
.flows-callout .flows-callout-body {
width: calc(100% - 24px);
padding-left: 20px;
}
.flows-callout .flows-callout-citacao {
border: 0px solid;
border-left-width: 3px;
border-left-color: #f36f21;
margin: 4px;
margin-left: 25px;
padding-left: 8px;
font-size: 13px;
}
.flows-callout .flows-callout-thumb {
width: 24px;
height: 24px;
}
.flows-callout .flows-callout-text {
color: #58595b;
line-height: 1.75;
margin: 0;
}

![](https://tdn.totvs.com/download/attachments/563436139/nota.png)

**NOTA:**  
Esse *flow* não está integrado a nenhum ERP ou outro sistema financeiro, também não recebe, envia ou filtra títulos que devem ser analisados.

]]>

Este *flow* segue as leis gerais de proteção de dados - LGPD. O tratamento de dados pessoais realizado, possibilita que o administrador do Fluig faça a anonimização de dados, caso deseje ou seja solicitado. Para isso, basta acessar: **Painel de controle > Segurança e acesso > Anonimizar e exportar dados pessoais.**

## Como adquirir

---

O *flow* de solicitação de pagamento é listado como uma solução paga no recurso [Store](https://tdn.totvs.com/x/frOcEw) do TOTVS Fluig Plataforma a partir da atualização **Mist - 1.8.0-230523**.

Para adquiri-lo, é necessário entrar em contato com o executivo de soluções de negócio responsável por sua conta.

Com o processo de aquisição finalizado, o acesso à instalação do *flow* é liberado, sendo necessário instalá-lo para utilizar. Neste caso, basta seguir os passos descritos em Instalar e configurar *flow*.

## Instalação

---

Depois de adquirir esse *flow*, ele estará liberado para instalação a partir do recurso [Store](https://tdn.totvs.com/x/frOcEw).

### Requisito para uso

---

Para instalar e utilizar esse *flow*, é necessário:

* ter o TOTVS Fluig Plataforma instalado e parametrizado a partir da atualização **Mist - 1.8.0-230523**.

### Parametrizações

---

Durante a instalação desse *flow*, é necessário definir algumas parametrizações, que são divididas em quatro etapas:

* **Geral**: onde são definidos os dados gerais do processo, como nome, gestor e prazos de expiração e de aviso;

* **Responsáveis**: onde são definidas as atribuições de cada atividade, notificações de acompanhamento e prazos;

* **Cadastros**: onde são definidas as informações que serão consumidas pelo processo, como o centro de custo.

* **Revisão**: onde são listados os principais dados do processo que será criado para conferência.

### Instalar e configurar *flow instalar*

---

100%true5%

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

É possível ainda acessar diretamente pelo ícone da **Store**  localizado no menu lateral, para ir diretamente para os aplicativos.

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no ***flow* Solicitação de pagamento**.

**04.** Clique em **Configurar**.

#f2f2f2#f2f2f2

A instalação é iniciada e, quando concluída, uma notificação é emitida.

**05.** Na etapa **Geral**, em **Dados gerais**, defina as informações solicitadas.

#f2f2f2#f2f2f2

**Código identificador do processo**  
Exibe o código de identificação do processo. Não é possível alterá-lo.

**Nome do processo**  
Nome que visa facilitar o reconhecimento do processo e do seu objetivo. Esse nome será exibido posteriormente no recurso [Iniciar solicitação](https://tdn.totvs.com/pages/viewpage.action?pageId=233763157).

**Descrição**  
Breve descrição sobre os detalhes do processo e instruções para os solicitantes utilizarem.

**Categoria**  
Categoria na qual o processo se enquadra. Ele será exibido dentro dessa categoria no recurso [Iniciar solicitação](https://tdn.totvs.com/pages/viewpage.action?pageId=233763157).

**Atribuição da pessoa gestora do processo**  
Pessoa que será definida como gestora do processo, ou seja, na ausência do responsável por alguma atividade, essa pessoa pode substituí-lo e continuar com a movimentação da solicitação. O preenchimento é obrigatório e as opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que os gestores serão qualquer pessoa cadastrada na plataforma.
* **Todos de um grupo específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado grupo;
* **Todos de um papel específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado papel;
* **Uma pessoa específica**: quando selecionada, determina que o gestor será uma pessoa específic

**Grupo, papel ou pessoa específica**Grupo, papel ou pessoa específica que poderá ser definida como gestora do processo, de acordo com a opção que foi selecionada em **Pessoa gestora do processo**.

**Prazo de expiração (em horas)**  
Tempo máximo acordado, em horas, durante o qual a solicitação ficará disponível. Ao atingir o tempo máximo, uma notificação é emitida informando que a solicitação expirou. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser menor que o prazo de notificação.

**Prazo de aviso (em horas)**  
Tempo acordado, em horas, para que uma notificação seja enviada antes do prazo de expiração da solicitação. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser maior que o prazo de expiração.

**06.** Clique em **Avançar**.

**07.** Na etapa **Responsáveis**, em **Solicitante**, determine a pessoa responsável por abrir a solicitação e aplique as regras necessárias.

#f2f2f2#f2f2f2

**1 - ABRIR SOLICITAÇÃO**

**Quem poderá abrir uma solicitação**Pessoas que podem abrir solicitação no processo criado por esse *flow*. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode abrir solicitação.
* **Todos de um grupo específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado grupo podem abrir solicitação;
* **Todos de um papel específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado papel podem abrir solicitação;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode abrir solicitação;

**Grupo, papel ou usuário**  
Grupo, papel ou pessoa que pode abrir solicitações nesse processo, de acordo com a opção que foi selecionada em **Quem poderá abrir uma solicitação**.

**Acompanhamento**  
Envio de notificação sobre o início da solicitação para as pessoas envolvidas. As opções disponíveis são: 

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao responsável pela primeira atividade;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao gestor do processo.

---

**2 - COMPLEMENTAR OS DADOS**A responsabilidade por complementar os dados é atribuída à pessoa que abriu a solicitação.

**Acompanhamento**  
Envio de notificação sobre o início da atividade de complemento de informações para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade de complemento de informações será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da atividade de complemento de informações será enviada ao solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade de complemento de informações será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a atividade de complemento de informações deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante recebeu ou assumiu a atividade.

**08.** Na etapa **Responsáveis**, em **Gestor do centro de custo**, defina as configurações relacionadas a atividade de aprovação conforme o centro de custo.

#f2f2f2#f2f2f2

**1 - ANALISAR SOLICITAÇÃO**A responsabilidade é definida de acordo com o gestor do centro de custo que será informado na abertura da solicitação.

**Acompanhamento**  
Envio de notificação sobre o início da análise da solicitação para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a análise da solicitação deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o responsável recebeu ou assumiu a atividade.

**09.** Ainda na etapa **Responsáveis**, em **Financeiro**, configure os responsáveis e como o setor financeiro deve realizar o atendimento da solicitação.

#f2f2f2#f2f2f2

**1 - REALIZAR PAGAMENTO**

**Quem poderá realizar o pagamento?**Pessoas que podem realizar o pagamento. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode assumir a atividade;
* **Uma pessoa de um grupo específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um grupo específico e apenas ela pode assumir a atividade.;
* **Uma pessoa de um papel específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um papel específico e apenas ela pode assumir a atividade;
* **Todos de um grupo específico**: quando selecionada, determina que a solicitação será enviada para um grupo específico e qualquer um do grupo pode assumir a atividade;
* **Todos de um papel específico**: quando selecionada, determina que a solicitação será enviada para um papel específico e qualquer um do papel pode assumir a atividade;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode assumir a atividade;

**Grupo, papel, usuário ou atividade**  
Grupo, papel, pessoa ou atividade da qual o executor será considerado para analisar a solicitação, de acordo com a opção que foi selecionada em **Quem poderá realizar o pagamento?**.

**Acompanhamento**  
Envio de notificação sobre o início da análise da solicitação para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a análise da solicitação deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o responsável recebeu ou assumiu a atividade.

**10.** Clique em **Avançar**.

**11.** Na etapa **Cadastros**, em **Centro de custo**, determine os centros de custo e seus responsáveis.

#f2f2f2#f2f2f2

**Código:** Inserir umcódigo do centro de custo. Não é possível gerar códigos repetidos. Após ser salvo, ele não poderá ser editado ou excluído. Campo de preenchimento obrigatório para poder avançar e instalar o Flow de Solicitação de pagamento.

**Nome do centro de custo:**definir um nome para o centro de custo.

**Gestor do centro de custo:**definir um gestor responsável pelo centro de custo.

Para adicionar um novo centro de custo, basta acionar o item **+ Adicionar novo centro de custo.**

**12.** Clique em **Avançar**.

**13.** Na etapa **Revisão**, em **Dados do processo**, confira as principais informações do processo que será criado.

#f2f2f2#f2f2f2

Se necessário, clique em **Voltar** até a etapa desejada para ajustar alguma configuração.

**14.** Clique em **Instalar** .

#f2f2f2#f2f2f2

Ao finalizar a instalação, um processo com o nome e na categoria definidos na configuração é listado no recurso .

### Editar *flow*

---

**100%true5%**

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) o *flow* Solicitação de pagamento.

**04.** Clique em **Configurar** – localizado no quadro do *flow*.

**05.** Altere as informações desejadas em cada etapa e avance até a última.

**06.** Clique em **Atualizar** .

#f2f2f2#f2f2f2

O processo será atualizado com as alterações efetuadas e sua versão será incrementada.

### Atualizar *flow*

---

Quando houver atualizações disponíveis, o indicativo Yellowatualizar será exibido no *flow* para informar que ele pode ser atualizado.

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** No recurso Itens da Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no ***flow* Solicitação de pagamento**.

**04.** Clique em **Atualizar**.

#f2f2f2#f2f2f2

Para pode utilizar as informações e melhorias da atualização liberada será necessário acessar o configurador do processo clicando em **Configurar**e passar pelas etapas **Geral**, **Responsável**, **Cadastros**e na etapa **Revisão**clicar no botão **Atualizar**.

Ao clicar em atualizar, uma nova versão do processo será criada com todas as correções e melhorias. As solicitações que estão em andamento continuarão com as configurações da versão antiga. Apenas as novas solicitações que forem abertas terão as configurações da nova versão do processo.

Ao realizar estes passos, as novidades e correções serão liberadas para o *flow*Solicitação de pagamento.

## Processo criado

---

Ao finalizar a instalação do *flow*, o processo criado é listado juntamente com os demais processos existentes na plataforma, tanto no recurso  quanto no .

As características do processo criado por esse *flow* são detalhadas a seguir.

### Diagrama

---

O diagrama define como o processo funciona, quais atividades o compõem e qual o caminho que a solicitação segue até a sua conclusão.

Este é o diagrama do *flow* de Solicitação de pagamento:

### Atividades

---

As atividades que compõem o processo são:

Solicitar pagamento

Solicitante inicia o processo, preenche as informações necessárias e envia para a atividade de "**Analisar solicitação**".

Analisar solicitação

O gestor do centro de custo entende a demanda, podendo aprovar, reprovar ou solicitar mais dados sobre o pagamento.

Se aprovado, avança para a atividade de "**Realizar pagamento**".

Se reprovado, avança para a atividade de "**Complementar dados**".

Se cancelado, o processo é automaticamente cancelado no sistema.

Cancelar

É executado o processo de cancelamento.

Complementar dados

O solicitante complementa os dados, ou altera, de acordo com a orientação do gestor do centro de custo.

Se aprovado, avança para a atividade de "**Analisar solicitação**".

Se cancelado, o processo é automaticamente cancelado no sistema.

Cancelar

É executado o processo de cancelamento.

Realizar pagamento

O gestor verifica se todos os dados estão corretos para realizar o pagamento.

Se for solicitado mais informações, o processo é enviado para a atividade de "**Complementar dados**".

Se o processo estiver de acordo, é enviado para a atividade de "**Finalizar**".

Finalizar

O processo é finalizado com sucesso.

### Restrições

---

O *flow* de solicitação de pagamento possui as seguintes restrições:

* não permite ser integrado a outros sistemas;

* não permite personalização, tais como, adicionar campos ao formulário, alterar o diagrama, adicionar ou remover atividades.

#fdf7e8#fdf7e8

![](https://tdn.totvs.com/download/attachments/563436139/importante.png)

**IMPORTANTE!**  
Como esse *flow* se torna um processo igual a qualquer outro dentro da plataforma, é possível alterá-lo ou até mesmo excluir seus artefatos. Porém, se for feita qualquer alteração no processo, diagrama, formulário ou outro artefato, o direito ao suporte padrão é automaticamente perdido.
