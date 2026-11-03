---
content_hash: a3545cb03f21fbd4ecacfa34524e0f9d97acb83209775f517a8e382708f1c56b
fetched_at: '2026-06-28T21:35:29.928489+00:00'
page_id: '775483565'
product: fluig
source: tdn-fluig
title: Flows | Solicitação de equipamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=775483565
version: 42
---

.\*ndice

# Falando de solicitação de equipamentos...

---

O *flow* de solicitação de equipamentos permite que um funcionário registre a sua solicitação de equipamentos para o almoxarifado. Podendo ainda definir uma alçada de aprovação com o teto de valor do equipamento que poderá ser aprovado automaticamente. Ou seja, se o valor estiver dentro do limite alçado, não é necessária a aprovação do gestor do centro de custo, indo diretamente para o responsável por fornecer o equipamento.

Depois de adquirido, instalado e configurado, ele cria um processo igual a qualquer outro processo padrão da plataforma, ou seja, a abertura de solicitações é a partir do recurso [Iniciar solicitação](https://tdn.totvs.com/pages/viewpage.action?pageId=233763157).

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
Esse *flow* não valida se o item está disponível em estoque, se existem ordens de compras em aberto para determinado equipamento e não contempla os processos relativos a ativos fixos: registro, plaqueta, responsável, depreciação, entre outros.

]]>

Este *flow* segue as leis gerais de proteção de dados - LGPD. O tratamento de dados pessoais realizado, possibilita que o administrador do Fluig faça a anonimização de dados, caso deseje ou seja solicitado. Para isso, basta acessar: **Painel de controle > Segurança e acesso > Anonimizar e exportar dados pessoais.**

## Como adquirir

---

O *flow* de solicitação de equipamentos é listado como uma solução paga no recurso [Store](https://tdn.totvs.com/x/frOcEw) do TOTVS Fluig Plataforma a partir da atualização **Mist - 1.8.0-230523**.

Para adquiri-lo, é necessário entrar em contato com o executivo de soluções de negócio responsável por sua conta.

Com o processo de aquisição finalizado, o acesso à instalação do *flow* é liberado, sendo necessário instalá-lo para utilizar. Neste caso, basta seguir os passos descritos em Instalar e configurar *flow*.

## Instalação

---

Depois de adquirir esse *flow*, ele estará liberado para instalação a partir do recurso [Store](http://tdn.totvs.com).

### **Requisitos para uso**

---

Para instalar e utilizar esse *flow*, é necessário:

* Ter o TOTVS Fluig Plataforma instalado e parametrizado a partir da atualização **Mist - 1.8.0-230523;**
* Utilização de processo padrão.

### Parametrizações

---

Durante a instalação desse *flow*, é necessário definir as seguintes parametrizações, que serão divididas em quatro etapas:

* **Geral**:onde são definidos os dados gerais do processo, gestor e prazos de expiração e de aviso;

* **Responsáveis**: onde são definidos os responsáveis e o SLA de cada atividade;

* **Cadastros**: onde são definidas as opções que serão consumidas durante o preenchimento da solicitação como centro de custo, estabelecimento, valor teto e equipamentos;

* **Revisão**: onde são listados os principais dados do processo que será criado para conferência.

### Instalar e configurar *flow instalar*

---

100%5%

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](http://tdn.totvs.com)**.

#f2f2f2#f2f2f2

É possível ainda acessar diretamente pelo ícone da **Store**  localizado no menu lateral, para ir diretamente para os aplicativos.

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no *flow* **Solicitação de equipamentos**.

**04.** Clique em **Configurar**.

#f2f2f2#f2f2f2

A configuração é iniciada e, quando concluída, uma notificação é emitida.

**05.** Na etapa **Geral**, em **Dados gerais**, defina as informações de apresentação e identificação.

#f2f2f2#f2f2f2

**Código identificador do processo**  
Exibe o código de identificação do processo. Não é possível alterá-lo.

**Nome do processo**  
Nome que visa facilitar o reconhecimento do processo e do seu objetivo. Esse nome será exibido posteriormente no recurso .

**Descrição**  
Breve descrição sobre os detalhes do processo e instruções para os solicitantes utilizarem.

**Categoria**  
Categoria na qual o processo se enquadra. Ele será exibido dentro dessa categoria no recurso .

**Perfil do gestor do processo**Pessoa que será definida como gestora do processo, ou seja, na ausência do responsável por alguma atividade, essa pessoa pode substitui-lo e continuar com a movimentação da solicitação.  Se não for definida uma pessoa gestora, apenas os responsáveis pelas atividades poderão movimentar a solicitação, ou seja, na ausência de algum responsável, a solicitação permanecerá parada. As opções disponíveis são:

* **Todos de um grupo específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado grupo;
* **Todos de um papel específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado papel;
* **Por uma pessoa**: quando selecionada, determina que o gestor será uma pessoa específica.
* **Qualquer pessoa**: quando selecionada, determina que o gestor pode ser qualquer pessoa.

**Grupo, papel ou pessoa específica**Grupo, papel ou pessoa específica que poderá ser definida como gestora do processo, de acordo com a opção que foi selecionada em **Pessoa gestora do processo**.

**Prazo de expiração (em horas)**  
Tempo máximo acordado, em horas, durante o qual a solicitação ficará disponível. Ao atingir o tempo máximo, uma notificação é emitida informando que a solicitação expirou. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser menor que o prazo de notificação.

**Prazo de aviso (em horas)**  
Tempo acordado, em horas, para que uma notificação seja enviada antes do prazo de expiração da solicitação. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser maior que o prazo de expiração.

**06.** Clique em **Avançar**.

**07.** Na etapa **Responsáveis**, em **Solicitante**, defina a pessoa responsável por abrir a solicitação e como ela deve interagir com as atividades sob sua responsabilidade, aplicando as regras necessárias de acordo com o seu modelo de negócio.

#f2f2f2#f2f2f2

**1 - ABRIR SOLICITAÇÃO**

**Quem poderá abrir uma solicitação**Pessoas que podem abrir solicitação no processo criado por esse *flow*. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode abrir solicitação.
* **Todos de um grupo específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado grupo podem abrir solicitação;
* **Todos de um papel específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado papel podem abrir solicitação;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode abrir solicitação;

**Grupo, papel ou usuário específico**  
Grupo, papel ou pessoa que pode abrir solicitações nesse processo, de acordo com a opção que foi selecionada em **Quem poderá abrir uma solicitação**.

**Acompanhamento**  
Envio de notificação sobre o início da solicitação para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao responsável pela primeira atividade;
* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao gestor do processo.

---

**2 - RECEBER E VALIDAR EQUIPAMENTO**A responsabilidade da atividade receber e validar equipamento é atribuída à pessoa que abriu a solicitação.

**Acompanhamento**  
Envio de notificação sobre o início da atividade para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao responsável por ela;
* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual essa atividade deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante iniciou a solicitação.

---

**Gestor do centro de custo**Defina as configurações relacionadas a atividade de aprovação, conforme centro de custo. O cadastro do centro de custo é definido no próximo passo, juntamente com o responsável.

**1 - Análise de centro de custo**A responsabilidade da atividade é definida de acordo com o gestor do centro de custo que será informado na abertura da solicitação.

**Acompanhamento**  
Envio de notificação sobre o início da atividade para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao responsável por ela;
* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual essa atividade deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante iniciou a solicitação.

---

**Almoxarifado**Configure na atividade os responsáveis pelo equipamento e como o setor de almoxarifado deve realizar o atendimento da solicitação.

**01 - Disponibilizar equipamentos**

**Quem poderá disponibilizar os equipamentos**Pessoas que podem disponibilizar equipamentos para este *flow*. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa poderá disponibilizá-lo;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode disponibilizá-lo.
* **Todos de um papel específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado papel podem disponibilizá-lo;
* **Todos de um grupo específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado grupo podem disponibilizá-lo;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode disponibilizá-lo;
* **Uma pessoa de um papel específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um papel específico e apenas ela pode assumir a atividade;
* **Uma pessoa de um grupo específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um grupo específico e apenas ela pode assumir a atividade.

**Grupo, papel ou usuário específico**  
Grupo, papel ou pessoa que pode abrir solicitações nesse processo, de acordo com a opção que foi selecionada em **Quem poderá disponibilizar os equipamentos**.

**Acompanhamento**  
Envio de notificação sobre o início da atividade para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao responsável por ela;
* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre o início atividade será enviada ao solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual essa atividade deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante iniciou a solicitação.

---

**02 - Analisar problema**

**Quem poderá analisar o problema**Pessoas que podem analisar o problema deste *flow*. As opções disponíveis são:

* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode analisar o problema;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode analisar o problema.
* **Uma pessoa de um grupo específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um grupo específico e apenas ela pode assumir a atividade;
* **Uma pessoa de um papel específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um papel específico e apenas ela pode assumir a atividade;
* **Todos de um grupo específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado grupo podem analisar o problema;
* **Todos de um papel específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado papel podem analisar o problema;
* **Atribuição por executor de atividade:** quando selecionada, determina que o responsável pela atividade será o mesmo pré-definido em uma atividade anterior.

**Grupo, papel ou usuário específico**  
Grupo, papel ou pessoa que pode abrir solicitações nesse processo, de acordo com a opção que foi selecionada em **Quem poderá analisar o problema**.

**Acompanhamento**  
Envio de notificação sobre o início da atividade para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao responsável por ela;
* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual essa atividade deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante iniciou a solicitação.

**08.** Para visualizar o fluxo da solicitação, clique em **Visualizar fluxo**.

**09**. Clique em **Avançar**.

**10.** Na etapa **Cadastros**, em **Centro de custo** determine os centros de custos e seus responsáveis.

#f2f2f2#f2f2f2

**Código:** código do centro de custo de itens. Não é possível gerar códigos repetidos. Após ser salvo, ele não poderá ser editado ou excluído. 

**Nome do centro de custo:** definir um nome para o centro de custo.

**Gestor do centro de custo:** definir um gestor responsável pelo centro de custo.

Para adicionar um novo centro de custo, basta acionar o item **+ Adicionar novo centro de custo.**

**11.** Ainda na etapa **Cadastros**, em **Estabelecimento**, insira o nome dos estabelecimentos (matriz, franquias e filiais) de sua empresa ou organização.

#f2f2f2#f2f2f2

**Nome do estabelecimento:**defina o nome do estabelecimento.

Para adicionar um novo estabelecimento, basta acionar o item **+ Adicionar novo estabelecimento.**

**12.** Ainda na etapa **Cadastros**, em **Valor teto**, defina um valor que determinará se a solicitação precisa do centro de custo (superior ao valor teto) ou irá direto para a atividade disponibilizar equipamentos (inferior ao valor teto).

#f2f2f2#f2f2f2

**Valor teto**: insira um valor em reais.

**13.** Ainda na etapa **Cadastros**, em **Equipamentos**, determine os tipos de equipamentos que os solicitantes podem solicitar.

#f2f2f2#f2f2f2

**Código:** insira um código para o equipamento.

**Nome do item:** insira um nome para o equipamento.

**UN de medida:** insira a unidade de medida do equipamento.

**Valor:** insira um valor por equipamento.

Para adicionar mais equipamentos à lista, determine a quantidade que deseja e acione **Confirmar**.

**14**. Clique em **Avançar**.

**15.** Na etapa **Revisão**, em **Dados do processo**, confira as principais informações do processo que será criado..

#f2f2f2#f2f2f2

Se necessário, clique em **Voltar** até a etapa desejada para ajustar alguma configuração.

**16.** Clique em **Instalar** .

#f2f2f2#f2f2f2

Ao finalizar a instalação, um processo com o nome e na categoria definidos na configuração é listado no recurso .

### Editar *flow*

---

100%5%

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](http://tdn.totvs.com)**.

#f2f2f2#f2f2f2

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) o *flow* Solicitação de equipamentos.

**04.** Clique em **Configurar** – localizado no quadro do *flow*.

**05.** Altere as informações desejadas em cada etapa e avance até a última.

**06.** Clique em **Atualizar** .

#f2f2f2#f2f2f2

Ao editar e atualizar o processo, uma nova versão será criada. As solicitações que estão em andamento continuarão com as configurações da versão antiga. Apenas as novas solicitações que forem abertas terão as configurações da nova versão.

### Atualizar *flow*

---

**Quando houver atualizações disponíveis, o indicativo Yellowatualizar será exibido no *flow* para informar que ele pode ser atualizado.**

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](http://tdn.totvs.com)**.

#f2f2f2#f2f2f2

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** No recurso **Store**, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no *flow* de **Solicitação de equipamentos**.

**04.** Clique em **Atualizar**.

#f2f2f2#f2f2f2

Para pode utilizar as informações e melhorias da atualização liberada será necessário acessar o configurador do processo clicando em **Configurar**e passar pelas etapas **Geral**, **Responsável**, **Cadastros**e na etapa **Revisão**clicar no botão **Atualizar**.

Ao clicar em atualizar, uma nova versão do processo será criada com todas as correções e melhorias. As solicitações que estão em andamento continuarão com as configurações da versão antiga. Apenas as novas solicitações que forem abertas terão as configurações da nova versão do processo.

Ao realizar estes passos, as novidades e correções serão liberadas para o ***flow* Solicitação de equipamento.**

## Processo criado

---

Ao finalizar a configuração do *flow*, o processo criado é listado juntamente com os demais processos existentes na plataforma, tanto no recurso  quanto no .

#fdf7e8#fdf7e8

![](https://tdn.totvs.com/download/attachments/563436139/importante.png)

**IMPORTANTE!**  
Como esse *flow* se torna um processo igual a qualquer outro dentro da plataforma, é possível alterá-lo ou até mesmo excluir seus artefatos. Porém, se for feita qualquer alteração no processo, diagrama, formulário ou outro artefato, o direito ao suporte padrão é automaticamente perdido.
