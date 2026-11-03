---
article_id: 360017785351
category: Ativo Fixo - Virada Anual
content_hash: c5b49fa32838a2fef717c0f646d3935e2ad5debea93cce0940acc8be3d656892
fetched_at: '2026-06-28T22:41:54.216809+00:00'
product: protheus
section_id: 1500001547482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -SIGAATF - ATFA080 Como devo utilizar
  a rotina Virada Anual
type: support-article
updated_at: '2025-01-31T12:25:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017785351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA080-Como-devo-utilizar-a-rotina-Virada-Anual
---

**Dúvida**Como devo utilizar a rotina Virada Anual?

**Ambiente**Protheus – Ativo Fixo  Versão 12  
  
  
**Solução**

A virada anual deve ser executada com o encerramento do exercício contábil.

No **Ativo Fixo**, o exercício deve ser encerrado após o cálculo da depreciação de dezembro, sendo que para executar a rotina deve ser alterada a database do sistema para 01 de janeiro do próximo exercício.

A rotina **Virada Anual (ATFA080)** é utilizada para gerar os saldos iniciais para o próximo exercício**N5\_TIPO = 0** (zero).

Por exemplo: Sendo efetuado o cálculo de 31/12/2003, deve ser alterada a database para 01/01/2004 e executada a rotina **Virada Anual(ATFA080)** nesta data.  
Após a virada anual, algumas contas podem aparecer com o saldo anterior negativo. Isto ocorre para bens patrimoniais (grupo de contas 2, com N1\_PATRIM $ “SAC”) quando o saldo da conta não é prejuízo.  
A rotina de **Virada Anual (ATFA080)** reconstruí a tabela **SN5**, baseada nos saldos contidos na tabela **SN3** que sejam consistidos com os movimentos da tabela **SN4**.

Ao realizar a **Virada Anual (ATFA080)**, é gravado na **SN0** tabela '**13**' a data da última virada anual realizada no sistema.

**Saiba Mais** :

[MP - SIGAATF - É possível realizar estorno (correção) da rotina ATFA080](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012953711-MP-SIGAATF-%C3%89-poss%C3%ADvel-realizar-estorno-corre%C3%A7%C3%A3o-da-rotina-ATFA080?source=search)

[Como funciona a rotina Virada Anual (ATFA080)](https://tdn.totvs.com/pages/releaseview.action?pageId=271163111)

<http://tdn.totvs.com/display/public/PROT/Virada+Anual+--+11330>
