---
article_id: 360058336413
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 81b338674c9cd6669f0641031cec9f870dd03ae461505279e27fdb1903228fd8
fetched_at: '2026-06-28T22:37:24.015301+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pedido de Compras gerado
  pelo Gestão de Contratros não pode ser Alterado ou Excluido
type: support-article
updated_at: '2022-05-19T21:31:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058336413-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pedido-de-Compras-gerado-pelo-Gest%C3%A3o-de-Contratros-n%C3%A3o-pode-ser-Alterado-ou-Excluido
---

**Dúvida**

Pedido de Compras gerado pelo Gestão de Contratos não pode ser Alterado ou Excluído

**Ambiente**

Protheus – Gestão de Contrato – A partir da versão 12.1.23

**Solução**

Por padrão os Pedidos de Compras gerados na Medição de Contratos não podem ser alterados ou excluídos para se manter a integridade do sistema conforme o que foi realizado na Medição do Contrato.

Caso tente-se excluir o alterar um Pedido de Compras nesta situação o sistema retorna o alerta abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095858574/mceclip0.png)

Para que o pedido seja excluído, ele não pode ter tido movimentações posteriores a sua inclusão pela medição, e estando desta forma, pode ser realizado o Estorno da Medição através do caminho a seguir Atualizações > Contratos > Nova Medição (**CNTA121**) > Outras Ações > Estornar:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098154073/mceclip1.png)

***Saiba Mais :***

*[Artigos Materiais - Gestão de Contratos -](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-) [(S](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)[IGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)*
