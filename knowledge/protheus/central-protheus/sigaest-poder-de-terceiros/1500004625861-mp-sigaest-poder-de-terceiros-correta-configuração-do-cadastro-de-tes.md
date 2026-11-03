---
article_id: 1500004625861
category: SIGAEST - PODER DE TERCEIROS
content_hash: 82db295a44954195c0d12b2681f4d61c80a45347d3f8c23afadcc3e4fddfcd96
fetched_at: '2026-06-28T22:39:03.290422+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: MP - SIGAEST - Poder de Terceiros - Correta configuração do cadastro de TES
type: support-article
updated_at: '2021-04-28T15:10:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004625861-MP-SIGAEST-Poder-de-Terceiros-Correta-configura%C3%A7%C3%A3o-do-cadastro-de-TES
---

**Dúvida**Como efetuar a configuração de TES para controle de Poder de Terceiros no Protheus?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para que o sistema consiga gerar os controles de poder de/em terceiros, primeiramente precisamos de TES devidamente configurados para tal.

**Premissa para o uso do controle de Poder de Terceiros**

Sendo assim, toda Remessa Geradora de Controle de/em Terceiros, independentemente de entrada ou saída, deve conter "R" (remessa) no campo SF4->F4\_PODER3.

E toda Devolução de Remessa Geradora de Poder de/em Terceiros, independentemente de entrada ou saída, deve conter "D" (devolução) no campo SF4->F4\_PODER3.

**Importância do Tipo da NF de Entrada e Tipo da NF de Saída**

Outro ponto importante nestas operações é o tipo da NF de entrada e o tipo do pedido de venda. Ou seja:

-  Ao enviar remessas para fornecedores (beneficiamento externo, armazenamento, conserto, etc.), devemos fazer pedido de venda com tipo "B", desta forma poderemos informar o código do fornecedor no pedido de venda.

- Ao enviar remessas para clientes (teste, demonstração, beneficiamento interno, etc) devemos fazer pedido de venda com tipo "N" (normal), pois informaremos o código de cliente.

- Ao receber remessas de clientes (beneficiamento interno, conserto, armazenamento, etc) devemos fazer NF de entrada com tipo "B", para que possamos informar o código do cliente na NF de entrada.

- Ao receber remessas de fornecedores (beneficiamento externo, conserto, armazenamento, etc) devemos fazer NF de entrada com tipo "N", pois informaremos o código do fornecedor.

A tabela a seguir facilita o entendimento:

|  |  |  |  |
| --- | --- | --- | --- |
| **Exemplo de Operação** | **NF** | **Tipo da NF** | **TES (3ºs)** |
| Beneficiamento Externo | Saída | B | R (Remessa) |
| Entrada\* | N | D (Devolução) |
| Beneficiamento Interno | Entrada | B | R (Remessa) |
| Saída\* | N | D (Devolução) |
| Envio para Demo/Testes | Saída | N | R (Remessa) |
| Entrada\* | B | D (Devolução) |
| Recebimento para Demo/Testes | Entrada | N | R (Remessa) |
| Saída\* | B | D (Devolução) |
| **\* Ao efetuar uma entrada ou saída digitar código do produto, TES e teclar F4 na quantidade** | | | |

Observação: Pedidos com poder de terceiros não é realizado a eliminação de resíduos.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)*
