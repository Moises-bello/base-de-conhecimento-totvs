---
article_id: 21677974135447
category: Faturamento - Cadastros
content_hash: cd00e6e158d6356a950d98575684bf06bb5252fb183e5299a745b3bc0db82a2e
fetched_at: '2026-06-28T22:38:36.770193+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da Condição de Pagamento
  Tipo 4
type: support-article
updated_at: '2024-03-04T18:43:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21677974135447-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21677975905047) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**

Como criar a condição de pagamento do tipo 4?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Recomendado para condições de pagamento com média complexidade;

**Exemplo em vídeo de como criar (How To Tutorial):**

Declara-se a quantidade de parcelas, o intervalo entre estas e o dia da semana padrão de vencimento.

![](https://tdn.totvs.com/download/attachments/240310845/41.png?version=1&modificationDate=1664165970200&api=v2)

**d(S) são os dias de semana, assume-se:**

1 - Domingo

2 - Segunda-Feira

3 - Terça-Feira

4 - Quarta-Feira

5 - Quinta-Feira

6 - Sexta-Feira

7 - Sábado

**OBS:** O sistema não retrocede a data para a semana vigente ao vencimento. Quando por intervalo de parcelas O vencimento cair na Quarta-Feira, a mesma semana o sistema levará a regra como vencimento para a Terça-Feira da semana seguinte.

**Exemplo:**

* Emissão 28/06/22 + 30 DDL
* Vencimento cairia para o dia 27/07 (Quarta-Feira), como a regra no pagamento é toda Terça-Feira , o vencimento correto será dia 02/08/22 (terça-feira da próxima semana), então o sistema reajusta, se utilizar essa condição de pagamento.

**Cadastrando:**

E4\_CODIGO = (critério do usuário)

E4\_TIPO = 4

E4\_COND = 4,30,3 (Terça-Feira)

![](https://tdn.totvs.com/download/attachments/240310845/42.png?version=1&modificationDate=1664165990423&api=v2)

**Resultado:**

Os pagamentos serão efetuados da seguinte forma:

* 1ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 2ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 3ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.
* 4ª parcela será paga após o vencimento da duplicata após os 30 dias de intervalo, a parcela será paga no reajuste para o dia da semana mais próximo (configurado) para cair.

**GIF Exemplo do resultado da simulação utilizando a condição de pagamento acima (Tipo 4 - E4\_TIPO = “4”):**

![](https://tdn.totvs.com/download/attachments/240310845/tipo4.gif?version=1&modificationDate=1656449039357&api=v2)

**Saiba mais:**

[**Condição de pagamento do tipo 3**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14307548200215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-3)

[**Todas as Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
