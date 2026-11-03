---
article_id: 360051732854
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: db7e29acacfeb20f9d73e309a287e5a184a22cdbd2c3e93c29655fe5cbe02da3
fetched_at: '2026-06-28T22:42:46.969677+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Saldo inicial MRP com opcional
type: support-article
updated_at: '2021-07-29T13:38:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051732854-Manufatura-Linha-Protheus-SIGAPCP-Saldo-inicial-MRP-com-opcional
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como funciona o saldo inicial para produto com opcionais?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Quando o produto possui em sua estrutura opcionais o **MRP - Material Requiriments Planning** não traz o saldo inicial, pois o Sistema não sabe qual o opcional foi utilizado para aquele produto.  
Porém quando o produto possui **Opcional Default**o saldo inicial é trazido no **MRP** para a necessidade que utiliza esse opcional.  
  
**Exemplo**  
**Estrutura**Componente PRODUTO000284 - Grupo: 001 Opcional: 0001  
Componente PRODUTO000285 **-** Grupo: 001 Opcional: 0002

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083341673/mceclip2.png)

Saldo do PA - 20.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083342313/mceclip3.png)

Previsão de vendas e o **opcional 010001** selecionado.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082218214/mceclip4.png)

Produto com **Opcional Default PA**.

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083342873/mceclip5.png)**

Quando existe **Opcional Default** no **MATA010 - Cadastro de Produto**, o saldo existente em estoque será considerado para esse **Opcional**.  
  
Neste caso o **Opcional Default** é **0010001**, por isso o saldo foi considerado.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082218974/mceclip6.png)

Previsão de vendas com o **opcional 010002** selecionado.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082219134/mceclip7.png)

Neste caso como o **Opcional Default** é **0010001**, e o opcional selecionado na previsão de vendas é o **010002** o saldo não foi considerado.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083343773/mceclip8.png)

Se não tem **Opcional Default** selecionado.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082222714/mceclip9.png)

Pode verificar que neste caso como não tem nenhum **Opcional Default** o saldo inicial não é trazido em nenhum opcional.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082223694/mceclip10.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082223874/mceclip11.png)
