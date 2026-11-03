---
content_hash: e794afbb6add01694a209e683e134e03ea3b89590378a297b489c530ba4080b3
fetched_at: '2026-06-29T00:10:12.746763+00:00'
page_id: '454835772'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4327 -  Opção de exibição de nomes exibindo informações divergentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454835772
version: 2
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Impressão de relatório no contrato do aluno |
| **Situação/Requisito:** | Ao editar uma parcela do contrato, ao utilizar o recurso de "Visualizar nomes dos campos" para os campos"Competência" e "Valor", era informado que estas colunas pertenciam a tabela SCONTRATO ao invés de SPARCELA. A situação ocorria apenas em bases Oracle. |
| **Solução/Implementação:** | Ajuste na consulta SQL responsável por retornar parcelas,além de remoção de JOINs desnecessários com FLAN e SLAN. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** |  |
