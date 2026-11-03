---
content_hash: 84ce4f53e577c67458001c1a850ee639e1a94fafb177c2e7963b778de8f32f1a
fetched_at: '2026-06-29T00:06:22.264738+00:00'
page_id: '223911954'
product: rm
source: tdn-rm
title: TTWETE_DT_SEFIP115_Diferenca_Aviso_Previo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWETE_DT_SEFIP115_Diferenca_Aviso_Previo
version: 3
---

# DIFERENÇA DO AVISO PRÉVIO NO SEFIP 115

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | *Na geração do SEFIP 115 com envelope de Rescisão Complementar Normal (sem ser por Dissídio) não está somando os valores dos eventos de Diferença de Aviso Prévio Indenizado (CC 99) e Diferença de 13o.Indenizado (CC 98).* |
| **Solução/Implementação:** | *Ajuste na geração do SEFIP 115 para acumular o valor do CC 99 no campo 16 - Remuneração Sem 13o. (colunas 168 - 182) e do CC 98 no campo 17 - Remuneração 13o. (colunas 183 - 197).* |
| **Chamados   relacionados:** | *TTWETE, TTYQXR, TUDAQZ* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
