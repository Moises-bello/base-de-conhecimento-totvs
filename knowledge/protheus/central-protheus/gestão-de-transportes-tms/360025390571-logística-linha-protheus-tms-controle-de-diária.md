---
article_id: 360025390571
category: Gestão de Transportes (TMS)
content_hash: 3114b4bff6efff6143bfff41aa8dddd0778b4d5c0d74a53ada60e09a2bae1984
fetched_at: '2026-06-28T22:45:27.606694+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Controle de Diária
type: support-article
updated_at: '2022-04-19T16:48:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025390571-Log%C3%ADstica-Linha-Protheus-TMS-Controle-de-Di%C3%A1ria
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:50 min****Dúvida**Como parametrizar o **controle de diária**?   
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Segue abaixo informações referente a parametrização e modelo de uso do **Cadastro de Diária**:  
  
**Inclusão do Cadastro de Diária:** Esta rotina permite cadastrar os valores das diárias para serem usadas como base na geração de diárias automáticas.

1. Em **Gestão de Transportes** - **SIGATMS**, acesse **Atualizações/Controle Diária/Cadastro Diária** - **TMSAB10**;
2. Inclua uma nova configuração de diária;
3. Clique em **Concluir**.

**Inclusão da Parametrização de Diária:**Esta rotina permite criar regras de diárias com o objetivo de estabelecer uma configuração para a inclusão de uma diária automática ou manual.

1. Em **Gestão de Transportes**, acesse **Atualizações/Controle Diária/Param. Diária** - **TMSAB20**;
2. Inclua uma nova parametrização de diária;
3. Clique em **Concluir**.

**Processo Automático:**

1. Em **Gestão de Transportes**, acesse **Atualizações/Viagens/Rodoviário Entrega/Viagem** - **TMSA141**;
2. Inclua uma viagem;
3. No complemento da viagem, vincule um motorista do tipo **Próprio**;
4. Após, acesse a opção **Outras Ações**, **Motorista** **da** **Viagem** e preencha o conteúdo do campo **Paga Diária - DUP\_PAGDIA** com a opção **Sim**;
5. Acesse **Atualizações/Viagens/Rodoviário Entrega/Fechamento -** **TMSA310**;
6. Efetue o fechamento da viagem. No momento do fechamento da viagem, caso o motorista da viagem esteja configurado para pagamento de diária, é gerada automaticamente a diária com *status* **Aprovada**, em seguida é emitido o título no **financeiro**. É apresentada a  
   tela para impressão do recibo e inclusão da despesa no **Movimento de Custo do Transporte**.

Observe que o Sistema automaticamente irá gerar:

* **Controle de Diárias** com *status* **Aprovado**;
* Título no **Financeiro**;
* Despesa em **Movimento de Custo de Transporte**, observe que o *status* é apresentado como **Baixado**;
* **Recibo**: o Sistema disponibiliza a tela para impressão do **Recibo**.

**Processo Manual:**

1. Em **Gestão de Transportes**, acesse **Atualizações/Controle Diária/Controle Diária** - **TMSAB30**;
2. Inclua uma diária;
3. Clique em **Aprovar**.

Observe que o Sistema automaticamente irá gerar:

* **Aprovação da Diária**;
* Título no **Financeiro;**
* Despesa em **Movimento de Custo de Transporte**, observe que o *status* é apresentado como **Baixado**;
* **Recibo**: o Sistema disponibiliza a tela para impressão do **Recibo**.

**Impressão de Relatório:**

1. Em **Gestão de Transportes**, acesse **Atualizações/Controle Diária/Controle Diária** - **TMSAB30**;
2. Clique em **Ações Relacionadas** e selecione a opção **Relatório**;
3. Informe a parametrização desejada;
4. Clique em **Imprimir**.
