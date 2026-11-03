---
content_hash: 09b0df77bee469621eb94df4b30eb8c445d744488aecc41e02a77b079b3c7fce
fetched_at: '2026-06-29T00:06:25.867215+00:00'
page_id: '224449423'
product: rm
source: tdn-rm
title: TUBBVO_DT_ENVELOPE_DE_PAGAMENTO_PORTAL
type: documentation
url: https://tdn.totvs.com/display/LRM/TUBBVO_DT_ENVELOPE_DE_PAGAMENTO_PORTAL
version: 117
---

# ENVELOPE DE PAGAMENTO (PORTAL)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope de Pagamento (Portal)* |
| **Situação/Requisito:** | Foi alterada a forma como são filtrados os períodos dos envelopes de pagamento visualizados pelo portal, causando confusão para os clientes que já utilizavam a funcionalidade da forma antiga. Após a alteração, o parametrizador passou a funcionar da seguinte forma:   * O cliente parametriza Mês/Ano/Período inicial e final para: 01/2015 - 01 a 01/2016 - 02. O portal só exibirá os períodos 01 e 02 de todos os meses de 01/2015 a 01/2016. |
| **Solução/Implementação:** | Foi restaurada a funcionalidade antiga do parametrizador, funcionando da seguinte forma:   * O cliente parametriza Mês/Ano/Período inicial e final para: 01/2015 - 01 a 01/2016 - 02. O portal exibirá os períodos 01, 02, 03, 15, 20... de todos os meses de 01/2015 a 01/2016, onde serão exibidos apenas os períodos 01 e 02 do mês 01/2016 (pois o período final definido foi o 02 da competência 01/2016). |
| **Chamados relacionados:** | *TUBBVO* |

divs
