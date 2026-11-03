---
content_hash: 7c5f8aee56abb55e579e783871db38333240aa78e93323e3feaa49c35823989d
fetched_at: '2026-06-29T00:06:22.568029+00:00'
page_id: '223922543'
product: rm
source: tdn-rm
title: TTUMFV_DT_13o_SituacaoZ_Grade_Selecao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUMFV_DT_13o_SituacaoZ_Grade_Selecao
version: 1
---

# SITUAÇÃO Z NÃO DEVE APARECER NA GRADE DE SELEÇÃO DO LANÇAMENTO DE 13o. SALÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *13o.Salário* |
| **Situação/Requisito:** | *O módulo de lançamento de 13º salário está realizando o cálculo de 13º para funcionários com admissão no próximo mês.*  *A situação Z não deveria aparecer como opção de marcação na grade de seleção dos funcionários deste módulo.* |
| **Solução/Implementação:** | *Ajuste no lançamento da 2a.Parcela de 13o.Salário para somar os valores, quando o mesmo evento está cadastrado como Código Fixo e como Evento Adicional de 13o., e consequentemente decrementar o número de vezes no cadastro do Código Fixo.* |
| **Chamados   relacionados:** | *TTUMFV, TTZTQ0* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
