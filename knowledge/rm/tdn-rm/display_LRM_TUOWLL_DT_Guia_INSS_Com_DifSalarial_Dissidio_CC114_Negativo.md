---
content_hash: 37bee1efd34a0427fcec92fd9353f9ddf53a39c362a57e94943bc269dd748d72
fetched_at: '2026-06-29T00:08:05.931364+00:00'
page_id: '236423246'
product: rm
source: tdn-rm
title: TUOWLL_DT_Guia_INSS_Com_DifSalarial_Dissidio_CC114_Negativo
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOWLL_DT_Guia_INSS_Com_DifSalarial_Dissidio_CC114_Negativo
version: 2
---

# GUIA DE INSS NÃO CONSIDERA VALOR NEGATIVO DO CC 114 APÓS DIFERENÇA SALARIAL POR DISSÍDIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Guia INSS* |
| **Situação/Requisito:** | *Na geração da Guia de INSS com cálculo de Diferença Salarial por Dissídio no mês, não está acumulando o evento de CC 114 - ESTORNO BASE INSS DISSÍDIO RET. FOLHA, quando o valor é negativo.*  *Neste caso, o valor negativo do CC 114 deve ser somado à Base de INSS, para que o total do mês não fique menor que a Base dos eventos da Folha Mensal.* |
| **Solução/Implementação:** | *Ajuste na Guia de INSS para somar o valor do evento de CC 114, quando este for negativo no envelope mensal do funcionário.* |
| **Chamados   relacionados:** | *TUOWLL, TUTXV9* |
| **Versões/Release:** | *11.82.44, 12.1.11* |
