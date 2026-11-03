---
article_id: 360025392891
category: Banco de Horas
content_hash: 1428a051f7f3e8c892e38940251df36a0bf2156cc0c9b4cfc87b3ceeb57acfbe
fetched_at: '2026-06-28T22:46:27.797175+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Ordenação da compensação e do lançamento do banco de horas
type: support-article
updated_at: '2024-06-12T18:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025392891-RH-RM-PTO-Ordena%C3%A7%C3%A3o-da-compensa%C3%A7%C3%A3o-e-do-lan%C3%A7amento-do-banco-de-horas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503457494679) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**  
Como funciona a ordenação da compensação e do lançamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – Todas as versões.  
  
**Solução**A ordenação da compensação e do lançamento pode ser priorizada de duas formas: **Ordenação por tipo** e **Ordenação por data**.

Caso a prioridade seja **por data**, o sistema ordenará as ocorrências por data mais antiga ou mais atual e posteriormente ordenará as ocorrências por tipo para realizar a compensação. Segue exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023914912)

A ordenação por tipo é referente às ocorrências de crédito, ou seja, as extras, onde poderão ser organizadas pelo tipo (Normal, Compensado, Descanso e Feriado) ou mesmo organizadas pelo código de cálculo ou faixas por tipo(1ª Faixa Extra Normal, 2ª Faixa Extra Normal.....1ª Faixa Extra Descanso, 2ª Faixa Extra Descanso). Segue print de exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023915012)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023915032)

Considerando então as prioridades por data ou por tipo a ordenação fica da seguinte forma:

* Compensação por data
  + Data mais antiga
  + Data mais atual
* Compensação por tipo
  + Tipo de ocorrência (extra normal, descanso, compensado e feriado)
  + Código de cálculo (tipo de faixa)

Além disso, os códigos de cálculo a considerar na compensação poderão ser selecionados conforme necessidade na caixa de seleção **Código de cálculo a considerar**.  
  
**Saiba Mais:**[RH - RM - PTO - Zerar o saldo do banco de horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012284812)  
[RH - RM - PTO - Zerar o saldo do banco de horas por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018164972)  
[RH - RM - PTO - Como lançar saldo parcial do banco de horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20892682356119)
