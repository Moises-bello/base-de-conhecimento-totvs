---
content_hash: e7cdc200f44ab6fad5129e9485532c10d6bea30bfe203d288ebf5d50ab39e304
fetched_at: '2026-06-29T00:10:43.741497+00:00'
page_id: '550329450'
product: rm
source: tdn-rm
title: Teleconsulta
type: documentation
url: https://tdn.totvs.com/display/LRM/Teleconsulta
version: 7
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configurações Globais para envio de E-mail**
3. **Configurações na unidade de atendimento**
4. **Configurações Teleconsulta por Convênio (Opcional caso utilizar Particular)**
5. **Inclusão do****Agendamento**

sumarioVisão Geral

## **Visão Geral**

Esse documento descreve as configuração e as alterações realizadas no processo de Agendamento de Atendimentos Externos para a realização de uma Teleconsulta. Todas as regras e configurações existentes na funcionalidade continuam as mesmas, adicionando regras referentes a Teleconsulta quando configurada.

Configurações Globais para envio de E-mail

## **Configurações Globais para envio de E-mail**

Para realização de uma telaconsulta é necessário realizar a configuração do envio de e-mails nos serviços globais, as imagens abaixo descreve o que deve ser configurado para envio de e-mails.

01. Acessar o menu dos **Serviços Globais**:

02. Selecionar a aba *Ambiente > Parâmetros > Parâmetros Globais*

03. Na tela de **Parâmetros Globais** Selecionar a Aba **Envio de E-mails** e incluir as informações do seu provedor de e-mails no Bloco **Parâmetros da Coligada Atual**. Será necessário marcar o a opção **E-mail da Coligada Atual** no bloco **Considerar como remetente padrão de envio de e-mails**.

Configurações na unidade de atendimento

## **Configurações na unidade de atendimento**

Para o processo da teleconsulta é necessário incluir na aba PEP o link para o **Termo de Consentimento,**sem essa informação o agendamento não irá enviar o e-mail para o paciente. Esse link deverá ser um link público para que o paciente leia o Termo de Consentimento, onde estarão todas as regras para teleconsulta.

**Atenção: O Termo de Consentimento é de autoria do Cliente onde deverá realizar sua elaboração conforme as leis vigentes para teleconsulta.**

Configurações Teleconsulta por Convênio (Opcional caso utilizar Particular)

## **Configurações Teleconsulta por Convênio (Opcional caso utilizar Particular)**

Para o processo da teleconsulta utilizando convênio, é necessário o preenchimento do procedimento que será utilizado pela TISS durante o agendamento.  
Para o preenchimento do mesmo, existem duas opções:

1. Preenchimento via agendamento.
2. Preenchimento via “Condição Contratual” do convênio.

**Obs.: Caso o parâmetro esteja preenchido, todo agendamento criado para este convênio virá com o “procedimento padrão” preenchido ao selecionar o tipo de teleconsulta.**

Inclusão do Agendamento

## **Inclusão do****Agendamento**

O processo de inclusão de agendamento de Teleconsulta segue as mesmas regras e comportamentos definidos no documento de [Agendamento](https://tdn.totvs.com/pages/viewpage.action?pageId=502446539). Ao salvar um agendamento um e-mail será enviado para o paciente onde estará detalhada todas as informações da consulta. Ao marcar o campo Teleconsulta um e-mail será solicitado no agendamento e sem essa informação não será possível salvar o agendamento. 

Ao salvar o agendamento as colunas Teleconsulta e E-mail Enviado estarão marcados demostrando que o agendamento é uma Teleconsulta e o e-mail foi enviado para o paciente. Se a coluna E-mail Enviado não for marcada significa que houve problemas ao tentar enviar o e-mail para o destinatário, para mais detalhes basta passar o mouse no check que uma dica será exibida com o motivo do não envio.

Na imagem acima a coluna Email Enviado está mostrando a dia "O parâmetro da urlportal não foi definida", essa mensagem é exibida por que a Teleconsulta se inicia na Gestão Hospitalar, mas é realizado no PEP RM para isso será necessário realizar algumas configurações no PEP.

]]>
