---
content_hash: 082877e864f5abeaef1f18f238a3f71ae4aa7087fabb21dd770e69cdeb203658
fetched_at: '2026-06-29T00:06:03.997827+00:00'
page_id: '200904023'
product: rm
source: tdn-rm
title: TTABQC_DT_Recesso_Prop_Estagiario_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTABQC_DT_Recesso_Prop_Estagiario_Rescisao
version: 1
---

# RECESSO DE ESTÁGIO NA RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão de Estagiário* |
| **Situação/Requisito:** | *Quando está confirmado o parâmetro "Lança Recesso de Estagiário proporcional aos dias de cada competência" no Parametrizador, não está sendo calculado o evento de CC 334 - RECESSO DE ESTÁGIO PROPORCIONAL, no processo de rescisão.* |
| **Solução/Implementação:** | *Ajustar no processo de rescisão para que, quando o funcionário for um estagiário que não recebe verbas rescisórias, calcular corretamente o evento de CC 334 - RECESSO DE ESTÁGIO PROPORCIONAL, independente do parâmetro "Lança Recesso de Estagiário proporcional aos dias de cada competência" estar confirmado no Parametrizador.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTABQC* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
