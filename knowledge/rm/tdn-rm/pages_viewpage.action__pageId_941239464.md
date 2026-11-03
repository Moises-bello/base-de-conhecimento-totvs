---
content_hash: 8725b6810de26f2c8e119c6d8862adee95dec0d770fe846ca648127cf3dab7de
fetched_at: '2026-06-29T00:12:09.164394+00:00'
page_id: '941239464'
product: rm
source: tdn-rm
title: Abertura Automática do Totem de Retirada de Senhas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=941239464
version: 16
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Importante**
3. **Funcionalidades**
4. **Outras funcionalidades**
5. **Pré-requisitos**
6. **Como funciona**
7. **Parametrização**

sumarioVisão Geral

## **01. VISÃO GERAL**

Este processo tem como objetivo automatizar a abertura do **Totem de Retirada de Senhas** no TOTVS RM Saúde, agilizando a abertura do RM no totem. Ele realiza o login automático no sistema RM e, conforme parametrização, já posiciona o totem na tela de solicitação de senha, pronto para o uso pelo paciente.

Importante

## **02. IMPORTANTE**

É necessário seguir a configuração de Login automático descrita no documento:

*[https://centraldeatendimento.totvs.com/hc/pt-br/articles/7724727057943-Framework-Linha-RM-Frame-Login-autom%C3%A1tico-no-RM-por-action](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7724727057943-Framework-Linha-RM-Frame-Login-autom%C3%A1tico-no-RM-por-action "Seguir link")***Action totem:**  
SauTotemProntoAtendimentoAction

Funcionalidades

## **03. FUNCIONALIDADES**

* Login automático no RM Saúde
* Abertura automática do Totem de Senhas
* Exibição direta na tela de retirada de senha
* Configuração centralizada via parâmetros do sistema
Outras funcionalidades

**04. OUTRAS FUNCIONALIDADES**

Com o uso do agendador de tarefas do sistema operacional, é possível configurar a abertura automática do Totem para que, ao iniciar o computador, o sistema RM seja executado automaticamente, garantindo maior agilidade e disponibilidade do serviço.

Pré-requisitos

## **05. PRÉ-REQUISITOS**

Antes de ativar o processo automático, verifique os seguintes pontos:

1. Configuração do RM Saúde concluída
2. Usuário com permissões adequadas para acesso ao Totem
3. Totem configurado e instalado no local desejado
4. Parâmetros de inicialização definidos corretamente
Como funciona

**06. COMO FUNCIONA**

1. Ao iniciar o sistema, o processo executa automaticamente o login no TOTVS RM.
2. Após a autenticação, o sistema verifica os parâmetros definidos.
3. Caso esteja configurado para abertura automática, o Totem é iniciado já na tela de solicitação de senha para o paciente.
4. O paciente visualiza a interface intuitiva e pode retirar sua senha imediatamente.
Parametrização

## **07. PARAMETRIZAÇÃO**

***Documentação de configuração de parâmetros por estação de trabalho [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=829293510#Painel-1359221099)***

Na tela de parametros por estação de trabalho navegue até a aba de Abertura Automática de TOTEM

São apresentados três parâmetros essenciais para a configuração dessa funcionalidade.

1. **Unidade de Atendimento:** Caso o totem esteja configurado por unidade de atendimento, informar qual a unidade de atendimento.
2. **Totem de Atendimento:** Caso o totem esteja configurado para mais de uma unidade de atendimento, informar qual o totem.
3. **Abre totem automaticamente:** Controla se o processo será executado ou não.
