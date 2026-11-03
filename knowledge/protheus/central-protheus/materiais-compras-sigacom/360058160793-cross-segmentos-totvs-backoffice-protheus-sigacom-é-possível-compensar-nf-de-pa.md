---
article_id: 360058160793
category: Materiais - Compras (SIGACOM)
content_hash: cc54eec43187c9ab0863affdec314f8dc8f0bdf12b453bdbf7b8ae8ba1c751e8
fetched_at: '2026-06-28T22:41:17.465170+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível compensar
  NF de PA vinculado ao PC com processo Entrega por Terceiro ?
type: support-article
updated_at: '2022-05-16T21:42:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058160793-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-compensar-NF-de-PA-vinculado-ao-PC-com-processo-Entrega-por-Terceiro
---

**Dúvida**

É possível compensar NF de PA vinculado ao PC com processo Entrega por Terceiro ?  
  
**Ambiente**

Microsiga Protheus – Compras – A partir da versão 12  
  
**Solução**

Sim. O sistema faz a compensação automática conforme o exemplo a seguir:

SIGACOM > Atualizações > Administração de Compras > Entrega por Terceiros (**COMA001**)

No cenário abaixo o fornecedor é o 000004, e quem vai entregar é o 000001.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097864693/mceclip0.png)

***\*Mais detalhes sobre Entrega por terceiros [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980311-MP-SIGACOM-Processo-de-entrega-Por-Terceiros?source=search)***

SIGACOM > Atualizações > Administração de Compras > Pedido de Compras (**MATA120/MATA121**)

Deve conter a condição de paramento como adiantamento e o fornecedor 000004.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097865153/mceclip1.png)

Deve verificar se o Pagamento antecipado consta vinculado ao Pedido de Compras conforme imagem a seguir:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095561854/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097865733/mceclip3.png)

***\*Mais detalhes sobre vincular o adiantamento no PC [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151-MP-SIGACOM-INCLUIR-E-EXCLUIR-RELACIONAMENTO-DO-PAGAMENTO-ANTECIPADO-NO-PEDIDO-DE-COMPRAS)***

Em seguida acessar SIGACOM > Atualizações > Movimentos > Documento de Entrada (**MATA103**)

Com o Fornecedor 000001 no cabeçalho do Documento de Entrada consultar o Pedido do Fornecedor 000004.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097865873/mceclip5.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097865833/mceclip4.png)

Para consultar o título acesse SIGAFIN > Atualizações > Contas a pagar> Contas a pagar (**FINA050**)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097866533/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097867053/mceclip7.png)

***Saiba Mais :***

* [MP - SIGACOM - Pedido de Compra com PA em outra Moeda e Compensação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361432-MP-SIGACOM-Pedido-de-Compra-com-PA-em-outra-Moeda-e-Compensa%C3%A7%C3%A3o)
* [MP - SIGACOM - Documento de Entrada atrelado a título do tipo PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567072-MP-SIGACOM-Documento-de-Entrada-atrelado-a-t%C3%ADtulo-do-tipo-PA-)
* [MP - SIGACOM - Como Incluir ou Excluir o relacionamento do Pagamento Antecipado no Pedido de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
