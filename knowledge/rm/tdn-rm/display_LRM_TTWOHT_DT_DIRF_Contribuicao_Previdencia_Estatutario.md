---
content_hash: 4ec8dbb9395818969021747f8a1859b84a86856a324a69f67540ff3ea4ac3617
fetched_at: '2026-06-29T00:06:21.748481+00:00'
page_id: '223179562'
product: rm
source: tdn-rm
title: TTWOHT_DT_DIRF_Contribuicao_Previdencia_Estatutario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWOHT_DT_DIRF_Contribuicao_Previdencia_Estatutario
version: 123
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | *Ao gerar a Dirf em arquivo, Informe de rendimentos e Dirf para conferência no caso de funcionário com evento de Contribuição à Previdência de Estatutário no envelope e evento cadastrado na aba Contribuição à Previdência de Estatutário na geração do arquivo Dirf, sistema não está deduzindo o valor corretamente da previdência.* |
| **Solução/Implementação:** | *Ajustado o cálculo da Contribuição à Previdência de Estatutário para abater o valor do INSS na competência.* |
| **Chamados relacionados:** | TTWOHT, TTXSC2 |
| **Versões/Release:** | *11.82.43,12.1.9* |

divs
