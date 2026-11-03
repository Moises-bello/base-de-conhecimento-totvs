---
article_id: 360048218733
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 69849de68bfe80e8d9e41f96986e4a5e8bc30daa58330c50c0ff93e848cc6a6a
fetched_at: '2026-06-28T22:38:38.432945+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Alteração do
  Pedido de Venda (MATA410) com ordem de produção vinculada
type: support-article
updated_at: '2024-01-08T13:25:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048218733-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Altera%C3%A7%C3%A3o-do-Pedido-de-Venda-MATA410-com-ordem-de-produ%C3%A7%C3%A3o-vinculada
---

**Dúvida**

Necessito de alterar a data de entrega do produto, mas o mesmo já tem Ordem de Produção.  
Quais as possibilidades existentes para que, em uma situação de exceção, seja possível a alteração ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Temos a seguintes situações a serem consideradas:

**1.** **Alteração de pedido com ordem de produção:**

Em situação de exceção ou contorno,  é possível alterar o conteúdo do parâmetro MV\_ALTPVOP para permitir a alteração do item do pedido com ordem de produção e, posteriormente, desabilitá-lo para que não haja alterações indevidas.

**2.** **Alteração de pedido com ordem de produção com faturamento parcial:**

Se o parâmetro **MV\_ALTPED** estiver configurado como **S**, para permitir a alteração, e se o item que foi alterado for o que estiver com ordem de produção, o sistema dará a mensagem informando que o item possui ordem de produção amarrada e deve verificar se a alteração na quantidade, TES ou data de entrega não irá alterar a programação planejada da ordem de produção, mas ele permite a alteração do item.  
  
Se for um item que não tenha Ordem de Produção, no mesmo pedido, poderá altera-lo normalmente, mesmo que no pedido tenha um outro item de ordem de produção.  
  
Se o parâmetro **MV\_ALTPED** estiver como **N**, e o item de ordem de produção estiver faturado, este item não poderá ser alterado, o sistema informará que você precisará alterar o **MV\_ALTPED**. Qualquer outro item sem faturamento ou com faturamento parcial que esteja no pedido de possui ordem de produção, poderá ser alterado sem restrições.  
  
Se o pedido for faturado total, com ordem de produção ou não, e o parâmetro **MV\_ALTPED** estiver igual a **N**, o sistema não permitirá nenhum tipo de alteração.

**Saiba mais**:

* [FAT0293 Ordem de Produção x Pedido de Vendas](https://tdn.totvs.com/x/YW52Hw)
* [Parâmetro MV\_ALTPED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025018113-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Par%C3%A2metro-MV-ALTPED)
