---
article_id: 360058127914
category: Manutenção de Ativos (SIGAMNT)
content_hash: b9e9e06d808415c54f251a613363f8501cb3bca9464a5dd358ef8e74dae0df4a
fetched_at: '2026-06-28T22:42:34.293540+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Ordenação das etapas através do campo de
  sequência de etapas
type: support-article
updated_at: '2021-09-09T21:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058127914-Manufatura-Linha-Protheus-MNT-Ordena%C3%A7%C3%A3o-das-etapas-atrav%C3%A9s-do-campo-de-sequ%C3%AAncia-de-etapas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura:**00:01:00 min**  
**Dúvida**Como deixar as etapas ordenadas corretamente utilizando o campo de **Sequência de Etapas - TQ\_SEQETA**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Para realizar a ordenação das etapas através do campo de **S****equência de Etapas - TQ\_SEQETA** é necessário se atentar ao preenchimento deste quando utilizar números pois este campo é do tipo **alfanumérico**, ou seja, pode-se informar um conjunto de caracteres alfabéticos e numéricos.  
A ordenação será realizada através dos caracteres informados. Por exemplo, se possuir 12 etapas cadastradas, e a sequência for **1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12**, pelo fato do campo ser alfanumérico, esta ordenação ficará da seguinte maneira **1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8 e 9**.   
Para se evitar que a ordenação fique desta forma é necessário preencher todos os caracteres do campo. Se o campo possuir um tamanho de 3 caracteres, poderá ser feito da seguinte maneira **001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011 e 012.** Se o preenchimento seguir esta orientação a ordenação ficará mais apropriada e correta.
