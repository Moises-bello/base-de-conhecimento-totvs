---
article_id: 1500001976082
category: Manutenção de Ativos (SIGAMNT)
content_hash: a606a48bbab5150a8d259409e9983ea04d5905edebfcc090601484dbab02a829
fetched_at: '2026-06-28T22:42:32.937356+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Comportamento da rotina Acum. Acompanhamento/Histórico
  - MNTA820
type: support-article
updated_at: '2021-06-02T12:39:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001976082-Manufatura-Linha-Protheus-MNT-Comportamento-da-rotina-Acum-Acompanhamento-Hist%C3%B3rico-MNTA820
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:03:45 min**  
**Dúvida**Como é o comportamento da rotina de **Acum. Acompanhamento/Histórico - MNTA820**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Utiliza-se essa funcionalidade somente para bens que requerem acompanhamento por contador ou produção, para verificação da necessidade de execução da manutenção.  
Uma vez gerado um plano, este não poderá mais ser excluído da base de dados, este terá o *status* **P - Pendente**, podendo passar para **L - Liberado** quando finalizado ou **C - Cancelado** quando excluído.  
  
A rotina **MNTA820** exclui as **Ordens Plano Acompanhamento - TQA** e grava na tabela de **Histórico de Acompanhamento - STW** quando **Plano de Acompanhamento - STO** terminado até a data informada como parâmetro na pergunta **Ate Data Acompan. ?** Informe nesse campo, um determinado período de data fim de Acompanhamento.  
  
Exemplo de utilização:

1. Em **Atualizações / Controle de Oficina / Bens / Bens - MNTA080**, inclua um **Bem** informando contador 1 e 2, preenchendo os campos **Período - T9\_PERACOM** e **Un. Acomp. - T9\_UNIACOM**;
2. Em **Atualizações / Controle de Oficina / Plano Acompanhamento / Plano - MNTA310**, incluir um **Plano - STO** informando um período que irá gerar **OS** **- Ordem de serviço** de acompanhamento na tabela **TQA**;
3. Em **Atualizações / Controle de Oficina / Plano Acompanhamento / Confirmação - MNTA320**, realizar a confirmação total/individual do plano incluso anteriormente;
4. Em **Atualizações / Controle de Oficina / Plano Acompanhamento / Retorno - MNTA390**, realizar o retorno de algumas **OS** confirmadas anteriormente, reportando contador 1 e 2; Nesse processo irá gerar **Ordens Serviço Acompanhamento - STP** e **OS Acompanhamento Contador 2 - TPP**.
5. Retornar à rotina **Plano - MNTA310**, selecionar o plano e finalizar o mesmo em **Outras Ações / Finalizar**.
6. Em **Miscelânea / Histórico / Acum. Acompanhamento/Histórico - MNTA820**, informar uma data superior a **Data início do Plano - TO\_DATAINI** no parâmetro **Ate Data Acompan.?**
