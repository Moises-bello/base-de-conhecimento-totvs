---
content_hash: 57a6f60ffc38f54e5cf9cc4abc5b002b4d90f5635eacfff6f227c4736621f618
fetched_at: '2026-06-29T00:09:08.465606+00:00'
page_id: '389548489'
product: rm
source: tdn-rm
title: 2997431 FINANCEIRO01-8484 DT Ajuste de transação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389548489
version: 1
---

# Erro na comunicação ao conectar com a Cielo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Ajuste de Transação - CheckOut Cielo |
| **Situação/Requisito:** | Ao realizar o processo de Ajuste de Transação o sistema apresenta a mensagem de erro:  "Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host" |
| **Solução/Implementação:** | Aplicada o protocolo de segurança do TLS para TLS12 na comunicação com a Cielo.  System.Net.SecurityProtocolType.Tls12 |
| **Tickets relacionados:** | 2997431, 3554728, 3505373 |
| **Requisito:** | FIN000284 |
