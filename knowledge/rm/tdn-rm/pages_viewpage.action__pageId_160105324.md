---
content_hash: dda40bdf8868722e3e5107feca499ff98ca958c72a22e661c8cb92b4e6db740f
fetched_at: '2026-06-29T00:05:56.943771+00:00'
page_id: '160105324'
product: rm
source: tdn-rm
title: Após a importação de batidas vejo que as batidas estão sendo consideradas em
  Naturezas incorretas.Como proceder ?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=160105324
version: 4
---

| **Produto** | **RM** |
| --- | --- |
| **Sintoma** | **Após a importação de batidas vejo que as batidas estão sendo consideradas em Naturezas incorretas. Como proceder ?** |
| **Solução** | **Ao processar o menu de Importação de batidas selecione um dos parâmetros:**  **"Considerando o horário planejado": A importação levará em consideração o horário planejado para definir a natureza da batida.**  **Exemplo:**  **Planejado: 08:00 12:00 13:00 17:00**  **Realizado: 09:00             13:30 17:40**  **Durante a importação o sistema compara a batida realizada com planejado.**  **Análise: 13:30 é mais próximo de qual batida do horário?**  **Decisão: 13:00, e esta batida é uma entrada, então a natureza da batida de 13:30 será entrada.**  **"Considerando a jornada":  O sistema calculará a natureza das batidas conforme a jornada(s) planejada(s)  do funcionário.**  **Neste caso o sistema irá encontrar a jornada do dia que pode variar conforme batida de entrada e fará a mesma validação entre batidas da jornada encontrada e o executado.** |
