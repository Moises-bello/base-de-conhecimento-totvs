---
article_id: 360012068432
category: Materiais - Compras (SIGACOM)
content_hash: a262b015e3a195f113f37372417c305931fa7fb8474d4480fac08db6e7ffddf2
fetched_at: '2026-06-28T22:41:08.903884+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A103FRETE no Documento
  de Entrada (MATA103) / F1_TPFRETE não traz conteúdo do Pedido de Compra
type: support-article
updated_at: '2021-10-01T20:51:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012068432-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A103FRETE-no-Documento-de-Entrada-MATA103-F1-TPFRETE-n%C3%A3o-traz-conte%C3%BAdo-do-Pedido-de-Compra
---

**Dúvida**

O que pode causar a ocorrência do Help A103FRETE na inclusão de um Documento de Entrada ?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409830909335/mceclip0.png)

**Ambiente**  
Protheus – Compras – A partir da versão 11

**Ocorrência:**

O Help é apresentado quando o parâmetro MV\_VALFRET está como .F. fazendo a validação se no pedido de compras está a informação de tipo FRETE e com isso não permite alterar no documento de entrada.

**Solução**

O Conceito padrão do campo F1\_TPFRETE é ser preenchido somente quando não há pedido vinculado ao documento, pois o SPED Fiscal recupera a informação da tabela de pedido de compras (SC7), uma vez que é possível ter vários pedidos de compras aglutinados a um único documento de entrada.

Porém, caso deseje habilitar a alteração deste campo mesmo que existe um PC vinculado, você deve utilizar o parâmetro MV\_VALFRET, deixando como .T. para que a validação seja desabilitada. No entanto, é importante levar em consideração que poderão existir dois ou mais pedidos com o campo tipo de frete com conteúdos diferentes.

MV\_VALFRET:  
.F. = Não desabilita validação do sistema (Continua a bloquear o campo quando a NF for amarrada com o PC).  
.T. = Desabilita validação e permite alterar o conteúdo do campo TIPO FRETE (F1\_TPFRETE)**.**

Exemplo:

Para que seja considerada a informação no Documento de Entrada, deve ser configurado o parâmetro MV\_VALFRET como .T..

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008636151/1.png)

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008636171/2.png)

***Saiba Mais :***

[MV\_VALFRET - Criação do Parâmetro](http://tdn.totvs.com/pages/releaseview.action?pageId=36309576&preview=%2F36309576%2F36438558%2FCOM_BT_Criacao+do+Parametro+MV_VALFRET_TFLWD9.pdf)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
