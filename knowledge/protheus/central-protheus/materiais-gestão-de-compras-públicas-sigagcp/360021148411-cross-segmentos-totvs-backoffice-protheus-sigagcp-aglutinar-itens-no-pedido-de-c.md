---
article_id: 360021148411
category: Materiais - Gestão de Compras Públicas - (SIGAGCP)
content_hash: 86d9046b803ea26673f4e60bb20a63169d1889d6df1344b911902f4d2b909b15
fetched_at: '2026-06-28T22:37:18.375905+00:00'
product: protheus
section_id: 1500001550562
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCP - Aglutinar itens no
  Pedido de Compra de um Edital com SC
type: support-article
updated_at: '2022-07-28T11:19:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021148411-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCP-Aglutinar-itens-no-Pedido-de-Compra-de-um-Edital-com-SC
---

**Dúvida**

|  |
| --- |
| Quando é gerado um edital baseando-se em solicitação de compras que tenham dois itens de serviço, com o mesmo código e data de referência, o sistema os aglutina em um único item no edital. Quando damos andamento no edital, ao gerar pedido de compras e posterior documento de entrada, ficam 2 itens de serviço no mesmo documento |

**Ambiente**A partir da versão P12  
  
**Solução**Criado o parâmetro MV\_GCPAGL para definir se itens iguais serão aglutinados na geração de Pedido de Compra por meio do Edital com SC.

1. *Criação*de **Parâmetros** no arquivo **SX6 – Parâmetros**:

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_GCPAGL |
| **Tipo** | Lógico |
| **Descrição** | Define se os itens do Edital, vindo da SC, serão aglutinados na geração do Pedido de Compra |
| **Valor Padrão** | .F. |

***Saiba Mais:***

[Gestão de Contratos Públicos](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=341222185)

[Mais Artigos Materiais - Gestão de Compras Publicas (SIGAGCP)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550562)
