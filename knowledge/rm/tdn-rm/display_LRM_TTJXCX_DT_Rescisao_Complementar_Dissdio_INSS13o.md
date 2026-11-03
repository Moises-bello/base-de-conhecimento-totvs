---
content_hash: eb6e52cb868522f9621b3e4cd8bc1be2bbc36b723578b835c462d735cb211149
fetched_at: '2026-06-29T00:06:12.513020+00:00'
page_id: '205916488'
product: rm
source: tdn-rm
title: TTJXCX_DT_Rescisao_Complementar_Dissdio_INSS13o
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJXCX_DT_Rescisao_Complementar_Dissdio_INSS13o
version: 2
---

# RESCISÃO COMPLEMENTAR POR DISSIDIO LANÇANDO INSS 13o.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Quando é gerada uma Rescisão Complementar por dissídio, o INSS 13o. é lançado no envelope o evento de CC 108 - INSS DE DIFERENÇA SALARIAL 13o.SALÁRIO.*  *Porém no caso de já ter descontado o valor do teto no INSS 13o. da rescisão original, e assim não ter nenhum valor de diferença a ser descontado no evento de CC 108, está sendo lançado indevidamente o evento de CC 103 - INSS 2ª PARCELA 13º SALÁRIO.* |
| **Solução/Implementação:** | *Ajuste no processo da Rescisão Complementar para nunca lançar o evento de CC 103 - INSS 2ª PARCELA 13º SALÁRIO, quando a geração for por dissídio.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTJXCX |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
