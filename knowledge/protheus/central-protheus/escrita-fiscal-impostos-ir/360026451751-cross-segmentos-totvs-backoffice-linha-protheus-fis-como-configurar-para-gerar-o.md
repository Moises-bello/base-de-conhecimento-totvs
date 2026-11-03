---
article_id: 360026451751
category: Escrita Fiscal - Impostos - IR
content_hash: 367865df24b66c62f4dfc64ecc1558bce9b1d191a606b4e1b6cc836292ab9691
fetched_at: '2026-06-28T22:39:31.864785+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar
  para gerar o IR no contas à pagar em notas de saída? '
type: support-article
updated_at: '2021-06-17T13:16:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026451751-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-para-gerar-o-IR-no-contas-%C3%A0-pagar-em-notas-de-sa%C3%ADda
---

**Dúvida**

Na criação de um pedido de venda com IRRF, como faço para gerar no meu contas à pagar.  
  
**Ambiente**

Protheus – Faturamento – A partir da versão 11.80  
  
**Solução**

Para geração do IR via pedido de venda é necessário seguir o boletim técnico abaixo, contudo, alguns clientes precisam fazer a auto retenção, ou seja o responsável pelo recolhimento é do prestador do serviço, não do tomador.

Boletim com a configuração do IRRF: <http://tdn.totvs.com/pages/releaseview.action?pageId=47908805>

Para geração do IR via contas à pagar:

1- No cadastro do cliente configure os seguintes campos:

Recolhe IRRF (A1\_RECIRRF) = NÃO

2- Na natureza financeira, configure os seguintes campos:

Calcula IRRF (ED\_CALCIRF) = SIM

Porc IRRF (ED\_PERCIRF) = Alíquota desejada

Cod Retenção (ED\_CODRET) =  código do IRRF, exemplo: 1708 ou 8045

Recolhe IRRF (ED\_RECIIRF) = 3 - Cad. Cliente
