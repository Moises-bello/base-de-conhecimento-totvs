---
content_hash: b4324ee4164561d23fe2650dfec978889ce893620a15286231c71df2e4136b61
fetched_at: '2026-06-29T00:08:51.050418+00:00'
page_id: '336400761'
product: rm
source: tdn-rm
title: 2166250 FINANCEIRO01-5209 DT Baixa de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336400761
version: 1
---

# Baixa de lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira. |
| **Função:** | Baixa de lançamentos |
| **Situação/Requisito:** | Ao baixar qualquer lançamento, é exibido o erro a seguir:  "A conexão de soquete foi descartada. Nome do objeto: 'System.ServiceModel.Channels.SocketConnection'." |
| **Solução/Implementação:** | No TOTVS Gestão Estoque Compras e Faturamento, foi adicionado mais três tipos primitivos de forma de pagamento, "TipoBoletoBancario", "SemPagamento" e "DuplicataMercantil. Dessa forma, foi necessário acrescentarmos esses três tipos primitivos ao enumerado financeiro que trata as formas de pagamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040. |
| **Documento de Referência:** | N/A. |
