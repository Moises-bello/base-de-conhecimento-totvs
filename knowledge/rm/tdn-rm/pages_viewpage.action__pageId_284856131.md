---
content_hash: 5edb4d8c1d5acec04b4d42b49f6989621d159fb49944f69b9176c6a034c0666d
fetched_at: '2026-06-29T00:08:36.938653+00:00'
page_id: '284856131'
product: rm
source: tdn-rm
title: 945995 FINANCEIRO01-927 Integração Bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284856131
version: 102
---

# Integração Bancária

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Integração Bancária |
| **Situação/Requisito:** | Ao realizar a importação de um arquivo de retorno o sistema esta montando o log ordenando pelo STATUSCNAB deixando o log todo desordenado. |
| **Solução/Implementação:** | Otimização no processo de arquivo de retorno. Agora o sistema mantem a ordem de linha do arquivo quando não tiver no mesmo arquivo um registro para registrar e baixar. Quando acontecer de ter no mesmo arquivo um registro para registrar e baixar, o sistema irá separa-lo para executar-lo na ordem correta, primeiramente registra e logo após realiza a baixa. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000087 |

divs
