---
article_id: 115016115388
category: Contabilidade Gerencial - Reprocessamento
content_hash: 27876ebac3df7dac5ed9b86a74f42384a398860437023ea2c1d43aa389b466de
fetched_at: '2026-06-28T22:40:41.880141+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB -  Saldo anterior zerado
  ou incorreto
type: support-article
updated_at: '2025-12-04T20:19:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016115388-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Saldo-anterior-zerado-ou-incorreto
---

**Ocorrência**  
Saldo anterior zerado nos relatórios contábeis  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12

**Solução**

Os Relatórios contábeis para saldo anterior buscam os dados na família de tabelas Saldos Diários e Saldos Mensais (CQ0 - CQ9), os movimentos são apresentados baseados na tabela Lançamento Contábeis (CT2)

Para solucionar essa ocorrência, realize os seguintes passos:

* Emita um relatório de movimento como o [Razão Contábil (CTBR400)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006683712-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-realizar-a-extra%C3%A7%C3%A3o-impress%C3%A3o-do-Raz%C3%A3o-Cont%C3%A1bil-no-PROTHEUS-CTBR400), para verificar se os movimentos estão corretos.

Se os dados forem apresentados de forma incorreta, devera:

Verificar via rotina Lançamento Contábeis Automáticos (CTBA102), se os lançamentos existem ou se estão incorretos e realizar o ajuste ou realizar a contabilização novamente.

Se for necessário realizar a recontabilização deve configurar o parâmetro MV\_CTBAPLA, para limpar o Flag de contabilização e realizar o processo de contabilização novamente:

[Cross Segmento - Backoffice Linha Protheus - Recontabilização das Flags - MV\_CTBAPLA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007819611-Cross-Segmento-Backoffice-Linha-Protheus-Recontabiliza%C3%A7%C3%A3o-das-Flags-MV-CTBAPLA)

* Caso os movimentos estejam corretos, no Razão indica que apenas os saldos estão incorretos.

Para ajuste dos saldos deve:

Verificar a data que esta inconsistente e executar o ajuste de saldos para o período contábil incorreto.

**Exemplo:**  
Primeiro lançamento registrado: 01/01/2025  
Período do Reprocessamento: 01/01/2025 até a data atual seguir os passos descritos na documentação:

A documentação auxilia no processo de ajuste de saldo:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como realizar o reprocessamento de saldos no SIGACTB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB)

Saiba Mais :

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR400 e CTBR040 diferença entre os relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013411871-MP-SIGACTB-Documenta%C3%A7%C3%A3o-CTBR400-e-CTBR040)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Saldos não estão sendo atualizados de forma online.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Fechamento Contábil.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34334419010839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Fechamento-Cont%C3%A1bil)
