---
content_hash: 15f8f6de93119d1a70f9b4419ee39e6e8847be941cbbde4bedb182b985b36d77
fetched_at: '2026-06-29T00:08:30.252913+00:00'
page_id: '272414019'
product: rm
source: tdn-rm
title: 613513 MEDU-3117 DT Bolsa Retroativa Para Lançamentos Baixado com Boleto Código
  de Barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272414019
version: 113
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Inclusão de Bolsa Retroativa |
| **Situação/Requisito:** | Ao incluir uma bolsa retroativa para uma lançamento e boleto baixado o sistema está apresentando a mensagem de não conformidade abaixo.  *Lançamento de boleto com código de barras ou lançamento de boleto do tipo débito automático ou lançamento de boleto com nosso número gerado pelo banco* |
| **Solução/Implementação:** | Realizada uma evolução no serviço de bolsa retroativa para que o lançamento que receberá a bolsa retroativa não tenha seu boleto alterado, pois o mesmo já está baixado.  Como regra no processo de bolsa retroativa os boletos de lançamentos baixados, baixados parcialmente ou lançamentos em abertos e que o status do boleto seja diferente de “Não Remetido” não terão seus boletos modificados.  Este ajuste foi necessário em função da mudança de boleto registrado, pois a partir desta mudança os boletos originados do educacional passam a conter códigos de barra. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 613513 |
| **Requisito:** |  |

divs
