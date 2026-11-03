---
content_hash: 09f315b9b12abc1193e0958d1860806d861435351a03602e8fd5d20634ca1a27
fetched_at: '2026-06-29T00:08:35.357745+00:00'
page_id: '279590958'
product: rm
source: tdn-rm
title: 874941 FOPCALCULO01-370 DT lançamento de férias quando integrado com (SIGAMNT)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=279590958
version: 106
---

# Lançamento de Férias quando Integrado com (SIGAMNT)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Lançamento de férias. |
| **Situação/Requisito:** | Ao realizar o Cálculo de Férias ou Recisão de Funcionário está disparando mensagem para o Protheus automaticamente (sem utilizar FV).   O cliente precisa que seja enviado somente através de FV porque não são todos os funcionários que vão ser integrados. |
| **Solução/Implementação:** | Premissa: Integração 1001 (BackOffice RM x SigaMNT) habilitada e entidade EMPLOYEE mapeada     ``` Parametrizador:Folha de Pagamento > Integrações > Outros BackOffice ```  * Criado o parâmetro: Utilizar Fórmula Visual em Integração (SIGAMNT)   Obs.: Com o parâmetro marcado a mensagem "EMPLOYEE" será disparada pelo gatilho definido na fórmula visual. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | [874941](https://totvssuporte.zendesk.com/agent/tickets/874941 "Open ticket in Zendesk Support") |
| **Requisito:** | FopFuFeriasPerAction |

divs
