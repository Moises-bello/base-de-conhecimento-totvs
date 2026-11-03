---
article_id: 360025333074
category: NFe - Nota Fiscal Eletrônica
content_hash: 216658c1dbb5ab3de4c80ebf5a4b3304165a11c402a7a2cc92e0de8641e29731
fetched_at: '2026-06-28T22:40:06.620275+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a mensagem
  em informações complementares de Aproveitamento de Crédito do Simples Nacional ?
type: support-article
updated_at: '2025-06-17T11:59:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025333074-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-mensagem-em-informa%C3%A7%C3%B5es-complementares-de-Aproveitamento-de-Cr%C3%A9dito-do-Simples-Nacional
---

**Dúvida**Como gerar a mensagem em informações completares de Aproveitamento de crédito do Simples Nacional ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Preencher no TES o campo  **F4\_CSOSN "Campo Cod. Sit.** deve ser igual: **101, 201 ou 900**

![F4_CSOSN.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15621532011927)

2- Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar**MV\_CODREG** = **1 Simples Nacional;**

![MV_CODREG.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12204741289879)

* **Assim será gerada a mensagem:**

"Documento emitido por ME ou EPP optante pelo Simples Nacional."  
"Permite o aproveitamento do credito de ICMS no valor de R$ "  " corresponde a alíquota de " "% , nos termos do art. 23 da LC 123/2006."

O valor é gerado do campo **F2\_VALICM** e a alíquota do campo **D2\_PICM**

* **Diferente disso será gerada a mensagem:**

"Documento emitido por ME ou EPP optante pelo Simples Nacional. Nao gera direito a credito fiscal de IPI."

* **Saiba mais:**

A mensagem com **alíquota e valor** só devem ser gerada para os CSOSNs abaixo:

**101, 201, ou 900**

**Parecer da consultoria:**

Destaque do CSOSN no Danfe, verifique no link abaixo:

**[Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=532035306)**
