---
article_id: 360022457452
category: Contabilidade Gerencial - Entidades
content_hash: 38ab258c65358feaa52d45502a6b86f56f82622cdcbb9f0fe2eb2e695c2c17a0
fetched_at: '2026-06-28T22:40:49.776868+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Tabelas CVX e CVY
type: support-article
updated_at: '2022-04-06T19:40:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022457452-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Tabelas-CVX-e-CVY
---

**Dúvida**O que são e como faço para alimentar as tabelas CVX e CVY?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**As tabelas CVX e CVY são as tabelas de saldos para controle de todas as entidades no sistema, podendo ser entidades padrão do sistema(Conta Contábil, Centro de Custo, Item Contábil ou Classe Valor) e também as adicionais, que podem ser criadas através do wizard U\_CTBWIZENT.

Caso deseje documentação sobre o wizard pode acessar o link: [MP - SIGACTB - Entidades adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013316351-MP-SIGACTB-Entidades-adicionais?source=search)

Na tabela CVX(Saldos Diários) são gravados os dados diários para as entidades, assim poderá ser feito um controle de saldos entre todas as entidades do sistema.

Na tabela CVY(Saldos Mensais Acumulados) são gravados os dados de forma mensal também para o controle das entidades.

Como são tabelas para controle de saldos entre as entidade padrão do sistema e as adicionais, para o correto funcionamento do processo de alimentação, o parâmetro MV\_CTBCUBE deve estar igual a 1. Com o parâmetro ativado, bastaria efetuar novos lançamentos ou reprocessar os saldos para que as tabelas sejam populadas.

Para verificar o conteúdo dessas tabelas pode-se utilizar o relatório CTBR051(Balancete por entidade), segue Help da rotina: <http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctbr051.htm>

Saiba Mais:

[MP - SIGACTB: Reestruturação dos Saldos Contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018467872-MP-SIGACTB-Reestrutura%C3%A7%C3%A3o-dos-Saldos-Cont%C3%A1beis?source=search)
