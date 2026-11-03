---
article_id: 21678283458455
category: Faturamento - Cadastros
content_hash: 7e81b5f2d79555ecf688a07301caf13f2caad5d1d84fa62c9fb583e2f73319c8
fetched_at: '2026-06-28T22:38:36.778940+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 6
type: support-article
updated_at: '2024-03-05T12:51:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678283458455-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-6
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21678315228695) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 6?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Recomendado para condições de complexidade alta;

**Exemplo em vídeo de como criar (How To Tutorial):**

Determina-se a quantidade de parcelas, o tempo em dias) até o início dos pagamentos, o dia da semana que o vencimento pode cair e a carência entre os vencimentos das parcelas (duplicatas).

![](https://tdn.totvs.com/download/attachments/240310845/61.png?version=1&modificationDate=1664166061000&api=v2)

**d(S) são os dias de semana, assume-se:**

1 - Domingo

2 - Segunda-Feira

3 - Terça-Feira

4 - Quarta-Feira

5 - Quinta-Feira

6 - Sexta-Feira

7 - Sábado

**Cadastrando:**

E4\_CODIGO = (critério do usuário)

E4\_TIPO = 6

E4\_COND = 6,15,4 (Quarta-Feira), 30

![](https://tdn.totvs.com/download/attachments/240310845/62.png?version=1&modificationDate=1664166078570&api=v2)

**Resultado:**

Os pagamentos serão efetuados da seguinte forma:

* 1ª parcela paga 15 dias após a emissão, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 2ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 3ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 4ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 5ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 6ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.

**GIF Exemplo do resultado da simulação utilizando uma condição de pagamento Tipo 6 (Tipo 6 - E4\_TIPO = “6”):**

![](https://tdn.totvs.com/download/attachments/240310845/tipo6.gif?version=1&modificationDate=1656449194650&api=v2)

**Saiba mais:**

[**Todas as Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
