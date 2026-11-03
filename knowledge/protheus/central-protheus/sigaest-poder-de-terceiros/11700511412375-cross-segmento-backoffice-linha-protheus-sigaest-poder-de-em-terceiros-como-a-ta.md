---
article_id: 11700511412375
category: SIGAEST - PODER DE TERCEIROS
content_hash: 63d2b6c361c5e3ceb271cd6a0877678579421a92007cfd912e93d0dbbee6b261
fetched_at: '2026-06-28T22:39:03.233112+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Poder de / em terceiros.
  Como a tabela SB6 efetua o controle dos saldos?
type: support-article
updated_at: '2023-01-16T17:39:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11700511412375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Poder-de-em-terceiros-Como-a-tabela-SB6-efetua-o-controle-dos-saldos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como analisar o controle de Poder de Terceiros pela tabela SB6?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**O Protheus controla o poder de/em terceiros através da tabela SB6. Nesta tabela existe o campo ***SB6->B6\_IDENT***, quando os TES envolvidos na movimentação entrada/saída controlando poder de terceiros estão configurados com o campo SF4->F4\_PODER3=Remessa ou Devolução. [Veja FAQ com instruções.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros-)

O campo B6\_IDENT grava a identidade da movimentação do material de/em terceiro conforme a origem da movimentação, porem sempre gravará exclusivamente nas tabelas SD1,SD2 e SB6.

Quando o processo é realizado, caso a devolução for parcial a identidade será a mesma para todas as notas de retorno, sendo alterado apenas o saldo gravado no campo SB6->B6\_SALDO.

No final de todos os retornos o sistema gravará os campos

Tabela - SD1 campo ***D1\_IDENTB6***

Tabela - SD2 campo ***D2\_IDENTB6***

Tabela - SB6  campo ***B6\_IDENT*** e o campo ***B6\_SALDO*** estará igual a ***0***.

***Dica:*** Utilizar o relatório ***SALDO EM ESTOQUE (MATR480)*** para controlar os saldos que constam DE/EM TERCEIROS.

 - No *exemplo simulado* abaixo, observe que o campo B6\_SALDO consta com quantidade 30.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11700786229527)

Caso, tentar devolver uma quantidade superior, exibirá o ***Help: A100N/PD3*** impedindo uma movimentação superior ao que foi enviado a terceiros. Ou, seja não é possível a devolução com quantidade a maior. Somente o saldo exato que foi enviado a terceiros.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11700807381911)

***Observações importantes:***

 - Os movimentos de/em Terceiros não devem ser efetuados diretamente pela base de dados, podendo causar impactos irreversíveis nos saldos.

  - Não existe uma função ou rotina para limpeza de saldo de/em terceiros. Por exemplo um inventário ou movimentos interno. Nesse caso, veja a FAQ com instruções sobre esse cenário. [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-um-retorno-simb%C3%B3lico-limpar-saldo-de-material-que-ficou-em-poder-de-terceiros-?source=search).

 - Atentar-se aos cenário que teve necessidade em alterar o tamanho das casas decimais nas tabelas SD1 e SD2, pode causar impacto nas devoluções caso não sejam também atualizadas as decimais na tabela SB6.

- Para os casos em que o Cliente ou Fornecedor não existirem mais, habilitar o parâmetro ***F12 Operação Triangular (print abaixo)*** e listar a devolução amarrada a outro Fornecedor ou Cliente para efetuar a baixa corretamente.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11701821138327)

**Saiba Mais*****:***

*[Como efetuar um retorno simbólico (limpar saldo) de material que ficou em poder de terceiros?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-um-retorno-simb%C3%B3lico-limpar-saldo-de-material-que-ficou-em-poder-de-terceiros-?source=search)*

*[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
