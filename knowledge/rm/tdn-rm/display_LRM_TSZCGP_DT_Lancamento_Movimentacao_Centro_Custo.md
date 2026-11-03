---
content_hash: 646705c1818583c011559946324ada999108b11edfe24c3dc1d5a7ae09e66114
fetched_at: '2026-06-29T00:06:03.172116+00:00'
page_id: '198950754'
product: rm
source: tdn-rm
title: TSZCGP_DT_Lancamento_Movimentacao_Centro_Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZCGP_DT_Lancamento_Movimentacao_Centro_Custo
version: 3
---

# ENVELOPE DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo por Centro de Custo* |
| **Situação/Requisito:** | *Ao realizar a distribuição por centro de custo quando é feito algum lançamento que teve com origem o centro de custo(Lançamento de Salário Composto por Centro de Custo), sistema faz com que tenha perda do valor real.*  *Exemplo:*  *Lançamento para o centro de custo 01.01 - 300,20 e 01.02 150,20*  *O valor total no envelope é 450,40 onde 300,20 é 66,651865% sobre o total, mas o sistema considera para o cálculo apenas 66,65%. Com isso a perda grandes de centavos para um centro de custo.*  *Se calcular 66,65% de 450,40 ficará: 300,19 (neste exemplo a diferença ficou pequena)* |
| **Solução/Implementação:** | *Foi aumentado o número de casas decimais que serão consideradas ao calcular o percentual sobre o valor total, aumento assim a precisão no calculo.* |
| **Conversores e Parâmetros:** | *-* |
| **Chamados relacionados:** | *TSZCGP* |
| **Requisito (ISSUE):** | - |
| **Versões/Release:** | *12.1.7* |
