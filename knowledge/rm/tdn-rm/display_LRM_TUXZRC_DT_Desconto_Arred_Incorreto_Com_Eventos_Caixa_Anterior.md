---
content_hash: c4fb0e84b22c77ada08ea91ae70503d442a6fc4715cb4888f967951c9716c07c
fetched_at: '2026-06-29T00:08:07.873573+00:00'
page_id: '237394792'
product: rm
source: tdn-rm
title: TUXZRC_DT_Desconto_Arred_Incorreto_Com_Eventos_Caixa_Anterior
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXZRC_DT_Desconto_Arred_Incorreto_Com_Eventos_Caixa_Anterior
version: 5
---

# DESCONTO DO ARREDONDAMENTO ESTÁ FICANDO INCORRETO QUANDO EXISTEM EVENTOS COM CAIXA ANTERIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Arredondamento* |
| **Situação/Requisito:** | *Quando existe no envelope atual eventos com data de pagamento no mês caixa anterior, o valor do desconto do arredondamento, CC 21, está sendo calculado incorretamente.* |
| **Solução/Implementação:** | *Ajuste no cálculo do evento de CC 21, Arredondamento Desconto, quando existe no envelope atual eventos com data de pagamento no mês caixa anterior.* |
| **Chamados   relacionados:** | *TUXZRC, TUYPQ2, TUSW51, TUZJTG* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
