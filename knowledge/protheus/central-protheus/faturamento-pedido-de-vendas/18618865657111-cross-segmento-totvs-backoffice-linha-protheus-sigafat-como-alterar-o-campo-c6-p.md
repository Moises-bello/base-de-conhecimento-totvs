---
article_id: 18618865657111
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 07e1ef5beb6bdd012cc714197e6ac7634fa9ebb6a5ee2c322e8e9a7110002574
fetched_at: '2026-06-28T22:38:42.456204+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Como alterar
  o campo C6_PEDCLI no Pedido de Venda gerado por Orçamento
type: support-article
updated_at: '2023-10-27T21:28:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18618865657111-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-alterar-o-campo-C6-PEDCLI-no-Pedido-de-Venda-gerado-por-Or%C3%A7amento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18618872609431) Tempo aproximado para leitura: **00:05:00 min****Dúvida:**Ao tentar alterar o campo **C6\_PEDCLI** no pedido de Venda gerado por orçamento o sistema não permite.  
  
**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.

**Solução:**

No padrão do sistema os campos **C6\_PEDCLI** e **CK\_PEDCLI** vem com o tamanho de 9 caracteres.

Ao alterar o tamanho do campo **C6\_PEDCLI** para um valor acima de 9 caracteres e não alterar o campo **CK\_PEDCLI**, quando se gera um pedido através da rotina de Orçamento de Venda, o sistema não irá permitir a alteração no campo **C6\_PEDCLI** para um valor maior do que o informado no orçamento.

Para que seja possível realizar a alteração no campo **C6\_PEDCLI** é necessário ajustar o tamanho do campo **CK\_PEDCLI** via configurador.

O ajuste dos campos deve ser feito pelo SIGACFG através das rotinas **SC6** e **SCK.**

**Veja também:**

**[Configurações e Campos para uso da Rotina Orçamento de Vendas (MATA415).](https://tdn.totvs.com/pages/releaseview.action?pageId=271168172)**
