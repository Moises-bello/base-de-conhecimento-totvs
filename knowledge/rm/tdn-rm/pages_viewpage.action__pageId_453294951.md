---
content_hash: a1babde901559e97c4a35acadfad34583341b89ba938bbc7e2cece8012884e98
fetched_at: '2026-06-29T00:10:11.874014+00:00'
page_id: '453294951'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-26 DT - Erro ao inserir bolsa em período letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453294951
version: 4
---

# Erro ao inserir bolsa em período letivo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Bolsa em período letivo |
| **Situação/Requisito:** | O sistema permitia ao usuário buscar bolsas pertencentes a outros níveis de ensino diferentes do logado ao informar o seu código no lookup. Além disso, foi implementado o bloqueio do lookup correspondente ao período letivo, visto que está informação já está subentendida, uma vez que o cadastro de bolsas para período letivo é um anexo de período letivo. |
| **Solução/Implementação:** | Ajuste na consulta SQL adicionando clausura WHERE o nível de ensino da sessão do usuário logado.  Bloqueio de edição para o lookup de período letivo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
