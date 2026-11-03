---
article_id: 360052879774
category: RH - Ponto Eletrônico
content_hash: ef720158ae63c88969e61704a9c590087f7dba6aaffb2a69a6739f456855ca61
fetched_at: '2026-06-28T22:44:58.216949+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como pagar o Intervalo e Adicional Noturno como
  Hora Trabalhada
type: support-article
updated_at: '2025-12-10T18:06:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052879774-RH-Linha-Protheus-PON-Como-pagar-o-Intervalo-e-Adicional-Noturno-como-Hora-Trabalhada
---

**Dúvida**Como pagar o Intervalo e Adicional Noturno como Hora Trabalhada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para **pagar** o **Intervalo** como **Hora Trabalhada** para o funcionário, primeiramente é necessário o **cadastro** dos **eventos** com **ID de Ponto 030A** (turnos diurnos) e **031A** (turnos noturnos).  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086952914/mceclip0.png)  
  
Após este cadastro, é necessário acessar a **Regra de Apontamento** que o funcionário está vinculado e marcar **quais intervalos serão pagos** como hora trabalhada no campo **Pg. Intervalo** e através do campo **Pg. Adn. Intv**, é possível informar se deverá ser pago **Adicional Noturno** para os intervalos ou não (em caso de Intervalo em horário Noturno).   
Além disso, o campo **Hr. Norm. Fol.** deve estar marcado como **Sim**, caso contrário os eventos **não serão gerados.**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086953034/mceclip1.png)

O campo **Pg. Intervalo** paga **intervalo** como **hora trabalhada** **independente do horário da pausa executado.**  
O campo **Pg. Adn. Intv.** paga o **adicional noturno sobre o intervalo** **independente se o funcionário descansou ou não**, por exemplo: mesmo que o funcionário **não tenha cumprido todo o expediente** do dia (ou seja, se teve uma **saída antecipada** antes mesmo do horário de **intervalo** cadastrado na Tabela de Horário Padrão), ou que **tenha cumprido todo o expediente** e tenha tido as marcações do intervalo (ou seja, um dia normal de trabalho, com todas as batidas no dia).  
  
**Importante:** as horas de **intervalo** pagas como horas trabalhadas **NÃO serão agrupadas** no evento de **Horas Normais/Horas Normais Noturnas** pois cada evento possui um **ID de Ponto** para tratamento.
