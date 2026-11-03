---
content_hash: cbf91cec359b6ab7e83c666d5da8ba2f319b3f97a01af5a86640f609df4a3f86
fetched_at: '2026-06-29T00:06:05.576100+00:00'
page_id: '201724620'
product: rm
source: tdn-rm
title: TSEUKN_DT_Ferias_Marcadas_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSEUKN_DT_Ferias_Marcadas_Rescisao
version: 2
---

# RESCISÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | *Ao calcular rescisão para funcionário com férias programadas para competências posteriores, o sistema apresenta mensagem de erro e não calcula a rescisão.* |
| **Solução/Implementação:** | Ajuste caso existam férias marcadas que ainda não tenham sido calculadas, elas serão excluídas e a rescisão será calculada normalmente. |
| **Chamados relacionados:** | TSEUKN |
| **Versões/Release:** | *11.82.41* |
