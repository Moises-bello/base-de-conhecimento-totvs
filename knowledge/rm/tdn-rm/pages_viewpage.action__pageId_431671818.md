---
content_hash: f68bbade99e3b94764e47e1ce5d54be154c14d307ea41f3d81a9585346579aeb
fetched_at: '2026-06-29T00:09:39.479409+00:00'
page_id: '431671818'
product: rm
source: tdn-rm
title: 4049118 FINANCEIRO01-9723 DT Atualização do Valor Disponível para Repasse conforme
  Baixa Parcial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431671818
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Repasse |
| **Situação/Requisito:** | Quando o lançamento a receber associado a um repasse tem um valor opcional (ou valor de integração), o cálculo do valor disponível para repasse fica incorreto, impedindo a baixa do(s) lançamento(s) a pagar. |
| **Solução/Implementação:** | Foi elaborado um novo modelo de cálculo. O valor disponível para repasse será proporcional à soma dos valores originais baixados, comparado ao valor original do lançamento a receber. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 4049118 |
| **Requisito:** | FINTRF000238 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | 12.1.20, 12.1.21, 12.1.22, 12.1.23 |
