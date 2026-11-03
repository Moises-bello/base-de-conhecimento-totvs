---
content_hash: d657bec055e2783f5e6b0a6d365e008e1747f4c003305961223fb9c683ab64da
fetched_at: '2026-06-29T00:11:43.044617+00:00'
page_id: '801329487'
product: rm
source: tdn-rm
title: DT - Fracionamento de Jobs - Cancelamento do movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Fracionamento+de+Jobs+-+Cancelamento+do+movimento
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cancelamento de Movimento |
| País: | Brasil |
| Ticket: | [#17623116](https://totvssuporte.zendesk.com/agent/tickets/17623116 "View ticket on the Zendesk portal") |
| Story: | [DRHCALCRM-5019](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5019) |

## **02. SITUAÇÃO/REQUISITO**

Atualmente o sistema não permite o fracionamento de JOBs no cancelamento do movimento da folha.

## **03. SOLUÇÃO**

O fracionamento do módulo de cancelamento do movimento da folha de pagamento foi implementado e para habilitar é necessário:

1. O host e exe esta configurado para n Camadas;
2. Cadastrar a classe de processo em Ambiente \ Processos \ Segurança de Jobs Fracionáveis, para o perfil que terá acesso. A classe do Job é a FopCancelarMovimentoProcess;
3. Em Ambiente \ Processos \ Cockpit deve ativar o processo na opção "Informações de Processamento e Memória" habilitar a "Executar Processos"

**Observação:**Quando a opção "Retificação folha/rescisão" for habilitada o cancelamento irá ocorrer em apenas um Job, 

## **04.** **ASSUNTOS RELACIONADOS**

* [Cancelamento de movimento - FOP](https://tdn.totvs.com.br/display/LRM/Cancelamento+de+movimento+-+FOP)
