---
article_id: 360024680071
category: Escrita Fiscal - Impostos - ICMS
content_hash: ac47b5d39e6c806acd084060088df1268076ac1e0177e4eb3366ba937bb3182f
fetched_at: '2026-06-28T22:39:24.196249+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar as tags
  do ICMS efetivo?
type: support-article
updated_at: '2021-07-28T02:15:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024680071-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-as-tags-do-ICMS-efetivo
---

**Dúvida**

Como gerar as tags do ICMS efetivo?  
  
**Ambiente**

Protheus – Livros Fiscais– A partir da versão 12.1.17

**Solução**

Para gerar as tags do ICMS efetivo configure conforme abaixo:

**Cliente**

Tipo (A1\_TIPO) = Consumidor Final

**TES**

Calcula ICMS (F4\_ICM) = Sim ou não

Livro Fiscal de ICMS (F4\_LFICM) = Outros

Sit Trib ICM (F4\_SITTRIB) = 60

Com essas configurações será gerado o grupo de tags do efetivo:

![](https://lh3.googleusercontent.com/-8M82ap9oNNg/XHfhZpNVDoI/AAAAAAAAAH0/0GGXCY2UEM0Cyd38dRTZlAhglApimcXVwCK8BGAs/s493/2019-02-28.png)

Rega de preenchimento Tags:

**pRedBCEfet**:  segundo a regra de validação deverá ser preenchido com percentual de redução, caso estivesse submetida ao regime comum de tributação, para obtenção da base de cálculo efetiva (vBCEfet).

**vBCEfet:**segundo a regra de validação deverá ser preenchido com Valor da base de cálculo que seria atribuída à operação própria do contribuinte substituído, caso estivesse submetida ao regime comum de tributação, obtida pelo produto do vProd por (1- pRedBCEfet).

 **pICMSEfet**: segundo a regra de validação deverá ser preenchido com a Alíquota do ICMS na operação a consumidor final, caso estivesse submetida ao regime comum de tributação.

**vICMSEfet**: segundo a regra de validação deverá ser preenchido Obtido pelo produto do valor do campo pICMSEfet pelo valor do campo vBCEfet, caso estivesse submetida ao regime comum de tributação. 

* **Saiba mais:**

Para **UF de RS é gerada as TAGS do ICMS efetivo para Produtor rural,**para isso realizar os procedimentos abaixo:

1- Configure o parâmetro **MV\_ESTADO = RS.**

2- No cadastro de cliente configure o campo **Tipo (A1\_TIPO)** = **L** **(Produtor Rural)**

3-  Configure o TES  conforme abaixo:

**Calcula ICMS (F4\_ICM)** = Sim ou não

**Livro Fiscal de ICMS (F4\_LFICM)** = Outros

**Sit Trib ICM (F4\_SITTRIB)** = 60

4 - Realize atualização do NFESEFAZ:

* Para aplicar o RDMAKE de **NFe, MDFe, NFSE há o link abaixo:**

<https://suporte.totvs.com/portal/p/10098/download#detail/950596>

Conforme o Print estão centralizados em pastas separadas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062955293/mceclip0.png)

* **Importante:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

Esse tratamento foi realizado para atender o **parecer do link abaixo:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=490661819>

* Referente ao destaque do **ICMS Efetivo destacar no Danfe segue o parecer** da consultoria **no link abaixo:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=552104177>
