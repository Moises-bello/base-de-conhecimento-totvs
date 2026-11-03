---
content_hash: 2337ca3d7766b79cba4970291cf831ceb89280a03750457e7ae1b186f05ac387
fetched_at: '2026-06-29T00:06:21.971736+00:00'
page_id: '223908336'
product: rm
source: tdn-rm
title: TTURHZ_DT_Rescisao_Coletiva_Selecao_Funcionarios
type: documentation
url: https://tdn.totvs.com/display/LRM/TTURHZ_DT_Rescisao_Coletiva_Selecao_Funcionarios
version: 2
---

# SELEÇÃO DE FUNCIONÁRIOS NA RESCISÃO COLETIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Coletiva* |
| **Situação/Requisito:** | *No processo da Rescisão Coletiva não estão sendo selecionados registros com o campo RESCISAOCALCULADA igual a nulo.*  *Só considera a chapa quando esta coluna está com o valor zero.* |
| **Solução/Implementação:** | *Ajuste na seleção de funcionários da Rescisão Coletiva para considerar o campo RESCISAOCALCULADA = 0 ou RESCISAOCALCULADA = NULO.*  *O valor padrão desta coluna é zero, mas ocasionalmente pode conter nulo.* |
| **Chamados   relacionados:** | *TTURHZ, TTYMG8* |
| **Versões/Release:** | *11.82.43* |
