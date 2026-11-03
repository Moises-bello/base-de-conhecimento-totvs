---
content_hash: cdbecf758374588b0cfe0659a08d6f7951f0a8563e54deb9b13a83c55b54f7d6
fetched_at: '2026-06-29T00:06:06.992654+00:00'
page_id: '201734161'
product: rm
source: tdn-rm
title: TTDWRL_DT_Rescisao_Complementar_Dissdio_INSS13o
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDWRL_DT_Rescisao_Complementar_Dissdio_INSS13o
version: 1
---

# RESCISÃO COMPLEMENTAR POR DISSIDIO LANÇANDO INSS 13o.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Quando é gerada uma Rescisão Complementar por dissídio, o INSS 13o. é lançado no evento de CC 108 - INSS DE DIFERENÇA SALARIAL 13o.SALÁRIO.*  *Porém no caso de já ter descontado o valor do teto no INSS 13o. da rescisão original, e assim não ter nenhum valor de diferença a ser descontado no evento de CC 108, está sendo lançado indevidamente o evento de CC 103 - INSS 2ª PARCELA 13º SALÁRIO.* |
| **Solução/Implementação:** | *Ajustar no processo da Rescisão Complementar para nunca lançar o evento de CC 103 - INSS 2ª PARCELA 13º SALÁRIO, quando a geração for por dissídio.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDWRL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
