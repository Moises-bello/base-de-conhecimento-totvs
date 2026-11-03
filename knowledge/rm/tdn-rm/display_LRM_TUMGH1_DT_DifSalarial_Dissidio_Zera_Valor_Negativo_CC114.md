---
content_hash: b0ba3791bb8b182e32e1f077052cbb2130b71ad6d7f359747ee8482de9d886c1
fetched_at: '2026-06-29T00:08:03.852078+00:00'
page_id: '235326490'
product: rm
source: tdn-rm
title: TUMGH1_DT_DifSalarial_Dissidio_Zera_Valor_Negativo_CC114
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMGH1_DT_DifSalarial_Dissidio_Zera_Valor_Negativo_CC114
version: 2
---

# NÃO PODE ZERAR VALOR NEGATIVO DO CC 114 NA DIFERENÇA SALARIAL POR DISSÍDIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | *Quando o parâmetro "Zerar evento de diferença quando o valor ficar negativo" está marcado, não pode zerar um eventual valor negativo do CC 114 - ESTORNO BASE INSS DISSÍDIO RET. FOLHA.*  *Se na diferença salarial por dissídio, o valor que estorna INSS for maior que o que incide, tem que lançar o valor negativo no CC 114 para zerar a base de INSS por dissídio no envelope da diferença.* |
| **Solução/Implementação:** | *Ajuste no cálculo da diferença salarial por dissídio para não considerar o parâmetro "Zerar evento de diferença quando o valor ficar negativo" no evento de CC 114, e assim manter o valor negativo do estorno de INSS.* |
| **Chamados   relacionados:** | *TUMGH1, TUPFLL* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
