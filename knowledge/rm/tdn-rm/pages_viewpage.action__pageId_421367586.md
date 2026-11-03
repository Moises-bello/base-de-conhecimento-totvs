---
content_hash: 1e6da30d77485535d88e1ff36e2cfe2c73addda5d7db7aa765291489e1ccf81c
fetched_at: '2026-06-29T00:09:13.539488+00:00'
page_id: '421367586'
product: rm
source: tdn-rm
title: 4088892 DEDUINTEGRACOES-3519 DT Baixa de lançamentos com bolsas condicionais
  e desconto por antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421367586
version: 2
---

# BAIXA DE LANÇAMENTOS COM BOLSAS CONDICIONAIS - DESCONTO POR ANTECIPAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Baixa de lançamentos |
| **Situação/Requisito:** | Ao baixar um lançamento com duas bolsas condicionais ou mais e desconto por antecipação, o sistema acusa erro de referência de objeto |
| **Solução/Implementação:** | O item de desconto por antecipação não estava sendo retornado corretamente na baixa de bolsas condicionais. Ajuste na baixa de bolsas condicionais quando o usuário muda o comportamento da bolsa para lançamentos já gerados, ou seja, muda uma bolsa de INCONDICIONAL para CONDICIONAL. Essa alteração do comportamento, fazia com que o sistema não encontrasse todas as bolsas condicionais na tabela SBOLSALANDESCPONTUAL, ocasionando um outro erro de referência de objeto. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A. |
| **Pacote:** | Informe o [linkdopacote] |
