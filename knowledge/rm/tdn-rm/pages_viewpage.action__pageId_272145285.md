---
content_hash: 8385ff54a33b3a03954557821e2be4d24002c9a6a627202ffc32125a32451bf1
fetched_at: '2026-06-29T00:08:29.415701+00:00'
page_id: '272145285'
product: rm
source: tdn-rm
title: 472782 MEDU-2891 DT Fechamento de Período Contábil - Performance
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272145285
version: 108
---

# Fechamento de Período Contábil - Performance

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Fechamento de Período Contábil |
| **Situação/Requisito:** | Cliente entrou em contato informando que ao executar o processo “Fechar Exercício Contábil” é apresentada a seguinte mensagem:   " Timeout expired. The timeout period elapsed prior to completion of the operation or the server is not responding. " |
| **Solução/Implementação:** | Melhoria em uma consulta feita para a tabela CCONT e melhoria de performance no processo que gera o Saldo Anterior.  Também foi identificado que a base de dados do cliente estava com um lançamento inconsistente (Lançamento com Partidas em Datas diferentes), o que impedia o Fechamento de Período concluir. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
