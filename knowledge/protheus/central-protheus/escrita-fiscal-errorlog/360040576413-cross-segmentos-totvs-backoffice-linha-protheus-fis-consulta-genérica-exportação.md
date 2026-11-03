---
article_id: 360040576413
category: Escrita Fiscal - Error.log
content_hash: 1a62c5363fe4be95343fb4d72acc83eacc31c5a917801e2e01acff97a51f35a8
fetched_at: '2026-06-28T22:39:32.823201+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Consulta Genérica
  - Exportação para XML
type: support-article
updated_at: '2021-07-08T12:50:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040576413-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Consulta-Gen%C3%A9rica-Exporta%C3%A7%C3%A3o-para-XML
---

**Dúvida**

Como gerar Consulta Genérica e fazer exportação para XML

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 12.0

**Documentação Totvs:**

Se uma consulta genérica gera um arquivo com mais de 50.000 linhas o arquivo não será mais aberto automaticamente.

Ele é gravado em partes dentro da pasta **temp** e uma mensagem é apresentada para o usuário, informando o local de gravação do arquivo.

[<https://tdn.totvs.com/pages/viewpage.action?pageId=507018521>]

**Solução:**

*Abrir o arquivo gerado manualmente, localizando a pasta indicada na mensagem gerada no sistema;*

**Exemplo:**

**1 - Clicar Exp. CSV**

**2 - Selecionar Formato XML**

**3 - \Users\USUARIO~\AppData\Local\Temp\   "**Significa a pasta temporária do usuário logado no momento da execução do relatório"

**4 - Navegar ate está pasta especifica e abrir o arquivo manualmente.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053169654/mceclip0.png)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054044513/mceclip1.png)**
