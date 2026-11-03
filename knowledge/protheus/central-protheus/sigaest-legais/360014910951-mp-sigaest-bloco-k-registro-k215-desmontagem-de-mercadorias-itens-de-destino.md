---
article_id: 360014910951
category: SIGAEST - LEGAIS
content_hash: 70f6b153d94cf9ac083eb31c524102c5ab4c71ccee1e49f6b06b00fc8a0b0420
fetched_at: '2026-06-28T22:38:51.539354+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'MP - SIGAEST - Bloco K - Registro K215: Desmontagem de Mercadorias - Itens
  de Destino'
type: support-article
updated_at: '2021-07-05T15:30:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014910951-MP-SIGAEST-Bloco-K-Registro-K215-Desmontagem-de-Mercadorias-Itens-de-Destino
---

**Dúvida**O que é o Registro K215: Desmontagem de Mercadorias - Itens de Destino?  
  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

Este registro contém as informações dos movimentos de desmontagem de produtos, no que se refere à entrada do estoque do item de destino.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K215" | C | 4 | - | O |
| 02 | COD\_ITEM\_DES | Código do item de origem (campo 02 do Registro 0200) | C | 60 | - | O |
| 03 | QTD\_DES | Quantidade de destino – entrada em estoque | N | - | 3 | O |

São consideradas as desmontagens de produtos geradas através da rotina MATA242, dentro do período de apuração, sendo que neste registro serão considerados apenas os movimentos de destino com **D3\_CF = DE7.**

**Tipos de Produtos considerados**  
00(ME), 01(MP), 02(EM), 03(PP), 04(PA), 05(SP) e 10(OI).

**Rotinas envolvidas**  
MATA242 – Desmontagem de Produtos

**Tabelas envolvidas**  
SD3 – Movimentações Internas

**Saiba mais:**

*[MP - SIGAEST - Bloco K - Registro K210: Desmontagem de Mercadorias - Itens de Origem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014701512)*

[*Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
