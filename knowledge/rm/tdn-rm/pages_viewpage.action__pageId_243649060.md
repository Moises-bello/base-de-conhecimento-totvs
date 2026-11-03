---
content_hash: c13e76c96bbdb92b0e3193094154a7f589e65327f462b8a293ba8c98834fb0fc
fetched_at: '2026-06-29T00:08:12.790182+00:00'
page_id: '243649060'
product: rm
source: tdn-rm
title: Integração - Cadastro X Fluxo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243649060
version: 6
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Criar uma integração padrão dos Cadastros da Linha RM, com qualquer aplicação de gerenciamento de fluxos de trabalhos (Workflows). Inicialmente serão suportados fluxos dos aplicativos CRM RM (Agilis) e do TOTVS ECM. Esta integração irá permitir que o usuário configure de forma dinâmica o estado do registro em edição de acordo com um fluxo determinado, e poderá bloquear a edição ou a execução de um processo de acordo com o estado do fluxo.

# Definição da Regra de Negócio:

---

       Serão alteradas as opções de menu referentes aos “Fluxo de Atendimentos”, no menu de processos das visões e edições RM que anteriormente eram utilizadas exclusivamente para fluxos do RM Agilis.

       Este menu continuará a ter a opção Gerenciar e uma opção para criar um fluxo associado ao registro selecionado para cada fluxo que esteja configurado.

       Poderão ser associados um ou mais fluxos de diferentes aplicações no mesmo cadastro, e cada fluxo deverá obedecer um conjunto de regras especifico.

       A tela de gerenciamento de fluxos (menu Gerenciar) permitirá ao usuário configurar os fluxos associados ao cadastro correspondente, e definir as opções de cada fluxo.

 

       Ao clicar no botão "Novo", deverá ser apresentado uma tela para selecionar o tipo de fluxo e as opções especificas do fluxo de acordo com o Tipo.

       Para cada fluxo associado, o usuário deverá informar uma condição para criação daquele fluxo, um assunto e um texto que serão utilizados para a criação do fluxo. Também deverá ter uma opção para que este fluxo seja criado automaticamente quando o usuário inserir um novo registro de forma que não seja necessária a execução do processo de criação de fluxo para o registro.

       Ainda dentro das configurações do fluxo, o usuário poderá definir as configurações específicas para cada estado do fluxo (um estado é um etapa do atendimento ágilis por exemplo). Onde será possível informar uma condição para aplicação de um bloqueio de registro ou processo. Cada estado poderá ter uma ou mais condições de bloqueio e definir se o cadastro ou processo está bloqueado.

       A condição será baseada nos dados do cadastro, e irá conter uma expressão de filtro, onde o usuário irá informar os dados do filtro utilizado o componente de filtro padrão.

       O assunto e o texto poderão utilizar informações do registro, o usuário poderá utilizar expressões entre chaves {}, que serão substituídas pelos valores dos campos do cadastro.

       A opção de Menu “Adicionar atendimento para o registro” será alterada e serão criadas uma opção de “Adicionar fluxo para o registro” para cada fluxo integrado, este processo irá criar um fluxo sob demanda para cada registro selecionado. Esta alteração é necessária devida a opção de criação automática de fluxos quando inserir um registro.

       Deverá também ser alterado o anexo para exibir os registros dos fluxos associados, esta opção deverá ser alterada para pemitir a exibição de fluxos dos vários tipos que poderão ser integrados. Nesta visão serão apresentadas as informações sobre o tipo do fluxo e os dados para identificação do fluxo.

# Operações Especificas por Engine de Workflow:

---

       Dependendo do tipo de workflow selecionado, o sistema irá fazer consultas e interações com o sistema de workflow. Para cada sistema de workflow, é feita uma determinada ação diferente. As seguintes ações são executadas de acordo com cada Engine:

**Funcionalidade: Parâmetros só fluxo**

**Engine: RM CRM**

       O usuário deverá informar qual o grupo de atendimento, tipo de atendimento e modelo de atendimento do Agilis que será utilizado como base da integração com o cadastro.

**Engine: FLUIG ECM**

       O usuário deverá informar qual o Id do Processo do Fluig que será obtido a partir do Web Service WorkflowEngine utilizando a função getAvailableProcess.

**Funcionalidade: Iniciar fluxo automaticamente/criar fluxo relacionado**

**Engine: RM CRM**

       Quando estiver integrado com o fluxo do Agilis o sistema irá criar um novo atendimento do Agilis baseado nos dados informados na tela de parâmetros do fluxo.

**Engine: FLUIG ECM**

       Será feita uma chamada ao Web Service WorkflowEngine utilizando a função startProcess para criar uma nova instância do workflow do Fluig, baseado nos dados informados na tela de parâmetros do fluxo.

**Funcionalidade: Enumerar lista de estados do fluxo**

**Engine: RM CRM**

       Utilizando o Agilis o sistema irá utilizar como base as etapas do atendimento, e as configurações de bloqueio serão baseadas no estado corrente do atendimento.

**Engine: FLUIG ECM**

       No caso do Fluig os estados do processos do serão usados como base das configurações de bloqueio, para buscar a lista de estado será utilizado o Web Service WorkflowEngine e a função exportProcess e para identificar o estado corrente deverá utilizar a função getAllActiveStates.

# Fluxo do Processo:

---

**1.****Diagrama – Casos de Uso**

* Não se aplica

**2.****Diagrama – Atividades**

* Não se aplica

**3.****Diagrama de Classes**

**4.****Diagrama de Entidade e Relacionamento**

**5.****Diagrama de Seqüência**

* Não se aplica

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** Integração Cadastro x Fluxo

falsefalse

**Status:** Finalizado

false

**Data:** 13/06/2016

false

**Autores:**
