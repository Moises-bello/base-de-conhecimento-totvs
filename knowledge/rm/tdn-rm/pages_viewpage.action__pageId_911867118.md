---
content_hash: a39299418feed7847353f9b2c104dadfdfc9d68f8833fac246fc2e72b24da176
fetched_at: '2026-06-29T00:12:03.608754+00:00'
page_id: '911867118'
product: rm
source: tdn-rm
title: Migrar jobs finalizados para tabela de histórico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911867118
version: 3
---

## **ÍNDICE**

---

ÍNDICE

## **01. VISÃO GERAL**

---

Na tela de Gerenciamento de Jobs, existe o processo **Migrar jobs finalizados para tabela de histórico**:

## **02. O PROCESSO**

---

Este processo permite migrar os registros de processos da tabela *GJOBXEXECUCAO* para a tabela *GJOBXEXECUCAOHST*.

Ele é de extrema importância para o ambiente, pois um acúmulo de registros na tabela *GJOBXEXECUCAO* pode deixar a execução de processos cada vez mais lenta.

### CRITÉRIOS DE MIGRAÇÃO

Os registros migrados pelo processo obedecerão os seguintes critérios:

* + - o processo deve ter sido finalizado;
    - a data de finalização do processo deve ser de 2 ou mais dias.
    - Status = 7 com DATAFIMEXEC = NULL.
    - Status > 1 and Status != 10 and  DATAFIMEXEC maior ou igual que 2 dias.

### **AGENDANDO**

Caso possua o ambiente com Job Server 3 Camadas ativo, ao executar o processo, é possível selecionar o seu agendamento:

Basta selecionar a data da primeira execução e, abaixo, a recorrência.

## **03. RECOMENDAÇÕES**

---

A partir do momento em que existirem 200000 registros ou mais na sua tabela *GJOBXEXECUCAO*, o seguinte aviso aparecerá caso entre no módulo de Serviços Globais:

Logo, é **extremamente** recomendado que a execução deste processo seja feita caso seja avisado.

Em casos de ambientes com execução de muitos jobs, é recomendado o agendamento recorrente da execução do mesmo.
