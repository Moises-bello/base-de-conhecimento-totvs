---
content_hash: 0ccad287feabb3cbc122fd7b3908c5c656164f7f304c237563f070064dbd149a
fetched_at: '2026-06-29T00:06:24.037962+00:00'
page_id: '224110613'
product: rm
source: tdn-rm
title: TUBMAP_DT_Emprestimo_Duplicado_Recibo_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TUBMAP_DT_Emprestimo_Duplicado_Recibo_Ferias
version: 2
---

# VALOR DO EMPRÉSTIMO ESTÁ DUPLICANDO NO RECÁLCULO DO RECIBO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Férias* |
| **Situação/Requisito:** | *No Cálculo das Férias, quando está marcado o parâmetro "Desconta empréstimo de folha nas férias", o valor do evento de empréstimo é calculado corretamente.*  *Entretanto ao recalcular o recibo de férias o valor do evento fica duplicado.* |
| **Solução/Implementação:** | *Ajuste no Cálculo das Férias, ao efetuar o desconto de empréstimos, para sempre substituir o valor após o recálculo do recibo.* |
| **Chamados   relacionados:** | *TUBMAP, TUCGLQ* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
