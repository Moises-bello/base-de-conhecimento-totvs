---
content_hash: 358709a844f03d36961eda0e3150301983b26ecc8f99a4661c0c7ae57f4b2af6
fetched_at: '2026-06-29T00:11:04.186389+00:00'
page_id: '625471503'
product: rm
source: tdn-rm
title: TestePortal Chatbot Carolina | Assistant - Funcionamento Carolina
type: documentation
url: https://tdn.totvs.com/display/LRM/TestePortal+Chatbot+Carolina+%7C+Assistant+-+Funcionamento+Carolina
version: 1
---

none30px

Olá, por aqui você fica por dentro de tudo o que diz respeito ao meu funcionamento (Carolina). É uma ótima oportunidade de conhecer sobre a nova assistente virtual da TOTVS como: consultas, tickets, chat, campos e muito mais!

2

10px100%JORNADA DE ATENDIMENTO CAROLINA

Confira o fluxo da jornada de atendimento da Carolina e mais abaixo maiores detalhes de alguns passos.

true

* **Área logada:** Os chatbots que são disponibilizados em área logada já reconhecem o usuário pelo sem login na própria página. Exemplo: Portal TOTVS.

* **Informar E-mail:** Para ambientes em que o usuário não está logado é necessário que seja informado o e-mail. Essa validação será realizada pela integração com o Zendesk. Os e-mails existentes no Zendesk estarão liberados para o acesso ao chatbot. Essa validação é necessária, pois são criados tickets por acesso, e para isso é essencial o solicitante.

* **Contatar com o Adm da Conta:** Toda organização possui um administrador da conta, esse usuário permite os ajustes no portal, com isso podem adicionar novos contatos. O usuário pode fazer 3 tentativas até que apresente a mensagem para entrar em contato com o Administrador.

* **Pesquisar módulos pelo macrossegmento:** É possível consultar os módulos que estão contemplados na assistente, aqueles que ela tem conteúdo para ajudar. Pode buscar no primeiro passo antes de iniciar a pergunta, ou em qualquer momento digitando macrossegmento.

* **Consultar sobre o produto:** Esta busca é realizada com o apoio dos artigos no modelo KCS. A partir de um modelo de integração é possível consultar soluções relacionadas aos artigos já criados no Guide da TOTVS.

* **Continuar no módulo da consulta anterior:** Após fazer o primeiro acesso, a Carolina já tem o histórico da sua última consulta, desta forma ela consegue continuar da onde o usuário parou.

* **Informar módulo:** Para a consulta ser com um filtro maior, o usuário precisa digitar o módulo que quer consultar, caso ele digite um módulo que exista em mais de um produto, todos serão apresentados e o usuário poderá selecionar o que deseja.

* **Informar dúvida:** A dúvida deve ser digitada com no mínimo 2 (duas) palavras.

* **Consultar no módulo informado:** O modelo faz a busca nos artigos vinculados ao módulo informado. Caso encontre uma resposta ele mostrará os 3 (três) artigos com maiores combinações. A apresentação será o conteúdo o artigo com maior combinação e os outros dois artigos (se existir) serão apresentados em formato de “link”.

* **Consultar família de módulos:** Caso não tenha um retorno dentro do módulo, será consultado os artigos dentro da família de módulos, a família pode ser cadastrada independente do módulo. Eles serão consultados de forma conjunta.

* **Exibir os 5 artigos mais buscados:** a partir do Analytics é possível identificar os artigos mais consultados dentro de cada seção do guide. Se a Carolina encontrar mais de 10 (dez) artigos dentro da busca que o usuário realizou, ela vai apresentar o link dos 5 (cinco) artigos mais buscados no portal, dentro dos 10 (dez) com maior combinação.

* **Apresentar pesquisa de satisfação:** A pesquisa utilizada na Carolina é “positivo” e “negativo”, conforme a resposta dada é uma ação que é executada. Se positivo, retorna ao início para o cliente digitar outra dúvida. Se negativo a Carolina questiona o motivo que a pesquisa não atendeu (Resposta não corresponde à busca, Retorno coerente, porém minha dúvida não foi respondida, Resposta correta, porém conteúdo está muito simples ou complexo e Outros).

* **Informar um comentário:** Caso o usuário clique em “Outros” será habilitada a opção para digitar o motivo que o cliente negativou, de forma livre.

* **Abrir ticket:** Caso o usuário esteja fora do horário de operação (07h às 19h) ou o departamento indicado para a consulta realizada esteja com seus analistas offline, será disponibilizada a criação de ticket. Para criação de ticket o usuário deverá informar o assunto e a descrição da solicitação. O ticket será gerado com o status “Novo” e com os campos do catálogo preenchidos, no grupo indicado pelo catálogo de serviços. Será um ticket de atendimento que ficará em Backlog.

* **Abrir Chat Online:** O chat online será disponibilizado quando estiver dentro do horário de operação (07h às 19h) e o departamento indicado para a consulta realizada estará com seus analistas online. Será apresentada outra janela na própria conversa da Carolina em que o cliente poderá interagir com o analista.

* **Consultar uma solicitação:** Ao clicar em consultar uma solicitação, deverá ser informado o ticket para consulta. Será apresentado o número da solicitação, data de criação, assunto (título), tipo do ticket (como é mostrado dentro do portal de clientes e não no Zendesk) e status. Como no formato a seguir:

*A solicitação 123456 criada em 10/11/2016 sobre Ref. MAPA EDI cobrança HSBC, com o tipo Suporte Técnico está Fechada.*

Caso for um ticket com o status pendente ou aguardando validação, será apresentado o conteúdo do último comentário público.

CRIAÇÃO DE TICKETS (RESOLVIDOS)

Para volumetria de atendimento dentro do Zendesk, são geradas solicitação resolvidas dentro do Zendesk. Desta forma é possível medir as consultas sobre o produto.

**1-** Quando são criados tickets resolvidos?

**R.:** Os tickets Resolvidos são criados somente quando o usuário realiza uma consulta sobre o produto, para cada consulta realizada é gerado um ticket.

**2 -** O usuário é notificado da criação deste ticket?

**R.:** O usuário não é notificado da criação dos tickets, pois os tickets gerados são somente para controle interno, e não devem ser consultados pelo cliente.

**3 -** O usuário não tem visibilidade do ticket no portal?

R.: O ticket não fica visível para o cliente no portal, isso é possível pois o comentário do ticket foi definido como privado.

**4 -** Quais informações são enviadas no ticket?

**R.:** Campos preenchidos:

* Título do ticket = Pergunta feita pelo usuário.
* Solicitante = Identificado pelo email que foi o acesso na Carolina;
* Organização = Organização que o Solicitante está vinculado;
* Status = Resolvido;
* Impacto = Baixo;
* Tipo da Solicitação = Suporte técnico;
* Causa = Orientação de processo;
* Catálogo de serviços

+ País
+ Macrossegmento
+ Produto
+ Módulo
+ Agrupador de rotina (quando o campo é existente)

* Chatbot (informa a origem do acesso)

+ Portal
+ Totvs News
+ Ícone dentro do protheus

* Tags = ‘origem\_ticket\_carol\_assistant’, ‘assistant\_ticket\_closed’, Tag identificador do segmento ('Plataformas': 'assistant\_plataformas', 'Supply': 'assistant\_supply', 'Saúde': 'assistant\_saude', 'Services': 'assistant\_services')
* Satisfação Carol Assistant

+ Ruim = csat\_bad
+ Bom = csat\_good

* Carol: Motivo Negativado

+ Resposta não corresponde a busca;
+ Retorno coerente, porém minha dúvida não foi respondida;
+ Resposta correta, porém conteúdo está muito simples ou complexo;
+ Outros;

* Obs. Pesquisa Carolina = Resposta aberta

+ Quando o usuário seleciona outros, é disponibilizado o campo para resposta aberta.

**5 -** Comentário do ticket:

**R.:** O comentário é apresentado no modo privado, pois possibilita que o usuário não consulte a solicitação.

No comentário são apresentadas as seguintes informações:

* Produto que foi realizada a consulta;
* Módulo que foi realizada a consulta;
* Perguntas feitas pelo usuário - caso tenha feito mais de uma pergunta, elas são exibidas em ordem, o usuário terá até 3 tentativas caso não tenha resposta para uma consulta;
* Título do primeiro artigo apresentado;
* Resposta = Primeiro trecho do artigo;
* URL do artigo apresentado na resposta = todos os links disponíveis na resposta, o primeiro link será o da resposta que foi apresentado o conteúdo.
TRANSBORDO DE ATENDIMENTO

O transbordo de atendimento acontece quando a Carolina não consegue ajudar o usuário, neste caso ele poderá se comunicar diretamente com um analista pelo chat online ou criar um ticket novo para a equipe de suporte.

O direcionamento dessas demandas é realizado por regras de catálogo de serviço.

2

10px100%Chat Online

Para que o usuário consiga realizar o transbordo para o chat online, é necessário:

* Esteja dentro do horário de atendimento 07h às 19h;
* Os analistas estejam com o status Online.

Toda vez que o feedback for negativado (se estiver dentro das regras acima), será apresentada a opção para o usuário conversar com um analista.

O chat online é totalmente integrado com o Zopim (Zendesk Chat). Quando ele é acionado é apresentada uma aba para separá-lo da conversa que já está acontecendo com a Carolina.

Na aba do chat online o usuário pode enviar mensagens, anexos, feedback do atendimento humano, e encerrar o atendimento para retornar para a Carolina.

Para o analista que está atendendo, o acionamento é o mesmo que já é realizado pelo pré chat no portal. Mas no caso da Carolina, será enviado o histórico da conversa, ou seja, o analista terá acesso à última consulta do usuário na Carolina.

O Analista também poderá enviar outros conteúdos e até mesmo anexos nesta conversa.

Para identificar os atendimento que são transbordo da Carolina, é enviada a tag “transbordo\_assistant”.

Ticket Novo

A ação de criação de um ticket novo ocorre quando o feedback é negativo, mas somente fora do horário de atendimento das 07h às 19h, ou quando todos os analistas estão offline.

Este ticket não é considerado um ticket de curadoria e sim de atendimento, pois estará no backlog da equipe. Mesmo com a geração deste ticket, na consulta será gerado um ticket de volumetria (ticket resolvido) para que a curadoria analise.

No momento da criação do ticket existem alguns parâmetros que precisam ser informados pelo usuário.

A Carolina pergunta se o usuário quer adicionar e-mails em cópia, se o cliente responder “Sim”, ele poderá informar os e-mails para acompanhar a solicitação. Após essa etapa a Carolina solicita um título para a solicitação e em seguida pede para detalhar o ticket. 

Quando todos os dados são informados, a Carolina apresenta como será enviado o ticket para o suporte.

Neste momento o cliente tem a opção de desistir do envio do ticket, alterar o que ele informou e confirmar o envio.

O ticket é enviado com os seguintes dados:

* Título do ticket = Informado pelo usuário com o identificar “[Assistant]” no início.
* Solicitante = Identificado pelo email que foi o acesso na Carolina;
* E-mails em cópia = Se informado pelo usuário;
* Organização = Organização que o Solicitante está vinculado;
* Formulário = Suporte Técnico;
* Status = Novo;
* Tipo = Pergunta;
* Impacto = Baixo;
* Tipo da Solicitação = Suporte técnico;
* Causa = Orientação de processo;
* Catálogo de serviços = Conforme o acesso feito pelo usuário no decorrer da conversa com a Carolina.

+ País
+ Macrossegmento
+ Produto
+ Módulo
+ Agrupador de rotina (quando o campo é existente)

* Chatbot (informa a origem do acesso)

+ Portal
+ Totvs News
+ Ícone dentro do protheus

* Tags = ‘origem\_ticket\_carol\_assistant’, ‘origem\_ticket\_carol\_assistant\_\_\_new’, ‘assistant\_ticket\_new’, Tag identificador do segmento ('Plataformas': 'assistant\_plataformas', 'Supply': 'assistant\_supply', 'Saúde': 'assistant\_saude', 'Services': 'assistant\_services')

Comentário do ticket:

O comentário é apresentado no modo público, para o acompanhamento do solicitante.

No comentário são apresentadas as seguintes informações:

* Detalhamento da solicitação que foi solicitado ao usuário antes da criação do ticket;
* Perguntas feitas pelo usuário na interação com a Carolina;
* URL do artigo apresentado na resposta.

A identificação dos tickets que foram transbordados como ticket novo é realizada pela tag “assistant\_ticket\_new”.

CONSULTA DE SOLICITAÇÕES

No portal existe uma regra para os clientes visualizarem status e tipos de tickets, isso foi replicado para Carolina, para não existir diferenciação nas consultas.

Como está o De Para na Carolina para o status e tipo do ticket:

Status do Ticket:

* new = Aberta,
* open = Aberta,
* pending = Aguardando sua validação,
* hold = Aberta,
* solved = Aguardando sua aprovação,
* closed = Fechada.

Tipo do ticket:

* Manutenção

+ Marcar = TOTVS,
+ Tipo = Problema
+ Tag = “issue\_criada\_jira” ou “issue\_associacao\_incidente”,

* Customização

+ Marcar = TOTVS,
+ Tipo = Tarefa
+ Classificação = Solicitação de customização

* Inovação

+ Tipo = Tarefa
+ Classificação = Sugestão de melhoria

* Legislação

+ Tipo = Tarefa
+ Classificação = Solicitação de legislação

* Administrativo:

+ Marca = TOTVS CST

* Suporte Técnico:

+ Diferente das regras anteriores.

Para visualizar os tickets existem algumas regras:

* Os usuários que são Agentes do Zendesk podem visualizar todos os tickets;
* A consulta deve ser pelo solicitante do ticket;
* Caso não for existem alguns cenários que o usuário poderá visualizar o ticket;

+ Deve estar em cópia na solicitação;
+ O usuário é o administrador da conta no portal;
+ A organização tem permissão para que todos os contatos visualizem os tickets;
+ O usuário tem permissão para visualizar todos os tickets da organização.

O que é apresentado na consulta de tickets:

* Número do ticket;
* Data de criação do ticket;
* Título do ticket;
* Tipo do ticket, conforme regras informadas anteriormente;
* Status do ticket, conforme regras informadas anteriormente;
* Data de acordo - se estiver preenchida e for maior que a data atual;
* Último comentário público do analista - se estiver com o status Pendente ou Resolvido;
* Link do detalhamento do ticket no portal.

É possível consultar outra solicitação, ou retornar ao início do fluxo. 

**Importante**: Essa consulta não gera tickets de volumetria.

CATÁLOGO DE SERVIÇOS

Para que a Carolina se comunicasse com o Zendesk de forma eficiente, ela precisaria tratar o principal identificador e direcionador utilizado no atendimento, ou seja, o Catálogo de Serviços.

2

10px100%Funcionamento do catálogo de serviços dentro da plataforma Carol

Diferente do Zendesk, foram criados vínculos necessários para que o catálogo fosse identificado pela Carolina. Esse vínculo é realizado pelo artigo apresentado para o usuário.

Para o usuário encontrar um conteúdo na Carolina ele precisa informar o módulo que quer tirar sua dúvida, a partir deste momento a Carolina começa a conversar com o catálogo de serviços.

O catálogo de serviços na plataforma está da seguinte forma:

* ID da seção = O ID da seção é o identificador das seções, pois podemos ter nomenclatura iguais, mas nunca códigos iguais, por este motivo é utilizado.
* Seção = Nomenclatura da seção que estão os artigos.
* Produto = Nome do produto conforme está no catálogo oficial da TOTVS.
* Módulo = Nome do módulo conforme está no catálogo oficial da TOTVS.
* Agrupador de Rotina = Nome do agrupador de rotina conforme está no catálogo oficial da TOTVS.
* Departamento = Departamento de chat padrão para o direcionamento do transbordo de Chat Online.
* Departamento Prime = Departamento de chat prime para o direcionamento do transbordo de Chat Online.
* Tags = Tags relacionadas às opções do catálogo de serviços.
* Grupo de atendimento = Grupo que serão direcionados os tickets de volumetria e de transbordo de tickets novos.

O relacionamento dessas informações é criado pelo próprio segmento.

* Antes de qualquer coisa, é necessária a definição das seções do Guide (ambiente dos artigos), onde a Carolina consultará.
* Em uma planilha serão informados o nome da seção e o ID dela.
* Agora é feito o relacionamento dos módulos, a Seção XXX deve combinar com o Módulo ZZZ. Com isso, quando o usuário acessar a Carolina, ele vai informar o módulo ZZZ, e a Carolina vai buscar os artigos que estão na seção XXX.
* O grupo de atendimento e departamento, funcionam da mesma forma.
* Na imagem abaixo, podemos visualizar o levantamento da seção e do código da seção. A informação do nome da seção está disponível na página da seção e o ID na URL da página da seção.
* Na imagem abaixo, podemos visualizar o levantamento do catálogo de serviços. O catálogo de serviço pode ser visualizado no próprio ticket, ou pode ser solicitada uma lista do catálogo dos módulos que são necessários.
* Na imagem abaixo, podemos visualizar o levantamento do grupo de atendimento e os departamentos padrão e prime. O Grupo de atendimento deve ser consultado no Zendesk e o Departamento é localizado no Zendesk Chat (Zopim), a nomenclatura dessas informações devem ser corretas, pois pode não ser direcionado corretamente por um erro de digitação.
* O usuário que estiver em uma organização prime, será identificado no seu cadastro pela própria Carolina, e o direcionamento do ticket e do chat será de acordo com o que está configurado no Zendesk.
5%
#title-text {
display: none !important;
}
]]>
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 5px;
padding-right: 5px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.expand-control-text {
color: #000000;
font-size: 17px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #16c4d6;
}
a:not(.aui-button,.aui-dialog2-header-close) {
color: #5c4397;
}
.aui-label {
background-color: #bae5ea;
font-size: 15px;
}
.wiki-content img.confluence-embedded-image, .wiki-content img.editor-inline-macro, .wiki-content table.wysiwyg-macro {
cursor: pointer;
}
]]>
