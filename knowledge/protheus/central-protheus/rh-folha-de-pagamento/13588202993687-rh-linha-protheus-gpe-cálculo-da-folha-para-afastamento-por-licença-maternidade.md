---
article_id: 13588202993687
category: RH - Folha de Pagamento
content_hash: fe358e23d8e5d48be0b8a94a53777b9407623b59c78b2f56387bbacba077796a
fetched_at: '2026-06-28T22:44:12.014080+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo da folha para afastamento por Licença Maternidade,
  todo o mês de Fevereiro, calcula 2 dias de saldo de salário
type: support-article
updated_at: '2024-09-09T19:07:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13588202993687-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-folha-para-afastamento-por-Licen%C3%A7a-Maternidade-todo-o-m%C3%AAs-de-Fevereiro-calcula-2-dias-de-saldo-de-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26236183246231) Tempo aproximado para leitura: 00**:03:00 min**

**Ocorrência**Cálculo da folha para afastamento por Licença Maternidade, todo o mês de Fevereiro, calcula 2 dias de saldo de salário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Ao calcular a folha no mês de Fevereiro, para Afastada por Licença Maternidade, sistema não obedece o conteúdo do mnemônico P\_PGSALFEV=.T., calcula dois dias de salário indevidamente e 28 dias de Salário Maternidade, quando o mesmo abrange todo o mês.  
  
**Solução**Para que cálculos efetuados no mês de Fevereiro considerem 30 dias e não os dias do mês (28/29), verifique se o mnemônico **P\_PGSALFEV,** está habilitado (**.T.).**  
  
Com o mnemônico ativado serão considerados 30 dias tanto para a divisão quanto para os dias trabalhados.

**P\_PGSALFEV = .T.**Admissão = 20/02/2022  
Salário = 5000,00

Temos:

Dias Trabalhados = 30 - 20 + 1 = 11 Dias  
5000,00 / 30 \* 11 = 1500,00

Caso o mnemônico esteja com **.F.** será realizado o seguinte cálculo:

Admissão = 20/02/2022  
Salário = 5000,00

Temos:

Dias Trabalhados = 28 - 20 + 1 = 9 Dias  
5000,00 / 28 \* 9 = 1607,14.

**Observação**Se o mnemônico **P\_PGSALFEV** estiver habilitado, e o sistema não considerar os 30 dias para pagamento do Salário Maternidade, verifique se o ambiente utilizado, está atualizado com nosso último pacote de Expedição Contínua (Acumulado) RH Protheus:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus>

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
