---
article_id: 360049161413
category: NFe - Nota Fiscal Eletrônica
content_hash: 10f4c03d1886b63bf454c708979dc543cbd49f4653cff1d3f0b17b2fe55cc09c
fetched_at: '2026-06-28T22:40:03.138599+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  029 : Falha de
  schema na Tag cmun'
type: support-article
updated_at: '2024-09-09T21:14:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049161413-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-cmun
---

**Dúvida**Como solucionar a falha de Schema referente a TAG cMUN ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- É necessário ajustar a informação no cadastro do cliente e a tag deve ser composta por 07 dígitos.

Se for cadastro de **cliente** preencher:

**A1\_EST** (dois primeiros digitos são representados pelo do cadastro do estado) e **A1\_COD\_MUN** (demais cinco próximos digitos do código do municipio)

Exemplo abaixo o código do municipio é **3550308** referente ao múnicipio de São Paulo, desta forma o preenchimento fica:

**A1\_EST** = SP

**A1\_COD\_MUN** = 50308

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26254404886295)

Se cadastro de fornecedor preencher:

**A2\_EST** (dois primeiros digitos são representados pelo do cadastro do estado) e **A2\_COD\_MUN** (demais cinco próximos digitos do código do municipio)

O padrão segue o mesmo abaixo o código do municipio é 3550308 referente ao múnicipio de São Paulo, desta forma o preenchimento fica:

**A1\_EST** = SP

**A1\_COD\_MUN** = 50308

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26254404887831)

2- Após isso, exclua a nota e gere novamente.

Dúvidas sobre o **Código de Município** podem ser esclarecidas no site do IBGE através do link:

<https://www.ibge.gov.br/explica/codigos-dos-municipios.php>

O código do estado fica gravado na tabela CC2.
