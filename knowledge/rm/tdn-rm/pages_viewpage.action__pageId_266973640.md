---
content_hash: d056a3d69d75ba3735f202970571a0be17099dcfef35eca1a54b85fc1b919254
fetched_at: '2026-06-29T00:08:18.896566+00:00'
page_id: '266973640'
product: rm
source: tdn-rm
title: TVVW71_DT_Módulo_de_Caixa-Baixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266973640
version: 110
---

# Módulo de Caixa - Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Módulo de Caixa - Baixa |
| **Situação/Requisito:** | Ao realizar a baixa de dois lançamentos via sessão de caixa gerando apenas um extrato para todos, o campo  IDSESSAO da tabela FXCX não está sendo alimentado. Quando é um extrato para cada lançamento este campo é  alimentado normalmente. |
| **Solução/Implementação:** | Otimização no processo de baixa de cheque com mais de um lançamento e extrato agrupado na Sessão de Caixa.  Agora o sistema preenche corretamente o campo IDSESSAO da tabela FXCX. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000223 |

divs
