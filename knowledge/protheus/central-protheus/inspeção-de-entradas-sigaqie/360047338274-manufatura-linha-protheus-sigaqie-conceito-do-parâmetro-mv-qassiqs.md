---
article_id: 360047338274
category: Inspeção de Entradas (SIGAQIE)
content_hash: 36400f615dc38e399a1e4f2bbc1900a7fb76f0b64f0852b8040f00a4f5eae1bd
fetched_at: '2026-06-28T22:42:26.931219+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Conceito do parâmetro MV_QASSIQS
type: support-article
updated_at: '2024-06-19T18:33:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047338274-Manufatura-Linha-Protheus-SIGAQIE-Conceito-do-par%C3%A2metro-MV-QASSIQS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24294785955735) Tempo aproximado para leitura: **00:02:20 min**  
**Dúvida**Qual o conceito do parâmetro **MV\_QASSIQS - Situação de Produto X Fornecedor pode ter categoria Skip-lote total se o fornecedor não tiver nota de IQS**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**O parâmetro **MV\_QASSIQS** é utilizado em **relatórios** eindica se a situação **Produto x Fornecedor** pode ter categoria de **Skip-lote** **Total** se o fornecedor não tiver **nota de IQS**.   
  
Se o parâmetro estiver com conteúdo igual a **N**, a nota de **IQS do fornecedor** é verificada, caso não exista, a categoria do mesmo é alterada.  
  
A situação do fornecedor é informada na rotina **MATA061 - Atualização Produto x Fornecedor** no campo **Situação**.  
  
E na rotina **MATA020 - Fornecedores** é informada a nota de **IQS - Índice de Qualificação do Sistema da Qualidade do Fornecedor** na aba **Outros** no campo **Fator Aval**.  
  
**Importante**O parâmetro **MV\_QASSIQS** é utilizado nos relatórios:

* **QIER100 - Relatório de índice de qualidade do produto;**
* **QIER120 - Relatório índice de qualidade - Fornecedor x Produto;**
* **QIER130 - Relatório de índice de qualidade do Produto x Fornecedor;**
* **QIER140 - Relatório índices gerais de fornecimento;**
* **QIER300 - Relatório de índices acumulados por fornecedor.**
