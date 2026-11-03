---
content_hash: 5178fc3ad15b9382d8f589c2bd36b26da9c33d438c9b9010942aeb3bc50d0b5e
fetched_at: '2026-06-29T00:06:17.657197+00:00'
page_id: '213983287'
product: rm
source: tdn-rm
title: TTRA12_DT_Erro_Estorno_Contabilização_Por_Competência_Novo_Modelo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=213983287
version: 2
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Gerar Contabilização por competência* |
| **Situação/Requisito:** | *Ao estornar a contabilização de um contrato no novo modelo, o sistema tenta editar a contabilização do contrato com o intuito de anular a operação contábil, porém como podem existir mais de uma contabilização por contrato, pode ocorrer do sistema tentar editar a contabilização de aumento ou redução com os dados da contabilização do contrato, causando violação de chave primária.* |
| **Solução/Implementação:** | *Foi realizada otimização do novo modelo de contabilização, permitindo ao sistema realizar o estorno corretamente para os contratos que tenham sofrido alteração ao longo de sua vigência.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *12.1.8* |
| **Versão Expedida:** | *12.1.8* |

divs
