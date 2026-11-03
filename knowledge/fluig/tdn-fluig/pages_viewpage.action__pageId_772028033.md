---
content_hash: f8203f274e53ef36acfaa1a2874b24046dddc969266a2794e589a5a260e9aa63
fetched_at: '2026-06-28T21:35:29.828467+00:00'
page_id: '772028033'
product: fluig
source: tdn-fluig
title: Flows | Solicitação de viagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772028033
version: 35
---

.\*ndice

# Falando de solicitação de viagem...

---

O *flow* de solicitação de viagem permite que os colaboradores registrem uma solicitação de viagem, definindo o motivo, além de colocar todos os serviços necessários e adiantamentos para então submeter esse pedido para aprovação do gestor.

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
Esse *flow* não está integrado a nenhum ERP nem a *Self booking*. Também não controla ou cria pedidos de compra dos serviços necessários para a viagem e não faz reservas automáticas.

]]>

Este *flow* segue as leis gerais de proteção de dados - LGPD. O tratamento de dados pessoais realizado, possibilita que o administrador do Fluig faça a anonimização de dados, caso deseje ou seja solicitado. Para isso, basta acessar: **Painel de controle > Segurança e acesso > Anonimizar e exportar dados pessoais.**

## Como adquirir

---

O *flow* de solicitação de viagem é listado como uma solução paga no recurso [Store](https://tdn.totvs.com/x/frOcEw) do TOTVS Fluig Plataforma a partir da atualização **Mist - 1.8.0-230523**.

Para adquiri-lo, é necessário entrar em contato com o executivo de soluções de negócio responsável por sua conta.

Com o processo de aquisição finalizado, o acesso à instalação do *flow* é liberado, sendo necessário instalá-lo para utilizar. Neste caso, basta seguir os passos descritos em Instalar e configurar *flow*.

## Instalação

---

Depois de adquirir esse *flow*, ele estará liberado para instalação a partir do recurso [Store](https://tdn.totvs.com/x/frOcEw).

### Requisito para uso

---

Para instalar e utilizar esse *flow*, é necessário:

* ter o TOTVS Fluig Plataforma instalado e parametrizado a partir da atualização **Mist - 1.8.0-230523**;

* utilização de processo padrão.

### *Links* externos

---

Esse *flow* faz uso do seguinte *link* externo:

* <https://servicodados.ibge.gov.br/api/v1/localidades/estados>: de onde são obtidos os estados e as cidades para seleção durante a abertura da solicitação.

### Parametrizações

---

Durante a instalação desse *flow*, é necessário definir algumas parametrizações, que são divididas em quatro etapas:

* **Geral**: onde são definidos os dados gerais do processo, como gestor e prazos de expiração e de aviso;

* **Responsáveis**: onde são definidos os responsáveis e o SLA de cada atividade;

* **Cadastros**: onde são definidas as opções que serão selecionadas durante o preenchimento da solicitação: centro de custo, filial, motivo da viagem e adiantamento;

* **Revisão**: onde são listados os principais dados do processo que será criado para conferência.

### Instalar e configurar *flow instalar*

---

100%true5%

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

É possível ainda acessar diretamente pelo ícone da **Store**  localizado no menu lateral, para ir diretamente para os aplicativos.

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no *flow* Solicitação de viagem.

**04.** Clique em **Configurar** – localizado no quadro do *flow*.

A instalação é iniciada e, quando concluída, uma notificação é emitida.

**05.** Na etapa **Geral**, em **Dados gerais**, defina as informações solicitadas.

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

**06.** Clique em **Avançar**.

**07.** Na etapa **Responsáveis**, em **Solicitante**, defina as informações necessárias para cada atividade de quem vai abrir solicitações.

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

**2 - AJUSTAR SOLICITAÇÃO**A responsabilidade por ajustar a solicitação é atribuída à pessoa que abriu a solicitação.

**Acompanhamento**  
Envio de notificação sobre o início da atividade de ajuste da solicitação. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade de ajuste da solicitação será enviada ao responsável por ela, que neste caso, é o próprio solicitante;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da atividade de ajuste da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade de ajuste da solicitação será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a atividade de ajuste da solicitação deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante recebeu ou assumiu a atividade.

**08.** Em **Gestor do centro de custo**, defina as configurações relacionadas a atividade de aprovação conforme o centro de custo.

#f2f2f2#f2f2f2

**1 - ANALISAR SOLICITAÇÃO**A responsabilidade é definida de acordo com o gestor do centro de custo que será informado na abertura da solicitação.

**Acompanhamento**  
Envio de notificação sobre o início da análise da solicitação para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a análise da solicitação deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o responsável recebeu ou assumiu a atividade.

**09.** Em **Financeiro**, configure os responsáveis e como o setor financeiro deve realizar o atendimento da solicitação.

#f2f2f2#f2f2f2

**1 - PROGRAMAR PAGAMENTO**

**Quem poderá realizar o pagamento?**Pessoas que podem realizar o pagamento dos custos da viagem que precisam ser adiantados. As opções disponíveis são:

* **Uma pessoa de um grupo específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um grupo específico e apenas ela pode assumir a atividade;
* **Uma pessoa de um papel específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um papel específico e apenas ela pode assumir a atividade;
* **Todos de um grupo específico**: quando selecionada, determina que a solicitação será enviada para um grupo específico e qualquer um do grupo pode assumir a atividade;
* **Todos de um papel específico**: quando selecionada, determina que a solicitação será enviada para um papel específico e qualquer um do papel pode assumir a atividade;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode assumir a atividade.

**Grupo, papel ou pessoa específica**  
Grupo, papel ou pessoa que pode assumir a programação dos custos da viagem que precisam ser adiantados, de acordo com a opção que foi selecionada em **Quem poderá programar o pagamento?**.

**Acompanhamento**  
Envio de notificação sobre o início da programação do pagamento para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da programação do pagamento será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da programação do pagamento será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da programação do pagamento será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a programação do pagamento deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o responsável recebeu ou assumiu a atividade.

**10.** Ainda na etapa **Responsáveis**, em **Reservas**, defina as informações necessárias para a atividade do setor de reservas da viagem.

#f2f2f2#f2f2f2

**1 - RESERVAR SERVIÇOS**

**Quem poderá reservar os serviços da viagem?**Pessoas que podem reservar os serviços necessários para a viagem. As opções disponíveis são:

* **Uma pessoa de um grupo específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um grupo específico e apenas ela pode assumir a atividade;
* **Uma pessoa de um papel específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um papel específico e apenas ela pode assumir a atividade;
* **Todos de um grupo específico**: quando selecionada, determina que a solicitação será enviada para um grupo específico e qualquer um do grupo pode assumir a atividade;
* **Todos de um papel específico**: quando selecionada, determina que a solicitação será enviada para um papel específico e qualquer um do papel pode assumir a atividade;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode assumir a atividade;

**Grupo, papel ou pessoa específica**  
Grupo, papel ou pessoa que pode assumir a reserva dos serviços da viagem, de acordo com a opção que foi selecionada em **Quem poderá reservar os serviços da viagem?**.

**Acompanhamento**  
Envio de notificação sobre o início da reserva dos serviços para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da reserva dos serviços será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da reserva dos serviços será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da reserva dos serviços será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a reserva dos serviços deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o responsável recebeu ou assumiu a atividade.

**11.** Clique em **Avançar**.

Caso queira visualizar o fluxo da solicitação, basta acionar a opção **Visualizar fluxo,** ao lado do botão **Avançar**.

**12.** Na etapa **Cadastros**, em **Centro de custo**, informe os centros de custo e seus respectivos responsáveis por fazer as aprovações de viagem. Esses centros de custo poderão ser selecionados no momento da abertura da solicitação.

#f2f2f2#f2f2f2

**Código**Código do centro de custo. Esse código deve ser único, não pode se repetir para mais de um centro de custo.

**Nome do centro de custo**Nome de identificação do centro de custo.

**Gestor do centro de custo**Gestor que será o responsável pelas aprovações enviadas para o centro de custo.

#fdf7e8#fdf7e8

![](https://tdn.totvs.com/download/attachments/563436139/importante.png)

**IMPORTANTE!**  
Depois de finalizada a configuração do *flow*, as informações relacionadas ao centro de custo não podem ser editadas e nem excluídas. Ou seja, ao editar as configurações do *flow* posteriormente, não será possível alterá-las e nem excluí-las.
