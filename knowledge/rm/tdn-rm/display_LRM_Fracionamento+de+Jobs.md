---
content_hash: 316426ddc0505a18e42c3643d334e1d8e0ecfaccfda720a9d8a5e31f3eb133e8
fetched_at: '2026-06-29T00:10:32.588008+00:00'
page_id: '527380748'
product: rm
source: tdn-rm
title: Fracionamento de Jobs
type: documentation
url: https://tdn.totvs.com/display/LRM/Fracionamento+de+Jobs
version: 8
---

O fracionamento de Jobs permite a execução de um processo através de múltiplos Jobs. Este tem como objetivo reduzir o tempo total de execução, assim como aproveitar melhor a capacidade de processamento do servidores.

**Requisitos**

* Deve estar habilitada a utilização do sistema em 3 camadas.

****Segurança****

* Para a utilização do recurso, o perfil do usuário deve estar associado ao processo. Esta configuração pode ser feita através do Menu → Ambiente → Segurança de Jobs Fracionáveis. Segue exemplo:

**Obs**: Serão listados apenas os processos que permitem o fracionamento.

**Utilização**

Ao executar um processo que permite o fracionamento de Job, será exibida a tela responsável pelo agendamento do processo. Nela será possível definir a quantidade de partes em que o processo será dividido. O sistema permite informar a quantidade de partes baseado no mínimo e máximo de frações configuradas no módulo de segurança do fracionamento.

Para os processos que não possuem uma tela de parâmetros, o sistema exibirá a tela abaixo para coletar essas informações:

Ao finalizar a execução do processo, o sistema exibe o log de cada uma das partes, ou seja, as mensagens são agrupadas pelo identificador do Job. Segue exemplo:

**Processos disponíveis**

O fracionamento de Jobs está disponível para os seguintes processos:

* Cancelamento de movimento
* Reabrir Financeiro
