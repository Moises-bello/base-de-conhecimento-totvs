---
content_hash: 42481cf4f75a408e2ea3cfb1bd5ed826b2f164ddef710301c59604278b364446
fetched_at: '2026-06-29T00:08:58.878928+00:00'
page_id: '361448575'
product: rm
source: tdn-rm
title: 2872573 FINANCEIRO01-7027 DT Corrige geração de IPTE para banco Santander com
  tipo de carteira 101
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361448575
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Geração de IPTE |
| **Situação/Requisito:** | Ao executar a geração do IPTE para banco Santander, com cobrança Registrada, mas com Tipo de Carteira nulo, o IPTE é gerado com tipo de carteira 102. |
| **Solução/Implementação:** | Constatamos que o correto valor para o tipo da carteira, para cobrança registrada é o valor 101. A formação do IPTE foi corrigido. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 2872573 |
| **Requisito:** | FINTRF000134 |
| **Documento de Referência:** | Não se aplica |
