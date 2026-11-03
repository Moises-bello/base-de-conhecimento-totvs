---
content_hash: 66d3d5752144f53d380adad3f164f9e10c18eee7b8678ecd0c6d1e60aa010b47
fetched_at: '2026-06-29T00:06:24.126757+00:00'
page_id: '224112573'
product: rm
source: tdn-rm
title: TUAZSG_DT_Finaliza_Ferias_CC44_Diferente_CC42
type: documentation
url: https://tdn.totvs.com/display/LRM/TUAZSG_DT_Finaliza_Ferias_CC44_Diferente_CC42
version: 2
---

# AO FINALIZAR FÉRIAS EVENTO DE CC 44 FICA DIFERENTE DO CC42

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Férias* |
| **Situação/Requisito:** | *No processo de Finalizar Férias, quando são partidas, o valor do evento de CC 44 - Férias Pagas no Mês Anterior, está ficando diferente do que foi lançando no evento de CC 42 - Férias próximo mês, na competência anterior.*  *A situação ocorre porque existem eventos adicionais de férias, parametrizados para serem lançados pro envelope no evento de CC 44.* |
| **Solução/Implementação:** | *Ajuste no processo de Finalizar Férias, para tratar a situação de existirem eventos adicionais de férias parametrizados para serem lançados no evento de CC 44 - Férias Pagas no Mês Anterior.*  *No caso de férias partidas, o valor do evento de CC 44 sempre deve conter o mesmo valor do evento de CC 42, lançado no primeiro mês das férias.* |
| **Chamados   relacionados:** | *TUAZSG, TUCNB2* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
