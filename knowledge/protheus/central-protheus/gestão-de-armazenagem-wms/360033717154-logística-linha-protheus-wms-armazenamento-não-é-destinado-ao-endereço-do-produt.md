---
article_id: 360033717154
category: Gestão de Armazenagem (WMS)
content_hash: 1423c3eac78cbc732530e4d569dd645796ad9f64faa603e3582ca081f6eaba8c
fetched_at: '2026-06-28T22:45:47.972695+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Armazenamento não é destinado ao endereço
  do produto
type: support-article
updated_at: '2024-01-30T00:11:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033717154-Log%C3%ADstica-Linha-Protheus-WMS-Armazenamento-n%C3%A3o-%C3%A9-destinado-ao-endere%C3%A7o-do-produto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)***Tempo aproximado para leitura: **00:01:18 min****Dúvida**Por que o armazenamento não é destinado ao endereço do produto?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) -  A partir da versão 12  
  
**Solução**No cadastro **Endereços - MATA015**, na aba **Wms**, há o campo **Cod. Produto - BE\_CODPRO** que se preenchido, fixa o produto a esse endereço.  
  
Quando o tipo de endereçamento da estrutura é diferente de **1- Endereços** vazios, na **Sequência Abastecimento - WMSA030**, o Sistema ordenará ou priorizará a busca do endereço por:  
**Endereço Ocupado + Movimentação Prevista + Ordem Zona + Ordem Produto + Distância Total + Código Endereço + Percentual Ocupação**.  
  
Já quando o tipo de endereçamento da estrutura é igual a **1 - Endereços** vazios, ordenará a busca do endereço por:  
**Ordem Zona + Ordem Produto + Endereço Ocupado + Movimentação Prevista + Distância Total + Código Endereço + Percentual Ocupação**.  
  
Caso o tipo de endereçamento da estrutura seja **2 - Endereços Parc. Cheios**, ou seja, diferente de endereços vazios, o **WMS - Warehouse Management System** primeiramente priorizará a busca de endereços ocupados, depois os endereços com movimentação prevista, na sequência ordenará pela zona de armazenagem e então, na quarta posição considerará o **endereço do produto - BE\_CODPROD**.
