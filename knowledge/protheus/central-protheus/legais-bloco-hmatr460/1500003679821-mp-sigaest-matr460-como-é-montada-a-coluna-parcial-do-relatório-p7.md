---
article_id: 1500003679821
category: LEGAIS - BLOCO H/MATR460
content_hash: 11d2832b499aa991d54d3d13540a8dee7cb0f6fbcd22cbd5178c46ba66eec360
fetched_at: '2026-06-28T22:42:15.210100+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: MP - SIGAEST - MATR460 - Como é montada a coluna "Parcial" do relatório P7?
type: support-article
updated_at: '2021-06-14T14:43:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003679821-MP-SIGAEST-MATR460-Como-%C3%A9-montada-a-coluna-Parcial-do-relat%C3%B3rio-P7
---

**Dúvida**Qual o significado da coluna "Parcial" no relatório MATR460 (P7)? Onde o sistema faz checagem para montar o valor impresso nesta coluna?  
  
**Ambiente**Microsiga Protheus - Estoque/Custos - A partir da versão 12.1.17

**Solução**

Para entendermos a coluna "Parcial", vamos abranger às demais colunas de Valores:

- A coluna "Unitário" representa o custo médio unitário do produto (campo B2\_CM1);

- A coluna "Parcial" representa o custo unitário por item classificado por categoria (processo, poder de terceiros, venda entre outros), apresentando o **custo total da movimentação** (D3\_CUSTO1).

- A coluna "Total"  é igual à somatória de todos os totais por grupo (seções).

Vamos a um exemplo abaixo onde temos:

Seção - Produto Intermediário (B1\_TIPO = PI)

Unitário: Custo unitário;

Parcial: Custo total (Qtde x Custo Unitário);

Total: Soma dos saldos Parciais.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003984021/mceclip1.png)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre o relatório MATR460 (P7)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)
