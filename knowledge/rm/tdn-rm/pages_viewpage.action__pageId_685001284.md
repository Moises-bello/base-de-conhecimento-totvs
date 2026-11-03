---
content_hash: 61414760aa3c32eaaad1fbaf790027f4104b9beb996dd7c846514906929b1202
fetched_at: '2026-06-29T00:11:20.486714+00:00'
page_id: '685001284'
product: rm
source: tdn-rm
title: TOTEM de Registro de Atendimento automático para ELETIVOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=685001284
version: 16
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Unidade de Atendimento - Habilitando o PAINEL ELETIVOS**
3. **Valores Padrão para Atendimento TISS**
4. **Cadastro de Especialidades**
5. **Cadastro de Agendas - Configuração**
6. **Agenda de Atendimentos**
7. **Parâmetros do Delphi**
8. **Totem Eletivos**
   1. **Recepção**
   2. **Auto Atendimento**
9. **Painel de Atendimentos Eletivos**

conteúdoVisão Geral

## **01. VISÃO GERAL**

Está função permite o registro de atendimento de forma automática. Os pacientes utilizam o TOTEM e, após identificação com o número do convênio, podem escolher entre seus agendamentos do dia e registrar automaticamente o atendimento, sem necessitar que passem pela recepção.  
Totem não conta mais com o tempo de logout do RM enquanto estiver aberto.

Unidade de Atendimento - Habilitando o PAINEL ELETIVOS

## **02. UNIDADE DE ATENDIMENTO - HABILITANDO O PAINEL ELETIVOS**

Somente as Unidades de Atendimento que possuem habilitado o checkbox / parâmetro correspondente ao TOTEM de Auto Atendimento de Eletivos (**Registra atendimento automático via TOTEM de Painel Eletivos**) no cadastro da **Unidade De Atendimento** poderão utilizar o registro de atendimento automático.

**Observação:**Apenas os agendamentos do paciente das Unidades de Atendimento com o parâmetro habilitado serão carregados no painel.**NÃO é possível**utilizar o Totem de pronto atendimento e o Totem de Painel Eletivos **AO MESMO TEMPO**.

**Painéis > Painel Registro de Atendimento Automático > Registra Atendimento automático via TOTEM de Painel Eletivos**

Valores Padrão para Atendimento TISS

## **03. VALORES PADRÃO PARA ATENDIMENTO**

Para fazer uso do registro de atendimento automático é necessário cadastrar os valores padrão para a Unidade de Atendimento que utilizará o TOTEM.

        Convênios que utilizam padrão **TISS**

Para isso, acesse **Cadastros > Uso Geral > Outros Cadastros > Valores Padrão Para Atendimento TISS**

Adicione um novo cadastro e preencha **TODOS**os dados antes de salvar.

Convênios que **não** utilizam padrão **TISS  
Para isso, acesse Cadastros > Uso Geral > Outros Cadastros > Valores Padrão Para Atendimento não TISS**

Desta forma, durante o registro de atendimento **automático**, os valores informados serão utilizados como default no preenchimento do atendimento.

Cadastro de Especialidades

## **04. CADASTRO DE ESPECIALIDADES**

É necessário cadastrar as especialidades que serão atendidas na unidade de atendimento. Para fazer isso acesse o Painel de Atendimentos Eletivos:

**Atendimento > Pronto Atendimento / Ambulatório > Pronto Atendimento > Painel de atendimentos** **Eletivos**

Selecione a **Unidade de Atendimento** desejada, vá até a aba **Plantão** e clique para incluir.

Preencha os dados. **Desmarque**a opção **Realiza Triagem**, pois não há triagem para atendimentos eletivos. **Marque** os parâmetros **Realiza Atendimento Médico** e **Ativo**. E clique em salvar.  
Cadastre todas as Especialidades desejadas para a Unidade de Atendimento escolhida.

Cadastro de Agendas - Configuração

## **05. CADASTRO DE AGENDAS - CONFIGURAÇÃO**

Acesse **Cadastros > Agendamento > Agenda**

Inclua uma nova Agenda. Selecione o Tipo de Agenda, podendo ser **Médico, Plantonista, Enfermagem, Téc. Enfermagem, Sala ou Outros**.

O agendamentos feitos em agendas do tipo **Agente de Coleta** **NÃO** aparecerão no totem de autoatendimento eletivos.

**Observação:** Caso escolha o tipo **Sala** é necessário, durante o AGENDAMENTO na **AGENDA DE ATENDIMENTOS, é OBRIGATÓRIO**informar o PRESTADOR para identificar qual o atendente.

Agenda de Atendimentos

## **06. AGENDA DE ATENDIMENTOS**

O TOTEM de atendimentos eletivos utiliza os agendamentos **DO DIA**para apresentar as opções ao usuário. Caso não haja agendamentos, o número da carteirinha não será encontrado e não haverá possibilidade de usar o TOTEM, sendo necessário passar na recepção.

Acesse **Atendimento > Agenda de Atendimentos**. Selecione a Unidade de atendimento e o médico desejados.

Selecione um horário na agenda e o Paciente para quem irá agendar o atendimento.

**Observação:** É necessário informar a **Carteira do Convênio**para que o paciente seja localizado no **TOTEM de registro automático de atendimento Eletivos**.

Parâmetros

## **07. PARAMETROS**

Alguns parâmetros referentes à obrigatoriedade de informações no registro de atendimento, por exemplo: Código Dependente e Motivo Pendência, podem interferir com o funcionamento do TOTEM DE REGISTRO AUTOMÁTICO, pois não possuem valores padrões, o que impedirá o registro de atendimento.  

**UTZTOTENMULTUNID**: Utiliza Totem para múltiplas unidades.  
Deve-se ir em Ambiente > Parâmetros > Gestão Hospitalar > Classificação de Risco

Caso esteja **DESMARCARDO**, o usuário escolherá para qual Unidade de Atendimento o Totem atenderá, mostrando as especialidades cadastradas para a mesma.

Para a Unidade de Atendimento aparecer na lista de opções é necessário que os parâmetros **Realiza classificação de risco** e **Utiliza senha de atendimento** estejam marcados (mesmo que não haja classificação de risco para Atendimentos Eletivos), Acesse **Cadastros > Uso Geral > Unidade de Atendimento > Painéis**.

Caso esteja **MARCADO**, o usuário escolherá o perfil de totem desejado, que pode conter múltiplas unidades de atendimento.

Para criar um perfil de totem acesse: **Cadastros > Registro e Controle > Outros Cadastros > Toten**

Clique para incluir novo perfil, adicione uma descrição e na Aba **Unidades de Atendimento associadas ao Toten**adicione as unidades de atendimento desejadas.

Totem Eletivos

## **08.****TOTEM ELETIVOS**

Caso o **parâmetro UTZTOTENMULTUNID esteja marcado**, o usuário escolherá a Unidade de Atendimento desejada. 

Após escolher a Unidade de Atendimento ou caso o **parâmetro UTZTOTENMULTUNID esteja desmarcado**.

## **08.A****RECEPÇÃO**

A opção **Recepção** irá enviar o usuário para a recepção, gerando uma senha para a Especialidade desejada.

## **08.B****AUTO ATENDIMENTO**

A opção **Auto Atendimento** irá mostrar os agendamentos **DO DIA** para o cliente registrar atendimento automaticamente.

Será exibido uma seleção para buscar os agendamentos previamente realizados usando o a carteirinha do convênio ou CPF

Caso a escolha seja o "CPF" será exibido a tela abaixo

Caso a escolha seja "Número carteirinha convênio" será exibido a tela abaixo.

É necessário que o usuário passe o cartão do convênio no leitor **OU**digite o numero utilizando o teclado da tela. Os dados dos agendamentos serão localizados utilizando o número da carteirinha.

Após digitar ou ler o número da carteira, será necessário verificar os dados do paciente.

Confirmar a Data de nascimento:

Confirmar o Nome da mãe:

Após **CONFIRMAR** serão apresentados os **AGENDAMENTOS DO DIA** para o número de carteira de convênio informado.

Após selecionar o agendamento desejado, será necessário pegar uma senha antes de registrar o atendimento.

Após retirar a senha o atendimento será registrado. E o fluxo do totem reiniciado para o próximo usuário.

A senha retirada irá para o **PAINEL DE ATENDIMENTOS ELETIVOS.**

Painel de Atendimentos Eletivos

## **09.****PAINEL DE ATENDIMENTOS ELETIVOS**

Acesse: **Atendimento > Pronto Atendimento / Ambulatório > Pronto Atendimento > Painel de atendimentos** **Eletivos**

A senha irá aparecer para na Unidade de Atendimento na aba **Atendimento Médico**.

**Observação:**Caso o parâmetro **Médico default para fila única,**esteja ativado e com um médico selecionado, o nome do Médico(a) para todos os atendimentos presentes no painel será o definido no parâmetro.

Deve-se ir em Ambiente >Parâmetros > Gestão Hospitalar > Classificação de Risco.

## **Assista as pequenas guias!**
