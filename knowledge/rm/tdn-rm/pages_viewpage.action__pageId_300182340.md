---
content_hash: da1036a6047be5d6b7f9e8bced3d951cd1383c2e68118a5d09bf5ba79fbba68e
fetched_at: '2026-06-29T00:08:42.876844+00:00'
page_id: '300182340'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-517 DT Regeração de lançamento finalizada com sucesso, porem
  os lctos não estão sendo atualizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=300182340
version: 100
---

# Regeração de lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Geração de lançamento |
| **Situação/Requisito:** | Dois lançamentos de contratos distintos foram gerados agrupados em um único boleto de forma correta. Em seguida foi incluída a mesma bolsa, para a mesma parcela, nos dois contratos e o processo de geração de lançamentos foi executado novamente.  O processo foi finalizado com sucesso e no LOG foram apresentadas informações de sucesso, porém, ao consultar os lançamentos gerados, verificamos que as bolsas não foram incluídas. |
| **Solução/Implementação:** | Melhoria no serviço de regeração de lançamentos  com boletos agrupados para que não seja apresentada nenhuma não conformidade quando regeramos simultaneamente todos os lançamentos.  Após regeração dos lançamentos, os valores de bolsas foram incluídos corretamente. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
