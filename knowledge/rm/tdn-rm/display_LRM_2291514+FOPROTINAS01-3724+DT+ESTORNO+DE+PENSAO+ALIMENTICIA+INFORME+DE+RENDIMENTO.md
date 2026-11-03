---
content_hash: 6aae7d4e56bd0cd60b787597996aaf465b5c6ae697bbdf548f7940df2baaa711
fetched_at: '2026-06-29T00:08:52.404656+00:00'
page_id: '340362655'
product: rm
source: tdn-rm
title: 2291514 FOPROTINAS01-3724 DT ESTORNO DE PENSAO ALIMENTICIA INFORME DE RENDIMENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/2291514+FOPROTINAS01-3724+DT+ESTORNO+DE+PENSAO+ALIMENTICIA+INFORME+DE+RENDIMENTO
version: 1
---

# DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de pagamento. |
| **Função:** | Calculo e demonstração do estorno de pensão alimentícia nas informações complementares. |
| **Situação/Requisito:** | Informação do campo 3.4 do informe de rendimento não coincidindo com os valores do campo 7 informações complementares no informe de rendimento. |
| **Solução/Implementação:** | Foi identificado que a para demonstrar de forma coerente a ficha financeira com o movimento de pensão no campo 7 de informação complementar deverá:    No anexo de movimentação de pensão para os dependentes que tiveram estorno de pensão deverá:     1) O tipo de movimentação deverá ser coerente com o movimento da ficha financeira. No caso em questão tipo 4 diferenças de movimento;     2) Como se trata de estorno o valor lançado no movimento de pensão do dependente deverá ser negativo.    Nos parâmetros da DIRF na sub aba "Informações complementares" da aba "Campo 7 - Informações Complementares" o evento do estorno da pensão deverá ser incluído com o campo "Subtrair Valor" marcado.    O sistema foi adaptado para descontar o valor negativo do estorno de pensão no mês anterior no campo Campo 7 de informações complementares, assim como já era feito para o campo  "04 - Pensão Alimentícia (inf. beneficiário no campo 7)" no informe de rendimento. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 2291514. |
| **Requisito:** |  |
| **Documento de Referência:** |  |
