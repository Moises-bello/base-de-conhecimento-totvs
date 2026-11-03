---
article_id: 15907807807127
category: Gestão de Frotas
content_hash: b67f2aacccc1f6ba654c4cf2a61f0a11a711c6ed961ffb0f8d79b2473d0ca509
fetched_at: '2026-06-28T22:42:39.385400+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Erro array out of bounds...on MNT877TQS(MNTA877.PRW)
type: support-article
updated_at: '2023-07-11T18:01:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15907807807127-Manufatura-Linha-Protheus-MNT-Erro-array-out-of-bounds-on-MNT877TQS-MNTA877-PRW
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15907866164887)* Tempo aproximado para leitura: **00:01:15 min**  
  
**Ocorrência**  
Ao realizar um processo ocorre o erro **array out of bounds...on MNT877TQS(MNTA877.PRW)****Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Causa**  
A situação acontece quando existe um pneu que possui um contador controlado pela estrutura, ao realizar processos no módulo, algumas informações da tabela **TQS - Complemento de pneus** precisam ser revisadas / atualizadas com base no **TQV - Histórico de sulco dos pneus** e por conta de uma inconsistência no valor da **Banda do pneu - TQV\_BANDA**. No caso a informação está **vazia**.  
  
**Solução**  
Para ajustar a situação será necessário realizar um ajuste via **APSDU** para os registros da tabela **TQV** buscando os registros que possuem o campo **TQV\_BANDA** igual a **vazio**, para anotar as informações dos códigos dos pneu que se encontram nessa situação. Com isso realize uma busca individual para cada pneu e informe o valor da **TQV\_BANDA** de acordo com os registros da tabela. Por exemplo, no *print* a seguir a informação **TQV\_BANDA**que está vazia precisa receber o valor **1**, porque o próximo registro de **TQV\_BANDA** continua sendo **1**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15907522346135)
