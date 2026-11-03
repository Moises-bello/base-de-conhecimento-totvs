---
article_id: 360027019611
category: Materiais - Compras (SIGACOM)
content_hash: 27c59b1dc9c17b86d9fe81ddd72bd924f5eef5682d36f5b72e49d69bfc364708
fetched_at: '2026-06-28T22:41:10.473337+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Validação Preço Unitário
  - Devolução de Vendas no Documento de Entrada - Conceito MV_VLDPDEV
type: support-article
updated_at: '2022-05-16T21:00:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027019611-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Valida%C3%A7%C3%A3o-Pre%C3%A7o-Unit%C3%A1rio-Devolu%C3%A7%C3%A3o-de-Vendas-no-Documento-de-Entrada-Conceito-MV-VLDPDEV
---

**Dúvida**Validação Preço Unitário - Devolução de Vendas no Documento de Entrada - Conceito **MV\_VLDPDEV**

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**O parâmetro MV\_VLDPDEV permite validar se o preço unitário, informado nos itens dos documentos de entrada de devolução de venda, é igual ao preço unitário utilizado no documento  
origem. Ele pode ser configurado da seguinte forma:

 - **U (Unitário)**: preço unitário.  
-  **T (Total)**: saldo de valor a devolver, ou seja, através do saldo de valor total que pode ser devolvido (o valor total do item do documento de devolução deve ser menor ou igual ao valor do documento origem)

Importante: Na ausência do parâmetro, é mantida a validação padrão do sistema que corresponde a configuração igual a opção T.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026449872/Capturar.PNG)
