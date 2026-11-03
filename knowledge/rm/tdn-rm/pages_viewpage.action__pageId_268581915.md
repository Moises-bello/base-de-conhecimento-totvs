---
content_hash: 891a1461208a556e7975a6b01cd2859333daaea8f9448d32367668b37f21dd85
fetched_at: '2026-06-29T00:08:20.637543+00:00'
page_id: '268581915'
product: rm
source: tdn-rm
title: TWAOFM_DT_Fatura-Serviço_de_Inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268581915
version: 115
---

# Fatura - Serviço de Inclusão

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Fatura - Serviço de Inclusão |
| **Situação/Requisito:** | Ao utilizar WebService para a inserção de Fatura no financeiro caso seja passado no XML um lançamento que não  exista na base de dados o SoapUI retorna a mensagem abaixo: "Referência de objeto não definida para uma  instância de um objeto.". |
| **Solução/Implementação:** | Otimização do processo de inserção de Fatura no financeiro via WebSerivce. Agora o sistema valida primeiro se  o lançamento a faturar realmente existe na base. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000103 |

divs
