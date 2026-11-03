---
content_hash: bc9d56eca11a2f2ce4b2b4f035e5fbc1190be136741f58e1e32fcc5b8d1267d5
fetched_at: '2026-06-29T00:09:32.633967+00:00'
page_id: '425458893'
product: rm
source: tdn-rm
title: Atualizar etapas das turmas/disciplinas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458893
version: 18
---

O Processo para atualizar etapas de turma/disciplina poderá ser executado a partir de dois cadastros: Período Letivo e Parametrização por Curso. Para ambos os processos, será permitido selecionar mais de um registro na visão dos cadastros para executar o processo de atualização; ao selecionar os registros para execução do processo, serão exibidas as turmas/disciplinas correspondentes aos registros marcados [x] da visão dos cadastros (Parametrização por Curso ou Período letivo).

Ao executar o processo pelo cadastro de "Período Letivo", o sistema irá exibir todas as turmas/disciplinas pertencentes ao(s) período(s) letivo(s) selecionado(s), inclusive as turmas/disciplinas livres, porém, quando este processo for executado pelo cadastro "Parametrização por curso", o sistema irá exibir todas as turma/disciplinas pertencentes a(s) matrizes aplicada(s) conforme a seleção do usuário, as turmas livres serão listadas conforme a informação do período letivo no qual serão copiados os modelos de etapas e avaliações para as turmas/disciplinas selecionadas. Para apresentar as turmas/disciplinas livres do período letivo informando, o usuário terá que habilitar os parâmetros: "Selecionar Modelo de Avaliação" e "Atualizar turma(s) livre(s) do período letivo informado".  
A atualização do modelo de etapa das turma/disciplinas marcadas [x] serão realizadas de acordo com a chamada do processo. Ou seja, se o processo for executado pelo cadastro de Período Letivo, as etapas serão atualizadas de acordo com o modelo de etapas do período letivo da turma/disciplina. Mas se o processo for executado pelo cadastro de Parametrização por Curso, as etapas serão atualizadas de acordo com o modelo de etapa cadastrado na Parametrização por Curso da turma/disciplina (Matriz aplicada da Turma/Disciplina).  
Para executar os processos em questão, seguir os caminhos abaixo:

* **Parametrização por curso:** Currículo e Oferta | Oferta | Parametrização por Curso [editar a(s) Parametrização(ões)] | Processo | Atualizar Etapas de Turmas/Disciplinas
* **Período Letivo:** Currículo e Oferta | Oferta | Período Letivo [editar o(s) Período(s) Letivo(s)] | Processo | Atualizar Etapas de Turmas/Disciplinas.

**Filtros:**  
     Para facilitar a seleção de um grupo específico de turma/disciplinas a serem atualizadas, existe a opção para as duas visões a criação /aplicação de um filtro sobre as turmas/disciplinas, assim o usuário poderá ter uma seleção mais criteriosa dessas turmas/disciplinas que deseja visualizar para realizar o processo de atualização.

**Ícone Exclusão:**  
 O Ícone de exclusão será aplicado de duas formas:

1. Exclusão da seleção de filtros: Quando o usuário executar o filtro que não condiz com as turmas desejada, basta clicar no ícone para desfazer a seleção, retornando a listagem original de todas as turmas/disciplinas cadastrados na Parametrização do Curso selecionada.
2. Exclusão da marcação selecionada: Quando usuário marcar um ou mais registros erroneamente, não será necessário clicar no checkbox a frente da turma/disciplina, o mesmo poderá clicar no ícone em questão para desfazer a seleção, retornando a listagem original de todas as turmas/disciplinas cadastrado na Parametrização do Curso selecionada.

**Parâmetros:**

1. Selecionar Modelos de etapas para atualização: Esse parâmetro irá definir se o modelo de avaliações será atualizado em todas as turmas/disciplinas selecionadas ao executar o processo. Ao marcar apenas este parâmetro, o sistema irá atualizar também as etapas de notas e faltas.
2. Atualizar modelo de Avaliação: Quando o processo for executado pelo cadastro de "Período Letivo", será possível selecionar um período letivo com seus modelos de etapas, e estes modelos serão utilizados para atualizar todas as turmas/disciplinas selecionadas; se o processo for executado pelo cadastro de parametrização por Curso.
3. Selecionar modelo de Etapas para Atualização: Este parâmetro tem como objetivo, oferecer mais praticidade ao usuário para excluir os modelos de etapas desnecessárias para atualização nas turmas/Disciplinas. Ao marcar este parâmetro, o sistema irá habilitar o botão: "Remover Etapas" onde o usuário tem a opção de remover os modelos de etapas. Para os modelos de Etapas de Notas que possui Avaliações vinculadas, ao remover a mesma, as avaliações associadas também serão removidas.
4. Atualizar Turmas(s) Livre(s) do Período letivo informado: Esse parâmetro estará disponível apenas quando o processo for executado no cadastro: *Parametrização por Curso*, pois quando o processo for executado pelo cadastro do *Período Letivo*, as turmas livres já estarão disponíveis e o processo de atualização do modelo de etapa selecionado será aplicado em todas as turmas livres do período letivo informado se o usuário selecionar as Turmas Livres em questão.

**Botões:**  
      Ao clicar no parâmetro: Selecionar modelos de etapas para atualização, o sistema irá habilitar o botão 'Carregar Modelos de Etapas', este botão é utilizado para visualizar os modelos de etapas de notas/faltas e os modelos de avaliação para a Parametrização informada, estas informações serão visualizadas na guia Modelos contendo duas sub-guias: Etapas e Avaliações.

### Ensino Básico

É possível atualizar as etapas das turmas/disciplinas do itinerário formativo, estas disciplinas virão listadas na grid principal do processo e estarão identificadas pela coluna de **itinerário formativo**ao qual a turma/disciplina pertence.

Observação

A partir da versão 12.1.32 foi criado o parâmetro "Permitir cadastrar avaliação", na etapa do tipo notas. Caso a etapa da turma/disciplina já tenha avaliação cadastrada não será possível desabilitar o parâmetro, mas os outros dados da etapa será atualizado, apenas o parâmetro não será desmarcado caso tenha no mínimo uma avaliação cadastrada na etapa da turma/disciplina. A seguinte mensagem de alerta será exibida para o usuário.

Recursos Adicionais

---

[Boletim Técnico - "Botão: Remover Modelo de Etapas" no processo: Atualizar Etapas Turma/Disciplina](http://tdn.totvs.com/download/attachments/187532827/EDU_BT_Atualizar_Etapas_TurmaDisciplina_PCREQ-3677%28C360464%29.pdf?version=1&modificationDate=1430758582000&api=v2)
