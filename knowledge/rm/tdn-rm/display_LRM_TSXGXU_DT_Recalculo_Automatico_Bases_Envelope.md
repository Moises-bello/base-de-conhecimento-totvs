---
content_hash: ae3e72f42ab57ba007958fab3663aa13a1183ef261b8faa8d71ebf7144917ce6
fetched_at: '2026-06-29T00:06:01.941982+00:00'
page_id: '198941938'
product: rm
source: tdn-rm
title: TSXGXU_DT_Recalculo_Automatico_Bases_Envelope
type: documentation
url: https://tdn.totvs.com/display/LRM/TSXGXU_DT_Recalculo_Automatico_Bases_Envelope
version: 4
---

# Envelope de Pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Recalculo de Bases* |
| **Situação/Requisito:** | ***Quando é feito alguma alteração manual no envelope e o usuário não recalcula as bases, fica inconsistente os eventos do envelope com o total das bases.*** |
| **Solução/Implementação:** | Para que as bases do envelope de pagamento estejam sempre integras com os valores dos eventos, a fim de não existir divergência de valores de bases na folha analítica com a aba incidência do envelope de pagamento.  Criado o parâmetro "Recalcular bases automaticamente no envelope" em Parametrizador / Folha Normal / Ficha Financeira. Quando alterado o envelope de pagamento e o parâmetro "Recalcular bases automaticamente no envelope" está marcado o sistema passa a calcular as bases automaticamente,  da seguinte forma:   1. Ao clicar em sim na mensagem: "Alguns valores do envelope foram alterados manualmente" o recalculo total é realizado e as bases são recalculadas. 2. Ao clicar em não na mensagem: "Alguns valores do envelope foram alterados manualmente" é recalculado somente as bases.   Para uma maior orientação ao usuário A mensagem abaixo foi altera quando o parâmetro 'Recalcular bases automaticamente no envelope' tiver sido marcado, a saber:  "Atenção! As bases serão recalculadas automaticamente.Alguns valores do envelope foram alterados manualmente.Confirma o recálculo geral do envelope para este funcionário?" |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSXGXU* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |

***Folha de Pagamento***
