---
content_hash: 9278da25d8a5bbc4becd8a521e08ad761ff6d0fb20d3d5e5dd3d270ec3f80eb0
fetched_at: '2026-06-29T00:09:14.788117+00:00'
page_id: '421385255'
product: rm
source: tdn-rm
title: Equipe de Mobilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Equipe+de+Mobilidade
version: 25
---

---

A equipe é um conjunto de pessoas (funcionários e terceiros) que podem possuir diferentes funções para o cumprimento de tarefas de um determinado projeto.

Equipe de Mobilidade

Não é permitido que uma pessoa esteja ativa como funcionário e terceiro em uma mesma coligada.

Para incluir uma equipe de mobilidade o usuário deverá clicar em <Novo> e informar os dados necessários para o cadastro, conforme os campos mostrados abaixo:

* **Descrição:** nome da equipe responsável por um determinado projeto.
* **Ativa:** define que a equipe está ativa. Por default, este campo virá marcado. Deverá ser desmarcado caso se deseje desativar a equipe para que não possa ser associada a um projeto.
* **Tipo do Responsável pela Equipe:** define a origem do usuário cadastrado.
* **Usuário (encarregado) responsável pela equipe:** visão de usuários do TOTVS Folha de Pagamento.

Será possível alterar ou excluir uma equipe. Para o caso de exclusão, o sistema irá validar se foi dada carga no coletor com algum membro da equipe.

Caso tenha carga em coletor pendente de apontamento de mão-de-obra, o sistema exibirá mensagem informativa e não permitirá a exclusão da equipe.

Em seguida, será exibida ao usuário a pergunta "Deseja desativar a equipe para lançamentos futuros?".

Caso o usuário confirme, a equipe será desativada e apontamentos desta equipe feitos após esta data não serão mais apropriados e a equipe não estará mais disponível para associação a nenhuma Folha Tarefa.

A equipe somente poderá ser excluída após retorno dos apontamentos do coletor e após apropriação dos apontamentos retornados.

Caso não tenha sido dada carga em coletor, todos os membros da equipe serão desassociados e a equipe será excluída.

**Importante:**

* Não existirão restrições sobre a quantidade de membros associados às equipes.
* Se após enviar a equipe para um coletor o encarregado for excluído, o responsável poderá fazer o apontamento no coletor normalmente e estas informações ficarão gravadas e disponíveis no TOP. Como a apropriação de mão de obra não leva em consideração o usuário que executou a tarefa e sim a equipe, estes dados poderão ser apropriados normalmente.
* No processo de admissão de um funcionário no TOTVS Folha de Pagamento, este irá gerar um registro no cadastro de pessoas do TOP. Este funcionário ficará "Ativo" e disponível para vínculo à equipe de mobilidade.
* No processo de demissão de um funcionário, caso ele seja um membro de equipe de projeto, este terá seu status modificado para "Inativo" e não poderá ser vinculado a nenhuma  equipe de projeto de mobilidade.
* A partir da data de sua demissão, o funcionário não poderá ter nenhum apontamento apropriado.
* Apontamentos retornados do coletor com data posterior à demissão serão desconsiderados. Os apontamentos com data anterior à demissão e ainda não importados do coletor serão importados e apropriados normalmente.
* Só estarão disponíveis os funcionários definidos no momento da entrada do Apontamento, que não possuem pendências no Encerramento.

Para esta funcionalidade existe uma aba dentro da edição da equipe chamada **'Mapa'**, durante o registro dos apontamentos informações da localização são coletadas e enviadas no sincronismo para o sistema, com isso é possível verificar as posições dos apontamentos do coletor.

Para habilitar esta funcionalidade é preciso configurar em menu Ambiente > Parâmetros > Parâmetros Globais > aba Google, e preencher o campo 'Chave de identificação para o Google Maps'.

Anexos

---

[Alocação de Mão de Obra da Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=421385139)

[Tarefas Associadas à Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=421385511)

 

[Apontamento de Mão de Obra](https://tdn.totvs.com/pages/viewpage.action?pageId=421385097)

[Histórico de Membros de Equipe (Folha de Produtividade)](https://tdn.totvs.com/pages/viewpage.action?pageId=886653264)

Processos

---

 

[Gerar Relatório de Membros de Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=555869084)

[Ativar/Desativar Membros de Equipe](https://tdn.totvs.com/pages/editpage.action?pageId=886646094)
