---
content_hash: 54e8082d5ed14227c3fdb3b1990de65cff1443fdccab1120c8c4987479d2ada4
fetched_at: '2026-06-29T00:10:20.266073+00:00'
page_id: '490336702'
product: rm
source: tdn-rm
title: Agendamento com fracionamento jobs
type: documentation
url: https://tdn.totvs.com/display/LRM/Agendamento+com+fracionamento+jobs
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Agendamento com fracionamento de jobs |
| Ticket: | [Ticket #4257815](https://totvssuporte.zendesk.com/agent/tickets/4257815 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue | FOPCALCULO01-5496 |

## **02. SITUAÇÃO/REQUISITO**

Solicitação para a criação de agendamento com fracionamento de jobs, com objetivo de acelerar os processos.

## **03. SOLUÇÃO**

Foi implementada a possibilidade de agendamento com o fracionamento de jobs, onde permite o fracionamento em N processos, e consequentemente acelerar determinados processos agendados.

Para o agendamento com fracionamento de jobs, primeiro deverá ser preenchida a tela do agendamento e logo em seguida se deseja ou não fracionar o processo, em caso de sim, deverá preencher em quantas partes o processo será dividido, caso selecione o não, o processo executará de forma padrão ao sistema.

## **04. DEMAIS INFORMAÇÕES:**

O Agendamento com fracionamento de jobs somente será possível para os processos descritos abaixo:

**Folha Mensal**:

* Lançamento Multi-Coligadas
* Executa Recálculo
* Recálculo Multi-Coligadas

**Encargos:**

* Geração dos Encargos
* Geração do Histórico de Provisão

**Esocial:**

* Gerar XML
* Integrar com TAF
* Integridade RM x TAF

**Geração da Contabilização:**

* [Parametrização para o Fracionamento de Jobs para o processo de Geração da Contabilização](https://tdn.totvs.com/pages/viewpage.action?pageId=545232022)

**OBS:** Para a  execução do Agendamento com Fracionamento de jobs, o ambiente deverá estar parametrizado em 3 camadas, e a flag **Habilita Fracionamento de Jobs** no parametrizador deverá estar marcada.
