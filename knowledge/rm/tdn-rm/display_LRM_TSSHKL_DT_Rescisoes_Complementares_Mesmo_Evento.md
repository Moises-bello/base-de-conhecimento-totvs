---
content_hash: e0baadeb5245ba13b5b877cf2997dadeb82bec5bf671b4a4e8ad53953fe1c0f0
fetched_at: '2026-06-29T00:06:01.841811+00:00'
page_id: '198940951'
product: rm
source: tdn-rm
title: TSSHKL_DT_Rescisoes_Complementares_Mesmo_Evento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSSHKL_DT_Rescisoes_Complementares_Mesmo_Evento
version: 6
---

# Várias Rescisões Complementares com mesmo Evento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Quando são calculadas várias rescisões complementares lançando o mesmo evento, comissão por exemplo, não está sendo considerado o valor existente no envelope da rescisão complementar anterior.* |
| **Solução/Implementação:** | *Ajustar o cálculo da rescisão complementar para que, no momento de acumular os valores dos envelopes à partir da rescisão original, antes de efetuar o recálculo para apurar as diferenças, não deixar de somar também o valor existente no último periodo de rescisão complementar.*  *Na situação ocorrida no cliente, quando foi calculada a terceira Rescisão Complementar, efetuando o lançamento do quarto valor de comissão, só estava sendo considerado o valor existente no envelope da rescisão original mais o valor da primeira complementar calculada.*  *O valor de comissão do envelope anterior ao atual não era acumulado no valor total do evento.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSSHKL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40* |
