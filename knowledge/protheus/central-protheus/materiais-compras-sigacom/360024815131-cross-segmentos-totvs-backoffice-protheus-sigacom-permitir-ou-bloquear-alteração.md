---
article_id: 360024815131
category: Materiais - Compras (SIGACOM)
content_hash: 5b7357942a0da3eae081f644809cbb0c1fda8f5e7a93b129fda79aae6b03d16b
fetched_at: '2026-06-28T22:41:10.165020+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Permitir ou Bloquear
  alteração do preço unitário informado no Pedido de Compras - MV_ALTPRCC
type: support-article
updated_at: '2023-08-15T18:06:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024815131-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Permitir-ou-Bloquear-altera%C3%A7%C3%A3o-do-pre%C3%A7o-unit%C3%A1rio-informado-no-Pedido-de-Compras-MV-ALTPRCC
---

**Dúvida**Permitir ou Bloquear alteração do preço unitário informado no Pedido de Compras - MV\_ALTPRCC

**Ambiente**Protheus - Compras - A partir da versão 11.80  
  
**Solução**

Como configurar se o preço unitário do produto pode ser alterado no registro da nf de entrada , na classificação da pré-nota ou na inclusão da autorização de entrega, mesmo quando os valores já foram informados no pedido compras, na autorização de entrega ou no contrato de parceria?

Este controle é efetuado pelo parâmetro **MV\_ALTPRCC** - Que permite configurar se o preço unitário do produto pode ser alterado no registro da entrada da Nota Fiscal, na classificação da Pré-Nota ou na Inclusão da autorização de entrega, mesmo quando os valores já forma informado no pedido de Compras.  
  
**Procedimento para alteração do parâmetro:**   
Acessar o Configurador através do **SIGACFG** -> Base de Dados -> Dicionário -> Base de Dados  -> Parâmetro, digitar **MV\_ALTPRCC**, alterar o conteúdo do parâmetro **MV\_ALTPRCC** para 0,1,2,3,4,5 e 6, conforme imagem abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023108932/mceclip0.png)**

* 0 - Desabilitado: o preço unitário do produto pode ser alterado em qualquer situação.
* 1 – Valida o preço informado no pedido de compras, ou seja, no registro da entrada da nota fiscal (rotina Documento de Entrada) ou na Classificação da Pré-Nota. Não permite alteração no preço unitário do produto quando relacionado a um pedido de compras.
* 2 – Valida o preço informado na autorização de entrega, ou seja, no registro da entrada da nota fiscal (rotina Documento de Entrada) ou na classificação da Pré-nota. Não permite alteração no preço unitário do produto quando relacionado a uma autorização de entrega.
* 3 – Valida o preço informado no pedido de compras e na autorização de entrega (ambos), no registro da entrada da nota fiscal (rotina Documento de Entrada)ou na classificação da Pré-nota. Não permite alteração no preço unitário do produto quando relacionado a um pedido de compras ou a uma autorização de entrega.
* 4 – Valida o preço informado no contrato de parceria, ou seja, na inclusão da autorização de entrega. Não permite alteração no preço unitário do produto relacionado ao contrato.
* 5 – Valida o preço informado no contrato de parceria e na autorização de entrega.
* 6 - Valida o preço informado no pedido de compras, na autorização de entrega e no contrato de parceria.

Abaixo consta exemplo do Help na validação do Contrato de Parceria, Classificação da Pré-Nota ou na confirmação do Documento de entrada.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098266693/mceclip1.png)
