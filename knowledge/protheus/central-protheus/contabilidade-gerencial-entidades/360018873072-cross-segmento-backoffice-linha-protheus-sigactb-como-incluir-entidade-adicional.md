---
article_id: 360018873072
category: Contabilidade Gerencial - Entidades
content_hash: ec03ad77560b5044b3bea04b96b1f4e45180f3b224546815b8ab6f07d9277b79
fetched_at: '2026-06-28T22:40:49.732580+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -  SIGACTB: Como Incluir entidade
  adicional'
type: support-article
updated_at: '2023-08-15T13:36:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018873072-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Incluir-entidade-adicional
---

**Dúvida**

Qual o procedimento para Incluir nova entidade contábeis , possibilitando assim selecionar a entidade deseja ao incluir o lançamento contábil?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014930151)  
  
**Ambiente**   
Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

* Após executar o**[U\_CTBWIZENT](https://tdn.totvs.com/pages/releaseview.action?pageId=59900337)**o sistema irá criar os campos das entidade adicionais
* Com o parâmetro [MV\_CTBCUBE](http://tdn.totvs.com/pages/viewpage.action?pageId=338368502) =1
* Através da rotina "CTBA005"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014896812)

* Antes de duplo *click,*veja o caso dessa "05 Entidade ADD" Tabela CV0

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014930851)

* Após o duplo *click* aparece na entidade o símbolo de “+”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014896992)

* Dê mais um *click* no símbolo de ”![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014897032)” e aparece Incluir a próxima entidade

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014897332)

* Preencher o campos obrigatórios e Inclua

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014932291)

* Ao confirmar o sistema salda a nova entidade

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014932411)

* Ao incluir o lançamento contábil (CTBA102) irá apresentar a nova entidade criada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014898392)
