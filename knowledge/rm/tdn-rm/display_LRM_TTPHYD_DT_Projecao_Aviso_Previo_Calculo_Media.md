---
content_hash: 28618e75d6711c655194de1f65f60a51b20b97c83a1fbaf08d1f6464811fdab3
fetched_at: '2026-06-29T00:06:21.575219+00:00'
page_id: '223172355'
product: rm
source: tdn-rm
title: TTPHYD_DT_Projecao_Aviso_Previo_Calculo_Media
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPHYD_DT_Projecao_Aviso_Previo_Calculo_Media
version: 2
---

# DESCONSIDERAR PROJEÇÃO DO AVISO PRÉVIO NO CÁLCULO DE MÉDIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | *No cálculo da média de férias vencidas na rescisão está sendo considerado o periodo da projeção do aviso prévio indenizado, quando está marcado o parâmetro para considerar o mês atual.*  *Como se trata de um periodo em que o funcionário não trabalhou, não deve ser contabilizado no periodo de apuração das médias.* |
| **Solução/Implementação:** | *Ajuste no cálculo da média de férias vencidas na rescisão para desconsiderar o periodo da projeção do aviso prévio indenizado, nos meses de apuração das médias, mesmo quando é considerado o mês atual nas médias.* |
| **Chamados   relacionados:** | *TTPHYD* |
| **Versões/Release:** | *12.1.9* |
