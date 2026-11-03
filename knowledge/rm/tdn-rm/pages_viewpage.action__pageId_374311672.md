---
content_hash: 5e0b6625e1e570075fc979d307ec6e0ae4ea1a6586297047354fa0548bc5e05c
fetched_at: '2026-06-29T00:09:01.628734+00:00'
page_id: '374311672'
product: rm
source: tdn-rm
title: 3099912 FINANCEIRO01-7628 DT Cancelamento de Baixa de Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=374311672
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | RM |
| **Função:** | Cancelamento de Baixa |
| **Situação/Requisito:** | Erro "Referência de objeto não definida para uma instância de um objeto" ao executar cancelamento de uma baixa de lançamento, quando o lançamento já teve mais de uma baixa parcial, e associado à última baixa há uma Nota de Crédito, e a baixa ocorreu por proporção. |
| **Solução/Implementação:** | Constatamos que a baixa da nota de crédito estava interferindo no processamento do estorno da baixa do item de baixa. O processo foi revisto para que o processamento ocorra sem falhas. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 3099912 |
| **Requisito:** | FIN000040 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | Não se aplica |
