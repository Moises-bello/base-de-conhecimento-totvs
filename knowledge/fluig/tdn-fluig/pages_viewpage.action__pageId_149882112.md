---
content_hash: 4c370d41bf1343c5a9e36d920c73b38d74a3f7c8d6b8ce4448d8e92879c7cad5
fetched_at: '2026-06-28T21:35:18.126060+00:00'
page_id: '149882112'
product: fluig
source: tdn-fluig
title: Atualização 1.3.4
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149882112
version: 43
---

Confira abaixo as novidades na atualização 1.3.4 do Fluig:

# ECM

******Publicação de PDFs com mais tranquilidade******

Agora, na publicação de PDFs, o Fluig verifica a versão do documento e indica qual é a melhor opção de visualizador interno para ser utilizado.

******Webservice ECMDocumentService******

Nesta atualização, foi otimizada a atribuição de valor do campo "*InternalVisualizer*" na publicação de documentos por meio de webservice.

Nota

Informações adicionais sobre webservices disponíveis no Fluig podem ser obtidas em [Utilização de Webservices](http://tdn.totvs.com/x/ZyxbB).

********Consulta por *Dataset* mais eficiente********

A consulta por meio de *Dataset* foi aperfeiçoada para garantir a integridade dos dados retornados quando são utilizados formulários com pai-filho, independente da forma de armazenamento dos dados.

# BPM

******Mais compatibilidade em formulários******

Foi aperfeiçoada a edição de formulários antigos na Web para torná-los compatíveis com novos atributos, tais como o tamanho.

******Central de tarefas aperfeiçoada e mais rápida******

A central de tarefas está otimizada e mais rápida, contando com as seguintes melhorias:

* foi aprimorada a apresentação das Minhas Solicitações, permitindo a visualização de todas as solicitações iniciadas pelo usuário, inclusive processos que contenham sub processos;
* agora, ao acessa-la, você visualizará suas pendências com redução de até 95% no tempo de apresentação da listagem de tarefas.

Nota

Para possibilitar esse salto de performance no produto, não é mais apresentado o total de tarefas existentes no item Minhas Tarefas sob Gerência.

******Expediente padrão mais dinâmico******

O expediente padrão considerado pelo Fluig para a realização de tarefas está mais dinâmico, agora é possível personaliza-lo de acordo com as preferências de horário praticadas na empresa.

# Social

******Extração de dados de formulários mais completa******

A extração de respostas dos formulários está mais completa. Agora, além dos dados já exibidos, é apresentado também o *e-mail* do usuário que respondeu o formulário, facilitando e agilizando um possível contato com ele.

******Mais praticidade no mural de avisos******

O mural de avisos está mais prático e permitindo buscas mais específicas. Agora ele conta com o filtro por Artigos, agilizando a busca do arquivo desejado.

******Timeline de comunidades mais leve******

Nessa atualização, a publicação de artigos somente é apresentada na timeline quando o artigo é criado. Quando o artigo é alterado, não é gerada uma nova publicação, tornando a timeline visualmente mais agradável.

******Notificação de formulários futuros aprimorada******

A partir de agora, ao criar um formulário com data de início futura em uma comunidade, os participantes dela recebem a notificação somente na data em que o formulário for publicado, ou seja, na data em que ele estará disponível para ser respondido.

******Mais praticidade na inclusão de usuários por grupo em comunidades******

Está mais dinâmico incluir usuários por grupo em uma comunidade. Agora, é possível navegar pelo sistema enquanto o processo de inclusão dos usuários está em andamento.

********Pesquisa em ambientes com nuvem de acesso mais segura********

A busca do Fluig agora está ainda mais segura. Em ambientes com nuvem de acesso, agora são considerados filtros de nuvem de relacionamento para segregar os resultados de publicações e comunidades, garantindo a privacidade das informações de acordo com as permissões definidas.

********Mais usabilidade e aparência renovada********

Essa atualização do Fluig conta com melhorias na usabilidade e apresentação de títulos e campos:

* foi otimizada a apresentação do título das categorias de artigos em comunidades;
* foi aperfeiçoada a disposição dos campos de filtro da busca global.

**********Mais acessibilidade para artigos**********

Agora, durante a navegação entre os artigos de uma comunidade, depois de visualizar um artigo, é possível retornar para os artigos da mesma categoria do artigo visualizado anteriormente, facilitando e agilizando o acesso.

# Arquitetura

******Mais velocidade no *deploy* com SQL Server******

Foi aperfeiçoado o processo de *deploy* com SQL Server, o que contribui para que o servidor esteja disponível mais rapidamente e com mais eficiência.

******Mais segurança na criação de grupos de usuários******

Criar grupos e subgrupos de usuários está mais seguro. Agora o Fluig avisa quando um caracter não pode ser utilizado no código do grupo ou subgrupo, garantindo assim a integridade das informações.

# Fluig Studio

******Mais facilidade na utilização de mecanismo de atribuição customizado******

Agora é possível relacionar um mecanismo de atribuição customizado – que foi criado no Fluig Studio e exportado para o Fluig – a uma tarefa sem precisar configurá-lo.
