---
article_id: 360011417431
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: 95bc632aed2d217e810707c05987970fa1097c7e292e2a26704494673094ca09
fetched_at: '2026-06-28T22:41:42.373081+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - VARIÁVEIS USADAS EM
  CONTABILIZAÇÃO TRANSFERÊNCIA DE ATIVO
type: support-article
updated_at: '2023-11-30T19:36:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011417431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-VARI%C3%81VEIS-USADAS-EM-CONTABILIZA%C3%87%C3%83O-TRANSFER%C3%8ANCIA-DE-ATIVO
---

**Dúvida**  
**VARIÁVEIS USADAS EM CONTABILIZAÇÃO TRANSFERÊNCIA DE ATIVO**  
  
**Ambiente**Microsiga Protheus – Ativo Fixo – A partir da versão 11.80.  
  
  
**Solução**Na configuração do **LP 830** OU **831 e 832** para transferências entre grupos e/ou contas/centros e demais atributos, temos outras variáveis internas que podem ser usadas na transferência:  
Estão disponíveis também as seguintes variáveis para Contas:

* **CTABEM** - conta do bem destino.
* **DESPDEPR** - conta de despesa de depreciação destino.
* **DEPREACUM** - conta de depreciação acumulada destino.
* **CORREBEM** - conta de correção do bem destino.
* **CORREDEPR** - conta de correção da depr. acum destino.

Estão disponíveis também as seguintes variáveis para demais atributos:

* **Centros de Custos**

CUSTBEMCTB  
CCCORRCTB  
CCDESPCTB  
CCCDESCTB  
CCCDEPCTB

* **Item Contábil**

SUBCCONCTB  
SUBCCORCTB  
SUBCDESCTB  
SUBCDEPCTB  
SUBCCDECTB

* **Classe de Valor**

**CLVLCONCTB**  
CLVLCORCTB  
CLVLDESCTB  
CLVLDEPCTB  
CLVLCDECTB

Saiba Mais

[MP\_SIGAATF - COMO FUNCIONA ROTINA ATFA060 TRANSFERÊNCIA DE ATIVO?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015091671-MP-SIGAATF-COMO-FUNCIONA-ROTINA-ATFA060-TRANSFER%C3%8ANCIA-DE-ATIVO-?source=search)
