---
content_hash: 7a85bcae6e627f5ffd8f5d3ddb495271bd771cf205d249056f051200bb7540db
fetched_at: '2026-06-29T00:06:10.303940+00:00'
page_id: '203760787'
product: rm
source: tdn-rm
title: TTGKNX_DT_Histórico_Ensino_Superior_Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203760787
version: 1
---

# HISTÓRICO DO ENSINO SUPERIOR NO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Histórico do ensino superior no portal.* |
| **Situação/Requisito:** | *Cliente não utiliza a parametrização de liberação de notas e faltas pelo professor e mesmo assim não é possível ao aluno as notas pelo histórico no portal. Ao consultar o histórico com o usuário pelo sistema em análise curricular o sistema exibe corretamente as notas e faltas, porém quando o aluno consulta o histórico pelo Portal, as notas não são apresentadas. O fato ocorre pois não está marcado na etapa a opção de exibir no portal.* |
| **Solução/Implementação:** | **O erro em questão ocorre pois não está marcado na etapa final de notas e faltas o campo "Exibe no portal". Para o ajuste é necessário um script para atualizar todas as etapas finais de notas e faltas para que neste campo "Exibe no portal" (EXIBENAWEB, campo da tabela SETAPAS) seja atribuído o valor de "S".** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
