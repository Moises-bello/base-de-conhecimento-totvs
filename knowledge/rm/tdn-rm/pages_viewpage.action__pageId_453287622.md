---
content_hash: 81849d138a4dad1447bbb42ce3597b3fe6f2e497784eecadced509de9e78df2f
fetched_at: '2026-06-29T00:10:11.822484+00:00'
page_id: '453287622'
product: rm
source: tdn-rm
title: 4911440 FINANCEIRO01-10795 Baixa pagamento via cartão pelo Checkout Cielo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453287622
version: 2
---

# **BAIXA DE BOLETO**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa de boleto |
| **Situação/Requisito:** | Ao realizar o pagamento via cartão de crédito pelo Checkout da Cielo, o lançamento não foi baixado automaticamente, dessa forma, executamos o processo de Ajuste de Transação e o sistema gera o erro abaixo:  *Erro ao efetuar a baixa de Lançamento: Estouro de SqlDateTime. Deve estar entre 1/1/1753 12:00:00 AM e 31/12/9999 11:59:59 PM* |
| **Solução/Implementação:** | Otimizado o processo de baixa do boleto que não estava informando a data do sistema corretamente para o serviço de contabilização. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
