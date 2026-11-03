---
content_hash: 5cd9eeb6b93306097d556f334ec0c08039a46009f1d2d97fe71f728548a7840f
fetched_at: '2026-06-29T00:09:51.755514+00:00'
page_id: '437261334'
product: rm
source: tdn-rm
title: FINANCEIRO01-10013 DT Execução de Validações do Cancelamento de Baixa antes
  do Estorno de Transação Sitef
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=437261334
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Cancelamento de Baixa da Sessão de Caixa |
| **Situação/Requisito:** | Ao executar o cancelamento de uma baixa, que tenha uma transação SITEF, eventualmente é possível que a transação de cartão seja estornada, e ocorra um impedimento ao cancelamento da baixa no sistema, gerando situação de inconsistência. |
| **Solução/Implementação:** | Foi implementada a execução de todas as validações do cancelamento de baixa antes da execução do estorno da operação de cartão de crédito, minimizando a possibilidade de que exista um impedimento após o estorno de cartão de crédito. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | Não se aplica |
| **Requisito:** | FIN000225 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | 12.1.20, 12.1.21, 12.1.22, 12.1.23 |
