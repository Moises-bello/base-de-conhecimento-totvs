---
article_id: 4412358944663
category: RH - Folha de Pagamento
content_hash: f4451b6733eed28517d171ec2b74b93c1a6763d966439f41b1270c0cf4ef3469
fetched_at: '2026-06-28T22:44:14.899065+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - É possível agendar a rotina de Cálculo por Roteiros
type: support-article
updated_at: '2025-08-11T21:03:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412358944663-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-agendar-a-rotina-de-C%C3%A1lculo-por-Roteiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337781026199) Tempo aproximado para leitura: **00:04:00 min****Dúvida**É possível agendar a rotina de Cálculo por Roteiros (GPEM020)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Com o uso do **RDMake GPEWORK** devidamente compilado no ambiente, **é possível** criar um **agendamento** para a efetuar a rotina de **Cálculo por Roteiros (GPEM020)**.  
  
Para isto é necessário seguir os passos como descrito abaixo, como exemplo:  
**1.** Baixar o Pacote de **Expedição Contínua do RH** e extrair o fonte **GPEWORK.PRW** e o include **GPEWORK.CH**;  
**2.** **Compilar** o fonte **GPERWORK.PRW** em seu ambiente;  
**3.** **Acessar** o Módulo de **Configurador**;  
**4.** **Acessar** a rotina em **Ambiente/Schedule/Schedule**;  
**5.** **Acessar** a opção em **Schedule/Agendamentos/Cadastro**;  
**6.** **Clicar** em **Incluir** um novo **Agendamento**;  
**7.** **Preencher** os dados do agendamento conforme necessidade e no campo Rotina, a **função U\_GPESCHEDULER** com **três parâmetros**, respeitando a seguinte regra:  
   **7.1.** **1º Parâmetro** (caractere): Código do Processo à ser calculado;  
   **7.2.** **2º Parâmetro** (caractere): Roteiro de Cálculo à ser calculado;  
   **7.3.** **3º Parâmetro** (lógico): Se considera os funcionários de todas as filiais (.T.) ou somente os da filial configurada (.F.)  
  
**8.** Um exemplo de preenchimento:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412358853015)  
  
**9.** **Definir** a **Recorrência** que este agendamento será executado, conforme necessidade;  
**10.** **Salvar** as alterações.  
  
**Informações complementares**  
Documentação Técnica da implementação: <https://tdn.totvs.com/pages/releaseview.action?pageId=647454949> 

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
