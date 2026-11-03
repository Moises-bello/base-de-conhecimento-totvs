---
content_hash: 9bae1545f79b2adca9e02f299a9fe77236fc2840d9a98b470d46763fe350a0f5
fetched_at: '2026-06-28T21:35:18.049712+00:00'
page_id: '146966504'
product: fluig
source: tdn-fluig
title: Atualização 1.3.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146966504
version: 27
---

Confira abaixo as novidades na atualização 1.3.2 do Fluig:

# ECM

**Melhoria na publicação de documentos via WebService**

Agora é possível publicar documento via WebService em nome de outro usuário, utilizando um usuário de integração para autenticação.

Nota

Acompanhe os detalhes dos métodos *createSimpleDocument* e *createDocument* na página .

**Mais eficiência na busca de registros**

A busca de registro de um zoom de formulário está mais eficaz, agora é possível criar formulários que buscam ainda mais registros garantindo performance e retornando resultados precisos.

**Customize mais!**

Agora é possível interceptar e adicionar destinatários aos emails enviados pelo Fluig através de customização, utilizando o evento global onNotify.

Nota

Veja os detalhes na página . Customize!

# BPM

**Maior performance na movimentação de solicitações em bloco**

A capacidade de movimentação de solicitações em bloco foi aprimorada, garantindo maior performance e permitindo que grandes quantidades de solicitações sejam movimentadas de uma vez só.

**Alteração de solicitações workflow via *webservices***

Agora é possível alterar o prazo de uma solicitação workflow configurado para um pool de recursos via *webservices*. Detalhes sobre *webservices* acesse o guia .

**Mensagens mais claras para o usuário**

Otimizada mensagens que são apresentadas ao usuário ao responder um formulário de uma comunidade. Agora, as mensagens de validação dos campos são apresentadas de forma mais clara, indicando exatamente a inconsistência que deve ser corrigida pelo usuário para salvar o formulário com sucesso.

**Melhoria visual na modelagem de processos na web**

Mais comodidade ao verificar os componentes de modelagem de processos em monitores de resoluções menores (ex: 1024x768).

**Melhoria ao 'Iniciar Solicitações' no Fluig**

Foram realizadas melhorias para garantir a inicialização de solicitações mesmo em cenários mais complexos. Crie processos com formulários vinculados, adicione customizações, crie diferentes regras e inicie as solicitações com tranquilidade!

**Otimização de Formulários no Internet Explorer**

Interaja com todos os tipos de campos de formulários em processos workflow. Utilize campos do tipo data, text, textArea, number para compor seu formulário.

**Aprimoramos a visualização de registros de formulário**

Agora, o Fluig apresenta maior consistência na exibição dos registros de formulários criados a partir de processos workflow, que utilizam campos do tipo 'Múltiplos Registros'.

# Social

**Compartilhamento de conteúdo**

Agora quando compartilhamos conteúdo podemos fazer nossos comentários sobre o que estamos divulgando para nosso colegas mantendo o conteúdo original da publicação. Isso torna a informação mais rica deixando todos +Conectados!

# WCM

**Ficou mais ágil gerenciar grupos e usuários no Fluig**

Otimizamos o relacionamento entre Usuários e Grupos! Adicione grupos a determinado usuário, consulte os grupos que o usuário participa com maior facilidade!

**Mais fluidez na criação de layouts**

Os layouts criados a partir do Fluig Studio, agora estão mais fluídos. A criação ocorre sem causar impactos visuais, permitindo utilizar layouts customizados sem preocupação!

Nota

Você que possui layouts criados com o Fluig 1.2.X, os passos para estabilização são simples.

Atualize o Fluig Studio (<http://update.fluig.com>) e realize novamente a exportação do layout para o servidor Fluig.

**Otimizamos a criação de páginas**

Foi otimizado o acesso às páginas públicas criadas no Fluig. Páginas públicas são recursos que podem ser acessados dentro do Fluig mesmo sem fazer login. Crie páginas, acesse, edite, remova!

Lembre-se

Para acessar páginas públicas sem autenticação, deve-se retirar os caracteres "/p" da URL. URL's com os caracteres "/p" sempre passam pelo processo de autenticação

**Novidades na Indexação de Documentos**

Agora é possível realizar a indexação de documentos através do Agendador de Tarefas. Sua funcionalidade é similar a opção *"Indexação de conteúdo novo ou alterado"* existente na indexação, porém, através do Agendador de Tarefas, você poderá definir um horário específico para execução.

**Otimização na edição de Páginas no Fluig**

Foram feitas melhorias para a edição de páginas criadas. Ao editar uma página, as alterações são criadas em um rascunho e apenas após publicá-la as alterações são visíveis na página pelos usuários. Durante a edição você é notificado sobre isso e caso desejar descartar um rascunho de página editada, basta acessar a opção *'Configurações > Descartar Rascunho'*.

# Fluig Studio

**Melhorias na Modelagem de Atividades Serviço**

Agora ficou mais fácil verificar e utilizar todas as propriedades das atividades adicionadas ao editor de modelagem.

**Renomeie diagramas já criados**

Nesta atualização, a partir do Fluig Studio é possível renomear elementos já criados sem perder suas propriedades. Basta uma única ação do usuário: clique sobre o diagrama com o botão direito e em seguida em 'Recriar -> Renomear'.

**Melhorias visuais na edição de processo**

Foram realizadas melhorias referente à atividades com nomes extensos. Além disso processos modelados no Fluig Studio são facilmente exportados para o servidor do Fluig com mais segurança sem causar inconsistências.

**Criação de Webservices CXF**

Agora ficou mais completo! No cadastro de webservices do tipo CXF é possível informar o caminho do arquivo de *bind* em sua geração.
