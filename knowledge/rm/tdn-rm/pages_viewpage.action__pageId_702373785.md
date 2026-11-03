---
content_hash: c793f7c19b90170db912b9ee3075590a6dbea8059beffdb272d630e352fdc8cd
fetched_at: '2026-06-29T00:11:22.404919+00:00'
page_id: '702373785'
product: rm
source: tdn-rm
title: Prospecções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=702373785
version: 44
---

---

O cadastro de prospecção tem o intuito de oferecer um plano de pagamento e/ou uma bolsa a um aluno, um candidato e/ou um prospect.

Entenda um prospect como uma pessoa que, ainda, não possui um cadastro no RM e não é vinculada a um papel de aluno e/ou candidato.

Após vinculado um plano de pagamento e/ou uma bolsa a um aluno, candidato ou prospect, esses serão atribuídos durante o seu processo de matrícula e serão sobrepostos a outros parametrizados no sistema.

Permissões

As permissão de acesso às prospecções estão disponibilizadas junto à arvore de permissões do menu de contratos.

Foram criadas as permissões para a visualização, inclusão, alteração e exclusão de prospecções.

false

**Caminho**: *Educacional | Financeiro / Contábil | Contratos | Prospecções*

Para o correto funcionamento do componente de Prospecção é preciso também liberar as permissões de acesso da Gestão Educacional.

false

**Caminho**: *Educacional | Educacional (Portal)/ Gestão Educacional*

A permissão principal irá impedir o acesso a tela de cadastro da prospecção, através do menu do Educacional:

Listagem das prospecções cadastradas

Através do botão "Listar prospecções cadastradas" é possível acessar todas as prospecções que foram cadastradas no sistema para a edição de informações e, também, sua exclusão.

A permissão de exclusão irá ser aplicada à lista de prospecções cadastradas, onde o ícone da lixeira, relacionado a exclusão, poderá ser desabilitado para evitar que essa ação seja realizada por quem não for autorizado.

O ícone referente a um lápis irá carregar todas as informações da prospecção para consulta e, também, para a inclusão/alteração de prospects.

Todas as informações, inclusas e/ou alteradas, na prospecção serão salvas através do botão **"Salvar"** no final da tela e o mesmo será habilitado, somente, se o usuário tiver as permissões de inclusão e/ou alteração atribuídas ao seu perfil.

Se uma **nova prospecção** estiver sendo cadastrada, será necessário que a **permissão de inclusão** seja atribuída. Contudo, se a prospecção for **carregada da lista de prospecções**, será necessária a atribuição da **permissão de alteração** para o gravação das informações.

Filtros de prospects

## **Filtros de prospects**

Existem 03 tipos de prospects que poderão ser utilizados para a inclusão de um plano de pagamento e/ou bolsa na prospecção: aluno, candidato, prospect.

Através de filtros específicos, podem encontrar um aluno ou um candidato, já existente, ou informar, através do tipo prospect, um CPF/Passaporte e um nome de alguém que não possui cadastro no sistema.

### Aluno

Através dos campos de coligada, filial, nível de ensino, período letivo, curso, habilitação, matriz, turno, turma e aluno é possível refinar uma pesquisa por um aluno trazendo um único ou um grupo de registros, caso não sejam informados todos os campos.

Os campos não são obrigatórios, com exceção das informações do contexto: coligada, filial e nível de ensino.

### Candidato

Através dos campos de coligada, filial, processo seletivo, área ofertada e candidato é possível refinar uma pesquisa por um candidato trazendo um único ou um grupo de registros, caso não sejam informados todos os campos.

Os campos não são obrigatórios, com exceção da coligada do contexto.

### Prospect

Como um prospect não possui cadastro no sistema, os campos disponibilizados são para a inclusão das informações que serão cadastrados e utilizadas em uma futura matrícula.

Poderão ser informados um código de CPF ou passaporte e o seu nome completo.

Importante

O nome do prospect precisa ter pelo menos um nome e um sobrenome que totalizem mais que 05 caracters.

## **Plano de pagamento/Bolsa**

A inclusão de um plano de pagamento e/ou uma bolsa depende totalmente de um filtro de prospect informado. Ao clicar em adicionar, será incluído um registro de todos prospects filtrados ao plano de pagamento ou a bolsa informada.

### Plano de pagamento

Para a inclusão do plano de pagamento, deverão ser informados os campos: Período letivo e o plano de pagamento.

### Bolsa

Para a inclusão da bolsa, deverão ser informados os campos: período letivo, período de validade da bolsa, bolsa, tipo de desconto, valor ou percentual, serviço, tipo do período (parcela ou data) e o número de parcela inicial e final ou a data inicial e final.

* O campo "**Período de validade da bolsa"** indica se a bolsa será aplicada apenas para um único período letivo ou para todo o curso.
  + **Em todo curso:** A bolsa é aplicada para todos períodos letivos que o prospect for matriculado respeitando a **Data inicial** e **Data final** ou seja a bolsa será aplicada a todos contratos do aluno que estejam dentro da data inicial e final da bolsa cadastrada via prospecção. (Neste caso, a bolsa de estudos selecionada deve estar vinculada a todos períodos letivos dentro de intervalo de datas informado para o prospect, paras mais informações vide )
  + **Período letivo:**A bolsa é aplicada apenas para o período letivo informado durante o cadastro.

A bolsa incluída através da prospecção deve seguir as regras aplicadas na bolsa futura. Vide ()

Regras para aplicação de bolsa prospect.

-As bolsas cadastradas para um prospect serão aplicadas ao contrato durante a criação e edição das parcelas.

-Para confirmação de matrícula via portal do aluno as seguintes regras são aplicadas:

1. Para uma matrícula sem contrato, a bolsa do prospect será aplicada normalmente.
2. Para uma matrícula com contrato previamente gerado sem bolsa de prospect e sem parcelas, as parcelas serão geradas e a bolsa de prospect serão gerados apenas se o plano de pagamento for alterado durante a matrícula via portal do aluno, caso contrário nada será feito.
3. Para uma matrícula com contrato previamente gerado sem bolsa de prospect com parcelas, a bolsa de prospect é incluída no contrato durante a matrícula via portal do aluno. Caso já existam lançamentos para as parcelas, as bolsas são vinculadas ao contrato, porém, os lançamentos deverão ser regerados para que a bolsa seja aplicada.
Lista de prospects

Após clicar no botão "Adicionar", todos os prospects serão inseridos na lista e serão relacionados a um plano de pagamento e/ou uma bolsa .

Os ícones relacionados à lixeira e e ao lápis permitirão a exclusão e edição do registro, respectivamente.

Matricula na Central do Candidato, Portal do Aluno e Oferta Online

O sistema disponibilizou uma funcionalidade que permitirá que a instituição de ensino realize negociações de plano de pagamento e de bolsa(s) com o prospect (futuro aluno) a fim de viabilizar a matrícula deles.

Essa negociação permitirá associar planos de pagamento e/ou bolsas criados previamente a uma pessoa, seja um prospect, ou aluno, para atender campanhas e negociações na captação de alunos.

Plano de pagamento e bolsa associado ao prospect:

Caso o aluno possua um único plano de pagamento e/ou bolsa(s) associado ao seu CÓDIGO de RA ou CPF (ou passaporte, no caso de estrangeiro), ao finalizar o processo de matrícula, será associado ao contrato, o plano e/ou bolsa(s) que está associados ao prospect. 

 

Caso o aluno possua mais de um plano de pagamento associado ao seu CÓDIGO ou CPF (ou passaporte, no caso de estrangeiro), o sistema irá exibir os planos associados para que o aluno selecione o de sua preferência, e irá associar ao contrato o plano de pagamento que foi selecionado na tela:

e nessa mesma tela também será possível ter a visão da simulação da(s) bolsa(s) associada(s) ao prospect.

**P.S.: Sempre que existir um plano de pagamento/bolsa associado ao Prospect, somente estes planos/bolsas serão exibidos para o aluno/candidato/prospect na Central do Candidato, Portal do Aluno e Oferta Online. Os planos de pagamento/bolsas parametrizados no sistema, para os processos em questão, não serão exibidos.**

ATENÇÃO

A partir dos patches **12.1.2306.197** e **12.1.2310.131** na realização da matrícula na central do candidato, caso o candidato tenha prospecções de bolsas, o sistema irá considerar as datas de vencimentos das parcelas do plano de pagamento vinculado à área de interesse considerada na matrícula para verificação da validade das bolsas.

ATENÇÃO

A aplicação de bolsas ao prospect depende da existência de parcelas correspondentes no plano de pagamento. Para que a bolsa seja integrada ao contrato:

* O plano de pagamento vinculado à prospecção deve possuir parcelas para o serviço vinculado à bolsa;
* Na ausência de um plano fixo na prospecção, o plano escolhido durante a matrícula deve contemplar esses mesmos serviços.

**Nota:** Sem essa correspondência entre o serviço da bolsa e a parcela do plano, o benefício não será aplicado.

  Recursos Adicionais

---

[Documentação da API de Prospecção (openAPI)](https://tdn.totvs.com/pages/viewpage.action?pageId=843148170)
