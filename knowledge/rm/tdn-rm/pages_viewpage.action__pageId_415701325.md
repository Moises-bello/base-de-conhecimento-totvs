---
content_hash: 2eb6c750cbd016016c3aeb27a8ca3a45b32d1e6f289ba95b1b61a389765ab89a
fetched_at: '2026-06-29T00:09:11.696257+00:00'
page_id: '415701325'
product: rm
source: tdn-rm
title: 3761833 FOPCALCULO01-4802 Diferença INSS de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415701325
version: 1
---

# INSS de Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Diferença de Férias |
| **Situação/Requisito:** | Ao fazer o cálculo da diferença de Férias, com a opção Dissídio Sim marcado, não está abatendo o valor do CC 3 no desconto de INSS de férias, sendo o mesmo descontado em duplicidade, no CC 3 e no CC 110. |
| **Solução/Implementação:** | ajuste no cálculo de diferença de férias afim de evitar que o código de cálculo 3 fosse descontado em duplicidade. Tratando o caso onde não atingiu o teto de INSS para deduzir o mesmo das verbas de INSS de férias. |
| **Tickets relacionados:** | 3761833 |
