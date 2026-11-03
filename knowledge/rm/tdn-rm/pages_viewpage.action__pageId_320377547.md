---
content_hash: 361c163bb2236c0a1d4eafc725d46967ac37d06bf47a8bfb021deb7c74e8f5ed
fetched_at: '2026-06-29T00:08:47.808664+00:00'
page_id: '320377547'
product: rm
source: tdn-rm
title: 756903 EDUCACIONAL01-235 DT função de fórmula BuscaCampoAvaliacao
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320377547
version: 3
---

# AJUSTE NA FUNÇÃO DE FÓRMULA BUSCACAMPOAVALIACAO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Função de fórmula BuscaCampoAvaliacao |
| **Situação/Requisito:** | Quando os campos da obrigatórios da função de fórmula BuscaCampoAvaliacao não eram inseridos na consulta SQL utilizada para carregar o contexto, o sistema emitia uma mensagem de “A fórmula Testing não pode ser executada! Referência de objeto não definida para uma instância de um objeto”. |
| **Solução/Implementação:** | Foi realizado um ajuste no método da fórmula BuscaCampoAvaliacao, para que, quando o usuário utilizar um contexto que não retorna todos os campos utilizados pela fórmula, o sistema não exiba a mensagem “A fórmula Testing não pode ser executada! Referência de objeto não definida para uma instância de um objeto”. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 756903 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
