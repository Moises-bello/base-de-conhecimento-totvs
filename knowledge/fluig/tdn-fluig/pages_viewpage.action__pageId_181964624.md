---
content_hash: b8beee0c5d880a962d5648e8f797f3cde58133d93653a79e942aeedbcf281041
fetched_at: '2026-06-28T21:35:18.680312+00:00'
page_id: '181964624'
product: fluig
source: tdn-fluig
title: Atualização 1.4.5
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181964624
version: 20
---

false

¿Habla Español? [Haga clic](http://tdn.totvs.com/x/P5TYCg) aquí para ver el Release Notes en Español.

Do you speak English? [Click here](http://tdn.totvs.com/x/bpTYCg) to view the Release Notes in English.

Confira abaixo as novidades na atualização 1.4.5 do Fluig:

## Arquitetura

**Crie e edite grupos de usuários e papéis com mais agilidade**

Ficou mais rápido criar e editar grupos e papéis. No navegador Internet Explorer, otimizou-se estas ações ao vincular usuários, até mesmo quando o número de usuários cadastrados no Fluig é maior que 1000.

## Guia de Estilos

**Novo componente de gráficos**

O novo componente de gráficos já está disponível no Guia de Estilos. Com ele você pode criar gráficos de linhas, barras, pizza, dentre outros, de um jeito simples e rápido. Esse componente é muito útil para demonstração visual e comparação de estatísticas e resultados. Basta informar um elemento DIV onde o gráfico será apresentado e escolher o tipo de gráfico desejado.

Nota

Encontre informações adicionais sobre o componente de gráficos no [Guia de Estilos](http://style.fluig.com/chart.html) do Fluig.

## Identity

**SmartSync com maior desempenho e robustez**

A nova versão do SmartSync conta com maior desempenho e comportamento robusto em caso de oscilação de rede ou instabilidade do servidor Active Directory.

**Mais flexibilidade na administração de empresas**

Agora o administrador de cada empresa pode selecionar se em sua empresa os usuários podem ou não acessar com a senha pessoal.

**Orientação sobre acesso negado**

A partir de agora o Fluig Identity apresenta uma mensagem explicativa ao usuário quando ele utilizar o recurso de auto cadastro informando um domínio não aceito pela empresa.

**Mensagem explicativa para o usuário**

Agora, ao acessar o aplicativo utilizando a senha do Active Directory e acessar a aba Pessoal, é apresentada uma mensagem explicativa ao usuário caso a senha esteja incorreta.

**Atualização de descrição e logotipos de aplicativos**

As descrições e logotipos de aplicativos foram atualizados para os modelos mais atuais, como por exemplo, o logotipo do Outlook.

## Correções

Nessa sessão listamos alguns bugs que matamos nessa atualização que garantem que tudo corra bem na sua plataforma.

* Apresentação da mensagem definida no evento *beforeCommunityLeave -* considerando permissões configuradas em um *dataset -* ao remover um usuário de uma comunidade.

  Nota

  Obtenha informações adicionais sobre esse evento em [Eventos de Customizações Sociais](http://tdn.totvs.com/pages/viewpage.action?pageId=172296472).

* Exibição da descrição de *Pools* e *Swimlanes* que compõem o diagrama de processos que foram exportados do Fluig Studio ou do Eclipse para o Fluig.

  Nota

  Saiba mais sobre *Pool* e *Swimlanes* em .

* Apresentação da mensagem de inconsistência ao movimentar uma solicitação que faça uso de métodos do *Webservice “ECMFolderService”* e é informado um usuário inexistente.

  Nota

  Mais informações sobre esse *Webservice* podem ser obtidas em [Utilização de *Webservices*](http://tdn.totvs.com/pages/viewpage.action?pageId=73084007).

* Atribuição do valor zero (0) ao campo Tamanho da Cota Contratada em MB – localizado na tela Parâmetros Gerais, da aba Gerais do Painel de Controle – quando ele não é preenchido, o que significa que o tamanho será ilimitado.

* Apresentação da data de conclusão definida em uma solicitação do processo AdHoc – Listar Tarefas ao movimentá-la para a próxima etapa sem adicionar tarefas, ou seja, enviá-la para a tarefa Aplicar Solução.

* Movimentação de uma solicitação em que o processo possui duas tarefas automáticas seguidas e na segunda tarefa foi definido o mecanismo de atribuição para um papel.

* Retorno da tarefa Aplicar Solução para a tarefa Criar Tarefas em uma solicitação do processo AdHoc – Listar Tarefas.

* Edição do nome de registros de formulário a partir da opção Renomear, da Navegação de Documentos, quando o novo nome possui mais de 100 caracteres.

* Edição de um formulário durante a configuração de processo, após a liberação de uma versão do processo e o retorno ao formulário para alterá-lo.

* Exibição do botão Responder de formulários publicados em comunidades quando o usuário é membro, não está marcada a opção Listar Conteúdo nas permissões do grupo para o formulário e o formulário pode ser respondido apenas uma vez.

* Configuração de mecanismos de atribuição em tarefas de processos criados no Fluig Studio quando é utilizado o idioma inglês ou o espanhol.

* Retorno do valor de campos de formulário em *datasets* quando o nome dos campos se diferem apenas pelo prefixo “id”, por exemplo “idItem” e “Item”.

* Conexão do *client* ao “version.fluig.com” considerando os parâmetros padrão da VM "http.proxyHost" e "http.proxyPort" para permitir a utilização de *proxy*.

* Remoção de arquivos do diretório de *upload* após efetuar a atualização de um documento utilizando a opção Atualizar Arquivo, disponível na Navegação de Documentos.

* Consulta de um *dataset* de registro de formulário utilizando uma *constraint* com a condição MUST\_NOT.

  Nota

  Para obter mais informações sobre a utilização de *datasets* e *constraints*, acesse [Desenvolvimento de *Datasets*](http://tdn.totvs.com/display/fluig/Desenvolvimento+de+Datasets).

* Ajuste na verificação do horário da última visualização de um documento publicado na Navegação de Documentos ao visualizá-lo novamente.

* Utilização do IP da máquina atual – e não do banco de dados – pelo Monitor de Serviços Fluig para a contagem de usuários.

* Inclusão de anexos por usuários substitutos em tarefas que estão sob sua responsabilidade por conta da substituição.

* Funcionamento do aplicativo Desktop Launcher com todas as versões do Skype e com o aplicativo Spark Messenger.

* Apresentação dos eventos de associação de aplicativos para grupos na *timeline* do usuário no fluig Identity.

* *Script* do DesktopSSO para criptografia da senha do usuário administrador do Active Directory e tratamento único para *e-mails* com caixa alta e caixa baixa.
