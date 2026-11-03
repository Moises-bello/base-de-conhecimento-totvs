---
article_id: 360037228414
category: Manutenção de Ativos (SIGAMNT)
content_hash: 60e3b8a9953f7e35ecc9e57e4c01124aa9bcbd4160c8100a05c384de5c4ffdde
fetched_at: '2026-06-28T22:42:32.983821+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Conceito da Solicitação de Serviço
type: support-article
updated_at: '2021-06-02T12:49:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037228414-Manufatura-Linha-Protheus-MNT-Conceito-da-Solicita%C3%A7%C3%A3o-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Qual o conceito e a utilização da **Solicitação de Serviço - MNTA280**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**É a rotina de cadastramento de **SS** - **Solicitação de Serviço** de manutenção. A **SS** é um estágio anterior a **Ordem de Serviço**. O usuário poderá cadastrar uma **SS** sem a definição de **Bem**, indicando somente o local da ocorrência para avaliação.  
Durante a inclusão ou alteração da **SS,** se já houver outra **solicitação** para o mesmo **bem/localização** e com o mesmo **tipo de serviço**, será emitida uma mensagem ao usuário alertando, onde poderá desconsiderar e continuar o processo ou poderá cancelar.  
O usuário também poderá determinar se será obrigatório responder a **pesquisa de satisfação** ou não, pela configuração do parâmetro **MV\_NGPSATI - Indica se utiliza Pesquisa de Satisfação das Solicitações de Serviço**.
