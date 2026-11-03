---
article_id: 4410340212887
category: RH - Provisão
content_hash: f6ebd888c7e59dd0b0b20f9b558386a28e26f26f762f1b8dadc558176f98ef41
fetched_at: '2026-06-28T22:43:56.838296+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório Divergências Provisão
type: support-article
updated_at: '2025-06-18T18:27:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410340212887-RH-Linha-Protheus-GPE-Relat%C3%B3rio-Diverg%C3%AAncias-Provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903502405783)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Emissão relatório de Divergências de Provisão (GPER071). 

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.

**Solução:**

O relatório de Divergências de Provisão (GPER071) tem por objetivo apresentar (listar) os funcionários que possuem algum saldo na provisão proveniente do mês anterior de acordo com determinada data fornecida pelo usuário nos parâmetros do relatório, e no mês atual estão com o saldo zerado por algum motivo, como por exemplo, o cálculo de provisão deles ainda não foi executado para aquele mês  
  
No módulo Gestão de Pessoal (SIGAGPE), acesse Miscelânia > Provisões > Provisões de Férias / 13º Salário:

1. Acesse "Outras Ações" e clique em "Divergências";
2. Clique em "Outras Ações" e posteriormente em "Parâmetros";
3. Preencha os parâmetros solicitados e clique em "OK";
4. Feito isso clique em "Imprimir".

**Exemplo:**

O funcionário D MG 01 100000 possui provisão calculada em 12/2016 e possui saldo de provisão pendente, mas para o mês 01/2017, não há cálculo de provisão:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410339373719)

Ou seja, caso seja retirado um relatório geral de provisão do mês de janeiro (01/2017) **o saldo deste funcionário não será apresentado.**

Nesse caso, executando o **Relatório de Divergências de Provisão** com a data base **31/01/2017**e filtrando apenas essa matrícula**,**esse funcionário será apresentado, conforme imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410339424919)

Retirando o mesmo relatório, com os mesmos parâmetros, porém de forma analítica, é demonstrado também o cálculo da provisão do funcionário:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410339927959)

**Observações:**

1. Caso o cálculo de provisão do mês preenchido no parâmetro do relatório, ainda não tenha sido executado para nenhum funcionário, **todos** os funcionários que possuíam saldo no mês anterior serão apresentados. Portanto o ideal é que somente após o cálculo da provisão do mês ter sido realizado, o relatório seja executado para que sejam identificados os funcionários com as divergências;
2. O objetivo do relatório **não é identificar os motivos** pelos quais os funcionários apresentados não foram considerados no mês atual, ou seja, possuíam saldo e no mês corrente estão zerados, mas sim identificar quais são os funcionários nessas condições.

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
