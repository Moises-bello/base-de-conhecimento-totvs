---
content_hash: b341e478d74c0fc5472bf88734e3040ea86b8ca9c019f881a3346b5af5d8eb64
fetched_at: '2026-06-29T00:06:01.448187+00:00'
page_id: '198938500'
product: rm
source: tdn-rm
title: TSSIMD_DT_Recalculo_Automatico_Bases_Envelope
type: documentation
url: https://tdn.totvs.com/display/LRM/TSSIMD_DT_Recalculo_Automatico_Bases_Envelope
version: 3
---

# Envelope de Pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Recalculo de bases* |
| **Situação/Requisito:** | *Recalculo de base de forma automática* |
| **Solução/Implementação:** | Para que as bases do envelope de pagamento estejam sempre integras com os valores dos eventos, a fim de não existir divergência de valores de bases na folha analítica com a aba  incidência do envelope de pagamento. A implementação abaixo se fez necessária.  Criado o parâmetro "Recalcular bases automaticamente no envelope" em Parametrizador / Folha Normal / Ficha Financeira. Quando alterado o envelope de pagamento e o parâmetro "Recalcular bases automaticamente no envelope" está marcado o sistema passa a calcular as bases automaticamente,  da seguinte forma:   1. Ao clicar em sim na mensagem: "Alguns valores do envelope foram alterados manualmente" o recalculo total é realizado e as bases são recalculadas. 2. Ao clicar em não na mensagem: "Alguns valores do envelope foram alterados manualmente" é recalculado somente as bases.   Para uma maior orientação ao usuário A mensagem abaixo foi altera quando o parâmetro 'Recalcular bases automaticamente no envelope' tiver sido marcado, a saber:   "Atenção! As bases serão recalculadas automaticamente.  Alguns valores do envelope foram alterados manualmente.  Confirma o recálculo geral do envelope para este funcionário?" |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** |  |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.39, 11.82.40* |
