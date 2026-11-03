---
content_hash: 968aea0a972849d0fe91fd1270bca22fad51f900406fcf29a7a23e9ebc382c3c
fetched_at: '2026-06-29T00:06:02.805663+00:00'
page_id: '198948974'
product: rm
source: tdn-rm
title: TSUE66_DT_Ajuste_de_codigo_para_customizacao_12_1_7
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUE66_DT_Ajuste_de_codigo_para_customizacao_12_1_7
version: 3
---

# MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Matrícula.* |
| **Situação/Requisito:** | *Matrícula com erro impactando customização.* |
| **Solução/Implementação:** | *Remoção da propriedade DBS da classe EduHabilitacaoAlunoObj do assembly RM.Edu.Matricula.Server que fazia o chaveamento do DBS no sistema*  *nos testes unitários. Esta propriedade pode ser removida, uma vez que na Lib foi alterada a herança para o DBS ser uma interface e não mais uma*  *classe.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.7.* |
