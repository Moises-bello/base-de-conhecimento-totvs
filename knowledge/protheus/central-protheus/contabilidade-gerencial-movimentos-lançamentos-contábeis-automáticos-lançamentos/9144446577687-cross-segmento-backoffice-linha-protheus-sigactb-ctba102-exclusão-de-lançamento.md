---
article_id: 9144446577687
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 6363798dafe8bb50b975d12a71f27b506b5a412ffc649dec94380c082c8f5957
fetched_at: '2026-06-28T22:40:32.445764+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Exclusão
  de lançamento contábil gera error.log : Invalid data type on (F3_DTLANC)'
type: support-article
updated_at: '2023-11-13T15:52:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9144446577687-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amento-cont%C3%A1bil-gera-error-log-Invalid-data-type-on-F3-DTLANC
---

**Ocorrência**

Error.log ao excluir lançamento contábil -  "Invalid data type on (F3\_DTLANC)"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Todas as versões

**Causa**

Este erro geralmente é gerado, quando o rastreio do lançamento contábil esta gravado incorretamente, ou seja quando o lançamento contábil aponta para uma origem diferente do realizado na contabilização.

Podendo ser causado por Packs nas tabelas que envolvem o processo da contabilização ou exclusões indevidas nas tabelas do lançamento.

**Solução**

O sistema grava os campos campos de rastreio CV3\_RECDES e CV3\_RECORI somente no momento da contabilização. Sendo assim para correção do erro é necessário excluir o lançamento sem limpar os Flags de contabilização e realizar a contabilização novamente, para que o  rastreio contábil seja gerado corretamente.

Para excluir o lançamento sem a limpeza do Flag deverá seguir a documentação abaixo para alteração do parametro MV\_CTBAPLA, que controla a gravação dos campos de Flags na exclusão do lançamento contábil.

[Cross Segmento - Backoffice Linha Protheus - RECONTABILIZAÇÃO DAS FLAGS - MV\_CTBAPLA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007819611-Cross-Segmento-Backoffice-Linha-Protheus-RECONTABILIZA%C3%87%C3%83O-DAS-FLAGS-MV-CTBAPLA)

Exemplo da gravação do rastreio Contábil:

A contabilização do Contas a pagar do módulo financeiro ira gerar movimentos na tabela SE2 que é a origem e ira gerar movimento na tabela CT2 destino, a tabela CV3 ira interligar as duas sendo informado a origem e destino gerando o rastreio contábil.

Abaixo um exemplo de como verificar se o rastreio contábil esta gravado corretamente:

![Gravar_2022_09_26_14_06_50_802.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/9143926355479)

**Saiba Mais**

<https://tdn.totvs.com/pages/releaseview.action?pageId=6068533>

[Cross Segmento - Backoffice Linha Protheus - CTBA105 Como é composta a chave de rastreamento na tabela CV3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022784291-MP-SIGACTB-CTBA105-Como-%C3%A9-composta-a-chave-de-rastreamento-na-tabela-CV3-)
