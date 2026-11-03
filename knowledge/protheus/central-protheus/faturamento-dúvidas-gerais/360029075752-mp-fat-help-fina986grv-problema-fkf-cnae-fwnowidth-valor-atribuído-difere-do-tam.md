---
article_id: 360029075752
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 999ecf84e48a81fb99e58ca2f778bc4946379726294fb304677372bd45896e18
fetched_at: '2026-06-28T22:38:31.076141+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Help - FINA986GRV - Problema FKF_CNAE - FWNOWIDTH - Valor atribuído
  difere do tamanho do campo - CNAE
type: support-article
updated_at: '2021-07-05T17:36:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029075752-MP-FAT-Help-FINA986GRV-Problema-FKF-CNAE-FWNOWIDTH-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-CNAE
---

**Ocorrência**

Ao tentar faturar a nota de saída (**MATA461**), apresenta Help:FINA986GRV

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030685232/mceclip0.png)  
  
**Ambiente**

Microsiga Protheus - a partir da versão 12.

**Causa**

O Help ocorre quando o campo FKF\_CNAE está com o  tamanho diferente do campo **CC3\_COD**.  O campo **FKF\_CNAE** pegará a informação da tabela **CC3**, e o campo precisa ter o mesmo tamanho do campo CC3\_COD ,que por padrão do sistema , o tamanho do campo é 9.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030685792/mceclip1.png)

**Solução**

Acerte o tamanho do campo FKF\_CNAE via configurador com base no campo da tabela CC3, que é a tabela de **CNAE** (**FATA500**).
