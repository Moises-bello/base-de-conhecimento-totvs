---
article_id: 4439840190999
category: Materiais - Compras (SIGACOM)
content_hash: 2b9151a361aece021d72955a6f9a646b70d9aeccfe196195226ee21433da95a8
fetched_at: '2026-06-28T22:41:17.441744+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível aprovar
  01 item do pedido de compras e rejeitar outro na aprovação por Entidade Contábil?
type: support-article
updated_at: '2022-02-17T20:36:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439840190999-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-aprovar-01-item-do-pedido-de-compras-e-rejeitar-outro-na-aprova%C3%A7%C3%A3o-por-Entidade-Cont%C3%A1bil
---

**Dúvida**É possível aprovar 01 item do pedido de compras e rejeitar outro na aprovação por Entidade Contábil com o mesmo Centro de Custo?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.  
  
**Solução**O sistema não irá atender o processo no padrão que é aprovar ou rejeitar o item do Pedido de Compras ou da Solicitação de Compras mesmo que seja da mesma entidade contábil, exemplo:  
  
**Pedido 001**

* item 001 **Centro de custo**01 - *aprovar*
* item 002 **Centro de custo** 01 - *rejeitar*

A utilização do parâmetro **MV\_IPAPREC** define se a liberação de alçada para o Tipo de Documento Itens de Pedido deve ocorrer por grupo de aprovação, permitindo assim o recebimento de Documentos de Entrada para os Itens Liberados, mesmo quando houver itens do pedido pendentes de aprovação. Para o processo de rejeição, bloqueio e estorno seguirá o mesmo conceito refletindo apenas para o grupo de aprovação envolvido no processo.  
Em outras palavras, não é necessário que o documento seja integralmente aprovado para vincular os itens já aprovado no documento de entrada.

Porém funcionará da seguinte maneira na rotina de Liberação de Documento (**MATA094**) quando posicionar no item 001 e clicar em aprovar será apresentado os itens 001 e 002 pois possuem o mesmo centro de custo, já os demais itens serão apresentados separados para aprovação devido o centro de custo ser distinto.  
  
**Pedido 002**  
*Aprovar/rejeitar*

* item 001 Centro de custo 01
* item 002 Centro de custo 01

*Aprovar/rejeitar*

* item 003 Centro de custo 02

*Aprovar/rejeitar*

* item 004 Centro de custo 03

***Saiba Mais :***

* [MV\_IPAPREC - Libera Itens de Pedido por Grupo de Aprovação](https://tdn.totvs.com/pages/releaseview.action?pageId=513426093)
* [Alçadas por Item de Pedido](https://tdn.totvs.com/pages/releaseview.action?pageId=513433386)
* [Alçadas - Itens de Pedido de Compra (IP) - Pedido de Compras.](https://tdn.totvs.com/pages/releaseview.action?pageId=544208912)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
* [MP - SIGACOM - MV\_IPAPREC - Como Vincular Pedido parcialmente Aprovado (com apenas alguns Itens aprovados) em Documento de Entrada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001343161-MP-SIGACOM-MV-IPAPREC-Como-Vincular-Pedido-parcialmente-Aprovado-com-apenas-alguns-Itens-aprovados-em-Documento-de-Entrada-)
