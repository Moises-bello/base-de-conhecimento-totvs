---
content_hash: 8fd45ec45908ea1ad8611758154ee25ea235d32e2d7af53358648bc157ac28e7
fetched_at: '2026-06-29T00:09:54.286496+00:00'
page_id: '444601359'
product: rm
source: tdn-rm
title: FISCAL01-7349 DT Associação de lançamentos de saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444601359
version: 2
---

# Não associar devoluções de compra

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Associação de lançamentos de saída |
| **Situação/Requisito:** | O processo de Associação foi alterado para não associar saídas cuja CFOP seja de devolução, pois estas saídas não podem ser associadas as entradas mais recentes e sim à nota que está sendo devolvida. Neste caso a associação deverá ser executada manualmente pelo usuário.  Permitir a associação dos Lançamentos de entrada cuja a devolução dos itens já tenham ocorrido, para que seja possível restaurar a quantidade de produtos disponível para associação. |
| **Solução/Implementação:** | Não será possível associar lançamentos de saída de devolução automaticamente pelo processo de associação. Uma mensagem no log informativa foi adicionada neste caso.  Alteração no processo de associação de lançamentos da saída para considerar devoluções de venda, desde que tenha ocorrido a associação inversa manual, para contar como saldo de itens disponíveis para futuras associações.  Alteração do campo de "documento fiscal" de associação de itens, para que possa-se associar lançamentos de saída aos lançamentos de entrada. Alteração no processo de associação de lançamentos, ele poderá ser executado para lançamentos de saída, independente se a natureza for de ressarcimento de ST.  Alteração na exibição do menu de associação, antes o mesmo só era apresentado para exportação e ressarcimento. Agora ficará habilitado para todos os lançamentos. |
