---
article_id: 360055836713
category: TAF - REINF
content_hash: 7e51bd4ae528ec8e5a92865f252bf209c0a311726f2b796e8f930c1d31ba8282
fetched_at: '2026-06-28T22:41:34.627978+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - ERP Protheus  x TAF Segregado
  - REINF
type: support-article
updated_at: '2023-03-31T17:05:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055836713-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-ERP-Protheus-x-TAF-Segregado-REINF
---

**Dúvida**Configuração para utilizar o ERP PROTHEUS com o TAF segregado para a EFD REINF.

**Ambiente**  
TAF – SIGATAF – A partir da versão 12.17  
  
**Solução**

Para identificação se o TAF é módulo ou segregado, o extrator usava uma funcionalidade de verificação da tabela de cadastro de complemento de empresa C1E.

Caso existisse ao menos uma filial configurada na C1E, o extrator entende o TAF como módulo e alimenta diretamente a tabela TAFST2.

Essa funcionalidade foi trocada pela configuração do parâmetro MV\_TAFGST2.

**Se MV\_TAFGST2 = F (false).**

- A extração ocorrerá com o uso da tabela TAFST1, entende-se TAF Segregado.

**Se MV\_TAFGST2 = T (true).**

- A extração ocorrerá sem o uso da tabela TAFST1, os dados são gerados diretamente na tabela TAFST2,

entende-se TAF como um módulo do Protheus.

ERP x TAF no mesmo banco de dados.

**Para criação manual do parâmetro**.

Nome: MV\_TAFGST2

Tipo: lógico

Descrição: Indica a integração do ERP diretamente na TAFST2.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093042953/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090917034/mceclip2.png)

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=563415222>
