---
content_hash: b3fb6ebe80136fc52ed798c73124eea459af2af519b67e3faecc8c8e23b77524
fetched_at: '2026-06-29T00:09:01.731255+00:00'
page_id: '377325934'
product: rm
source: tdn-rm
title: 2982053 FINANCEIRO01-7715 DT Baixa integração protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=377325934
version: 1
---

# Ao realizar a baixa não é enviado histórico formatado.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | Ao realizar a baixa de lançamento financeiro no RM, a mensagem enviada para o Protheus não formatou os Mnemônicos parametrizados enviando as variáveis. |
| **Solução/Implementação:** | Ajuste no envio da mensagem de baixa do Protheus, agora o histórico do processamento da baixa passa pelo processamento de formatação de histórico se existir Mnemônicos. |
| **Tickets relacionados:** | 2982053 |
| **Requisito:** | FIN000040 |
