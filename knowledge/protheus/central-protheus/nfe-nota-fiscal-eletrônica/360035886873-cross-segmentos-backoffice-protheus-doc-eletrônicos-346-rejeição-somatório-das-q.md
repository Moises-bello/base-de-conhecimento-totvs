---
article_id: 360035886873
category: NFe - Nota Fiscal Eletrônica
content_hash: babe3fbd00d3918a52dc9e1e38e8bb26d3518f6162a18595697ec2c826e05938
fetched_at: '2026-06-28T22:40:01.394028+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 346 Rejeição :
  Somatório das quantidades informadas na Exportação Indireta não corresponde a quantidade
  total do item'
type: support-article
updated_at: '2021-08-10T14:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035886873--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-346-Rejei%C3%A7%C3%A3o-Somat%C3%B3rio-das-quantidades-informadas-na-Exporta%C3%A7%C3%A3o-Indireta-n%C3%A3o-corresponde-a-quantidade-total-do-item
---

**Dúvida**Como resolver a 346 Rejeição : Somatório das quantidades informadas na Exportação Indireta não corresponde a quantidade total do item  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O erro ocorre quando o valor da tag **<qCom></qCom>** está diferente do informado na tag **<qExport></qExport**> conforme o print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046101274/mceclip0.png)

Essas Tags devem ser preenchidas com o mesmo valor.

Neste exemplo o campo CDL\_QTDEXP estava com o valor divergente do informado na tag <qCom></qCom>, em caso de exportação indireta, este campo deverá ser informado.

Faça o preenchimento e então faça a transmissão da nota.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046960653/mceclip1.png)
