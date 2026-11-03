---
content_hash: bc1d5056825b99ef08837112dc34ce898dd0f49c4411b596511bf99da23326ee
fetched_at: '2026-06-29T00:09:32.707265+00:00'
page_id: '425458905'
product: rm
source: tdn-rm
title: Atualizar Etapas de Turma/Disciplinas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458905
version: 12
---

Este processo compreende a atualização de etapas criadas no anexo "Modelos de etapas por período" do anexo do "Período Letivo" dentro do Anexo "Etapas" das Turmas/Disciplinas. O mesmo poderá ser executado no contexto superior e básico.   
Selecione um ou mais registro na visão de cadastro do Período Letivo, ao chamar o respectivo processo, o sistema irá exibir todas as turmas/disciplinas pertencentes ao(s) período(s) letivo(s) selecionado(s).  
Filtro: para um seleção mais criteriosa dos registros listados no processo, é possível criar filtros específicos para serem atualizados. Exemplo dentro de um período letivo em que são listadas mais de uma turma, é possível selecionar apenas uma. O sistema permite executar e remover filtro.  
Selecione as turmas que terão suas etapas atualizadas.

Selecione os parâmetros abaixo de acordo com o tipo de processo que se quer realizar.

**Parâmetros:**  
-> Duplicidade de Etapa final manter:

1
incomplete
Da Turma/Disciplina

2
incomplete
Do Modelo de Etapa

Aqui o usuário informa em caso de duplicidade de Etapa final qual etapa deverá ser mantida, se da turma/disciplina ou do modelo de etapa.

-> Selecionar modelo de Etapas para Atualização:

Este parâmetro tem como objetivo, oferecer mais praticidade ao usuário para excluir os modelos de etapas desnecessárias para atualização nas turmas/Disciplinas. Ao marcar este parâmetro, o sistema irá habilitar o botão: "Remover Etapas" onde o usuário tem a opção de remover os modelos de etapas. Para os modelos de Etapas de Notas que possui Avaliações vinculadas, ao remover a mesma, as avaliações associadas também serão removidas.

**Exemplo:**  
Na turma/disciplina existem as etapas com os códigos:  
**- 01 -** Tipo Nota, configurada como Etapa Final.  
**- 02 -** Tipo Nota  
**- 03 -** Tipo Nota No Período Letivo existem as etapas com os códigos:  
**- 02 -** Tipo Nota  
**- 03 -** Tipo Nota  
**- 04 -** Tipo Nota, configurada como Etapa Final.

Ao executar o processo para atualizar as etapas com a opção **Da Turma/Disciplina** selecionada, o sistema irá manter a etapa **01**, atualizar as etapas **02** e **03** e adicionar a etapa **04** na turma/disciplina.

Como não é possível ter 2 etapas do mesmo tipo como "Etapa Final" e foi selecionada a opção para manter a etapa final da Turma/Disciplina, o sistema irá manter a etapa **01** como Etapa Final e a **04** deixará de ser etapa final.

Selecionar Modelo de Etapas para Atualização - ao marcar este parâmetro o sistema irá listar o modelo de etapas disponíveis para o período letivo informado na aba seleção, ao clicar no botão 'Carregar modelos de etapas", os respectivos modelos serão carregados.

Atualizar Modelo de Avaliações - aqui o sistema irá definir se o modelo de avaliações também serão atualizados nas respectivas turma/disciplinas. Caso estes dois itens não sejam marcados, os mesmos não serão carregados para visualização e seleção, em seguida o processo será executado.

Clique em "Executar" para execução do processo.

Obs.: Você poderá ver este processo com outra perspectiva em: Currículo e Oferta > Oferta > Parametrização por curso > Processos > Atualizar etapas de turma/disciplina.

**Filtro:** para uma seleção mais criteriosa dos registros listados no processo, é possível criar filtros específicos para serem atualizados. Exemplo dentro de um período letivo em que são listadas mais de uma turma é possível selecionar apenas uma. O sistema permite executar e remover filtro.

**Ícone Exclusão:**

O Ícone de exclusão será aplicado de duas formas:

1. Exclusão da seleção de filtros: Quando o usuário executar o filtro que não condiz com as turmas desejadas, basta clicar no ícone para desfazer a seleção, retornando a listagem original de todas as turmas/disciplinas cadastrado na Parametrização do Curso selecionada.
2. Exclusão da marcação selecionada: Quando usuário marcar um ou mais registros erroneamente, não é será necessário clicar no checkbox a frente da turma/disciplina, o mesmo poderá clicar no ícone em questão para desfazer a seleção, retornando a listagem original de todas as turmas/disciplinas cadastrado na Parametrização do Curso selecionada.

**Parâmetros:**

1. Selecionar Modelos de etapas para atualização: Esse parâmetro irá definir se o modelo de avaliações será atualizado em todas as turma/disciplinas selecionadas ao executar o processo. Ao marcar apenas este parâmetro, o sistema irá atualizar também as etapas de notas e faltas.
2. Atualizar modelo de Avaliação: Quando o processo for executado pelo cadastro de "Período Letivo", será possível selecionar um período letivo com seus modelos de etapas, e estes modelos serão utilizados para atualizar todas as turma/disciplinas selecionadas; se o processo for executado pelo cadastro de parametrização por Curso.
3. Atualizar Turmas(s) Livre(s) do Período letivo informado: Esse parâmetro estará disponível apenas quando o processo for executado no cadastro: *Parametrização por Curso*, pois quando o processo for executado pelo cadastro do *Período Letivo*, as turmas livres já estarão disponíveis e o processo de atualização do modelo de etapa selecionado será aplicado em todas as turmas livres do período letivo informado se o usuário selecionar as Turmas Livres em questão.

**Botões:** Ao clicar nos parâmetros: Selecionar modelos de etapas para atualização, o sistema irá habilitar o botão 'Carregar Modelos de Etapas', este botão é utilizado para visualizar os modelos de etapas de notas/faltas e os modelos de avaliação para a Parametrização informada, estas informações serão visualizadas na guia Modelos contendo duas sub-guias: Etapas e Avaliações.

### Ensino Básico

É possível atualizar as etapas das turmas/disciplinas do itinerário formativo, estas disciplinas virão listadas na grid principal do processo e estarão identificadas pela coluna de **itinerário formativo**ao qual a turma/disciplina pertence.

Veja Também

---

[Boletim Técnico - "Botão: Remover Modelo de Etapas" no processo: Atualizar Etapas Turma/Disciplina](http://tdn.totvs.com/download/attachments/187532827/EDU_BT_Atualizar_Etapas_TurmaDisciplina_PCREQ-3677%28C360464%29.pdf?version=1&modificationDate=1430758582000&api=v2)
