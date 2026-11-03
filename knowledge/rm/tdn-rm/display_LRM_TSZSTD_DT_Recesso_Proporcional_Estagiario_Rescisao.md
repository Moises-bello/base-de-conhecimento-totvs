---
content_hash: 600682f9cb97fad6acd0aac3900ba9009d1b49ef4cbc5b3d95332d1ac6d51074
fetched_at: '2026-06-29T00:06:03.985917+00:00'
page_id: '200903866'
product: rm
source: tdn-rm
title: TSZSTD_DT_Recesso_Proporcional_Estagiario_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZSTD_DT_Recesso_Proporcional_Estagiario_Rescisao
version: 3
---

# RECESSO DE ESTÁGIO NA RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão de Estagiário* |
| **Situação/Requisito:** | *Quando está confirmado o parâmetro "Lança Recesso de Estagiário proporcional aos dias de cada competência" no Parametrizador, não está sendo calculado o evento de CC 334 - RECESSO DE ESTÁGIO PROPORCIONAL, no processo de rescisão.* |
| **Solução/Implementação:** | *Ajuste no processo de rescisão para que, quando o funcionário for um estagiário que não recebe verbas rescisórias, calcular corretamente o evento de CC 334 - RECESSO DE ESTÁGIO PROPORCIONAL, independente do parâmetro "Lança Recesso de Estagiário proporcional aos dias de cada competência" estar confirmado no Parametrizador.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSZSTD* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
