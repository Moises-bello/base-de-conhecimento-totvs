---
content_hash: 1b050d73a48dc765b5b740403c8cdd3ec9917f821318700a393c693364324d44
fetched_at: '2026-06-28T21:35:18.618377+00:00'
page_id: '172300383'
product: fluig
source: tdn-fluig
title: Atualização 1.4.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=172300383
version: 48
---

Confira abaixo as novidades na atualização 1.4.1 do Fluig:

# Arquitetura

****Mais facilidade e segurança na autenticação integrada****

Agora a configuração de usuário e senha para a autenticação integrada pode ser realiza na tela Configurações do Sistema na aba Autenticação, não sendo mais necessário realizar este procedimento manualmente. Além disso, agora a senha fica criptografada no *script* de autenticação, aumentando a segurança das informações. A geração do *script* também permite a configuração do servidor AD e contexto para pesquisa dos usuários, possibilitando uma configuração mais precisa e confiável para a validação dos usuários na autenticação integrada.

Nota

Mais informações podem ser obtidas em [Configuração Autenticação Integrada](http://tdn.totvs.com/pages/viewpage.action?pageId=162170863).

****Instalador Fluig no idioma Espanhol****

Agora o Fluig conta com a opção de instalação no idioma Espanhol, proporcionando mais dinamismo e facilidade pra quem utiliza e prefere esse idioma.

# BPM

************Mais controle em tarefas para grupos de usuários************

Agora o Fluig não permite que um grupo de usuários seja excluído quando existem tarefas em *pool* definidas para ele e que ainda não foram assumidas.

# Fluig Studio

**Mais informações de conexão**

Agora, na listagem de servidores do *plugin*, quando as informações do servidor são recuperadas com sucesso, é exibido o ícone que representa que ele está conectado e algumas informações sobre a conexão. Caso, contrário, é exibido o ícone que indica que não há uma conexão ativa.

# Social

****Mais flexibilidade em páginas de comunidades****

Agora, para novas comunidades, os moderadores e os administradores também podem definir permissões dos *widgets* ao editar a página.

# WCM

**Consulta rápida de registros de formulários**

*Visualize em tempo real os registros de formulários em sua página ou comunidade!*

Você deseja acompanhar o formulário de uma comunidade? Uma enquete? Com o widget "Listar registros de datasets", é possível consultar rapidamente registros de formulários em sua página ou comunidade.

|  |  |  |
| --- | --- | --- |
|  |  |  |

Confira:

360640

**Novo Widget: Processos**

*Relacione processos workflow às suas comunidades!*

Nesta atualização do Fluig está disponível (mais) um novo widget: Processos! Com ele, é possível selecionar processos favoritos, criar uma lista de processos personalizada ou selecionar todos os processos para serem exibidos.

|  |  |  |
| --- | --- | --- |
|  |  |  |

Veja como é fácil utilizá-lo:

360640

# Guia de Estilos

**Acesse nossos componentes de negócio**

Conheça os nossos componentes de negócio! Acelere o seu desenvolvimento com estes componentes simples e fáceis de utilizar.

Nota

Informações mais detalhadas podem ser obtidas em [Componentes de Negócio](http://tdn.totvs.com/x/OwCLCQ).

**Modal flexível**

Agora o componente de modal possibilita renderizar *widgets* de uma forma simples e rápida. Informe apenas o código de seu *widget* e o *view.ftl* para que ele seja aberto em uma modal.

***Datagrid* mais completo**

Nosso componente de *DataGrid* agora possibilita renderizar dados de *RESTs* simples que retornam apenas a lista de resultados que serão apresentados no *DataGrid.*

# Correções

Nessa sessão listamos alguns *bugs* que matamos nessa atualização que garantem que tudo corra bem na sua plataforma.

* Execução de eventos intermediários condicionais de forma programada por meio da modelagem BPMN.

  Nota:

  Mais informações podem ser obtidas em [Eventos Intermediários](http://tdn.totvs.com/pages/viewpage.action?pageId=126714787).

* Listagem de *colleagueIds* no método *WebService startProcess* do serviço *ECMWorkflowEngine* quando há a utilização do mecanismo de atribuição por campo de formulário.

  Nota

  Mais informações podem ser obtidas em [Utilização de Webservices](http://tdn.totvs.com/x/ZyxbB).

* Visualização de relatórios que utilizam um *dataset* customizado no BIRT.

  Nota

  Mais informações podem ser obtidas em [Desenvolvimento de Relatórios](http://tdn.totvs.com/x/KAJzB).

* Exportação de diagramas com imagens de fim terminal do Studio para a Web.

* Apresentação do nome de atividade intermediária, que foi criada no Studio, no diagrama do processo.

* Permissões na consulta de *datasets* em formulários.

* Movimentação de processos que possuem formulários e que foram acessados a partir do *link* apresentado na notificação de recebimento da solicitação.

* Notificação para os administradores do sistema sobre a expiração da atualização do Fluig utilizada.

* Limite de solicitações por páginas na visualização de "Minhas Tarefas Sob Gerência" na Central de Tarefas.

* Utilização das portas informadas para o *Realtime* no momento da instalação do Fluig.

* Registro de dados na solicitação e nos formulários durante a execução de processos.

* Criação de formulário na Web ou no gerador automático utilizando o código de paginação UTF-8.

* Consulta de *datasets* customizados que possuem um campo do tipo *checkbox* quando utilizada uma *constraint* vazia.

* Evento para não apresentar determinado campo de um formulário em determinada atividade de um processo *workflow* no .

* Movimentação de solicitações com uma propriedade de apontamento de horas atrelada.

* Movimentação de solicitações que possuem anexo *workflow* incluído por intermédio de *upload*.

* *Upload* de *widgets* na Central de Componentes e de arquivos na Navegação de Documentos utilizando o Internet Explorer 9 e o Opera.

* Consulta de *dataset**workflowColleagueRolePK* quando utilizado *alias* muito extenso, ultrapassando o limite de 30 caracteres do banco de dados Oracle.

* Frequência do envio de e-*mail* de notificação de tarefas atrasadas pelo Agendador de Tarefas.

* Exclusão de documentos no resultado de uma busca.

* Conteúdo do *template* de *e-mails* de notificação de tarefas de processo.

  Nota

  Se você possui *template* customizado, o *backup* dele com a correção estará disponível na pasta **<diretório padrão>/templates/tplmail\_backup**.

* Exportação da consulta de solicitações em XLS para exibir de forma separada cada campo de formulário e os responsáveis/datas de conclusão das atividades para cada processo pesquisado, se solicitado, separando-os pelo *header* da coluna no XLS, que contém o código do processo.
* Movimentação de processos que possuem duas atividades automáticas consecutivas.
