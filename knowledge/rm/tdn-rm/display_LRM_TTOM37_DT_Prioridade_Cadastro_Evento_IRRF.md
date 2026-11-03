---
content_hash: 78b1551e4880bf36c1cad8fdb98664c2f04866779a35259ebfb3213960ac5f8d
fetched_at: '2026-06-29T00:06:20.253337+00:00'
page_id: '221550568'
product: rm
source: tdn-rm
title: TTOM37_DT_Prioridade_Cadastro_Evento_IRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOM37_DT_Prioridade_Cadastro_Evento_IRRF
version: 1
---

# PRIORIDADE NO CADASTRO DO EVENTO DE IRRF

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Eventos* |
| **Situação/Requisito:** | *Internamente no cálculo é utilizada a prioridade 83 para os eventos de IRRF.*  *Entretanto, no cadastro do evento está sendo informado o número 81 no campo prioridade.*  *Este conteúdo no cadastro é apenas informativo, e não influencia nos cálculos. Mas deve ser demonstrado o valor correto da prioridade utilizada internamente.* |
| **Solução/Implementação:** | *Ajuste no cadastro dos eventos que utilizam códigos de cálculo de IRRF para demonstrar a prioridade correta utilizada nos cálculos, com o número 83.* |
| **Chamados   relacionados:** | *TTOM37* |
| **Versões/Release:** | *12.1.9* |
