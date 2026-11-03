---
content_hash: f018c6b7322fd55a781ef1154eef0f37cd1218813009cab2338d801c3e7c4db5
fetched_at: '2026-06-29T00:08:55.930347+00:00'
page_id: '351031667'
product: rm
source: tdn-rm
title: 1256708 EDUCACIONAL01-2284 DT Imprimir Relatório de MDI Antiga da Turma Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351031667
version: 1
---

# IMPRIMIR RELATÓRIO DE MDI ANTIGA DA TURMA DISCIPLINA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Imprimir relatório |
| **Situação/Requisito:** | Ao tentar gerar um relatório do gerador antigo no processo de "imprimir relatório", o sistema fica só executando e não concluí a geração. Porém, executando o mesmo relatório na mdi antiga o relatório é gerado instantaneamente. |
| **Solução/Implementação:** | Foi identificado que a tabela STURMADISC não foi definida como master no relatório e a rotina de geração de relatórios da turma/disciplina devem usar a STURMADISC como master, portanto, foi incluída uma validação na geração dos relatórios para verificar se STURMADISC é a tabela master. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
