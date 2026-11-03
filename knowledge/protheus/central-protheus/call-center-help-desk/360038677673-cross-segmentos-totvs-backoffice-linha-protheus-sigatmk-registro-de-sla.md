---
article_id: 360038677673
category: Call Center - Help Desk
content_hash: d1742f20a7f94103546caf352a3b040da15e01f52b0deb6e6347ed84b49cd4bc
fetched_at: '2026-06-28T22:41:27.652351+00:00'
product: protheus
section_id: 1500001537181
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-- Registro de SLA
type: support-article
updated_at: '2023-02-02T10:55:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038677673-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Registro-de-SLA
---

**Dúvida**

Cálculo do registro de SLA.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- - a partir da release 11.80.  
  
**Solução**

O registro de SLA é calculado de acordo com a data, baseada em turno. Veja a seguir, as características do registro de SLA:

• Pausa num registro de SLA  
Permite efetuar uma parada na contagem de tempo. Dessa forma, o operador é isento da responsabilidade pela sua contagem. Para configurar essa funcionalidade, é necessário incluir uma nova ocorrência com a ação SLA de pausa. Para reiniciar a ocorrência é necessário incluir um novo item no atendimento com uma atualização do registro SLA.

• Tamanho do campo de horas do SLA,  
Permite configurar uma quantidade maior de horas.

• Cálculo de expiração de contrato de SLA baseado em calendário e turno.  
Para calcular a data de expiração do SLA, respeitando um turno de trabalho, é necessário configurar a tabela de horário padrão, turnos de trabalho e configurar o grupo de atendimento, ou contrato SLA com o turno desejado. Quando houver um turno cadastrado tanto no grupo de atendimento quanto no contrato de SLA, o turno do grupo de atendimento tem precedência sobre o contrato SLA.

• Inclusão de exceções por período para os turnos utilizados no cálculo das datas limites de SLA  
Utilize Exceções por período. para incluir dias, ou ainda, período de dias específicos para um turno que não deva ser considerado durante o cálculo da data limite de SLA.
