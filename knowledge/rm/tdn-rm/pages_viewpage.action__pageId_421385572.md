---
content_hash: c449e2a9503dc60da36267d0cb9c0f823cd684c9fe789258ba37d20e789df913
fetched_at: '2026-06-29T00:09:16.837412+00:00'
page_id: '421385572'
product: rm
source: tdn-rm
title: Visão de Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385572
version: 5
---

---

Na visão de projetos serão listados todos os projetos por coligada, de acordo com a permissão de acesso a projetos do usuário. O usuário que for supervisor tem acesso a todos os projetos.

Veja [Permissão de acesso ao Projeto](http://tdn.totvs.com/pages/viewpage.action?pageId=421385180).

**Observação:**

Na visão de projetos será apresentado o campo "Tipo Projeto" e seu conteúdo poderá exibir os valores 0,1 ou 2, onde:

0 - Significa novo projeto; 1-  Significa projeto de licitação; 2 - Significa projeto de revisão.

* **Filtros na visão**

Através desta opção é exibida a janela de filtros e será possível incluir novos filtros, modificar filtros já cadastrados, ou ainda executar a seleção de dados determinada por algum dos filtros selecionados. O filtro de visão de Projetos passou a ser gravado por usuário, ou seja, se o usuário utilizar um filtro, na próxima vez que a visão de projetos for aberta ela estará sendo filtrada pelo último filtro utilizado pelo usuário.

**Dica:**

Para filtrar os projetos por Posição é necessário saber a codificação utilizada na gravação do status dos projetos que são: - Em Andamento = 1; - Paralisado = 2; - Concluído = 3; - A Executar = 4; - Em Negociação = 5; - Revisado = 6; - Cancelado = 7.

**Exemplo:**

Para fazer um filtro de todos os projetos com a posição Em Andamento, na edição do filtro, selecione o campo Posição, selecione o = (igual) como 1º Op. e um (1) como 1º Valor.

* **Somente Projetos que o Usuário possui acesso**

Marcando a opção "Somente Projetos que o Usuário possui acesso" serão listados apenas os projetos a que o usuário tem acesso, evitando assim que ele tente abrir projetos para os quais não tem permissão.

Este botão terá sua visualização definida pela tag abaixo:

* **Projeto Global**

* Só será possível cadastrar um único projeto global por coligada;
* No projeto Global serão permitidos apenas os cadastros de Grupo de Custo, Insumos, Composições, Modelo de taxas, Mobilidade (Coletores Móveis, Usuários de Coletores Móveis, Log de Importação e Exportação) e Gestão de Riscos (Objetivos do Projeto, Escalas, Grupo de Áreas de Prioridade, EAR);
* O Projeto Global é muito útil na montagem de um orçamento pois ele possui todos os insumos e composições básicas utilizadas pela organização. O projeto Global, será um "banco" padrão, basicamente um projeto que terá o cadastro de todos os insumos composições e grupos de custo;
* Os insumos, preços de insumos e composições de um projeto global poderão ser utilizados por qualquer outro projeto cadastrado na coligada do projeto global em questão.  
    
  **Observação:** Um projeto que não é global não pode ser simplesmente alterado para global, pois há necessidade de alteração de todos os dados existentes no mesmo para Global e para alguns dados isso não é possível. Portanto, caso você queira alterar um projeto de local para global, a dica é criar um projeto novo como global e efetuar a cópia de itens dos recursos do projeto origem para o projeto global.

* **Projeto Modelo**

Se o usuário não possuir acesso a algum projeto e este projeto estiver setado com projeto modelo, será possível efetuar a cópia de itens do mesmo, apesar do usuário não possuir permissão de acesso a ele.

* **Exclusão de Projeto**

Para remover os projetos selecionados o sistema irá seguir as seguintes premissas:

* Verifica se existe algum usuário conectado ao Projeto;
* Verifica se existem recursos do projeto (insumo, composição) utilizados em projetos locais;
* Valida se não existem contratos com revisões de preço;
* Valida se não existem projetos filhos (revisões do projeto);
* Valida se não existem pedidos de material extra;
* Considera todas as informações do projeto referentes às funcionalidades de Mobilidade, sendo as mesmas excluídas antes da exclusão do projeto. São elas:
* Avanço Físico; - Ciclo de Transporte; - Equipamentos; - Mão de Obra.

**ATENÇÃO:** Ao tentar excluir um projeto que tenha funcionalidades de mobilidade, será efetuada a validação da existência de associação a coletores móveis ou folhas tarefa cadastradas. Existindo algum destes itens, um alerta é exibido, e em seguida a tela com os impedimentos que não permitem a exclusão do projeto.

Mensagem de alerta exibida: "Não é possível excluir projetos com integrações, remova as integrações e tente novamente".

**UX Design Thinking Projeto**

Anexo associado a visão de projetos que exibirá os últimos projetos acessados pelos usuários permitindo a escolha.

Após o acesso a um projeto, será disponibilizado no menu do sistema a opção de acesso aos últimos projetos para facilitar ao usuário a troca de projetos.

No anexo de últimos projetos e no menu de acesso rápido, serão exibidos os últimos 7 projetos. Este é o limite para que permita melhor visualização para monitores configurados para trabalhar com a resolução 1024 x 768.

O usuário poderá registrar as funcionalidades de sua preferência, sendo que está serão automaticamente executadas imediatamente a abertura do projeto.

**Registro de acesso do Usuário ao Projeto**

Permite registrar a data e hora de acesso do usuário ao projeto, sendo possível classificá-los por ordem de acesso.  A cada acesso do usuário ao projeto ficará registrado e atualizado em uma tabela.

**Observação**: O projeto corrente será exibido em destaque.

**Abertura de Funcionalidades no Acesso Inicial a Projetos**

Acessando em: Projeto/ Construção e Projetos/ Funções de Acesso Inicial a Projetos. Permite que o usuário possa definir quais as funcionalidades serão inicializadas imediatamente a abertura do projeto. Será informado as funcionalidades de preferência, que serão por coligada e aplicadas em todos os projetos.

Observação: Serão permitidas o cadastro de até 5 funcionalidades para que não ocorra abertura em excesso, degradando a inicialização do sistema. Após o cadastro da terceira funcionalidade, o sistema emitirá um alerta para o usuário. Serão inicializadas de acordo com a ordem de cadastro realizada.

**Projetos Recentes**

Em cada página do Fluig referente às telas do sistema existe um botão para escolher o contexto de informações que serão aplicadas e utilizadas nas páginas.

Exemplo: Escolher ou alterar uma coligada, escolher ou alterar um projeto.

Será exibido um campo para escolher os projetos da base. O campo possui a funcionalidade de filtrar os projetos pelo código ou descrição facilitando assim que o projeto seja encontrado.

Logo abaixo desse campo será exibido uma lista com os 7 últimos projetos recentes, ou seja, os últimos projetos que foram abertos pelo usuário.

Essa lista irá conter as seguintes informações do Projeto ordenados pela data de acesso mais recente para a mais antiga:

* Código;
* Descrição;
* Nome da Fase;
* Código Auxiliar;
* Número da Revisão;
* Data e hora do último acesso

Ao clicar no Código ou Descrição do Projeto, o sistema automaticamente realiza o acesso ao mesmo obedecendo todas as regras para acesso aplicadas no processo atual.

**Acesso Rápido aos Projetos Recentes**

Além do seletor de contexto, a barra de projeto é exibida em quase todas a páginas HTML do TOTVS Obras e Projetos. Na barra de projeto existe um campo onde o usuário poderá trocar de projeto escolhendo os projetos que ele tem acesso. O campo é uma lista de projetos do sistema. Os projetos recentes serão exibidos primeiro e abaixo deles estarão os outros projetos do sistema.

Na barra de projeto, os projetos mais recentes serão ordenados pela data de último acesso e posteriormente os outros projetos do sistema, ordenados pelo código.

**Observação: O projeto corrente será exibido em destaque na barra.**

 Informações Complementares

---

 Como Fazer

---
