---
content_hash: b075ca63b5a209ea1b483559442c593be6962fc3a0de86396d1102ef41647cc6
fetched_at: '2026-06-29T00:08:04.709058+00:00'
page_id: '235578068'
product: rm
source: tdn-rm
title: TUPNHI_DT_SEFIP150_Nao_Leva_Funcionario_Tomador_SemCEI
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPNHI_DT_SEFIP150_Nao_Leva_Funcionario_Tomador_SemCEI
version: 2
---

# SEFIP 150 NÃO LEVA FUNCIONÁRIO VINCULADO A TOMADOR SEM CEI

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | *Na geração do SEFIP por tomador, com código de recolhimento 150, não está levando funcionários rateados em tomadores que não possuem a informação do CEI.* |
| **Solução/Implementação:** | *Ajuste no processo de geração do SEFIP, para tratar o erro ao selecionar o movimento rateado por tomador, que só considera tomadores com CEI.* |
| **Chamados   relacionados:** | *TUPNHI, TURRA8* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
