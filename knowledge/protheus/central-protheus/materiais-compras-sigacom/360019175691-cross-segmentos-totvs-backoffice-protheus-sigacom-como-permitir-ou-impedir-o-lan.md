---
article_id: 360019175691
category: Materiais - Compras (SIGACOM)
content_hash: dd851502ffe5a51f52eee69c8c8c4526379233f40ba935d16bc291a4f663b60d
fetched_at: '2026-06-28T22:41:08.642485+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como permitir ou impedir
  o lançamento de um Documento de Entrada com pedidos bloqueados ?
type: support-article
updated_at: '2025-10-14T21:13:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019175691-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-permitir-ou-impedir-o-lan%C3%A7amento-de-um-Documento-de-Entrada-com-pedidos-bloqueados
---

**Dúvida**

Como permitir ou impedir o lançamento de um Documento de Entrada com pedidos bloqueados ?  
  
**Ambiente**

Protheus - Compras - A partir da versão 11   
  
**Solução**

Para que seja possível ou impedido efetuar o lançamento de um Documento de Entrada pedidos ainda bloqueados, ou seja, dar entrada em nota fical com pedido que ainda estão sem Aprovação por Alçadas, é disponibilizado o parâmetro ***MV\_RESTNFE*** (Indica se restringe o uso de pedidos bloqueados no recebimento de materiais) para devida configuração e permissão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097059094)

![1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24848423112343)

![20220630_081849.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7134394991895)

***Obs:***

Por Padrão do Sistema, estando com o MV\_RESTNFE pra permitir a utilização, e caso um pedido bloqueado que está para ser aprovado na rotina de LIberação de Documento MATA094, seja utilizado em um Decumento de Entrada, o Pedido tem seu status modifcado para "atendido", porém ele ainda permanecerá na rotiana de liberação aguardando para ser liberado.

Para que isso não aconteça, deve-se configurar o MV\_RESTNFE para não permitir utilização de Pedidos Bloqueados em NFs.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
