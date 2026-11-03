---
content_hash: 25a2de9a6496d5af9cbf7d028adc9da6647ddc897b4ed667c44ab842174a033e
fetched_at: '2026-06-29T00:09:16.020760+00:00'
page_id: '421385443'
product: rm
source: tdn-rm
title: Inclusão de Membro(s) 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385443
version: 18
---

---

Este processo irá buscar no TOTVS Folha de Pagamento os dados do funcionário para associá-lo como um membro de uma determinada equipe.

Esta funcionalidade está disponível através do menu Cadastros|Minha Obra|Equipe do Projeto|Processos|Inclusão de Membros, apenas se o TCOP estiver parametrizado para integração com a Folha de Pagamento.  
Será exibida uma tela (wizard) para execução do processo (vínculo) do funcionário/terceiro com a equipe do projeto selecionado. Caso esteja parametrizado, este vínculo se dará da seguinte forma:

1. Na primeira tela, o usuário deverá informar qual será o tipo do membro, se "funcionário" ou "terceiro";
   1. Se funcionário, o sistema irá buscar, na folha de pagamento, todos os funcionários cadastrados e ativos e que não possuam vínculos a outra(s) equipe(s). Serão considerados apenas os funcionários vinculados ao projeto em questão, identificados através da Filial do projeto.
   2. Se terceiro, o sistema irá buscar no cadastro de terceiros ativos no sistema e que não possuam vínculos a outra(s) equipe(s).
2. Na segunda tela, será exibido o resultado numa grid, para que o usuário possa selecionar um ou mais membros para realização do vínculo.
3. Na terceira tela, será a finalização do processo. O sistema irá fazer o vínculo com a equipe do projeto de todos os funcionários ou terceiros selecionados.

O usuário também poderá fazer a inclusão do membro individualmente. Para isso, basta clicar no botão <Novo> na visão de membros da equipe e será exibido um cadastro no padrão do ERP. O usuário deverá informar qual o tipo do membro (funcionário ou terceiro) e, através de um Lookup da origem dos dados, poderá ser feito o vínculo do membro à equipe.

Será possível também alterar ou excluir um membro da equipe. Para o caso de exclusão, o sistema irá validar se foi dada carga no coletor com algum membro da equipe. Caso haja, o sistema irá verificar se existe algum apontamento de mão de obra pendente para a tarefa em que o membro possui carga. Se existir, o sistema irá gerar uma exceção e informará ao usuário que o membro não poderá ser excluído da equipe e somente poderá ser excluído após a apropriação deste(s) apontamento (s). Caso não exista nenhum apontamento para o membro, o sistema exibirá mensagem informativa "O membro \[nome\_do\_membro\] possui carga em coletor móvel. Deseja continuar a exclusão?". Se confirmar, o membro da equipe será desassociado da equipe.

Caso não tenha sido dada carga em nenhum coletor, seguirá o fluxo normal do sistema e nenhuma mensagem será exibida. Para o caso de alteração, o sistema irá permitir ao usuário editar e alterar os dados do membro, através de cadastro padrão do ERP.

O parâmetro de Projeto "Desconsiderar situação do funcionário/terceiro ao enviar para o coletor" influencia nas equipes e membros que serão enviados para o coletor pois ele define a restrição de situação de funcionários/terceiros que serão enviados para o coletor. Se estiver marcado, não haverá restrição, caso contrário, as situações de pessoas com Apos. Invalidez(I), Demitido(D),  C/[Dem.no](http://dem.no/) mês(X) e Contrato de Trabalho Suspenso(C) serão retiradas da lista de envio para o coletor.

**Importante:**

Se após enviar a equipe para um coletor o encarregado for excluído, o responsável poderá fazer o apontamento no coletor normalmente e estas informações ficarão gravadas e disponíveis no TOP. Como a apropriação de mão de obra não leva em consideração o usuário que executou a tarefa e sim a equipe, estes dados poderão ser apropriados normalmente.  
No processo de admissão de um funcionário no TOTVS Folha de Pagamento, este irá gerar um registro no cadastro de pessoas do TOP. Este funcionário ficará "Ativo" e disponível para vínculo à equipe de mobilidade.  
No processo de demissão de um funcionário, caso ele seja um membro de equipe de projeto, este terá seu status modificado para "Inativo" e não poderá ser vinculado à nenhuma equipe de projeto de mobilidade.   
A partir da data de sua demissão, o funcionário não poderá ter nenhum apontamento apropriado. Apontamentos retornados do coletor com data posterior à demissão serão desconsiderados. Os apontamentos com data anterior à demissão e ainda não importados do coletor serão importados e apropriados normalmente.

É possível incluir um funcionário ou terceiro que já existe na equipe, mas somente se o membro da equipe que já existia estiver inativo e se o novo membro possuir uma função (insumo associado) diferente da função do que foi inativado.

**Observação:**

Esta funcionalidade não deverá estar disponível para projetos globais.
