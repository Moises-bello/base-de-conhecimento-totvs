---
content_hash: e69e1807561c457f005eb9ea548b5d6fc05bc095579e1da612e65eafc6fc4559
fetched_at: '2026-06-29T00:08:07.270844+00:00'
page_id: '237376870'
product: rm
source: tdn-rm
title: TUWCA6_DT_Contabilizacao_Com_DifFerias_Gera_Valores_Multiplicados
type: documentation
url: https://tdn.totvs.com/display/LRM/TUWCA6_DT_Contabilizacao_Com_DifFerias_Gera_Valores_Multiplicados
version: 2
---

# CONTABILIZAÇÃO COM DIFERENÇA DE FÉRIAS NO MÊS GERA VALORES MULTIPLICADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Contabilização* |
| **Situação/Requisito:** | *Ao gerar a contabilização de eventos quando há diferença de férias no mesmo mês das férias, os valores estão sendo multiplicados pelo número de eventos de diferença.*  *Por exemplo, se existem 9 eventos de diferença no envelope, e o valor do evento de IRRF Férias é 200, está sendo contabilizado 200 \* 9 = 1800.* |
| **Solução/Implementação:** | *Ajuste no processo de contabilização quando há diferença de férias no mês, para gerar os valores corretos dos eventos no envelope.* |
| **Chamados   relacionados:** | *TUWCA6, TUXCVT* |
| **Versões/Release:** | *11.82.44, 12.1.11* |
