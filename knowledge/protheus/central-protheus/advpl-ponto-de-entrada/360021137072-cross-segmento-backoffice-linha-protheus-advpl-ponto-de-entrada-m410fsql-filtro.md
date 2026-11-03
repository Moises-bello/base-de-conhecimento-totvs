---
article_id: 360021137072
category: ADVPL - Ponto de Entrada
content_hash: 2e3222838d1175a1e86d3877b945082c9ccd70ab64c48de213b055ce3dd318af
fetched_at: '2026-06-28T22:40:11.568882+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Ponto de entrada M410FSQL:
  Filtro de pedidos de venda'
type: support-article
updated_at: '2021-12-21T20:55:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021137072-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-M410FSQL-Filtro-de-pedidos-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como criar um filtro no ponto de entrada **M410FSQL** na versão protheus 12?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**O ponto de entrada **M410FSQL** tem comportamentos diferentes na P11 e na P12, a expressão utilizada na P11 deverá ser em SQL já na P12 a expressão deverá ser em ADVPL, pois ambas utilizam classe diferentes:

**Descrição na P11**: Ponto de Entrada que permite filtrar os pedidos de venda exibidos na *mBrowse*, em que deve ser informada uma expressão SQL para a realização do filtro.

**Retorno: cFilSQL -**Carácter - Expressão SQL

**Descrição na P12** : Ponto de Entrada que permite filtrar os pedidos de venda exibidos na *FWMBrowse*, em que deve ser informada uma expressão ADVPL para a realização do filtro.

**Retorno: cFilSQL -**Carácter - Expressão ADVPL

Exemplo de customização na p12

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "rwmake.ch"  
  
User Function M410FSQL()  
  
Local _vpFiltro := ""  
  
   Alert("M410FSQL")  
         _vpFiltro := "C5_CLIENTE = 'CL0003'"  
         _vpFiltro := "C5_NUM > '000015' .and. C5_TIPO == 'N'"  
         _vpFiltro := "C5_CLIENT $ 'CL0007|CL0003|'"  
Return(_vpFiltro)
```

**Saiba mais**  
[M410FSQL: Filtro de pedidos de venda](https://tdn.totvs.com/display/public/PROT/M410FSQL+-+Filtro+de+pedidos+de+venda)
