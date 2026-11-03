---
article_id: 360006986251
category: Contabilidade Gerencial - Balancetes
content_hash: eefe75ebe60875ad64cb6ab78b2ee05f9ec5ec47a0a268a7ae0dd30b1d40affb
fetched_at: '2026-06-28T22:41:04.203361+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR040 - SALDO DO RELATÓRIO
  APÓS MIGRAÇÃO
type: support-article
updated_at: '2021-12-28T11:59:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006986251-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-SALDO-DO-RELAT%C3%93RIO-AP%C3%93S-MIGRA%C3%87%C3%83O
---

**Ocorrência**

Após migração da versão  P11 para a versão  P12

Ao imprimir o relatório CTBR040 - Balancete e o CTBR400 Razão,  são apresentadas situações abaixo :

* Msg - Não ha dados a serem impressos
* Saldos do balancete não batem com o razão contábil
* Saldo anterior do razão não é exibido

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.017  
  
**Causa**

Na versão P12 algumas tabelas CT's foram descontinuadas e substituídas pelas tabelas  CQ's

Correspondência da Versão 11 para a versão 12

      CT7 = CQ0 e CQ1  
      CT3 = CQ2 e CQ3  
      CT4 = CQ4 e CQ5  
      CTU = CQ8 e CQ9  
      CTI = CQ6 e CQ7

A tabela CT2 permanece sendo utilizada na versão P12

**Solução**

Após a migração para a versão 12, é necessário a execução da rotina de reprocessamentos, a partir do primeiro período de movimentação na contabilidade até o período atual, ou seja toda a movimentação.

Verifique o COMPARTILHAMENTO DE TABELAS

**O compartilhamento da tabela de saldos deve ser igual ao da CT2**

<http://tdn.totvs.com/display/public/mp/Compartilhamento+de+tabelas+SigaCTB+--+23595>

Para que as tabelas CQ seja alimentada corretamente é necessário realizar o reprocessamento de saldo com Base no primeiro lançamento existente na tabela CT2 até a data de hoje.

<http://tdn.totvs.com/pages/releaseview.action?pageId=235583698>  
  
Segue documento sobre a restruturação:  
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=274843987>
