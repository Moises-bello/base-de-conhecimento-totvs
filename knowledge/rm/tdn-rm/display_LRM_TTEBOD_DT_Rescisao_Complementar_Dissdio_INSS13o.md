---
content_hash: a60fe9793062c279ed1c5f5e23ae8cb4bbdf9bc2304dd1a2b6716cc87a11137d
fetched_at: '2026-06-29T00:06:07.026927+00:00'
page_id: '201734347'
product: rm
source: tdn-rm
title: TTEBOD_DT_Rescisao_Complementar_Dissdio_INSS13o
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEBOD_DT_Rescisao_Complementar_Dissdio_INSS13o
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
| **Chamados relacionados:** | *TTEBOD* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
