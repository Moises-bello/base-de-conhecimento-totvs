---
article_id: 360006908032
category: Ativo Fixo - Bloqueio/Desbloqueio de Movimentação
content_hash: ece1a46f8798929ead8545bb6399e06434d9b7c0499eb4a9b67355297c420494
fetched_at: '2026-06-28T22:41:49.661379+00:00'
product: protheus
section_id: 1500001547562
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Bloqueio de movimentações
  de ativo imobilizado
type: support-article
updated_at: '2024-04-24T17:36:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Bloqueio-de-movimenta%C3%A7%C3%B5es-de-ativo-imobilizado
---

**Dúvida**Como realizar bloqueio de movimentações de ativo imobilizado?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Ativo Fixo – A partir da versão 12.  
  
**Solução**

No módulo de Ativo Fixo existem quatro abordagens para o bloqueio de movimentações do ativo, que são:

* Parâmetro MV\_ATFBLQM.  
  Este parâmetro bloqueia todas as movimentações de todos os ativos até a data parametrizada. Utilizado para manter a integridade das informações do módulo após, por exemplo, o fechamento contábil evitando que usuários façam operações com a database retroativa ao fechamento.
* Campo N1\_STATUS.  
  Campo na ficha do ativo que determina o estado atual do bem, que indica se está ativo, pendente de classificação ou transferido de filial.

Pode também ser utilizado para o bloqueio através da função **Bloqueio** no cadastro de ativo. Quando o bem se encontra nesse estado, todas as operações com ele, exceto a transferência de locais, ficam indisponíveis.

* Campo N1\_DTBLOQ.  
  Campo na ficha do ativo que determina uma data para o bloqueio da depreciação de um ativo. Podendo somente efetuar as movimentações após o período do bloqueio.

Este campo tem o seu comportamento relacionado com o parâmetro MV\_ATFMBLQ **(não confundir com MV\_ATFBLQM)**, que caso o campo de data de bloqueio esteja preenchido, a depreciação nesse ultimo mês, será integral, ou proporcional até a data do bloqueio.

Existe a rotina Bloqueio de Movimentações (ATFA330), este rotina bloqueio todos os tipos de movimentações (Baixa, Transferência, Calculo de Depreciação e etc.) até a data informada na rotina, evitando assim que haja movimentações no Ativo Fixo.
