---
content_hash: 0b7cada95d641d89c69c88729814a997617ce5984d790ac3d0914ed6699462f8
fetched_at: '2026-06-29T00:06:09.252040+00:00'
page_id: '203556140'
product: rm
source: tdn-rm
title: TTGMUY_DT_Desconto_Adiantamento_Pensao_Alimenticia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGMUY_DT_Desconto_Adiantamento_Pensao_Alimenticia
version: 2
---

# DESCONTO DO ADIANTAMENTO NO CÁLCULO DA PENSÃO ALIMENTÍCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Evento de CC 19 (Desconto do Adiantamento) está deduzindo da Base de IRRF do cálculo de Pensão Alimentícia.*  *Apesar do evento ser dedutível de IRRF, seu valor não pode ser abatido na Base porque o Provento de Adiantamento (CC 34) está em outro mês caixa.* |
| **Solução/Implementação:** | *Ajuste no cálculo da Pensão Alimentícia para não deduzir o valor do CC 19 (Desconto do Adiantamento) da Base de IRRF, mesmo que o evento esteja marcado como Dedutível de IRRF.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGMUY* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
