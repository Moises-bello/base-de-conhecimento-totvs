---
content_hash: 3c8ffd7fa6dd2d7ee61e40bb9660d4dc07a865c2dfdc9e6c032979c7eea889f5
fetched_at: '2026-06-29T00:08:21.435521+00:00'
page_id: '268823965'
product: rm
source: tdn-rm
title: MEDU-395_DT_Lançamento-Importação_de_Arquivo_Texto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268823965
version: 112
---

# Lançamento - Importação de Arquivo Texto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Lançamento - Importação de Arquivo Texto |
| **Situação/Requisito:** | Ao importar um arquivo de lançamentos financeiros, quando o sistema não encontra o cliente/fornecedor  informado no arquivo, apresentando a mensagem abaixo informando a Linha errada:  Linha: 531 - Erro ao tentar importar o lançamento: o cliente/fornecedor "0-" não está cadastrado na base de dados. |
| **Solução/Implementação:** | Otimização no LOG do processo de importação de lançamento. Agora é apresentado corretamente a Linha do arquivo  do qual não foi possível encontra o cliente/fornecedor informado no arquivo. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000150 |

divs
