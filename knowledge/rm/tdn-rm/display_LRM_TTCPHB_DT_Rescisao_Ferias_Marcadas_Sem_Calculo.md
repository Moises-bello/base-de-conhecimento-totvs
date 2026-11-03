---
content_hash: 32766779ee4018b1402ac1567753a50189952f04c7de0e33811df916a25ee3f4
fetched_at: '2026-06-29T00:06:06.813398+00:00'
page_id: '201732036'
product: rm
source: tdn-rm
title: TTCPHB_DT_Rescisao_Ferias_Marcadas_Sem_Calculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCPHB_DT_Rescisao_Ferias_Marcadas_Sem_Calculo
version: 1
---

# RESCISÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | *Ao calcular rescisão para funcionário com férias programadas para competências posteriores, o sistema apresenta mensagem de erro e não calcula a rescisão.* |
| **Solução/Implementação:** | Não exibir o erro no processo de cálculo, apenas caso as férias estejam com a situação "Marcadas" e nenhum cálculo destas férias tenha sido feito. |
| **Chamados relacionados:** | TTCPHB |
| **Versões/Release:** | *12.1.8* |
