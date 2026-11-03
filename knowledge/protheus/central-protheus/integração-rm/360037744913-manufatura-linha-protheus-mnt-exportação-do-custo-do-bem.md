---
article_id: 360037744913
category: Integração RM
content_hash: 9167c4206f5656e1215373ed0007fdc1d946ece1aa00ac4efab2fed433f7929b
fetched_at: '2026-06-28T22:42:36.900357+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Exportação do Custo do Bem
type: support-article
updated_at: '2021-09-02T19:37:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037744913-Manufatura-Linha-Protheus-MNT-Exporta%C3%A7%C3%A3o-do-Custo-do-Bem
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:50 min**  
**Dúvida**Como funciona o processo para exportação do **Custo do Bem**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**Para utilizar o processo de exportação do **Custo do Bem:**

* **MNTA494 - Chamada e cálculo de custos diretos e indiretos.**
* **MNTA494A - Mensagem Única de Custos Indiretos Mensais do bem.**
* **MNTA494B - Mensagem Única de Custos Diretos Mensais do bem.**

Observe que no módulo de **Manutenção de Ativos - MNT**, são registrados os custos de manutenção **corretiva**, **preventiva**, **abastecimentos**, **despesas com multas**, **sinistros**, **parte diária**, entre outros. Todas estas informações de custos estão disponíveis no Sistema **MNT** e podem ser divididas conceitualmente entre custos **diretos** e **indiretos**.  
  
**Custos diretos** evolvem custos relacionados à parte diária e os **indiretos** são os custos dos demais processos controlados pelo Sistema. O processo integrado visa enviar para o Sistema **Corpore/TOP** da **RM** as informações referentes a esses custos.  
  
Os parâmetros de entrada para essa rotina são o **código do equipamento** e o **mês de referência**. Dessa forma, a exportação considera custos mensais referentes a um **equipamento**. Para cada **equipamento** também é transferido as informações relativas à **parte diária**, **horas produtivas** e **improdutivas** no mês, apuradas com base nas informações de apontamento da parte diária, seja manualmente ou por coletores de dados.
