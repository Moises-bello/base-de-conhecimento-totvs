---
article_id: 29589786067479
category: Financeiro - Faturas a Pagar
content_hash: 5365e54a58b228a2d5422bda997e9d5cc564267544a5776f978cb78dbcd9d556
fetched_at: '2026-06-28T22:37:34.252087+00:00'
product: protheus
section_id: 35057532916375
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA290 -  Ao gerar a fatura,
  a data de vencimento dos impostos não é alterada
type: support-article
updated_at: '2026-01-07T17:41:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29589786067479-Cross-Segmentos-Backoffice-Linha-Protheus-FINA290-Ao-gerar-a-fatura-a-data-de-vencimento-dos-impostos-n%C3%A3o-%C3%A9-alterada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29589791986583) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Ao gerar a fatura, a data de vencimento dos impostos não é alterada. O que fazer?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33  
  
**Solução**  
Por padrão, a rotina de fatura não altera a data de vencimento dos impostos.

A rotina de fatura permite a aglutinação de diversos títulos, o que possibilita a geração de um ou mais títulos de destino. Isso dificulta controlar quais impostos devem ser alterados no momento da baixa do título gerado pela fatura.

Entendemos que a alteração da data de vencimento do imposto não deve ocorrer durante a geração da fatura, pois, embora o processo de fatura realize a baixa do título original, isso não caracteriza uma baixa definitiva. Trata-se, na verdade, de uma renegociação, onde o valor permanece em aberto.

Caso seja necessário alterar os vencimentos dos impostos no momento da fatura, é possível utilizar pontos de entrada para customizar essa alteração. Os pontos de entrada que podem ser utilizados para atender a essa necessidade específica são: **FI290GE5** e **FAT290SE5**.

[FI290GE5 - Complemento de gravação do movimento bancário](https://tdn.totvs.com/pages/releaseview.action?pageId=653132877)

[FAT290SE5 - Complemento de gravação dos títulos faturados](https://tdn.totvs.com/pages/releaseview.action?pageId=653133933)
