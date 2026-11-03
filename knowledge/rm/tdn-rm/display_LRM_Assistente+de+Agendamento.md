---
content_hash: 0beb6dd1cd260cac05a68d5768d03506e075c3e77f4bd8261615302f923d9db0
fetched_at: '2026-06-29T00:11:27.455114+00:00'
page_id: '725734277'
product: rm
source: tdn-rm
title: Assistente de Agendamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Assistente+de+Agendamento
version: 11
---

## **CONTEÚDO**

1. **Visão geral**
2. **Formula Visual**
3. **DataSet**

PainelVisão Geral

O Assistente de agendamento esta localizado no menu Atendimento > Agenda de  Atendimentos > Assistente de Agendamento

 Clicar no Assistente de Agendamento e o sistema irá exibir a tela para o agendamento, para buscar horários para exames e consultas não é obrigatório preencher os dados do paciente, porém para avançar dessa tela é necessário o preenchimento.

Clicar nos ... do Nome para realizar a busca do paciente

Após a seleção do paciente é necessário preencher : Convênio , Plano, Sub plano (se houver), Código do beneficiário e validade da carteira do convênio e Atividade

**Botão Incluir Exames:** são exibidos todos os exames ativos, com agenda aberta, e suas respectivas unidades de realização, podemos selecionar um ou mais exames marcando o checkbox e logo após no botão OK

Os exames que possuem o tempo de execução superior ao da agenda, ao selecionar um horário, os horários seguintes serão bloqueados pra fechar o tempo de execução do exame

**Botão filtrar Unidade:**  no filtro da unidade são exibidos as unidades ativas e que possuem 1 ou mais horários para agendamento dos exames disponíveis, o campo de atividade, o campo de especialidade e os campos de data, a data inicial do período é preenchida pelo usuário, mas a final é preenchida automaticamente com 60 dias para frente, porém também é possível alterar a data final. O checkbox "Exames devem ser realizados no mesmo dia" vem marcado por default.

**Campo Especialidade Incluído para filtro:** o campo especialidade não tem obrigatoriedade e só serão buscadas as especialidades que estiverem visíveis e configuradas na agenda do medico (tela de opções da agenda):

Nesse exemplo selecionei consulta:

Após selecionar os parâmetros e clicar ok uma busca será feita:

**Botão incluir Consultas:**   
Poderão ser utilizados para realizar consultas:  
 - Unidade atendimento (opcional)  
 - Atividade (opcional)  
 - Profissional (opcional)  
 - Turno (opcional)  
 - Dia da Semana (opcional)  
 - Período de agendamento (opcional)  
 - Consultas devem ser realizadas no mesmo dia (opcional)

Podendo ser aplicado os filtros abaixo.

* Somente a especialidade
* Especialidade + unidade
* Especialidade + profissional
* Especialidade + atividade
* Especialidade + turno
* Especialidade + dia da semana
* Especialidade + período
* Especialidade + todos

Após preencher a unidade de atendimento são apresentados somente as especialidades que contém dentro da unidade.  
Após selecionar uma especialidade são retornados os profissionais que atendem a especialidade selecionada caso contrario não serão retornado os profissionais.  
Após selecionar uma única especialidade o campo "Consultas devem ser realizadas no mesmo dia?" será desabilitada, caso contrario o campo permanecerá habilitado.  
Após informar a data inicial o RM preenche a data final para 90 dias da data inicial.  
  
Ao confirmar, o RM buscará as datas e horas mais próximas ao dia atual como sugestão de datas e horas para realizar as consultas.

**Opção de Encaixe :** Com a agenda devidamente configurada será possível selecionar o horário de exame/consulta como encaixe.

Ao clicar no checkbox de encaixe, será possível informar o horário de encaixe na coluna de Horário e continuar com o processo.

**Botão incluir grupo de serviços:** é um facilitador para exames que são solicitados juntos, é exibido o cadastro de grupos ( cadastros > unidade de diagnostico> grupo de exames) para a seleção

**Botão excluir item:** ao selecionar exames ou consulta e clicar no excluir a linha do agendamento será excluído, é possível excluir um ou mais itens por aba  Exames ou Consultas

**Botão Voltar: Retorna para a pagina anterior**

Após a inclusão dos exames / consultas e seleção das datas e horário, clicar no Avançar.  Será exibida a tela de confirmação dos dados do agendamento , essa tela é somente para visualização e inclusão ou alteração do campo email e observações, caso o exame tenha preparo será exibido no campo Instruções do exame

Ao executar o processo finalizando os agendamentos é enviado o email com os dados do que for agendado e as instruções de preparo, as informações do campo observação não são enviados por email, fica salvo no campo observação do agendamento dentro da agenda

**Prioridades:** as prioridades dos exames são informadas no cadastro de exames e serviços no campo prioridades, no assistente será exibido na coluna Prioridade, na marcação dos exames será considerada a prioridade com numero menor , sendo a 1 a mais prioritário para o maior e posteriormente os exames sem prioridade definida.

**Alertas:**

Campos obrigatórios

Caso o usuário não tenha selecionada data/hora para todos os exames/consultas incluídos no grid o sistema exibe a mensagem abaixo e solicita que o usuario preencha os dados faltantes ou exclua os itens

Se o usuário não respeitar a ordem de prioridade dos exames o sistema exibe a mensagem abaixo e não permite avançar no processo

Se houver uma agenda inativa ou com a data máxima para agendamento ultrapassada dentro de um grupo de serviços o sistema irá exibir o alerta com o nome do exame/ consulta informando o usuário e irá incluir no grid somente os procedimentos que tenham agenda aberta

Exames obrigatórios de ser realizado no mesmo dia, esse cadastro é realizado em Cadastro> Unidade de Diagnóstico> Exames e Serviços > aba exames obrigatórios,  ao realizar o agendamento em datas diferentes o sistema exibe um alerta e pergunta se o cliente deseja continuar

Exames ou consultas agendados no mesmo horário

 Alerta de restrição por faixa etária

Formula Visual

## **FORMULA VISUAL**

Na aba **Registro e Controle III** foi adicionado um grupo de parâmetro para o Assistente de Agendamento.

Parâmetro **Formula Visual:** Permite ao usuário selecionar **uma** fórmula visual para ser aplicada no Assistente de Agendamento.

Parâmetro **Etapa de Aplicação:** Permite ao usuário indicar qual etapa do processo em que a formula visual será executada ou não.

**DataSet**

Dentro do DataSet dtsItens existem três tabelas: PACIENTE, EXAMES e CONSULTAS.

DataSet

## **1.**DataSet.Tables[“**PACIENTE**”]

Ao selecionar o paciente desejado no Assistente de agendamento, os dados da Row serão preenchidos.

Cada **Row** na tabela de paciente possui as seguintes colunas:

**CODCLIENTE**: Código do paciente (Int32)  
**NOMECLIENTE**: Nome do paciente (string)  
**DATANASC**: Data de nascimento do paciente (DateTime)  
**RESPONSAVEL**: Responsável do Paciente (string)  
**EMAIL**: e-mail do paciente (string)  
**TELEFONECOM**: Telefone Comercial (string)  
**TELEFONECEL**: Telefone Celular (string)  
**CEP**: CEP do endereço do paciente (string)  
**ENDERECO**: Rua do Endereço do paciente (string)  
**NUMERO**: Número do endereço do paciente (string)  
**COMPLEMENTE**: Complemento do endereço (string)  
**BAIRRO**: Bairro do endereço do paciente (string)  
**CIDADE**: Cidade do endereço do paciente (string)  
**NUMCARTAOSUS**: Número do cartão SUS (string)  
**CONVENIO**: Código do Convenio (Int32)  
**CODPLANO**: Código do plano (string)  
**CODSUBPLANO**: Código do sub plano (string)  
**CODIGOUSUARIO**: Código da carteirinha (string)  
**QUEMINDICOU**: Quem indicou (string)  
**CODTIPOINDICACAO**: Tipo de Indicação (Int32)  
**CODINDICACAO**: Código da indicação (Int32)  
**CODCOLIGADA**: Código da Coligada (Int32)  
**VALIDADECARTEIRA**: Validade da carteirinha (DateTime)

DataSet.Tables[“**PACIENTE**”] .Rows[0] [“NOMEDACOLUNA”]

## **2**. DataSet.Tables[“**EXAMES**”]

Ao inserir um exame na Aba de Exames, uma **Row** será criada. Os campos Unidade, Data, Hora e Código da Agenda

são preenchidos à medida que o usuário preenche a tabela no Assistente de Agendamento para o respectivo exame.

Cada **Row** na tabela de Exames possui as seguintes colunas:

**CODIGO**: Código do exame (Int32)  
**DESCRICAO**: Descrição do exame (string)  
**IDUNID**: Unidade de atendimento em que o exame será realizado (Int32)  
**DATA**: Data do agendamento a ser criado (DateTime)  
**HORA**: Horário do agendamento a ser criado (string)  
**PRIORIDADE**: Prioridade do exame definida em seu cadastro (string)  
**CODAGENDA**: Código da agenda em que o agendamento será criado. (Int32)

## **3** . DataSet.Tables[“**CONSULTAS**”]

Ao inserir um exame na Aba de Consultas, uma **Row** será criada. Os campos Unidade, Data, Hora, Agenda e Profissional

são preenchidos à medida que o usuário preenche a tabela no Assistente de Agendamento para a especialidade selecionada.

Cada **Row** na Consultas de paciente possui as seguintes colunas:

## 

**CODIGO**: Código da especialidade (string)  
**DESCRICAO**: Descrição da especialidade (string)  
**IDUNID**: Unidade de atendimento em que o exame será realizado (Int32)  
**DATA**: Data do agendamento a ser criado (DateTime)  
**HORA**: Horário do agendamento a ser criado (string)  
**AGENDA**: Código da agenda em que o agendamento será criado (Int32)  
**PROFISSIONAL**: Nome do profissional, dono da agenda, que realizará a consulta (string)

**OBSERVAÇÃO**: Como acessar o DataSet passado para a **Fórmula Visual**

1. Edite a formula visual
2. Adicione uma atividade **Executar Código Fonte**

    3. Clique com o botão direito na atividade e em **Selecionar código fonte**

    4. Edite o código fonte selecionado ou crie um novo

5. No editor é possível acessar o DataSet por dataServerParams.DataSet e utilizar como se estivesse trabalhando no Visual Studio,

conforme exemplo do print em que obtém o nome do paciente presente no dtsItens.
