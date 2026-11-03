---
content_hash: 23b8242d34dc45e3b2d3ff7df6e6124403cc8de983440f368738a13836d50fc2
fetched_at: '2026-06-29T00:08:39.409018+00:00'
page_id: '286019055'
product: rm
source: tdn-rm
title: 1184266 EDUCACIONAL01-1958 Gravação do código de pessoa na tabela de campos
  complementares
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286019055
version: 102
---

# CAMPOS COMPLEMENTARES - INSCRIÇÃO DE CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Processo Seletivo |
| **Função:** | Campos complementares - Inscrição de candidatos |
| **Situação/Requisito:** | Ao realizar uma inscrição de um candidato com campos complementares, o código da pessoa do candidato inscrito não é registrado na tabela. |
| **Solução/Implementação:** | Após a remoção do CODPESSOA da chave primária das tabelas, o código na tabela de campos complementares não era mais gravado.  Foi realizada uma alteração para que seja gravado o código de pessoa juntamente com a informação do campo complementar.  Caso seja uma inscrição em um novo portal, será grava do o código do usuário do Processo Seletivo. (CODUSUARIOPS). |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
