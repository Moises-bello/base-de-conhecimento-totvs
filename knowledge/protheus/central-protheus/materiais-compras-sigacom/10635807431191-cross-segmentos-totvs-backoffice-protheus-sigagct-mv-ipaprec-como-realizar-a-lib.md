---
article_id: 10635807431191
category: Materiais - Compras (SIGACOM)
content_hash: d92a770ec699ccb320fbc8cb8edfd9cfbc3e41fee28d9ed69cc8387907ab6aec
fetched_at: '2026-06-28T22:41:25.465929+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT -   MV_IPAPREC - Como
  Realizar a Liberação  dos Itens do Pedido  por Grupo de Aprovação ou por Documento
  na Alçada por entidade contábil?
type: support-article
updated_at: '2022-12-01T20:23:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10635807431191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-MV-IPAPREC-Como-Realizar-a-Libera%C3%A7%C3%A3o-dos-Itens-do-Pedido-por-Grupo-de-Aprova%C3%A7%C3%A3o-ou-por-Documento-na-Al%C3%A7ada-por-entidade-cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

MV\_IPAPREC - Como Realizar a Liberação  dos Itens do Pedido  por Grupo de Aprovação ou por Documento na Alçada por entidade contábil?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução:**

O parâmetro **MV\_IPAPREC** define se a liberação de Alçada para o Tipo de Documento Itens de Pedido deve ocorrer por Grupo de aprovação, permitindo assim o recebimento de Documentos de Entrada para os Itens Liberados, mesmo quando houver itens do pedido pendentes de aprovação. Para o processo de rejeição, bloqueio e estorno seguirá o mesmo conceito refletindo apenas para o grupo de aprovação envolvido no processo.

O parâmetro **MV\_IPAPREC** poderá ser configurado por Documento,  podendo ser configurado como .F. para que o documento seja aprovado somente quando todos os itens forem liberados ou com .T. por Grupo de Aprovação.

**Exemplo**

Pedido com 2 Itens, cada item com um Centro de Custo Diferente e Grupo de Aprovação Diferentes.

**MV\_IPAPREC = .F. – Libera por Documento**

Item 001 - centro de custo **14** - Grupo de Aprovação **000038** - Item 001 - Pendente de Aprovação Legenda Azul Bloqueado.

Item 002 - centro de custo **07** - Grupo de Aprovação **000037** - O Item 002- O item Foi aprovado e  e continua com a legenda Bloqueada, pois, com o parâmetro = .F. só será atualizado a legenda dos itens quando todos os itens forem aprovados devido a aprovação ser por Documento.

**MV\_IPAPREC = .T. – Libera por Grupo de Aprovação.**

Ao alterar o parâmetro para **MV\_IPAPREC = .T.**e realizar novamente a aprovação do item 002

Item 002 - centro de custo **07** - Grupo de Aprovação **000037** - O Item 002- Foi aprovado e sua legenda consta verde como Liberada, pois, a aprovação é por Grupo de Aprovação.

![Gifteste0112.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10634811760023)

***Saiba Mais :***

* [MV\_IPAPREC - Libera Itens de Pedido por Grupo de Aprovação](https://tdn.totvs.com/pages/releaseview.action?pageId=513426093)
* [Alçadas por Item de Pedido](https://tdn.totvs.com/pages/releaseview.action?pageId=513433386)
* [Alçadas - Itens de Pedido de Compra (IP) - Pedido de Compras.](https://tdn.totvs.com/pages/releaseview.action?pageId=544208912)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
* [MP - SIGACOM - MV\_IPAPREC - Como Vincular Pedido parcialmente Aprovado (com apenas alguns Itens aprovados) em Documento de Entrada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001343161-MP-SIGACOM-MV-IPAPREC-Como-Vincular-Pedido-parcialmente-Aprovado-com-apenas-alguns-Itens-aprovados-em-Documento-de-Entrada-)
