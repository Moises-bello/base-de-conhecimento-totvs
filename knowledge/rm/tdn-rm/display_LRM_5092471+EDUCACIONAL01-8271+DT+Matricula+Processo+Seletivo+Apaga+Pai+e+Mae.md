---
content_hash: 12bb27870916bb22ed873a88ff2385c6ebdd6bc31602b148e8d37f86543758b0
fetched_at: '2026-06-29T00:10:13.412853+00:00'
page_id: '458753903'
product: rm
source: tdn-rm
title: 5092471 EDUCACIONAL01-8271 DT Matricula Processo Seletivo Apaga Pai e Mae
type: documentation
url: https://tdn.totvs.com/display/LRM/5092471+EDUCACIONAL01-8271+DT+Matricula+Processo+Seletivo+Apaga+Pai+e+Mae
version: 2
---

# MATRÍCULA PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Gestão Educacional. |
| **Função:** | Matrícula processo seletivo |
| **Situação/Requisito:** | Foi identificado que ao matricular um aluno através do processo seletivo RM, o sistema estava apagando os dados de pai e mãe da tabela SPESSOA. |
| **Solução/Implementação:** | Foi identificado que a situação ocorria pois o sistema não estava carregando os dados da tabela VFILIACAO, sem estes dados, o sistema entendia que o usuário não possuía dados de filiação e limpava os campos, sendo que o dados de filiação estavam preenchidos, foi feito o ajuste. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
