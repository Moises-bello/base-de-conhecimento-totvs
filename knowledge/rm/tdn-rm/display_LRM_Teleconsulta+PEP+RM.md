---
content_hash: e3c7b9d3b8f787bb32c8e2fb70af9071af37c3cfc42c3639c61d788c56bb6a6b
fetched_at: '2026-06-29T00:10:43.948869+00:00'
page_id: '551433702'
product: rm
source: tdn-rm
title: Teleconsulta PEP RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Teleconsulta+PEP+RM
version: 25
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela da agenda do dia**
   1. **Outras Ações / Ações relacionadas**
4. **Passo a passo da funcionalidade de teleconsulta**

TeleconsultaVisão Geral

## **01. VISÃO GERAL**

Funcionalidade que permite a realização da consulta entre médico e paciente, através de videoconferência, utilizando o próprio prontuário eletrônico.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Acessar o PEP RM > Minha Agenda > Selecionar a Unidade > Buscar paciente por nome ou data da consulta marcada.

Tela da Agenda do Dia

## **03. TELA DA AGENDA DO DIA**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Buscar paciente | Clicar nos três pontos e selecionar: **"Iniciar atendimento"; "Paciente ausente"; "Finalizar atendimento"; "Retornar para fila de espera" e "Retornar ao prontuário".** |

Passo a passo da funcionalidade de Teleconsulta

## **04. PASSO A PASSO DA FUNCIONALIDADE DE TELECONSULTA**

* Para utilizar a tele consulta é necessário informar duas parametrizações na tela de configurações gerais aba **PEP RM**:

|  |  |  |
| --- | --- | --- |
| **RM Saúde** | **Necessário estar configurado o RM saúde conforme documentação** | **<https://tdn.totvs.com.br/display/public/LRM/Teleconsulta>** |
| Url Telemedicina | Informar a url externa do sistema disponibilizada pelo cliente | <http://www.meuprprm.com/TOTVS.RM.PEP> |
| **Token da DailyCo** | **Informar o token gerado no site da DailyCo** | É necessário criar uma conta, acessar <https://dashboard.daily.co/developers>**e****ir na área de developers e gerar o token.** *Onde existem duas opções de conta: a versão gratuita que dá X quantidades de participantes-minutos/mês gratuitos e tem as versões pagas, com mensalidades que variam de preço de acordo com os recursos que o cliente deseja.* |
| **Utilizar o [Daily.co](http://Daily.co) dentro do PEP (Embedded).** | **Para exibição do videochat da DailyCo(embedded) dentro do PEP, é obrigatório que o servidor tenha conexão HTTPS.** |  |
| **Parametrização para usar o [Daily.co](http://Daily.co) em nova aba ou dentro do PEP(Embedded)** | **Verifique ao acessar o PEP > Minhas Configurações > Padronização Teleconsulta.** | **A opção "Integrada ao prontuário" faz com que o Daily seja aberto dentro PEP(Embedded).**  **A opção "Em uma nova guia" faz com que uma nova aba seja criada com a chamada. Essa opção é indicada caso o sistema não esteja como HTTPS.** |

* Para mais informações referentes aos limites das chamadas entre em contato com a DailyCo ou verifique a documentação no site.

* Tela principal da "Agenda do dia"

* Após selecionar a unidade de atendimento, será exibido uma lista de pacientes agendados.
* Os pacientes agendados para teleconsulta ficarão com um ícone de câmera na lista.
* OBS: A lista de pacientes do dia anterior e posterior podem ser visualizadas e somente é possível modificar o status do dia anterior e do dia atual. Na lista do dia posterior é permitido apenas visualizar os pacientes agendados.

* Ao selecionar **"Iniciar atendimento",** o usuário será redirecionado para a tela principal do prontuário do paciente.

* Nessa opção o médico consegue voltar para a lista e alterar os status dos pacientes que estão na agenda.

O paciente não terá acesso a tela de videochamada até o profissional iniciar o atendimento.

* Na tela do prontuário do paciente, o médico consegue navegar, visualizar e adicionar informações e também visualizar a tela da vídeochamada.

* Ao clicar em **"Finalizar atendimento"** o sistema irá exibir uma mensagem solicitando confirmação para finalizar o atendimento.

* Ao clicar em "Confirmar" para finalizar o atendimento, o status do paciente ficará como **"Finalizado"** na agenda.
