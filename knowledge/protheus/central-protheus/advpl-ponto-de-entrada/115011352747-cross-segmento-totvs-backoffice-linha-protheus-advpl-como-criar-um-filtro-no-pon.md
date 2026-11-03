---
article_id: 115011352747
category: ADVPL - Ponto de Entrada
content_hash: 5af4c25cc42ac7a144943b14ffa7a6b9b8fe41f537c66f8de314c1fc81aee673
fetched_at: '2026-06-28T22:40:11.676047+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como criar um filtro
  no ponto de entrada M410FSQL
type: support-article
updated_at: '2022-06-21T17:56:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011352747-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-filtro-no-ponto-de-entrada-M410FSQL
---

**Dúvida**Como criar um filtro no Ponto de Entrada M410FSQL?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**O ponto de entrada M410FSQL tem comportamentos diferentes na P11 e na P12, a expressão utilizada na P11 deverá ser em SQL já na P12 a expressão deverá ser em ADVPL pois ambas utilizam classe diferentes.  
 **Descrição na P11**: Ponto de Entrada que permite filtrar os pedidos de venda exibidos na mBrowse, em que deve ser informada uma expressão SQL para a realização do filtro.  
**Retorno: cFilSQL -**( Caracter) - Expressão SQL

**Descrição na P12** : Ponto de Entrada que permite filtrar os pedidos de venda exibidos na FWMBrowse, em que deve ser informada uma expressão ADVPL para a realização do filtro.  
**Retorno: cFilSQL -**( Caracter) - Expressão ADVPL  
  
Exemplo

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "rwmake.ch"  
  
User Function M410FSQL()  
  
Local _vpFiltro := ""  
  
Alert("M410FSQL")  
  
//_vpFiltro := "C5_CLIENTE = 'CL0003'"  
//_vpFiltro := "C5_NUM > '000015' .and. C5_TIPO == 'N'"  
_vpFiltro := "C5_CLIENT $ 'CL0007|CL0003|'"  
  
Return(_vpFiltro)
```

**Saiba mais**[ADV0012 Ponto de entrada M410FSQL](http://tdn.totvs.com/display/PROT/ADV0012_PE_M410FSQL)
