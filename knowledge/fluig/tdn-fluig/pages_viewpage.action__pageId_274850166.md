---
content_hash: 0517bb84b4623f6ab99cd2b039c1eac39647ac39289a203130f8de048786c3a0
fetched_at: '2026-06-28T21:35:25.241635+00:00'
page_id: '274850166'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Recursos de aprendizado e avaliações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274850166
version: 90
---

# Índice

true.\*ndicenone

## Falando de recursos de aprendizado e avaliações...

Por meio das opções de permissão de aprendizado e avaliações existentes no Painel de Controle é possível liberar ou restringir recursos para usuários específicos, papéis ou grupos de usuários. É possível, por exemplo, ocultar recursos que por padrão são visíveis ou liberar recursos de administração para um usuário comum.

Para que um usuário tenha acesso a um recurso, é necessário que ele possua permissão para visualizar a página e o *widget* desse recurso.

**Exemplo**:  
Utilizando o recurso Avisos como exemplo, seriam necessárias as permissões:

* **para visualizar a página Avisos**: ao liberar essa permissão o usuário em questão poderá visualizar o recurso Avisos no menu Aprendizado e visualizar o conteúdo (listagem de avisos existentes) desde que tenha também permissão no *widget* Avisos. Nesse exemplo, se o usuário possuir apenas permissão na página Avisos mas não possuir no *widget* Avisos, ele visualizará esse recurso no menu Aprendizado, porém, sem conteúdo, pois a página será exibida em branco.

* **para visualizar o *widget* Avisos**: ao liberar essa permissão o usuário em questão poderá visualizar esse *widget* em qualquer página na qual ele existir, desde que também tenha permissão para visualizar a página. Nesse exemplo, se o usuário possuir apenas permissão no *widget* Avisos mas não possuir na página Avisos, esse recurso nem aparecerá no menu Aprendizado.

* **para executar ações específicas**: ao liberar permissão em ações específicas, o usuário em questão poderá executá-las. Nesse caso, ao ativar, por exemplo, a permissão Salvar da gerência de avisos, o usuário poderá incluir e editar avisos; ao ativar a permissão Remover ele poderá remover os avisos existentes. As ações específicas podem ser efetuadas desde que o usuário também possua permissão para visualizar o *widget* e a página de avisos, pois caso contrário, não visualizará nem o recurso em si e nem as ações específicas.

Opções de permissão em páginas e widgets

As opções de permissão existentes para as páginas são as mesmas para cada uma delas. O mesmo ocorre com os *widgets*.

Essas permissões estão detalhadas em  e Opções de permissão em *widgets*.

## Recursos de aprendizado

As páginas, os *widgets* e as permissões específicas de aprendizado são listadas a seguir.

### Menu aprendizado

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página do item  do menu principal, onde são agrupados os recursos de aprendizado. | PAGE | Aprendizado - menu aprendizado (página) - pagelearning | Detalhadas em . |

#### Meu aprendizado

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Aprendizado do menu principal – que exibem os itens nos quais o aluno está matriculado, seu histórico em turmas, trilhas e treinamentos e suas atividades extraclasse. | PAGE | Meu aprendizado - pagemyplan | Detalhadas em . |
| WIDGET | Aprendizado | Detalhadas em Opções de permissão em *widgets*. |

#### Tarefas de aprendizado

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  que pertence ao item Aprendizado do menu principal. | PAGE | Tarefas de aprendizado - pagelearntasks | Detalhadas em . |
| WIDGET | Tarefas de aprendizado | Detalhadas em Opções de permissão em *widgets*. |

#### Disciplinas e turmas

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Aprendizado do menu principal – que exibem o catálogo de disciplinas e turmas. | PAGE | Disciplinas e turmas - pagecatalogdiscipline | Detalhadas em . |
| WIDGET | Disciplinas e turmas | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento do catálogo de disciplinas e turmas. | LMSDIS | Aprendizado - Catálogo de disciplinas e turmas | * **Ler**: quando ativada, permite visualizar o catálogo de disciplinas e turmas. Os itens do catálogo serão exibidos conforme as permissões definidas em cada um deles, inclusive considerando as permissões definidas na [pasta raiz](https://tdn.totvs.com/x/Bv7uDQ#Plataforma%E2%9D%99Disciplinaseturmas-Editarcat%C3%A1logo), ou seja, se não for liberada pelo menos permissão de leitura na pasta raiz, o catálogo será exibido vazio, mesmo que a opção **Ler** esteja ativa.  * **Ignorar restrições**: quando ativada, permite visualizar o catálogo de disciplinas e turmas como se fosse um usuário administrador, ou seja, ignorando todas as restrições e ausência de permissões nos itens. |
|  | Página e *widget* que exibem os detalhes de uma disciplina. | PAGE | Visão da disciplina - pagedisciplineview | Detalhadas em . |
| WIDGET | Visão da disciplina | Detalhadas em Opções de permissão em *widgets*. |
|  | Página e *widget* de execução de uma , ou seja, que exibem os tópicos da turma para os alunos que estão matriculados. | PAGE | Execução de turmas - pagelearningclass | Detalhadas em . |
| WIDGET | Execução de turmas | Detalhadas em Opções de permissão em *widgets*. |
|  | Permissão específica para o gerenciamento da  de turmas. | LMSWAI | Aprendizado - Gerência de lista de espera | * **Acessar**: quando ativada, permite gerenciar a lista de espera de turmas. O usuário que possui essa opção ativa está apto a ser definido como responsável por gerenciar a lista de espera da turma no cadastro da  ou da  e pode visualizar as opções [Salvar](https://tdn.totvs.com/x/IfzuDQ#Plataforma%E2%9D%99Listadeespera-Alterarprioridadedoalunonalistadeespera) – para editar a prioridade do aluno na lista – e [Remover](https://tdn.totvs.com/x/IfzuDQ#Plataforma❙Listadeespera-Removeralunodalistadeespera) – para remover o aluno da lista – na página de gerenciamento da lista de espera das turmas pelas quais é responsável por essa atividade. |

#### Trilhas e treinamentos

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Aprendizado do menu principal – que exibem o catálogo de trilhas e treinamentos. | PAGE | Trilhas e treinamentos - pagecatalogtrainingtrack | Detalhadas em . |
| WIDGET | Trilhas e treinamentos | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento do catálogo de trilhas e treinamentos. | LMSCAT | Aprendizado - Catálogo de trilhas e treinamentos | * **Ler**: quando ativada, permite visualizar o catálogo de trilhas e treinamentos. Os itens do catálogo serão exibidos conforme as permissões definidas em cada um deles, inclusive considerando as permissões definidas na [pasta raiz](https://tdn.totvs.com/x/SPzuDQ#Plataforma%E2%9D%99Trilhasetreinamentos-Editarcat%C3%A1logo), ou seja, se não for liberada pelo menos permissão de leitura na pasta raiz, o catálogo será exibido vazio, mesmo que a opção **Ler** esteja ativa.  * **Ignorar restrições**: quando ativada, permite visualizar o catálogo de trilhas e treinamentos como se fosse um usuário administrador, ou seja, ignorando todas as restrições e ausência de permissões nos itens. |
|  | Página e *widget* que exibem os detalhes de uma [trilha](https://tdn.totvs.com/x/Hf7uDQ#Plataforma%E2%9D%99Trilha-Visualizarinforma%C3%A7%C3%B5eseitensdatrilha) ou de um [treinamento](https://tdn.totvs.com/x/Gv7uDQ#Plataforma%E2%9D%99Treinamento-Visualizarinforma%C3%A7%C3%B5eseconte%C3%BAdodotreinamento) existente no catálogo. | PAGE | Visão do Treinamento/Trilha - pagetrainingtrackview | Detalhadas em . |
| WIDGET | Visão de trilhas e treinamentos | Detalhadas em Opções de permissão em *widgets*. |
|  | Página e *widget* de execução de uma  ou , ou seja, que exibem os itens da trilha ou do treinamento para os alunos que estão matriculados. | PAGE | Execução de trilhas e treinamentos - pagelearningtrainingtrack | Detalhadas em . |
| WIDGET | Execução da trilha e treinamento | Detalhadas em Opções de permissão em *widgets*. |

#### Administrar

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página que agrupa os recursos do item  que pertence ao item Aprendizado do menu principal. | PAGE | Administrar - app\_\_lms\_\_learning\_\_admin | Detalhadas em . |

##### Conteúdos

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Administrar, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem os conteúdos e as ações que podem ser efetuadas sobre eles. | PAGE | Conteúdos - app\_\_lms\_\_learning\_\_contents | Detalhadas em . |
| WIDGET | Conteúdos | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de conteúdos. | LMSCONT | Aprendizado - Gerência de conteúdos | * **Ler**: quando ativada, permite visualizar a lista de conteúdos existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhum conteúdo.  * **Visualizar todos os conteúdos**: quando ativada, permite visualizar todos os conteúdos existentes, inclusive os que foram definidos como particular. Usuários que possuem essa opção ativa podem visualizar a opção [Pré-visualizar](https://tdn.totvs.com/x/dv7uDQ#Plataforma%E2%9D%99Conte%C3%BAdos-Pr%C3%A9-visualizarconte%C3%BAdo) na página de conteúdos.  * **Salvar**: quando ativada, permite incluir e editar conteúdos. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/dv7uDQ#Plataforma❙Conteúdos-Adicionarconteúdo) e [Editar](https://tdn.totvs.com/x/dv7uDQ#Plataforma❙Conteúdos-Editarconteúdo) na página de conteúdos.  * **Remover**: quando ativada, permite remover qualquer conteúdo existente. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/dv7uDQ#Plataforma❙Conteúdos-Removerconteúdo) na página de conteúdos. |

##### Certificados

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Administrar, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem os certificados e as ações que podem ser efetuadas sobre eles. | PAGE | Certificados - pagecertificates | Detalhadas em . |
| WIDGET | Certificados | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de certificados. | LMSCER | Aprendizado - Gerência de Certificados | * **Ler**: quando ativada, permite visualizar a lista de certificados existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhum certificado.  * **Salvar**: quando ativada, permite incluir e editar certificados. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/9oz5DQ#Plataforma❙Certificados-Adicionarcertificado), [Editar](https://tdn.totvs.com/x/9oz5DQ#Plataforma❙Certificados-Editarcertificado), [Ativar](https://tdn.totvs.com/x/9oz5DQ#Plataforma❙Certificados-Ativarcertificado)/[Inativar](https://tdn.totvs.com/x/9oz5DQ#Plataforma❙Certificados-Inativarcertificado) na página de certificados.  * **Remover**: quando ativada, permite excluir certificados existentes. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/9oz5DQ#Plataforma❙Certificados-Removercertificado) na página de certificados. |

##### Habilidades

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Administrar, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem as habilidades e as ações que podem ser efetuadas sobre elas. | PAGE | Habilidades - pageskills | Detalhadas em . |
| WIDGET | Habilidades | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de habilidades. | LMSSKL | Aprendizado - Habilidades | * **Ler**: quando ativada, permite visualizar a lista de habilidades existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhuma habilidade.  * **Salvar**: quando ativada, permite incluir e editar habilidades. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/f-7uDQ#Plataforma❙Habilidades-Adicionarhabilidade) e [Editar](https://tdn.totvs.com/x/f-7uDQ#Plataforma❙Habilidades-Editarhabilidade) na página de habilidades.  * **Remover**: quando ativada, permite excluir habilidades existentes. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/f-7uDQ#Plataforma❙Habilidades-Removerhabilidade) na página de habilidades. |

##### Configurações de trilhas e treinamentos

|  | Descrição | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Administrar, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem as configurações disponíveis para trilhas e treinamentos. | PAGE | Configuração de trilhas e treinamentos - pagetrainingtrackconfiguration | Detalhadas em . |
| WIDGET | Configurações de trilhas e treinamentos | Detalhadas em Opções de permissão em *widgets*. |

##### Contas

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Administrar, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem as contas e as ações que podem ser efetuadas sobre elas. | PAGE | Contas - app\_\_lms\_\_learning\_\_accounts | Detalhadas em . |
| WIDGET | Contas | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de contas. | LMSACC | Aprendizado - Gerência de contas | * **Ler**: quando ativada, permite visualizar as contas das quais o usuário é responsável. Usuários que possuem essa opção ativa podem visualizar a opção [Extrato](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Visualizarextratodaconta), que permite gerar um extrato das contas pelas quais ele é responsável.  * **Ler tudo**: quando ativada, permite visualizar todas as contas existentes, independentemente de ser ou não responsável por elas. Usuários que possuem essa opção ativa podem visualizar a opção [Extrato](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Visualizarextratodaconta), que permite gerar um extrato de qualquer conta.  * **Adicionar créditos**: quando ativada, permite adicionar créditos em contas do tipo Crédito independentemente de ser o responsável por elas ou não, ou seja, depende do que foi definido nas opções **Ler** e **Ler tudo**. Usuários que possuem essa opção ativa podem visualizar a opção [Adicionar créditos](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Adicionarcréditosnaconta) na página de contas.  * **Salvar**: quando ativada, permite incluir e editar contas. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Criarconta) e [Editar](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Editarconta) na página de contas.  * **Inativar**: quando ativada, permite inativar contas independentemente de ser o responsável por ela ou não, ou seja, depende do que foi definido nas opções **Ler** e **Ler tudo**. Usuários que possuem essa opção ativa podem visualizar a opção [Inativar](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Inativarconta) na página de contas.  * **Reativar**: quando ativada, permite reativar contas independentemente de ser o responsável por elas ou não, ou seja, depende do que foi definido nas opções **Ler** e **Ler tudo**. Usuários que possuem essa opção ativa podem visualizar a opção [Reativar](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Ativarconta) na página de contas.  * **Remover**: quando ativada, permite remover contas independentemente de ser o responsável por elas ou não, ou seja, depende do que foi definido nas opções **Ler** e **Ler tudo**. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/AY35DQ#Plataforma❙Contas-Removerconta) na página de contas. |

##### Console EAI

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  –  pertencente ao item Administrar, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem as configurações do console EAI. | PAGE | Console EAI - pageconsoleeai | Detalhadas em . |
| WIDGET | Console EAI | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de mensagens EAI. | LMSEAI | Aprendizado - EAI | * **Acessar**: quando ativada, permite gerenciar o console EAI. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará o console, ou seja, o recurso será exibido em branco. |

#### Avisos

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Aprendizado do menu principal – que exibem os avisos e as ações que podem ser efetuadas sobre eles. | PAGE | Avisos - pageadvices | Detalhadas em . |
| WIDGET | Avisos | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de avisos. | LMSADV | Aprendizado - Gerência de avisos | * **Ler**: quando ativada, permite visualizar a lista de avisos existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhum aviso.  * **Salvar**: quando ativada, permite incluir e editar avisos. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/w-LuDQ#Plataforma❙Avisos-Adicionaraviso) e [Editar](https://tdn.totvs.com/x/w-LuDQ#Plataforma❙Avisos-Editaraviso) na página de avisos.  * **Remover**: quando ativada, permite excluir avisos existentes. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/w-LuDQ#Plataforma❙Avisos-Removeraviso) na página de avisos. |

#### Eventos

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  –  pertencente ao item Aprendizado do menu principal – que exibem os eventos e as ações que podem ser efetuadas sobre eles. | PAGE | Eventos - pageevents | Detalhadas em . |
| WIDGET | Eventos | Detalhadas em Opções de permissão em *widgets*. |

#### Agenda

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Aprendizado do menu principal – que exibem a agenda e as ações que podem ser efetuadas sobre ela. | PAGE | Agenda - pageschedule | Detalhadas em . |
| WIDGET | Agenda | Detalhadas em Opções de permissão em *widgets*. |

#### Matrículas

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página que agrupa os recursos do item  que pertence ao item Aprendizado do menu principal. | PAGE | Matrículas - app\_\_lms\_\_learning\_\_enrollments | Detalhadas em . |

##### Gerenciamento de matrículas

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Matrículas, que por sua vez, pertence ao item Aprendizado do menu principal – que permitem efetuar ações em matrículas. | PAGE | Gerenciamento de matrículas - app\_\_lms\_\_learning\_\_enrollments\_\_manage | Detalhadas em . |
| WIDGET | Gerenciamento de matrículas | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações relacionadas a  usuários. | LMSENC | Aprendizado - Matrículas | * **Cancelar matrículas em treinamentos/trilhas**: quando ativada, permite cancelar a própria matrícula em treinamentos e trilhas que fazem parte do plano de aprendizado. Usuários que possuem essa opção ativa podem visualizar a opção [Cancelar matrícula](https://tdn.totvs.com/x/Gv7uDQ#Plataforma%E2%9D%99Treinamento-Cancelarmatr%C3%ADculaemtreinamento), tanto no próprio plano de aprendizado quanto nos itens nos quais estão matriculados e foram visualizados a partir do catálogo.  * **Cancelar matrículas em turmas**: quando ativada, permite cancelar a própria matrícula em turmas que fazem parte do plano de aprendizado. Usuários que possuem essa opção ativa podem visualizar a opção [Cancelar matrícula](https://tdn.totvs.com/x/S-7uDQ#Plataforma%E2%9D%99Turma-Cancelarmatr%C3%ADculanaturma), tanto no próprio plano de aprendizado quanto nas turmas nas quais estão matriculados e foram visualizadas a partir do catálogo.  * **Matricular todos os usuários**: quando ativada, permite matricular outros usuários em treinamentos, trilhas e turmas disponíveis no catálogo. Usuários que possuem essa opção ativa podem visualizar a opção [Matricular usuários](https://tdn.totvs.com/x/Gv7uDQ#Plataforma%E2%9D%99Treinamento-Matricularusu%C3%A1riosemtreinamento) nos itens do catálogo e a aba  no recurso Gerenciamento de matrículas.  * **Cancelar matrículas**: quando ativada, permite cancelar a matrícula de outros usuários em turmas, trilhas e treinamentos - [individualmente](https://tdn.totvs.com/x/mv7uDQ#Plataforma%E2%9D%99Gest%C3%A3odematriculados-Cancelarmatr%C3%ADcula) ou em [lote](https://tdn.totvs.com/x/mv7uDQ#Plataforma%E2%9D%99Gest%C3%A3odematriculados-Cancelarmatr%C3%ADculasemlote). |
| Permissão específica para a . | LMSENR | Aprendizado - Gerenciamento de matrículas | * **Administrar**: quando ativada, permite gerenciar matrículas de outros usuários em trilhas, treinamentos e turmas. Usuários que possuem essa opção ativa podem visualizar a aba Gestão de matriculados e as opções [Bloquear matrícula](https://tdn.totvs.com/x/mv7uDQ#Plataforma%E2%9D%99Gest%C3%A3odematriculados-Bloquearmatr%C3%ADcula), [Desbloquear matrícula](https://tdn.totvs.com/x/mv7uDQ#Plataforma❙Gestãodematriculados-Desbloquearmatrícula) e [Cancelar matrícula](https://tdn.totvs.com/x/mv7uDQ#Plataforma❙Gestãodematriculados-Cancelarmatrícula). |
|  | Permissão específica para a criação de registros de matrícula por meio da API. | LMSHIS | Aprendizado - Histórico de matrículas | * **Criar histórico de execução de matrículas via API**: quando ativada, permite que seja criado um registro de matrícula – por meio da API – para um usuário que executou uma trilha, um treinamento ou uma turma em outra plataforma de aprendizado, pelo fato desse item não estar cadastrado nos catálogos de aprendizado, permitindo assim, que o aluno tenha o seu histórico completo. |

##### Alterar *status* de matrícula

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso Alterar *status* de matrículas – pertencente ao item Matrículas, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem o *status* das matrículas e as ações que podem ser efetuadas sobre elas. | PAGE | Alterar *status* de matrícula - pageenrollchangestatus | Detalhadas em . |
| WIDGET | Alterar *status* de matrícula | Detalhadas em Opções de permissão em *widgets*. |
| Permissão específica para o gerenciamento do *status* das matrículas. | LMSMEN | Aprendizado - Alteração de *status* de matrículas | * **Situação**: quando ativada, permite alterar o *status* das matrículas em turmas. O usuário que possui essa opção ativa está apto a ser definido como responsável por alterar o *status* de matrículas no cadastro da  ou da  e pode visualizar as opções [Editar](https://tdn.totvs.com/x/nv7uDQ#Plataforma%E2%9D%99Alterarstatusdematr%C3%ADcula-Editarpontua%C3%A7%C3%A3odoaluno) – para editar a pontuação do aluno –, [Aprovar aluno](https://tdn.totvs.com/x/nv7uDQ#Plataforma❙Alterarstatusdematrícula-Aprovaraluno), [Reprovar aluno](https://tdn.totvs.com/x/nv7uDQ#Plataforma❙Alterarstatusdematrícula-Reprovaraluno) e [Cancelar matrícula](https://tdn.totvs.com/x/nv7uDQ#Plataforma❙Alterarstatusdematrícula-Cancelarmatrícula) na página de alteração do *status* de matrículas. |

##### Finalizar turmas

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Matrículas, que por sua vez, pertence ao item Aprendizado do menu principal – que exibem as turmas que ainda não foram finalizadas e que estão sob responsabilidade do usuário autenticado. | PAGE | Finalizar turmas - pagefinishclasses | Detalhadas em . |
| WIDGET | Finalizar turma | Detalhadas em Opções de permissão em *widgets*. |
| Permissão específica para a finalização manual de turmas. | LMSMFN | Aprendizado - Finalização manual de turmas | * **Acessar**: quando ativada, permite finalizar turmas manualmente, ou seja, o usuário que possui essa permissão ativa está apto a ser definido como responsável por finalizar turmas manualmente no cadastro da  ou da  e pode visualizar a opção [Finalizar turma](https://tdn.totvs.com/x/of7uDQ#Plataforma%E2%9D%99Finalizarturma-Finalizarturma) na página de finalização de turmas. |

## Recursos de avaliações

As páginas, os *widgets* e as permissões específicas de avaliações são listadas a seguir.

### Menu avaliações

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página do item  do menu principal onde são agrupados os recursos de avaliações. | PAGE | Menu avaliações - pageassessment | Detalhadas em . |

#### Avaliações

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Avaliações do menu principal – que exibem as avaliações e as ações que podem ser efetuadas sobre elas. | PAGE | Avaliações - pageassessments | Detalhadas em . |
| WIDGET | Avaliações | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de avaliações. | LMSGEA | Avaliações - Gerenciamento de avaliações | * **Ler**: quando ativada, permite visualizar a lista de avaliações existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhuma avaliação.  * **Salvar**: quando ativada, permite incluir e editar avaliações. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/sv7uDQ#Plataforma%E2%9D%99Avalia%C3%A7%C3%B5es.-Criaravalia%C3%A7%C3%A3o) e [Editar](https://tdn.totvs.com/x/sv7uDQ#Plataforma❙Avaliações.-Editaravaliação) na página de avaliações.  * **Remover**: quando ativada, permite excluir avaliações existentes. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/sv7uDQ#Plataforma❙Avaliações.-Removeravaliação) na página de avaliações. |

#### Blocos

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Avaliações do menu principal – que exibem os blocos de questões que podem ser reutilizados e as ações que podem ser efetuadas sobre eles. | PAGE | Blocos - pageblocks | Detalhadas em . |
| WIDGET | Blocos | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de blocos de questões. | LMSBLO | Avaliações - Gerência de blocos | * **Ler**: quando ativada, permite visualizar a lista de blocos de questões existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhum bloco de questões.  * **Salvar**: quando ativada, permite incluir e editar blocos. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/tP7uDQ#Plataforma❙Blocos-Criarbloco) e [Editar](https://tdn.totvs.com/x/tP7uDQ#Plataforma❙Blocos-Editarbloco) na página de blocos.  * **Remover**: quando ativada, permite excluir blocos existentes. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/tP7uDQ#Plataforma❙Blocos-Removerbloco) na página de blocos. |

#### Tópicos e questões

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Avaliações do menu principal – que exibem o catálogo de tópicos e questões. | PAGE | Tópicos e questões - pagecatalogquestions | Detalhadas em . |
| WIDGET | Tópicos e questões | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento do catálogo de tópicos e questões. | LMSTOP | Avaliações - Catálogo de questões | * **Ler**: quando ativada, permite visualizar o catálogo de tópicos e questões. Os itens do catálogo serão exibidos conforme as permissões definidas em cada um deles, inclusive considerando as permissões definidas na [pasta raiz](https://tdn.totvs.com/x/t-7uDQ#Plataforma%E2%9D%99T%C3%B3picosequest%C3%B5es-Editarcat%C3%A1logo), ou seja, se não for liberada pelo menos permissão de leitura na pasta raiz, o catálogo será exibido vazio, mesmo que a opção **Ler** esteja ativa.  * **Ignorar restrições**: quando ativada, permite visualizar o catálogo de tópicos e questões como se fosse um usuário administrador, ou seja, ignorando todas as restrições e ausência de permissões nos itens. |

#### Grupos de alternativas

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Avaliações do menu principal – que exibem os grupos de alternativas e as ações que podem ser efetuadas sobre eles. | PAGE | Grupos de alternativas - pagealternativesgroups | Detalhadas em . |
| WIDGET | Grupos de alternativas | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento de grupos de alternativas. | LMSALG | Avaliações - Grupo de alternativas | * **Ler**: quando ativada, permite visualizar a lista de grupos de alternativas existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhum grupo de alternativa.  * **Salvar**: quando ativada, permite incluir e editar grupos de alternativas. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/vf7uDQ#Plataforma❙Gruposdealternativas-Adicionargrupodealternativas) e [Editar](https://tdn.totvs.com/x/vf7uDQ#Plataforma❙Gruposdealternativas-Editargrupodealternativas) na página de grupos de alternativas.  * **Remover**: quando ativada, permite excluir grupos de alternativas existentes. Usuários que possuem essa opção ativa podem visualizar a opção [Remover](https://tdn.totvs.com/x/vf7uDQ#Plataforma❙Gruposdealternativas-Removergrupodealternativas) na página de grupos de alternativas. |

#### Correção de questões

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Avaliações do menu principal – que exibem as questões dissertativas de avaliações e as ações que podem ser efetuadas sobre elas. | PAGE | Correção de questões - pagequestioncorrection | Detalhadas em . |
| WIDGET | Corrigir questões dissertativas | Detalhadas em Opções de permissão em *widgets*. |

#### Histórico de avaliações

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Avaliações do menu principal – que exibem as aplicações de avaliações por usuário. | PAGE | Histórico de avaliações - pagehistoricalassessments | Detalhadas em . |
| WIDGET | Histórico de avaliações | Detalhadas em Opções de permissão em *widgets*. |
| Permissão específica para visualização do histórico de aplicação de avaliações. | LMSUAHV | Avaliações - Histórico de avaliações | * **Visualizar o histórico de todos usuários da mesma empresa**: quando ativada, permite visualizar o histórico de execução de avaliações de qualquer usuário da mesma empresa. Usuários que possuem essa opção ativa, podem efetuar uma [busca por um aluno específico](https://tdn.totvs.com/x/5-LuDQ#Plataforma%E2%9D%99Hist%C3%B3ricodeavalia%C3%A7%C3%B5es-Visualizarhist%C3%B3ricodealunoespec%C3%ADfico) que seja da mesma empresa que a sua e visualizar o histórico desse aluno. |

#### Agendamento de avaliações

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | Página e *widget* do recurso  – pertencente ao item Avaliações do menu principal, e que exibem as aplicações de avaliações por usuário. | PAGE | Agendamento de avaliações - pagescheduleassessments | Detalhadas em . |
| WIDGET | Agendamento de avaliações | Detalhadas em Opções de permissão em *widgets*. |
| Permissões específicas para as ações de gerenciamento do agendamento da aplicação de avaliações. | LMSAS | Avaliações - Agendamento de avaliações | * **Ler**: quando ativada, permite visualizar a lista de agendamentos de avaliações existentes. Mesmo que o usuário possua permissão para visualizar a página e o *widget,* se esta opção não estiver ativa, ele não visualizará os registros, ou seja, o recurso será exibido como se não existisse nenhum agendamento.  * **Salvar**: quando ativada, permite incluir e editar agendamento de avaliações. Usuários que possuem essa opção ativa podem visualizar as opções [Novo](https://tdn.totvs.com/x/9PLuDQ#Plataforma%E2%9D%99Agendamentodeavalia%C3%A7%C3%B5es-Agendaraplica%C3%A7%C3%A3odeavalia%C3%A7%C3%A3o) e [Editar](https://tdn.totvs.com/x/9PLuDQ#Plataforma❙Agendamentodeavaliações-Editaragendamentodeaplicaçãodeavaliação) na página de agendamento de avaliações.  * **Cancelar**: quando ativada, permite cancelar agendamentos de avaliações existentes. Usuários que possuem essa opção ativa podem visualizar a opção [Cancelar](https://tdn.totvs.com/x/9PLuDQ#Plataforma❙Agendamentodeavaliações-Cancelaragendamentodeaplicaçãodeavaliação) na página de agendamento de avaliações. |

## *Widgets* avulsos

| Descrição | | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- | --- |
|  | *Widget* que exibe as trilhas e os treinamentos que o usuário inseriu em sua lista de desejos e que pode ser inserida em páginas para personalizá-las – na Home, por exemplo. | WIDGET | Lista de desejos | Detalhadas em Opções de permissão em *widgets*. |
|  | *Widget* que exibe a evolução do usuário nas turmas, trilhas e treinamentos nos quais ele está matriculado e que pode ser inserida em páginas para personalizá-las – na Home, por exemplo. | WIDGET | Evolução | Detalhadas em Opções de permissão em *widgets*. |
|  | *Widget* que exibe as conquistas que o usuário alcançou ao executar trilhas e treinamentos e participar de turmas e que pode ser inserida em páginas para personalizá-las – na Home, por exemplo. | WIDGET | Conquistas | Detalhadas em Opções de permissão em *widgets*. |
|  | *Widget* que exibe os detalhes das conquistas do usuário, bem como as habilidades conquistadas, e que pode ser inserida em páginas para personalizá-las – na Home, por exemplo. | WIDGET | Detalhes de conquistas | Detalhadas em Opções de permissão em *widgets*. |
|  | *Widget* que exibe os avisos pertinentes às turmas de disciplinas nas quais o usuário está matriculado e que pode ser inserida em páginas para personalizá-las – na Home, por exemplo. | WIDGET | Quadro de avisos | Detalhadas em Opções de permissão em *widgets*. |

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
