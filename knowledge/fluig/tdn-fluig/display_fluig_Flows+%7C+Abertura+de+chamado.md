---
content_hash: 7fc19941baddd3f54a631f90e9fc075e1fc584fc00cc291b3880109826a48d29
fetched_at: '2026-06-28T21:35:29.384270+00:00'
page_id: '745756124'
product: fluig
source: tdn-fluig
title: Flows | Abertura de chamado
type: documentation
url: https://tdn.totvs.com/display/fluig/Flows+%7C+Abertura+de+chamado
version: 50
---

.\*ndice

# Falando de abertura de chamado...

---

O *flow* de abertura de chamado permite que os colaboradores abram um chamado solicitando algum tipo de suporte. Desta forma, ele direciona a solicitação para a equipe que fará a tratativa correta, tudo de forma automatizada.

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
Esse *flow* não está integrado a nenhum ERP e nem a sistemas de abertura de chamados.

]]>

Este *flow* segue as leis gerais de proteção de dados - LGPD. O tratamento de dados pessoais realizado, possibilita que o administrador do Fluig faça a anonimização de dados, caso deseje ou seja solicitado. Para isso, basta acessar: **Painel de controle > Segurança e acesso > Anonimizar e exportar dados pessoais.**

## Como adquirir

---

O *flow* de abertura de chamado é listado como uma solução paga no recurso [Store](https://tdn.totvs.com/x/frOcEw) do TOTVS Fluig Plataforma a partir da atualização **Mist - 1.8.0-230523**.

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

* **Geral**: onde são definidos os dados gerais do processo, como gestor e prazos de expiração e de aviso;

* **Responsáveis**: onde são definidos os responsáveis e o SLA de cada atividade;

* **Cadastros**: onde são definidas as opções que serão selecionadas durante a abertura de solicitação do processo que, nesse caso, são os tipos de ocorrência;

* **Revisão**: onde são listados os principais dados do processo que será criado para conferência.

### Instalar e configurar *flow instalar*

---

100%true5%

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

É possível ainda acessar diretamente pelo ícone da **Store**  localizado no menu lateral, para ir diretamente para os aplicativos.

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso **Store**, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no ***flow* Abertura de chamados.**

**04.** Clique em **Configurar**.

#f2f2f2#f2f2f2

A instalação é iniciada e, quando concluída, uma notificação é emitida.

**05.** Na etapa **Geral**, em **Dados gerais**, defina as informações solicitadas.

#f2f2f2#f2f2f2

**Código identificador do processo**  
Exibe o código de identificação do processo. Não é possível alterá-lo.

**Título do processo**  
Título que visa facilitar o reconhecimento do processo e do seu objetivo. Esse título será exibido posteriormente no recurso .

**Instruções**  
Breve descrição sobre os detalhes do processo e instruções para os solicitantes utilizarem.

**Categoria**  
Categoria na qual o processo se enquadra. Ele será exibido dentro dessa categoria no recurso .

**Pessoa gestora do processo**  
Pessoa que será definida como gestora do processo, ou seja, na ausência do responsável por alguma atividade, essa pessoa pode substitui-lo e continuar com a movimentação da solicitação. Se não for definida uma pessoa gestora, apenas os responsáveis pelas atividades poderão movimentar a solicitação, ou seja, na ausência de algum responsável, a solicitação permanecerá parada. As opções disponíveis são:

* **Um grupo específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado grupo;
* **Um papel específico**: quando selecionada, determina que os gestores serão as pessoas que fazem parte de um determinado papel;
* **Uma pessoa específica**: quando selecionada, determina que o gestor será uma pessoa específica.

**Grupo, papel ou usuário**Grupo, papel ou pessoa que será definida como gestora do processo, de acordo com a opção que foi selecionada em **Pessoa gestora do processo**.

**Prazo de expiração (em horas)**  
Tempo máximo acordado, em horas, durante o qual a solicitação ficará disponível. Ao atingir o tempo máximo, uma notificação é emitida informando que a solicitação expirou. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser menor que o prazo de notificação.

**Prazo de notificação (em horas)**  
Tempo acordado, em horas, para que uma notificação seja enviada antes do prazo de expiração da solicitação. Ao ser configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma. Esse prazo não pode ser maior que o prazo de expiração.

**06.** Clique em **Avançar**.

**07.** Na etapa **Responsáveis**, em **Solicitante**, defina as informações necessárias para cada atividade de quem vai abrir solicitações.

#f2f2f2#f2f2f2

**1 - ABRIR SOLICITAÇÃO**

**Quem poderá abrir uma solicitação**Pessoas que podem abrir solicitação no processo criado por esse *flow*. As opções disponíveis são:

* **Um grupo específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado grupo podem abrir solicitação;
* **Um papel específico**: quando selecionada, determina que todas as pessoas que fazem parte de um determinado papel podem abrir solicitação;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode abrir solicitação;
* **Qualquer pessoa**: quando selecionada, determina que qualquer pessoa pode abrir solicitação.

**Grupo, papel ou usuário**  
Grupo, papel ou pessoa que pode abrir solicitações nesse processo, de acordo com a opção que foi selecionada em **Quem poderá abrir uma solicitação**.

**Acompanhamento**  
Envio de notificação sobre o início da solicitação para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao responsável pela primeira atividade;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da solicitação será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual essa atividade deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante iniciou a solicitação.

---

**2 - COMPLEMENTAR OS DADOS DA SOLICITAÇÃO**

**Acompanhamento**  
Envio de notificação sobre o início da atividade de complemento de informações para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da atividade de complemento de informações será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da atividade de complemento de informações será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da atividade de complemento de informações será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a atividade de complemento de informações deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante recebeu ou assumiu a atividade.

---

**3 - ANALISAR SERVIÇO**

**Acompanhamento**  
Envio de notificação sobre o início da análise do serviço para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da análise do serviço será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da análise do serviço será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da análise do serviço será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a análise do serviço deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o solicitante recebeu ou assumiu a atividade.

**08.** Ainda na etapa **Responsáveis**, em **Analista**, defina as informações necessárias para a atividade de quem vai analisar as solicitações.

#f2f2f2#f2f2f2

**1 - ANALISAR SOLICITAÇÃO**

**Quem poderá analisar a solicitação**Pessoas que podem assumir e analisar a solicitação do processo criado por esse *flow*. As opções disponíveis são:

* **Um grupo específico**: quando selecionada, determina que a solicitação será enviada para um grupo específico e qualquer um do grupo pode analisá-la;
* **Um papel específico**: quando selecionada, determina que a solicitação será enviada para um papel específico e qualquer um do papel pode analisá-la;
* **Uma pessoa de um grupo específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um grupo específico e apenas ela pode analisá-la;
* **Uma pessoa de um papel específico**: quando selecionada, determina que a solicitação será enviada para uma pessoa de um papel específico e apenas ela pode analisá-la;
* **Uma pessoa específica**: quando selecionada, determina que apenas uma pessoa específica pode analisar a solicitação.

**Grupo, papel ou usuário**  
Grupo, papel ou pessoa que pode assumir a solicitação, de acordo com a opção que foi selecionada em **Quem poderá analisar a solicitação**.

**Acompanhamento**  
Envio de notificação sobre o início da análise da solicitação para as pessoas envolvidas. As opções disponíveis são:

* **Notificar responsável**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao responsável por ela;
* **Notificar requisitante**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao requisitante/solicitante;
* **Notificar gestor**: quando assinalada, determina que uma notificação sobre o início da análise da solicitação será enviada ao gestor do processo.

**Prazo de conclusão (em horas)**  
Tempo, em horas, dentro do qual a análise da solicitação deve ser concluída. Após esse tempo, ela será considerada atrasada. Se configurado, o tempo é calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o responsável recebeu ou assumiu a atividade.

**09.** Clique em **Avançar**.

**10.** Na etapa **Cadastros**, em **Categorizar solicitações**, defina os tipos de ocorrência que podem ser atendidas pelo processo criado por esse *flow*. Esses tipos são as opções que poderão ser selecionadas no momento de abertura da solicitação.

#f2f2f2#f2f2f2

**Ordenação**Ordem dos tipos de ocorrência. Ela não pode ser alterada.

**Rótulo**Nome dos tipos de ocorrência que podem ser atendidas pelo processo, como dúvida, apoio, suporte, dentre outros.

**Adicionar mais itens à lista**Número de itens que deseja adicionar à lista de tipos de ocorrência. Para adicionar, basta informar o número e clicar em **Confirmar**.

**11.** Clique em **Avançar**.

**12.** Na etapa **Revisão**, em **Dados do processo**, confira as principais informações do processo que será criado.

#f2f2f2#f2f2f2

Se necessário, clique em **Voltar** até a etapa desejada para ajustar alguma configuração.

**13.** Clique em **Instalar** .

#f2f2f2#f2f2f2

Ao finalizar a instalação, um processo com o nome e na categoria definidos na configuração é listado no recurso .

### Editar *flow*

---

**100%true5%**

**01.** No menu lateral do TOTVS Fluig Plataforma, clique em .

**02.** No agrupador , clique em **[Store](https://tdn.totvs.com/x/frOcEw)**.

#f2f2f2#f2f2f2

Por padrão, apenas administradores da plataforma tem acesso ao Painel de controle e, consequentemente ao recurso Store. Porém, como as permissões podem ser personalizadas, o acesso a esse recurso segue o que foi definido na sua plataforma.

**03.** Na área **Flows** do recurso Store, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) o *flow* Abertura de chamados.

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

**03.** No recurso **Store**, [localize](https://tdn.totvs.com/x/frOcEw#Plataforma%E2%9D%99ItensdaStore-Buscarsolu%C3%A7%C3%B5es) e clique no ***flow* de abertura de chamados**.

**04.** Clique em **Atualizar**.

#f2f2f2#f2f2f2

Para pode utilizar as informações e melhorias da atualização liberada será necessário acessar o configurador do processo clicando em **Configurar**e passar pelas etapas **Geral**, **Responsável**, **Cadastros**e na etapa **Revisão**clicar no botão **Atualizar**.

Ao clicar em atualizar, uma nova versão do processo será criada com todas as correções e melhorias. As solicitações que estão em andamento continuarão com as configurações da versão antiga. Apenas as novas solicitações que forem abertas terão as configurações da nova versão do processo.

Ao realizar estes passos, as novidades e correções serão liberadas para o ***flow* Abertura de chamado**.

## Processo criado

---

Ao finalizar a instalação do *flow*, o processo criado é listado juntamente com os demais processos existentes na plataforma, tanto no recurso  quanto no .

As características do processo criado por esse *flow* são detalhadas a seguir.

### Diagrama

---

O diagrama define como o processo funciona, quais atividades o compõem e qual o caminho que a solicitação segue até a sua conclusão.

Este é o diagrama do *flow* de abertura de chamado:

### Atividades

---

As atividades que compõem o processo são:

Início

Solicitante inicia o processo, preenche as informações necessárias e envia a solicitação.

Analisar solicitação

1. Responsável entende a demanda e pode tomar as seguintes ações:

a. Consegue resolver?

1. 1. 1. **Sim** - envia para a atividade **Analisar Serviço**, de forma que o solicitante possa validar a solução proposta;
      2. **Não** - surgem duas opções:
         1. a atual solicitação possui inconsistências que impedem sua movimentação: nesse caso, a solicitação será **finalizada;**
         2. a atual solicitação carece de informações, o que limita o entendimento da real necessidade do usuário: nesse caso, a solicitação é enviada para a atividade **Solicitar informações ao usuário**, onde a atribuição é automática devolvendo-a para quem solicitou o serviço pedindo mais informações.

Analisar serviço

O solicitante indica se a situação foi resolvida, suas opções são **Sim** ou **Não.** Se foi resolvida, o processo é **finalizado**.Caso contrário, retorna ao técnico responsável para ajuste da solução.

Solicitar informações ao usuário

1. O solicitante precisa colocar informações adicionais para complementar o entendimento sobre sua demanda. Esse complemento pode ser informações adicionais em texto ou anexo de documentos e imagens, conforme o que for mais interessante para ilustrar a situação reportada.

2. Após complementar as informações, o responsável envia a atividade que passará por uma nova análise (atividade **Analisar serviço**), reiniciando o fluxo.

fim

O processo é finalizado.

### Restrições

---

O *flow* de abertura de chamados possui as seguintes restrições:

* não permite ser integrado a outros sistemas;

* não permite personalização, tais como, adicionar campos ao formulário, alterar o diagrama, adicionar ou remover atividades.

#fdf7e8#fdf7e8

![](https://tdn.totvs.com/download/attachments/563436139/importante.png)

**IMPORTANTE!**  
Como esse *flow* se torna um processo igual a qualquer outro dentro da plataforma, é possível alterá-lo ou até mesmo excluir seus artefatos. Porém, se for feita qualquer alteração no processo, diagrama, formulário ou outro artefato, o direito ao suporte padrão é automaticamente perdido.
