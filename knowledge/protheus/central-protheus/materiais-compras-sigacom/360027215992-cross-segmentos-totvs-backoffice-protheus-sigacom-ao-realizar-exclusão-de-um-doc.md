---
article_id: 360027215992
category: Materiais - Compras (SIGACOM)
content_hash: 48b59984ea125d86a4991420ec37c8b4d01ff5ec9d2693152d156c9e885803d9
fetched_at: '2026-06-28T22:41:14.173486+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao realizar exclusão
  de um documento de entrada, o sistema apresenta a validação 'Help A103NEXCOR' 
type: support-article
updated_at: '2022-05-16T21:14:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027215992-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-realizar-exclus%C3%A3o-de-um-documento-de-entrada-o-sistema-apresenta-a-valida%C3%A7%C3%A3o-Help-A103NEXCOR
---

**Dúvida**Ao realizar exclusão de um documento de entrada, o sistema apresenta a validação 'Help A103NEXCOR'

**Ambiente**Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Esta validação ocorre, devido a existência de notas fiscais complementares vinculadas ao documento a ser excluído. Para localizar quais os documentos estão vinculados, siga o procedimento abaixo:

• Via opção no menu Consulta -> Cadastros -> Genéricos, tabela SD1, com o numero, série e fornecedor+loja localize o conteúdo nos campos: D1\_NFORI + D1\_SERIORI + D1\_FORNECE + D1\_LOJA;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000632381/mceclip0.png)

• Os registros encontrados referem-se a notas vinculadas ao documento que se está excluíndo;

• Após identificado o vínculo, será necessário excluir primeiramente os documentos complementares, para posteriormente excluir o documento desejado.

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
