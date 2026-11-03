---
article_id: 1500009301082
category: Materiais - Compras (SIGACOM)
content_hash: 858352b8ddc554dfd91278ed40f0e26485fd4d6a27fdb19992debf57aa845952
fetched_at: '2026-06-28T22:41:12.948069+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Quais Lançamentos
  Padrões para Contabilização do Rateio de Múltiplas Naturezas no documento de entrada  ? '
type: support-article
updated_at: '2024-02-07T21:21:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009301082-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-Lan%C3%A7amentos-Padr%C3%B5es-para-Contabiliza%C3%A7%C3%A3o-do-Rateio-de-M%C3%BAltiplas-Naturezas-no-documento-de-entrada
---

**Dúvida**Quais Lançamentos Padrões para Contabilização do Rateio de Centro de Custo com Múltiplas Naturezas ?  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.17.  
  
**Solução**

Para contabilização Online corretamente com rateio por múltiplas naturezas deve ser configurado os LP's abaixo:

**65C** - Documento de Entrada - Rateio Múltiplas Naturezas  
**65D** - Documento de Entrada - Cancelamento Rateio Múltiplas Naturezas

Lembrando que é necessário observar:  
  
1) Parâmetro **MV\_MULNATP** deve estar = **.T.**

2)Parâmetro **MV\_MULNATS** deve estar = **.T.**

3) A TES do documento de entrada deve ser de Gera Financeiro (Contas a pagar)

4) Deverá ser configurado nos parâmetros **F12** do documento de entrada a opção para **Contabilização Online = Sim.**

***Saiba Mais :***

[MP - SIGAFIN - Como utilizar rateio de múltiplas naturezas por Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022094831-MP-SIGAFIN-Como-utilizar-rateio-de-m%C3%BAltiplas-naturezas-por-Centro-de-Custo)

[TSQORN\_DT\_CONTABILIZACAO\_ONLINE\_RATEIO\_MULTIPLAS\_NATUREZAS](https://tdn.totvs.com/display/public/PROT/TSQORN_DT_CONTABILIZACAO_ONLINE_RATEIO_MULTIPLAS_NATUREZAS)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
