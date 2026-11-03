---
article_id: 1500001343161
category: Materiais - Compras (SIGACOM)
content_hash: 519e6ae2a9607c5db71776e118850cbf0a32f4b91a57a2f2ffa1cf18b9d1f3a7
fetched_at: '2026-06-28T22:41:20.226080+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MV_IPAPREC - Como Vincular
  Pedido parcialmente Aprovado (com apenas alguns Itens aprovados) em Documento de
  Entrada ?
type: support-article
updated_at: '2022-05-18T21:05:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001343161-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MV-IPAPREC-Como-Vincular-Pedido-parcialmente-Aprovado-com-apenas-alguns-Itens-aprovados-em-Documento-de-Entrada
---

**Dúvida**  
MV\_IPAPREC - Como Vincular Pedido com Alçada parcialmente aprovado (com apenas alguns Itens aprovados) em Documento de Entrada ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

 O parâmetro MV\_IPAPREC define se a liberação de alçada para o tipo de documento "Itens de Pedido" (também conhecido como alçada por entidades contábeis) deve ocorrer por grupo de aprovação, permitindo assim o recebimento de Documentos de Entrada para os Itens Liberados, mesmo quando houver itens do pedido pendentes.

 Em outras palavras, não é necessário que o documento seja integralmente aprovado para vincular os itens já aprovado no documento de entrada.

**IMPORTANTE:** Esse parâmetro só funcionará caso os parâmetros MV\_APRSCEC e MV\_APRPCEC estejam ativos (Alçada por entidades contábeis), saiba mais clicando [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=544208912).

Abaixo exemplifico a utilização do parâmetro:

**Exemplo 1:**  
  
- Ao criar um pedido de compras com 2 itens, e **cada** item for destinado a um grupo de aprovação diferente:

   **Item                Grupo de aprovação                    Entidade contabil                    Status**        
- Item 1      -                00001      -                         (Centro de custos RH01)      -     Pendente;          
- Item 2      -                00002      -                          (Centro de custos TI02)        -    Aprovado;     
  
Com a utilização do parâmetro **MV\_IPAPREC** (conteúdo igual a .T.)**,** ao liberar apenas um deste item, será possível relaciona-lo no documento de entrada imediatamente **(Neste caso, o status do pedido de compras NÃO precisará estar "Aprovado" para permitir a utilização dele no documento de entrada);**  
  
Com parâmetro desativado (conteúdo igual a .F.), só será possível relacionar o pedido de compras no documento de entrada, quando **TODOS** os itens forem aprovados **(Neste caso, o status do pedido de compras PRECISARÁ estar "Aprovado" para permitir utilizar dele no documento de entrada);**  
  
**Exemplo 2:**  
  
- Ao criar um pedido de compras com 2 itens, e **ambos** itens forem destinado ao mesmo grupo de aprovação:  
  
   **Item                Grupo de aprovação                    Entidade contábil                    Status**        
- Item 1      -                00001      -                         (Centro de custos RH01)      -      Aprovado;          
- Item 2      -                00001      -                         (Centro de custos RH01)        -    Aprovado;    
  
Neste caso, não será possível escolher qual item aprovar (não existe aprovação parcial quando os itens estão em bloqueio no mesmo grupo de aprovação), pois ambos passaram pela aprovação ou rejeição juntos, desta forma, não entraremos no caso do exemplo 1, onde existem itens aprovados e pendentes no mesmo pedido de compras, ou seja, os itens serão aprovados/rejeitados ou ficaram pendentes no mesmo momento.

***Saiba Mais :***

* [MV\_IPAPREC - Libera Itens de Pedido por Grupo de Aprovação](https://tdn.totvs.com/pages/releaseview.action?pageId=513426093)
* [Alçadas por Item de Pedido](https://tdn.totvs.com/pages/releaseview.action?pageId=513433386)
* [Alçadas - Itens de Pedido de Compra (IP) - Pedido de Compras.](https://tdn.totvs.com/pages/releaseview.action?pageId=544208912)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
