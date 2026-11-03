---
content_hash: 74654fa06ed43212b3f5db3fa690324e5e01a8ef3dd3227c4d6cc47645cbc14b
fetched_at: '2026-06-29T00:08:43.777491+00:00'
page_id: '306841166'
product: rm
source: tdn-rm
title: 1280726 DEDUINTEGRACOES-658 DT Conversão de base de dados com integração Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=306841166
version: 3
---

# Validações RM Atualizador

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Validações do RM Atualizador |
| **Situação/Requisito:** | Ao executar o atualizador para a versão 12.1.17 ou 12.1.18 em uma base de dados que tenha integração com Protheus, porem utilizando a integração nova (folha, financeiro ou contabilidade) o sistema estava validando se os parâmetros da base de dados do Protheus estavam preenchidos. |
| **Solução/Implementação:** | Estes parâmetros devem ser requisitados somente se estiver habilitada a integração modelo antigo, portanto realizamos a evolução na validação para que seja aplicada somente quando for modelo antigo de integração com Protheus. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
