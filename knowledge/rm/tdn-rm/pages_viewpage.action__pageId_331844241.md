---
content_hash: 3bd0efe633261c47ee2e7bf80adf2aa0f2d435ab98bfab5ad85b9a70418b10fd
fetched_at: '2026-06-29T00:08:49.560758+00:00'
page_id: '331844241'
product: rm
source: tdn-rm
title: DT Férias Globais - Dias de Direito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331844241
version: 3
---

# Criado Parâmetro para Conceder a Quantidade de Dias de Direito em Férias Globais

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | Férias Globais |
| **Solução/Implementação:** | Foi implementado um parâmetro para conceder a quantidade de dias de direito na marcação de Férias Globais. |
| **Requisito:** | [FOPCALCULO01-1736](http://jiraproducao.totvs.com.br/browse/FOPCALCULO01-1736) |

Foi implementado um parâmetro, para que, na marcação de férias globais, cada funcionário que não tiver direito ao total de dias de férias informado na tela, seja considerado apenas a quantidade de dias que ele tem direito.

Acessando **Folha de Pagamento | Férias | Coletivas Globais**, no cadastro foi criado o parâmetro **Limita aos Dias de Direito**;

Neste caso, o funcionário selecionado tem direito a 10 dias somente.

No log de cálculo, é informado que o funcionário não tem os dias necessários, então foi diminuído os dias de gozo;

E no cadastro das férias, os dias de férias, ficou conforme o funcionário tem disponível:
