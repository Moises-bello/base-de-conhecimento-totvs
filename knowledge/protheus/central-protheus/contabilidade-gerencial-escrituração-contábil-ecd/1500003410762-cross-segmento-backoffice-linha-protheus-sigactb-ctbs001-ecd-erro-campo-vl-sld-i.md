---
article_id: 1500003410762
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: f7ac8448ba0f3769353d80505d0cfcdf1e51f0acc87eea9d4dfbfacd5b91013f
fetched_at: '2026-06-28T22:40:45.638729+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001- ECD Erro campo
  VL_SLD_IN registro I157 não corresponde a soma dos saldos iniciais, registro I157
type: support-article
updated_at: '2021-09-04T00:03:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003410762-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Erro-campo-VL-SLD-IN-registro-I157-n%C3%A3o-corresponde-a-soma-dos-saldos-iniciais-registro-I157
---

**Dúvida**

Erro no Validador, campo VL\_SLD\_IN: O valor informado no campo saldo inicial do registro de Saldos Periódicos (I155) não corresponde à soma dos valores de saldos iniciais informados nos registros de transferência de saldos do plano de contas anterior (I157).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003504661/mceclip0.png)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução:**O relacionamento do registro I157, para contas que possuem saldos implantados deve ser realizado em 31/12/XX . Período anterior ao que esta sendo entregue a ECD atual.

Exemplo: ECD de 2020, relacionar o I157 com lançamentos implantados em 31/12/2019.

Os relacionamentos para lançamentos em 2020, neste caso, são para contas que não possuem lançamentos de implantação de saldos, ou seja, conta zerada.

Rotina CTBA102, Posicionar sobre o lançamento que foi "implantado os saldos" em 31/12/XX

**+ outras ações + LCT. TRANSF. SALDO**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003458502/mceclip1.png)

**Saiba mais**

**[Como gerar o registro I157 da ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003409082-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-gerar-o-registro-I157-da-ECD)**
