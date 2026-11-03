---
article_id: 360042569273
category: Faturamento - Cenários de Venda
content_hash: 5030ce3c50520912be8b0daf6f95a211fd3c4eaada9b65b9d40f7b3b66d9e498
fetched_at: '2026-06-28T22:38:34.055458+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Limite de Itens da tabela de preços (FWGRIDLINE)
type: support-article
updated_at: '2024-07-29T14:09:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042569273-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Limite-de-Itens-da-tabela-de-pre%C3%A7os-FWGRIDLINE
---

**Dúvida**

Como incluir mais de 9.999 itens na Tabela de Preços?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Solução**

Inclusão de item novo em tabela de preços com mais de 9.999 itens.   
  
Tabelas envolvidas: DA0 e DA1  
Rotina: OMSA010  
  
1) No módulo Faturamento acessar a tabela de preços (Cenário de Vendas - Tabelas de Preços);  
2) Digitar F12 no browse (dela anterior a incluir / alterar a tabela);  
3) Deixar o parâmetro Demonstrar por ? " Produto " e inserir o produto (que deve já estar cadastrado anteriormente na tabela de produtos - SB1);  
4) Clicar em Alterar;  
5) Na linha do item incluir qual a tabela de preços o produto deve ser incluído no campo Cod. tabela (DA1\_CODTAB)  
  
**Importante: Caso o F12 esteja para demonstrar por "Tabela" o sistema bloqueará a inclusão do novo item na tabela apresentando o Help FWGRIDLINE.**

Somente será permita a inclusão do novo item pelo processo mencionado acima.
