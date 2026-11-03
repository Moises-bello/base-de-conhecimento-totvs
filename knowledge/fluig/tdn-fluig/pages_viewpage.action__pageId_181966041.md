---
content_hash: 6f5a99f5da96f352c2044d4e2aa29a0a27b78dd0249043ae68fe15739f0ef0df
fetched_at: '2026-06-28T21:35:18.692993+00:00'
page_id: '181966041'
product: fluig
source: tdn-fluig
title: Atualização 1.4.6
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181966041
version: 27
---

false

¿Habla Español? [Haga clic](http://tdn.totvs.com/pages/viewpage.action?pageId=184780088) aquí para ver el Release Notes en Español.

Do you speak English? [Click here](http://tdn.totvs.com/display/fluigeng/Version+1.4.6) to view the Release Notes in English.

Confira abaixo as novidades na atualização 1.4.6 do Fluig:

## BPM

**Novo método para anexos em solicitações**

Agora você pode anexar um documento publicado na Navegação de Documentos a uma solicitação. Para isso, basta utilizar o novo método *attachDocument* da hAPI, que permite anexar documentos por meio de eventos de *workflow*.

Nota

Clique [aqui](http://git.fluig.com/projects/SAMPLES/repos/sample-document-attach/browse) e confira um projeto de exemplo deste novo método. Se desejar mais informações, acesse a documentação .

## ECM

**Novo evento disponível para documentos**

Já está disponível para utilização o novo evento *beforeDownloadContent* que permite executar procedimentos e validações customizadas antes de efetuar o *download* de um documento.

Nota

Acesse [Desenvolvimento de Eventos](http://tdn.totvs.com/display/fluig/Desenvolvimento+de+Eventos) e confira mais detalhes sobre a utilização do novo evento.

**Informação sobre assinatura digital desabilitada**

Agora o Fluig apresenta uma mensagem informando que a assinatura digital está desabilitada quando o servidor de licenças não está configurado de acordo com os requisitos necessários para a sua utilização.

## Identity

**Plugins de navegadores**

Os novos *plug-ins* dos navegadores Chrome, IE e Firefox permitem a autenticação através de *injection* em widgets do fluig.

O plugin foi adaptado para aceitar que o campo usuário aceite um atributo do tipo 'ID' e o campo senha um atributo do tipo 'name' e vice-versa facilitando o desenvolvimento de aplicativos autenticados.

**Mensagens amigáveis de integração com o Active Directory**

Facilitando a administração das conexões com Active Directory, todas as mensagens de erro foram revisadas e melhoradas trazendo muito mais informação ao administrador do Identity.

**Autenticação intuitiva**

A partir da versão 1.4.6 usuários integrados ao AD escolhem se irão utilizar o e-mail ou usuário de rede durante a rotina de login.

É necessário atualizar o SmartSync para a versão 1.3.3.

Exemplo : o usuário pode informar [lucas@suaempresa.com.br](mailto:lucas@suaempresa.com.br) ou <Dominio>\lucas.

**Nova identidade visual**

Muito mais intuitivo e prático, a versão 1.4.6 traz melhorias de usabilidade na rotina de Launchpad. O recurso foi totalmente modificado trazendo uma nova experiência de navegação aos usuários do Identity.

## Correções

Nessa sessão listamos alguns bugs que matamos nessa atualização que garantem que tudo corra bem na sua plataforma.

* Seleção de atividade destino quando a atividade inicial direciona diretamente para uma atividade automática com decisão baseada em um campo de formulário da solicitação.

* Movimentação de solicitações em dispositivos móveis quando uma atividade do processo possui um mecanismo de atribuição definido por campo de formulário.

* Envio de *e-mails* de acordo com o que foi definido na opção “Notificação de publicação na comunidade” da Central de Notificações.

* Utilização do método “*datasets”* disponível na API pública *Dataset*.

  Nota

  Informações adicionais sobre o método “*datasets*” podem ser obtidas na [API Pública](http://api.fluig.com/resource_DatasetServiceRest.html#path__ecm_dataset_datasets.html) do Fluig.

* Compartilhamento de conteúdo publicado na Navegação de Documentos apenas em comunidades nas quais o usuário participa.

* Publicação de documentos de extensão não suportada pelo visualizador interno na pasta Meus Documentos por meio da opção *drag and drop* (arrastar e soltar).

* Exibição da quantidade de acesso às páginas nas estatísticas apresentadas no relatório do Analytics.

* Envio de *e-mail* com as estatísticas de uso quando o TLS está habilitado.

* Movimentação de solicitação que possui um formulário após concluir uma atividade por meio de um dispositivo móvel.

* Exclusão dos campos descritores relacionados ao formulário de um processo quando o processo é excluído.

* Exportação das tarefas a concluir considerando o filtro definido por processo na Central de Tarefas.

* Desempenho do método “*updateCardData*” do *webservice* *CardService* ao retornar informações quando o formulário em questão possui acima de 600 itens.

* Padronização da opção Imprimir para utilizar a impressão de cópia controlada em todos os locais em que é possível imprimir um documento.

  Nota

  Informações adicionais sobre impressão de cópia controlada podem ser obtidas na página .

* Utilização de *hAPI.setCardValue()* em processos com a atividade inicial do tipo Timer e com formulário associado.

* Visualização de documentos relacionados que foram migrados do ECM 3.0 para o Fluig e que estão publicados na Navegação de Documentos.

* Movimentação de solicitações que possuem registros de formulários relacionados.

* Ao incluir um novo usuário via APIs, os dados de nomenclatura e e-mail são validados.
* Usuários do Active Directory que não possuam a nomenclatura com nome e sobrenome não são mais importados
* Correção de integração com o GoodData caso o cliente utilize o fluig Analytics e o TOTVS SmartAnalytics na mesma empresa
