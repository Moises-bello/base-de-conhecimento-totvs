---
content_hash: 4bdcf3905e49398e570a7e444bfdb3f9e4baef4641df8ee9ac8f36b926f28619
fetched_at: '2026-06-29T00:11:44.779193+00:00'
page_id: '815585623'
product: rm
source: tdn-rm
title: Internação e Procedimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=815585623
version: 29
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Solicitação de internação**
4. **Solicitação de procedimentos**
5. **Solicitação de procedimentos e internação e OPME**
6. **Prorrogação**
7. **Cadastro RM**
8. **Atualização V.12.1.2410**
9. **Atualização V.12.1.2506**

falsepaineltrueVisão Geral

## **01. VISÃO GERAL**

Recurso que permite ao usuário realizar a solicitação de internação, procedimentos ou internação e procedimentos. 

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

* Ao clicar no menu de "Solicitações" e no submenu de "Internação e Procedimentos", será exibido na tela, se houver, uma lista com o histórico de solicitações com a opção de expandir e visualizar as informações preenchidas anteriormente.

* Ao expandir o accordion é exibido na tela os detalhes da solicitação e os botões para imprimir, suspender ou visualizar a solicitação.

* Ao clicar em "Imprimir" será exibido um modal para selecionar qual relatório o usuário deseja imprimir. Após selecionar clique no botão "Imprimir." A página para impressão será exibida em uma nova guia do navegador no formato PDF.

* Ao clicar em "Visualizar", será exibido na tela as informações preenchidas anteriormente pelo usuário:
  + Se o registro estiver salvo como rascunho os campos estarão desbloqueados e o usuário poderá fazer alterações e finalizar a solicitação ou excluir o rascunho.

* + Se a solicitação estiver finalizada os campos estarão bloqueados e não será permitido ao usuário fazer alterações, somente suspender.

* Ao clicar em "Suspender", será exibida a tela um modal solicitando confirmação para a suspensão. Para concluir clique no botão "Confirmar". O registro ainda será exibido na tela com a sinalização de suspensão conforme comportamento já existente.

Solicitação de Internação

## **03. SOLICITAÇÃO DE INTERNAÇÃO**

* Para realizar o registro de uma nova internação, clique no botão "+ Novo". Será exibido um modal para selecionar qual solicitação o usuário deseja realizar.

* Após selecionar  "Somente Internação", ao clicar no botão "Criar" no modal será exibido a tela com as informações a serem preenchidas.

* Para finalizar a solicitação devem ser informados os campos obrigatórios:
  + "Tipo de internação"
  + "Regime de internação"
  + "Caráter de internação"
  + "Indicação de acidente"
  + "Quantidade de diárias"
  + "CID principal"
  + "Indicação clínica"
  + Também podem ser informados os campos não obrigatórios: "Tipo de doença", "Tempo de doença" e "Observação/Justificativa".
* Para incluir a solicitação clique no botão "Finalizar" ou para cancelar a solicitação clique no botão "Excluir".

* Ao finalizar a solicitação, se a assinatura digital estiver habilitada o modal de assinatura será exibido:

* Se assinatura digital estiver desabilitada será exibido o modal de confirmação:

Solicitação de Procedimentos

## **04. SOLICITAÇÃO DE PROCEDIMENTOS**

* Para realizar o registro de um novo procedimento, clique no botão "+ Novo". Será exibido um modal para selecionar qual solicitação o usuário deseja realizar.

* Após selecionar "Somente procedimentos", ao clicar no botão "Criar" no modal será exibido a tela com as informações a serem preenchidas.

* O usuário poderá salvar um modelo de solicitação ou utilizar um modelo salvo anteriormente clicando nos botões "Salvar modelo" e  "+ Usar modelo", leia mais sobre
* Para finalizar a solicitação devem ser informados os campos: 
  + "Caráter do Atendimento" (se Eletivo ou Urgência/Emergência)
  + Indicação clínica (TISS)
  + Observação / Justificativa
  + No campo "Adicionar procedimentos" o usuário terá acesso a todos os itens da lista ou poderá buscar por um procedimento especifico. Poderá ser adicionado um ou mais itens por vez clicando no botão "Adicionar".

* Ao selecionar os itens, será criada uma lista na parte inferior. Ao expandir o accordion de cada item serão exibidos os campos: "Data", "Hora" e "Observação".
* Para excluir o procedimento adicionado clique no ícone, e o item será apagado da lista.

* Para incluir a solicitação clique no botão "Finalizar".
* Ao clicar no botão "Finalizar e imprimir", será exibido um modal para selecionar a forma de impressão por relatório padrão ou por guia TISS.

Solicitação de Internação e Procedimentos e OPME

## **05. SOLICITAÇÃO DE INTERNAÇÃO E PROCEDIMENTOS E****OPME**

* Para realizar o registro de uma internação e procedimentos, clique no botão "Novo". Será exibido um modal para selecionar qual solicitação o usuário deseja realizar.

* Após selecionar "Internação e Procedimentos", ao clicar no botão "Criar" no modal será exibido a tela com as informações a serem preenchidas.

* Para finalizar a solicitação devem ser informados os campos obrigatórios:
  + "Tipo de internação"
  + "Regime de internação"
  + "Caráter de internação"
  + "Indicação de acidente"
  + "Quantidade de diárias"
  + "CID principal"
  + "Indicação clínica"
  + Também podem ser informados os campos não obrigatórios: "Tipo de doença", "Tempo de doença" e "Observação/Justificativa" (com limite de até 2000 caracteres).
* **Na tabela de "Procedimentos"** serão  exibidas as colunas de "Tipo", "Nome do procedimento", "Data" e "Hora".
* Para incluir um procedimento, clique no botão "Adicionar".

* Será exibido na tela um modal para escolher o tipo de procedimento: "Cirúrgico" ou "Outros".

* Ao selecionar **"Outros"**, serão exibidos os campos "Selecione o procedimento" e "Observação". Após preencher os campos, para incluir o procedimento na tabela clique no botão "Adicionar".

* Ao selecionar procedimento **"****Cirúrgico"**, serão exibidos os campos: "Selecione o procedimento", "Data", "Hora", "Descrição da cirurgia" e "Observação". Para incluir o procedimento na tabela clique no botão "Adicionar".
* Após salvar um procedimento cirúrgico com a inclusão de data e hora, ao adicionar outro procedimento também cirúrgico, o campo "Descrição" é preenchido automaticamente, com a possibilidade do profissional alterar a descrição.

* Ao expandir o accordion, serão exibidos na tela os campos preenchidos durante a inclusão dos procedimentos:

* **A tabela relacionada aos itens de OPME** exibe as colunas: "Procedimento" (nome do procedimento cirúrgico), "Material/Medicamento", "Quantidade" e "Observação", com as opções de excluir ou editar cada item.
* Para os procedimentos cirúrgicos que tiverem um OPME vinculado no RM, será exibido abaixo da tabela de procedimento uma tabela com todos os OPME cadastrados para aquele respectivo procedimento.
* O usuário pode adicionar um novo OPME clicando no botão "Adicionar".

* Será exibido um modal para preenchimento dos campos:
  + Procedimento Cirúrgico (a lista é composta pelos procedimentos adicionados na tabela "Procedimento")
  + Material/Medicamento
  + Quantidade
  + Observação
* Os campos são obrigatórios, exceto "Observação".
* Clique no botão "Adicionar" para incluir o material/medicamento na tabela.

* Ao adicionar um procedimento cirúrgico será exibido na tabela o OPME vinculado a ele no RM.
* Não é possível adicionar o mesmo OPME mais de uma vez.
* Ao clicar no ícone  é exibido um modal que possibilita editar os campos "Quantidade" e "Observação". Para finalizar a edição clique no botão "Adicionar".
* O campo "Quantidade" sempre exibirá a quantidade mínima de 1 material/medicamento e o usuário poderá adicionar mais.
* Para concluir a solicitação clique no botão "Finalizar".
* Para cancelar a solicitação clique no botão "Excluir".

* Ao clicar no ícone , é exibido um modal de confirmação para a exclusão. Para excluir clique no botão "Confirmar". Os itens serão apagados da tabela.

* Ao finalizar a solicitação, se a assinatura digital estiver habilitada o modal de assinatura é exibido:

* Se assinatura digital estiver desabilitada é exibido o modal de confirmação:

Prorrogação

## **06. Prorrogação**

* Ao clicar no menu de solicitação de "Procedimentos e Internação", será exibido a lista com os registros para o mesmo atendimento.
* Para realizar a prorrogação de uma internação clique no botão "Novo".

* Será exibido no modal um aviso alertando ao usuário que o paciente já está internado e as opções para selecionar qual solicitação o usuário deseja realizar.

* Após selecionar  "Somente Internação" ou "Internação e Procedimentos", para finalizar a prorrogação devem ser informados os campos "Quantidade de diárias", "CID principal" e  "Indicação clínica".

* Ao finalizar a solicitação, se a assinatura digital estiver habilitada o modal de assinatura é exibido:

* Se assinatura digital estiver desabilitada é exibido o modal de confirmação:

Cadastro RM

## **07. CADASTRO RM**

**Cadastro da lista de procedimentos "Cirúrgicos":** RM > Cadastro > Cirurgias > Procedimentos para agenda de cirurgia > (ícone   ou Ctrl+Ins) > Aba "Identificação" > Preencha os campos "Descrição" e "Tempo do Procedimento em horas" > Salvar > OK.

**Cadastro da lista de procedimentos "Outros":** RM > Cadastros > Prescrição médica > Itens da Enfermagem > Filtro "Tipo Item" > Selecione "Procedimento" > Clique no ícone  (ou Ctrl+Ins) para adicionar > Descreva o procedimento no campo "Descrição" > No campo "Tipo Item" selecione "Procedimento" > Salvar > Ok.

**É possível realizar a impressão de duas formas ao finalizar, por relatório padrão ou por guia TISS.** Existe um parâmetro que define o padrão de impressão para solicitações de procedimento em:

RM > Cadastros > Unidade Atendimento > Aba PEP RM > Aba Solicitação de procedimentos > Selecione o padrão desejado > Salvar > OK.

**Para configurar a guia TISS:** RM > Cadastros > TISS > Versão TISS e configurar com a opção correta na aba PEP RM. 

**Cadastro OPME:** RM > Cadastro > Cirurgias > Procedimentos para agenda de cirurgia > (ícone   ou Ctrl+Ins) > Identificação (preencher código, descrição e tempo do procedimento em horas, clique em "Salvar" >  Órtese/Prótese (ícone   ou Ctrl+Ins) > Preencha os campos com o nome do material/medicamento e a quantidade > Salvar > OK. .

Atualização V.12.1.2410

## **8.****Atualização V. 12.1.2410**

##### **Funcionalidade disponível a partir da versão 12.1.2410.**

A partir da versão 12.1.2410, a funcionalidade de "Solicitação de internação" e "Internação e procedimentos" cirúrgicos do PEP passaram por atualização visual e foram adicionados novos campos na tela de solicitação. As informações preenchidas nesses campos serão disponibilizadas para a equipe administrativa no sistema de , para realizar o cadastro do pré-agendamento cirúrgico no RM, compra de materiais e para que as autorizações de convênios sejam registradas de forma completa, facilitando o planejamento e garantindo que todos os requisitos sejam atendidos.

**Campo para "Solicitação de internação":**

* Vaga de UTI?: Campo obrigatório onde o profissional deverá indicar se o paciente precisará ou não de uma vaga de UTI.
* Unidade de Atendimento: Campo opcional para selecionar a unidade específica para a qual o paciente será internado. A unidade selecionada será exibida no sistema de gestão de leitos, facilitando a alocação dos pacientes e garantindo que a ocupação dos leitos seja feita de forma eficiente e segura.

**Campos para solicitação de "Internação e procedimentos" (os campos de informações cirúrgicas serão exibidos após o usuário adicionar um procedimento do tipo cirúrgico):**

* Vaga de UTI?: Campo obrigatório onde o profissional deverá indicar se o paciente precisará ou não de uma vaga de UTI.
* Unidade de Atendimento: Campo opcional para selecionar a unidade específica para a qual o paciente será internado.
* Necessita de leito?: Campo obrigatório para informar se o(a) paciente precisará de leito selecionando uma das opções: "Unidade de internação", "UTI" e "Não".
* Hemocomponentes: Campo obrigatório para informar se o(a) paciente precisará de hemocomponentes selecionando uma das opções: "Sim" ou "Não".
* Alergia a látex: Campo opcional para informar se o(a) paciente possui alergia a látex selecionando uma das opções: "Sim" ou "Não". Se o(a) paciente não souber informar sobre a alergia, o(a) médico(a) poderá deixar o campo em branco, não selecionando nenhuma opção.
* Gestante: Campo opcional para informar se a paciente é gestante, selecionando uma das opções: "Sim" ou "Não". Se a paciente não souber informar sobre a gravidez, o(a) médico(a) poderá deixar o campo em branco, não selecionando nenhuma opção.

Atualização V.12.1.2506

## **9.****Atualização V. 12.1.2506**

##### **Funcionalidade disponível a partir da versão 12.1.2506.**

A partir da versão **12.1.2506**, foi incluída no Prontuário Eletrônico do Paciente (PEP) a funcionalidade de **registro da criticidade da cirurgia durante a solicitação de procedimentos cirúrgicos**. Agora, ao realizar uma solicitação de cirurgia, o profissional da saúde deve obrigatoriamente informar o nível de criticidade do procedimento, selecionando uma das seguintes opções: **Emergência, Urgência, Urgência Relativa ou Eletiva**. Esse novo campo faz parte das informações cirúrgicas e só será exibido quando o procedimento adicionado for do tipo cirúrgico. A criticidade informada será salva junto aos demais dados da solicitação e estará disponível para consulta pelas equipes de **Pré-agendamento Cirúrgico** e **Agenda de Cirurgias**, dentro do sistema **RM**, acessível pelo menu **Atendimento > Cirurgia**. Além da exibição, a fila de solicitações na tela de Pré-agendamento agora é automaticamente ordenada de forma decrescente conforme a criticidade, priorizando os casos mais urgentes (Emergência primeiro, seguido por Urgência, Urgência Relativa e, por último, Eletiva). Essa atualização tem como objetivo dar maior visibilidade aos casos críticos, facilitando a triagem e o planejamento das cirurgias pelas equipes administrativas.

### Visualizar a Criticidade no Pré-agendamento e Agenda de Cirurgias (RM)

**Passo a passo:**

1. Abra o aplicativo: **RM**
2. Navegue até o menu: **Atendimento**
3. Acesse a guia: **Cirurgia**
4. Clique em: **Pré-agendamento Cirúrgico ou Agenda de Cirurgias**
5. Localize a solicitação desejada
6. A criticidade da cirurgia será exibida junto com as demais informações da solicitação.
