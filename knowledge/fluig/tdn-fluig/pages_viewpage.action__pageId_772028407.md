---
content_hash: b6d13db8b7754c77b592dff0fea3ab7d770c2140686ab59e7da7e068619478f5
fetched_at: '2026-06-28T21:35:29.854436+00:00'
page_id: '772028407'
product: fluig
source: tdn-fluig
title: Flows | Inclusão de contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772028407
version: 30
---

.\*ndice

# Falando de inclusão de contratos...

---

O *flow* inclusão de contratos permite ao colaborador registrar os dados cadastrais de um contrato, tais como: fornecedor ou cliente, itens do contrato, data de validade e valor do contrato. Quando aprovada a etapa de Análise do contrato, o documento será publicado no ECM e herdará as propriedades de validade e notificação.

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
Esse *flow* não está integrado a nenhum ERP. Também não contempla a Gestão do Contrato: medições, cronograma financeiro, cláusulas, aditivo, paralisação ou suspensão.

]]>

Este *flow* segue as leis gerais de proteção de dados - LGPD. O tratamento de dados pessoais realizado, possibilita que o administrador do Fluig faça a anonimização de dados, caso deseje ou seja solicitado. Para isso, basta acessar: **Painel de controle > Segurança e acesso > Anonimizar e exportar dados pessoais.**

## Como adquirir

---

O *flow* de inclusão de contrato é listado como uma solução paga no recurso [Store](https://tdn.totvs.com/x/frOcEw) do TOTVS Fluig Plataforma a partir da atualização **Mist - 1.8.0-230523**.

Para adquiri-lo, é necessário entrar em contato com o executivo de soluções de negócio responsável por sua conta.

Com o processo de aquisição finalizado, o acesso à instalação do *flow* é liberado, sendo necessário instalá-lo para utilizar. Neste caso, basta seguir os passos descritos em Instalar e configurar *flow*.

## Instalação

---

Depois de adquirir esse *flow*, ele estará liberado para instalação a partir do recurso [Store](https://tdn.totvs.com/x/frOcEw).

### Requisito para uso

---

Para instalar e utilizar esse *flow*, é necessário:

* ter o TOTVS Fluig Plataforma instalado e parametrizado a partir da versão **Mist - 1.8.0-230523**;

* utilização de processo padrão.

### Parametrizações

---

Durante a instalação desse *flow*, é necessário definir algumas parametrizações, que são divididas em quatro etapas:

* **Geral**: onde são definidos os dados gerais do processo, como gestor e prazos de expiração e de aviso;

* **Responsáveis**: onde são definidos os responsáveis e o SLA de cada atividade;

* **Cadastros**: onde são definidas as opções que serão selecionadas durante o preenchimento da solicitação: cadastro de centro de custo e tipo de contrato;

* **Revisão**: onde são listados os principais dados do processo que será criado para conferência.

### Instalar e configurar *flow instalar*

---

100%5%

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

É possível ainda acessar diretamente pelo ícone da **Store**  localizado no menu lateral, para ir diretamente para os aplicativos.

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no *flow* **Inclusão de contrato**.

**04.** Clique em **Configurar** – localizado no quadro do *flow*.

**06.** Na etapa **Geral**, em **Dados gerais**, defina as informações de apresentação e comportamento geral deste processo.

#f2f2f2#f2f2f2

**Código identificador do processo**  
Exibe o código de identificação do processo. Não é possível alterá-lo.

**Nome do processo**  
Nome que visa facilitar o reconhecimento do processo e do seu objetivo. Esse nome será exibido posteriormente no recurso .

**Descrição**  
Breve descrição sobre os detalhes do processo e instruções para os solicitantes utilizarem.

**Categoria**  
Categoria na qual o processo se enquadra. Ele será exibido dentro dessa categoria no recurso .

**Pessoa gestora do processo**  
Pessoa que será definida como gestora do processo, ou seja, na ausência do responsável por alguma atividade, essa pessoa pode substitui-lo e continuar com a movimentação da solicitação. Se não for definida uma pessoa gestora, apenas os responsáveis pelas atividades poderão movimentar a solicitação, ou seja, na ausência de algum responsável, a solicitação permanecerá parada. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode ser gestor da solicitação;
* **Todos de um grupo específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado grupo;
* **Todos de um papel específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado papel;
* **Uma pessoa específica**: quando selecionada, determina que o gestor será uma pessoa específica.

**Grupo, papel ou pessoa específica**Grupo, papel ou pessoa que será definida como gestora do processo, de acordo com a opção que foi selecionada em **Pessoa gestora do processo**.

**Prazo de expiração (em horas)**  
Tempo máximo acordado, em horas, durante o qual a solicitação ficará disponível. Ao atingir o tempo máximo, uma notificação é emitida informando que a solicitação expirou. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser menor que o prazo de notificação.

**Prazo de aviso (em horas)**  
Tempo acordado, em horas, para que uma notificação seja enviada antes do prazo de expiração da solicitação. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser maior que o prazo de expiração.

**07.** Clique em **Avançar**.

**08.** Na etapa **Responsáveis**, em **Solicitante**, defina o perfil responsável por abrir a solicitação e configure suas atividades.

#f2f2f2#f2f2f2

**1 - ABRIR SOLICITAÇÃO**

**Quem poderá abrir uma solicitação**Pessoas que podem abrir solicitação no processo criado por esse *flow*. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode abrir solicitação;
* **Todos de um grupo específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado grupo podem abrir solicitação;
* **Todos de um papel específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado papel podem abrir solicitação;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode abrir solicitação.

**Grupo, papel ou pessoa específica**  
Grupo, papel ou pessoa que pode abrir solicitações nesse processo, de acordo com a opção que foi selecionada em **Quem poderá abrir uma solicitação**.

**Acompanhamento**  
Envio de notificação sobre o início da solicitação para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao responsável pela primeira atividade;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao gestor do processo.

---

**2 - AJUSTAR DADOS DO CONTRATO**A responsabilidade por ajustar dados do contrato é atribuída à pessoa que abriu a solicitação.

**Acompanhamento**  
Envio de notificação sobre o início da atividade de ajuste da solicitação. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade de ajuste da solicitação será enviada ao responsável por ela, que neste caso, é o próprio solicitante;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da atividade de ajuste da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade de ajuste da solicitação será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a atividade de ajuste da solicitação deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante recebeu ou assumiu a atividade.

**09.** Ainda na etapa **Responsáveis**, em **Contratos**, defina o perfil responsável pelo setor de contratos e configure sua atividade

#f2f2f2#f2f2f2

**1 - ANALISAR CONTRATO**

**Quem poderá analisar o contrato.**  
Pessoas que podem analisar o contrato neste *flow*. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa poderá analisar o contrato;
* **Todos de um grupo específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado grupo podem analisar o contrato;
* **Todos de um papel específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado papel podem analisar o contrato;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica poderão analisar o contrato.
* **Uma pessoa de um papel específico:** quando selecionada, determina que apenas uma pessoa de um papel específico e apenas ela poderá analisar o contrato;
* **Uma pessoa de um grupo específico:** quando selecionada, determina que apenas uma pessoa de um grupo específico e apenas ela poderá analisar o contrato;

**Acompanhamento**  
Envio de notificação sobre o início da atividade de análise do contrato. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade de análise do contrato será enviada ao responsável por ela, que neste caso, é o próprio solicitante;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da atividade de análise do contrato será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade de análise do contrato será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a atividade de análise do contrato deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante recebeu ou assumiu a atividade.

**10.**Para visualizar o fluxo da solicitação, clique em **Visualizar fluxo**.

**11**. Clique em **Avançar**.

**12.** Na etapa **Cadastros**, em **Centro de custo**, determine os centros de custos e seus responsáveis.

#f2f2f2#f2f2f2

**Código**Código do centro de custo do contrato. Não é possível gerar códigos repetidos. Após ser salvo, ele não poderá ser editado ou excluído. 

**Nome do centro de custo**Definir um nome para o centro de custo.

**Gestor do centro de custo**Definir um gestor responsável pelo centro de custo.

Para adicionar mais centros de custo, clique em **Adicionar novo centro de custo** e preencha as informações necessárias. Para excluir um centro de custo adicionado, basta clicar em **Excluir**.

**13.** Ainda na etapa **Cadastros**, em **Estabelecimento**, insira o nome dos estabelecimentos e filiais de sua empresa ou organização.

#f2f2f2#f2f2f2

**Nome do estabelecimento**Insira um nome para o estabelecimento.

Para adicionar mais estabelecimentos, clique em **Adicionar novo estabelecimento** e informe o nome do estabelecimento. Para excluir um estabelecimento adicionado, basta clicar em **Excluir**.

**14.** Ainda na etapa **Cadastros**, em **Tipo de contrato,** insira o nome dos contratos que poderão ser adicionados na abertura da solicitação.

#f2f2f2#f2f2f2

**Nome do tipo**Insira um nome para o tipo de contrato.

Para adicionar mais tipos de contrato, clique em **Adicionar novo tipo de contrato** e informe o nome do novo tipo. Para excluir um tipo de contrato já adicionado, basta clicar em **Excluir**.

**15.** Clique em **Avançar**.

**16.** Na etapa **Revisão**, em **Dados do processo**, confira as principais informações do processo que será criado.

#f2f2f2#f2f2f2

Se necessário, clique em **Voltar** até a etapa desejada para ajustar alguma configuração.

**17.** Clique em **Configurar processo**.

#f2f2f2#f2f2f2

Ao finalizar a instalação, um processo com o nome e na categoria definidos na configuração é listado no recurso .

### Editar *flow*

---

100%5%

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

É possível ainda acessar diretamente pelo ícone da **Store**  localizado no menu lateral, para ir diretamente para os aplicativos.

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) o *flow* Inclusão de contrato.

**04.** Clique em **Configurar** – localizado no quadro do *flow*.

**05.** Altere as informações desejadas em cada etapa e avance até a última.

**06.** Clique em **Atualizar**.

#f2f2f2#f2f2f2

Uma nova versão do processo será criada. As solicitações que estão em andamento continuam com os dados da versão antiga. Apenas as novas solicitações que forem abertas terão as informações que foram alteradas na nova versão.

### Atualizar *flow*

---

Quando houver atualizações disponíveis, o indicativo Yellowatualizar será exibido no *flow* para informar que ele pode ser atualizado.

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

É possível ainda acessar diretamente pelo ícone da **Store**  localizado no menu lateral, para ir diretamente para os aplicativos.

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** No recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no *flow* de Inclusão de contrato.

**04.** Clique em **Atualizar**.

#f2f2f2#f2f2f2

Para pode utilizar as informações e melhorias da atualização liberada será necessário acessar o configurador do processo clicando em **Configurar**e passar pelas etapas **Geral**, **Responsável**, **Cadastros**e na etapa **Revisão**clicar no botão **Atualizar**.

Ao clicar em atualizar, uma nova versão do processo será criada com todas as correções e melhorias. As solicitações que estão em andamento continuarão com as configurações da versão antiga. Apenas as novas solicitações que forem abertas terão as configurações da nova versão do processo.

Ao realizar estes passos, as novidades e correções serão liberadas para o ***flow* Inclusão de contrato.**

## Processo criado

---

Ao finalizar a configuração do *flow*, o processo criado é listado juntamente com os demais processos existentes na plataforma, tanto no recurso  quanto no .

#fdf7e8#fdf7e8

![](https://tdn.totvs.com/download/attachments/563436139/importante.png)

**IMPORTANTE!**  
Como esse *flow* se torna um processo igual a qualquer outro dentro da plataforma, é possível alterá-lo ou até mesmo excluir seus artefatos. Porém, se for feita qualquer alteração no processo, diagrama, formulário ou outro artefato, o direito ao suporte padrão é automaticamente perdido.
