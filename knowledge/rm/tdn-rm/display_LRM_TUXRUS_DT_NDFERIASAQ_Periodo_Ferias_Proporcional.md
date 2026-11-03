---
content_hash: f5750632bb9109d8e5a09bca65731a67bed4511f6a215fd3e068a9dc17dfb08e
fetched_at: '2026-06-29T00:08:17.194154+00:00'
page_id: '253989123'
product: rm
source: tdn-rm
title: TUXRUS_DT_NDFERIASAQ_Periodo_Ferias_Proporcional
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXRUS_DT_NDFERIASAQ_Periodo_Ferias_Proporcional
version: 112
---

# FUNÇÃO DE FÓRMULA NDFERIASAQ NÃO ESTÁ CONSIDERANDO PERIODO DE FÉRIAS PROPORCIONAL NA RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | A função de fórmula NDFERIASAQ estava com comportamento diferente quando calculada na rescisão, e quando calculada na provisão de férias de demitido.  Na provisão considera o periodo aquisitivo vencido no CC 24 e o periodo aquisitivo proporcional no CC 25.  Já na rescisão estava considerando o periodo vencido nos 2 eventos, CC's 24 e 25. |
| **Solução/Implementação:** | Foi ajustado na rescisão para que a função NDFERIASAQ tenha o mesmo comportamento da provisão de férias de demitido no mês. |
| **Chamados relacionados:** | *TUXRUS* |

divs
