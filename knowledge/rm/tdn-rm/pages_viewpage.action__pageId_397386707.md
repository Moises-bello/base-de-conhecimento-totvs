---
content_hash: 94c16e8ac06263b50b2dea7bef6ef005a0b2894339319430d63100cce885420c
fetched_at: '2026-06-29T00:09:10.462943+00:00'
page_id: '397386707'
product: rm
source: tdn-rm
title: DT Integração via mensagem única não considerar máscara do código do produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=397386707
version: 2
---

# RECEBIMENTO MENSAGEM ITEM

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cadastro de Produto. |
| **Situação/Requisito:** | Nas integrações quando o BackOffice é Protheus o Produto é incluído no RM via mensagem única. Quando o Código do Produto não utilizar máscara e possui caractere de espaço no conteúdo do código, é apresentado mensagem de consistência **Código do produto não está de acordo com a máscara**. |
| **Solução/Implementação:** | Ao gravar um Produto, caso esta ação tenha sido realizada via EAI (recebimento de mensagem) e a máscara do código do produto possuir caracteres "**QQQQQQQQQQQQQQQ**", a consistência de máscara do código do produto não será aplicada. |
| **Tickets relacionados:** | MATESTCNTFTOF01-3275 |
| **Requisito:** | EstPrdAction. |
