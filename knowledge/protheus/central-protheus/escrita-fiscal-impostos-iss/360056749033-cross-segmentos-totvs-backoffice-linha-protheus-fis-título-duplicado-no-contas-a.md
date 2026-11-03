---
article_id: 360056749033
category: Escrita Fiscal - Impostos - ISS
content_hash: c26801c857705fbbf29a586b4c31b14bf41efa90710397390782207063593ac5
fetched_at: '2026-06-28T22:39:35.260173+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Título duplicado
  no contas a pagar após confirmar a apuração do ISS (MATA954)
type: support-article
updated_at: '2024-07-24T11:42:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056749033-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-T%C3%ADtulo-duplicado-no-contas-a-pagar-ap%C3%B3s-confirmar-a-apura%C3%A7%C3%A3o-do-ISS-MATA954
---

**Dúvida**Após finalizar a apuração o título do ISS está duplicando no meu contas à pagar, qual a provável causa?  
  
**Ambiente**Protheus – Faturamento – A partir da versão 12.1.17.  
  
**Solução**Verifique a sua apuração se o campo descrição (aba - Por Municípios - Saídas) se o conteúdo está vazio:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092799634/mceclip0.png)

Caso esteja vazio, localizei o fornecedor da Prefeitura destacado no parâmetro MV\_MUNIC ou MV\_FPADISS.

Visualize o fornecedor e confirme se os campos abaixo está devidamente preenchidos:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095019953/mceclip1.png)

Caso o fornecedor utilizado não esteja devidamente configurado, o sistema pode perder a função/validação e duplicar os títulos no financeiro.
