---
content_hash: 0deb175118b5bd623143a911e25fc8337f21e067b6ca2de7ae8ae9ccbab4b3c4
fetched_at: '2026-06-29T00:09:11.344440+00:00'
page_id: '403746925'
product: rm
source: tdn-rm
title: Perfil
type: documentation
url: https://tdn.totvs.com/display/LRM/Perfil
version: 29
---

**CONTEÚDO**

# **01. Visão geral**

O cadastro de Perfil é um dos itens de cadastramento necessários ao funcionamento dos recursos de Segurança dos aplicativos.

Ao acessar este cadastro, o usuário Supervisor poderá definir perfis de acesso para serem posteriormente relacionados aos usuários cadastrados no aplicativo através da inclusão e manutenção de Usuários.

## **O que é um perfil?**

Perfil é um grupo de características e permissões/limitações de acesso ao banco de dados, a menus, campos e relatórios. Um perfil pode ser associado a vários usuários ao mesmo tempo.

O objetivo é criar com os perfis, diferentes tipos de acesso ao sistema e posteriormente, associá-los ao cadastro de usuários. Todos os usuários que possuírem um determinado perfil associado herdam suas características e permissões ou restrições de acesso.

**Exemplo:** Para exemplificar e esclarecer melhor este Cadastro suponha que a empresa possua determinado Aplicativo RM e que resolva criar diferentes níveis de acessos para diferentes usuários. Como exemplo, a empresa então criaria perfis para: Consultar - Para usuários que possam somente consultar uma, várias ou mesmo todas as tabelas do aplicativo, mas que não possam alterar incluir ou excluir dados nas tabelas.  
Relatórios - Para usuários que possam ter acesso somente à impressão de relatórios necessários ao desempenho de suas funções.  
Cadastramento Parcial - Para usuários que possam cadastrar (incluir, excluir, alterar) dados em algumas tabelas, tendo o acesso vedado em outras.  
Cadastramento Total - Para usuários que possam acessar e realizar quaisquer inclusões ou alterações em todas as tabelas do Aplicativo.

Atenção!

O sistema permite a exclusão de um perfil mesmo que ele esteja associado a um ou mais usuários.

Observação

* Um usuário não poderá visualizar ou imprimir relatórios quando não existir impressora instalada no computador, ou seja, será permitida somente a edição e a formatação dos relatórios.

* Ao criar estes perfis, você poderá associá-los aos usuários conforme a permissão recomendada por usuário ou grupo de usuários. Por exemplo, no RM Labore (Aplicativo RM) os funcionários do departamento de Recursos Humanos poderiam ter acesso irrestrito às tabelas de Funcionários para realizarem as rotinas do departamento.

  Por outro lado, os funcionários em geral, de outros departamentos, embora necessitem acessar o Aplicativo, não poderiam ter acesso às tabelas dos funcionários, em função dos dados sigilosos relativos a salário, dados pessoais dos funcionários, etc. Neste caso, você poderia associar ao grupo de usuários do departamento de Recursos Humanos os perfis Cadastramento Total ( sem quaisquer restrições de acesso) e aos demais usuários, Cadastramento Parcial ( com restrição de acesso às tabelas de Funcionários ).

  Quando existir menus sem acessos, comum em todos os Perfis, será exibido um aviso esta informação, ao ser acessada a Tela de Perfil.

  Observe que um usuário poderá estar vinculado a vários perfis diferentes. Da mesma forma, um mesmo perfil poderá estar vinculado para vários usuários diferentes.

---

# **02. Exemplo de utilização**

* ## **Identificação**

Na janela de edição de Perfis estarão disponíveis algumas pastas nas quais serão definidos os acessos, entre elas a de identificação do perfil. Preencha os campos abaixo para identificar o perfil a ser criado:

**01.****Cód. Perfil:**Digite um código para o perfil. Este código poderá ser alfanumérico, ou seja, comporta letras e números como código.

**02.****Identificação:**Informe o nome desejado para o perfil. A título de sugestão, os nomes dos Perfis poderiam refletir os departamentos ou seções da empresa, ou os tipos de cargos de funcionários que deverão ter acesso ao aplicativo, etc.  
Por padrão, serão colocados os nomes dos Perfis criados, acrescidos do nome do Aplicativo corrente entre parênteses.

**Exemplo:**Funcionários da Diretoria (RM Labore);  
Funcionários da Administração (RM Bonum);

**03.****Identificador do perfil:**O cód. perfil é um identificador que permanece o mesmo quando se altera o módulo, já o identificador de perfil é único para cada módulo selecionado.

O mesmo perfil pode ter permissões diferentes para cada módulo que ele está.

**Exemplo:**

O perfil   possui diferentes permissões a cada módulo que ele está presente e esses "sub-perfis" podem ser nomeados, mas, não deixam de pertencer ao perfil "DBA"

**Serviços globais:**

**OBS**.: Este é o nome que aparecerá quando for selecionar um perfil em usuário.

**Gestão de conteúdos:**

**04.****Ativo:**

Habilite este campo para confirmar o usuário no acesso ao aplicativo. Somente com este campo habilitado o usuário poderá ter seu acesso validado, mesmo que demais permissões estejam confirmadas.

---

* ## **Acesso a campos**

Nesta pasta você poderá definir os acessos e restrições que os usuários possuirão ao serem associados a cada perfil.

Relação de Campos À esquerda, nesse espaço, clique no sinal de mais  ao lado da expressão: + Todas as Tabelas. Automaticamente, serão exibidas as tabelas disponíveis no aplicativo, todas precedidas do sinal de mais . Ao clicar sobre este sinal em cada uma delas, serão apresentados seus respectivos campos, além de uma área à direita contendo a descrição desses campos. Selecione cada campo que deseja dar permissão ao usuário e defina as opções no campo Permissões.

Atenção Este acesso é permitido somente aos usuários Supervisores.

As acessos poderão ser definidos das seguintes formas:

Tabela por tabela, para todas as suas colunas ao mesmo tempo (em cada tabela selecionada);

Tabela por tabela, mas para cada coluna de forma diferenciada (algumas colunas com permissão e outras sem permissão).  
Veja quais são os campos e funcionalidades desta pasta:  
Encolher Tudo Recolhe todos os campos abertos na árvore de tabelas.  
  
Exibir apenas campos com restrição São exibidos apenas os campos que possuírem restrição na coluna das tabelas.  
  
**Tabela** Nome da tabela selecionada.

**Campo** Nome do campo da tabela selecionada.

**Descrição** Descrição do campo ou da tabela selecionada.  
Conheça a legenda dos ícones para Permitir ou restringir o acesso aos campos:  
[Permissões e Restrições](https://tdn.totvs.com/display/LRM/Perfil)

**Pode consultar** Deixando este parâmetro marcado, será permitida aos usuários com este perfil a consulta do(s) campo(s) selecionado(s) em cada tabela. Caso desmarcado, os campos não serão exibidos na edição e na visão dos registro da tabela.

Observação

**Observação** Para que os relatórios criados por um usuário não sejam visíveis por todas as coligadas é preciso abrir a tabela RRELAT, selecionar o campo CODCOLIGADA e desmarcar a opção Pode Consultar. Lembrando que somente o usuário supervisor pode conceder esta permissão.

**Pode alterar** Deixando este parâmetro marcado, será permitida aos usuários a consulta e alteração do(s) campo(s) selecionado(s) desta tabela ou,     dependendo do caso, permissão para toda a tabela selecionada. Caso desmarcado, os campos ficarão visíveis, porém sem a possibilidade de alteração do conteúdo.

Observação

**Observação** Cada opção marcada (habilitada) valerá somente para o campo selecionado, ou somente para a tabela selecionada, ou seja, deverá ser definida a permissão tabela por tabela, ou conforme o caso, campo a campo.

**Dica** Pela subpasta "Restrições" você pode visualizar a lista de campos que estão com restrições.

---

* ## **Acesso a menus**

  Nesta janela serão definidos quais menus serão visualizados ou bloqueados. Assim como ocorre na opção "Acesso a Campos", que disponibiliza os campos das tabelas, o Acesso a Menus permite que seja definido para cada perfil, quais os menus do sistema poderão ser acessados e utilizados ou as restrições de acesso impostas aos menus para os usuários que possuírem o perfil em edição. Para que você possa dar permissão de acesso aos menus ou retirar, será necessário selecionar o menu e clicar na opção Permitir Acesso.  
    
  **Expandir** **Tudo** Mostra todos os itens disponíveis daquele menu selecionado. Para visualizar todos os itens, clique no nome do aplicativo e clique na opção Expandir Tudo.  
   **Encolher Tudo** Esconde todos os itens disponíveis daquele menu selecionado. Para esconder todos os itens, clique no nome do aplicativo e clique na opção Encolher Tudo.  
   **Observação** Outra forma de expandir os itens é clicar no sinal ( - ) à esquerda do campo. Outra forma de reduzir os itens é clicar no sinal ( + ) à esquerda do campo.  
   **Permitir Acesso** Permite o acesso ao menu selecionado. Para permitir acesso a todos os itens, clique no nome do aplicativo e clique na opção Permitir Acesso.  
   **Proibir Acesso** Retira o acesso ao menu selecionado. Para retirar acesso a todos os itens, clique no nome do aplicativo e clique na opção Proibir Acesso.**Observação** Os usuários da linha RM podem ser incluídos em vários perfis de vários Sistemas.  
    
  **Exemplo**  
  1 - Sistema "RM Labore" possui o perfil "perfil1".  
  2 - Sistema "RM Fluxus" possui o perfil "perfil1".  
  3 - O usuário "João" pertence ao pefil1 do RM Labore e ao perfil1 do RM Fluxus.  
  4 - Cada Sistema possui seus respectivos perfis. Nos exemplos acima, tanto o Sistema RM Labore como o RM Fluxus possuem um perfil de nome "perfil1" (não é o mesmo para os dois Sistemas).  
  5 – RM Labore - perfil1: Acesso ao Cadastro de Cliente Fornecedor  
  6 – RM Fluxus - pefil1: Acesso NEGADO ao Cadastro de Cliente Fornecedor  
  7 - O usuário João consegue acessar o Cadastro de Cliente Fornecedor pelo RM Fluxus, e o faz também pelo RM Labore. Isso porque a Action do sistema é a mesma. Para evitar o acesso à action totalmente, é preciso negar a permissão em todos os perfis associados ao usuário.

---

* ## **Acesso a Relatórios/Planilhas**

Através da Janela de Edição de Perfis poderá ser acessada a pasta de Acesso a Relatórios/Planilhas, que apresentará os Grupos de Relatórios/Planilhas com os respectivos níveis de alteração e emissão para o perfil selecionado.

Ao acessar esta opção, o usuário (na condição de Supervisor) poderá definir para os demais usuários desse perfil quais os grupos de relatórios/planilhas eles terão acesso e como será a permissão de alteração e emissão dos mesmos.  
Para tal, basta incluir um novo Acesso a Relatórios/Planilhas, e incluir:

* Um Grupo de Usuário: Clique nas reticências para incluir um novo grupo. Caso desejar listar os grupos já disponíveis, digite '%'no local da busca.
* Definir Nível de Alteração
* Definir Nível de Emissão

  **Exemplo:** O usuário João possui um perfil como acesso a relatórios do grupo Listagens com nível de alteração 1 e emissão 2. As situações onde ele se enquadrará são:
* Relatórios sem grupo - João poderá alterar e emitir esse relatório. Pois este relatório está desprotegido.
* Relatórios com grupo diferente do grupo Listagens - João não poderá alterar e emitir esse relatório. O relatório nem será exibido na visão de relatórios para João porque ele não possui permissão de acesso a este outro grupo.
* Relatórios do grupo Listagens com nível de acesso igual a 1 - João poderá alterar e emitir esse relatório porque o nível de acesso ao relatório é menor ou igual aos níveis de alteração e emissão.
* Relatórios do grupo Listagens com nível de acesso igual a 2 - João poderá apenas emitir esse relatório porque o nível de acesso ao relatório é menor ou igual ao nível de emissão. Ele não poderá alterar porque o relatório possui um nível de acesso maior que o nível de alteração cadastrado no seu perfil.
* Relatórios do grupo Listagens com nível de acesso igual a 3 - João não poderá alterar e emitir esse relatório. O relatório nem será exibido na visão de relatórios para João, porque o nível de acesso ao relatório é maior que os níveis de alteração e emissão dele.

Observação

* **Observação:** O usuário só poderá alterar/emitir um relatório/planilha que tiver nível menor ou igual ao nível do grupo correspondente no perfil do usuário.

Não é possível inserir um valor para o nível de Permissão menor que o nível de Alteração. Caso o usuário tente inserir será emitida uma mensagem de advertência: "O nível de Emissão deve ser maior ou igual ao nível de Alteração!"  
Os números informados nestes campos se relacionam com o nível dos relatórios/planilhas. É importante saber com antecedência quais os relatórios/planilhas possuem os maiores níveis no aplicativo.  
**Exemplo** Suponha um relatório que somente a diretoria da empresa deverá ter acesso. No Gerador de Relatórios este relatório possui Nível 50. Ao incluir um usuário da diretoria em determinado grupo de relatório (atribuir permissão do usuário para o grupo), o nível de acesso desse usuário deverá ser superior a 50 para que também este relatório possa ser visualizado e/ou alterado.  
Este mesmo procedimento, deverá ocorrer com a opção abaixo (Emissão), para que o usuário possa também emitir um relatório/planilha que possua nível inferior ao atribuído para o usuário.

NovasRestriçõesBI Self-Service

         A partir da ***12.1.26.109*** estará disponível a tag, BI Self-Service, para controle de acesso ao ícone “***BI Self-Service***“ disponível no menu "*Gestão Estratégica*" do produto *Inteligência de Negócios*.

false

*Como em versões anteriores a mencionada acima não havia controle de segurança para o ícone BI Self-Service, a partir desta, o botão por default ficará desabilitado.*

Veja também:

 ***Veja os principais conteúdos::***
