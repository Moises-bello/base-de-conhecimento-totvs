---
content_hash: 1caea7cf832d1ff271abd4b206b365ad94ad5d5a13a9cc3760d83d8abdd31a90
fetched_at: '2026-06-29T00:08:19.298821+00:00'
page_id: '267780212'
product: rm
source: tdn-rm
title: TVVLGM_DT_Calculo_Ferias_Valor_Recibo_Diferente_Tabela_PFUFERIASRECIBO
type: documentation
url: https://tdn.totvs.com/display/LRM/TVVLGM_DT_Calculo_Ferias_Valor_Recibo_Diferente_Tabela_PFUFERIASRECIBO
version: 112
---

# FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias* |
| **Situação/Requisito:** | Ao calcular as férias de um funcionário que possui múltiplos vínculos o sistema mostra um valor de líquido de férias no recibo, no entanto o valor levado na tabela PFUFERIASRECIBO é diferente.  Exemplo:  Valor do recibo de férias: 19.961,26  Valor do campo LIQUIDO na tabela PFUFERIASRECIBO: 13.583,02 |
| **Solução/Implementação:** | *Ajuste para zerar o valor do IRRF de Pensão, quando este não for utilizado no recibo de férias.* |
| **Chamados relacionados:** | *TVVLGM* |

divs
