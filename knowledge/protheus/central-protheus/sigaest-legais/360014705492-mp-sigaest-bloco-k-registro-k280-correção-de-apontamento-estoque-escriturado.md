---
article_id: 360014705492
category: SIGAEST - LEGAIS
content_hash: 7f6329875f530b45185f66ba4e3a7c712533f3fa61f75f63ec8caf47550da80e
fetched_at: '2026-06-28T22:38:51.576767+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'MP - SIGAEST - Bloco K - Registro K280: Correção de Apontamento – Estoque
  Escriturado'
type: support-article
updated_at: '2021-08-12T20:46:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014705492-MP-SIGAEST-Bloco-K-Registro-K280-Corre%C3%A7%C3%A3o-de-Apontamento-Estoque-Escriturado
---

**Dúvida**O que é o Registro K280: Correção de Apontamento – Estoque Escriturado do SPED FISCAL?  
  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

Este registro tem o objetivo de escriturar a correção de apontamento de estoque escriturado de período de apuração anterior escriturado (no Registro K200).

A correção de um apontamento deve ocorrer, obrigatoriamente, entre o levantamento de 02 inventários (Campo 02 do Registro H005), uma vez que, com a contagem do estoque se terá conhecimento de uma eventual necessidade de correção de apontamento

A correção do estoque escriturado de um período de apuração poderá influenciar estoques escriturados de períodos anteriores, uma vez que o estoque final de um período de apuração é o estoque inicial do período de apuração seguinte

**Observações:**

É importante salientar que apontamento de correções dos registros K270/K275 refletirão em um acréscimo ou decréscimo de insumo/produto no estoque. Logo, itens gerados nestes registros são levados para o Registro K280

Caso o cliente possua um processo automatizado/customizado **ou** deseje informar manualmente este registro, foi disponibilizado o ponto de entrada **REGK280,** onde é possível realizar a gravação do arquivo de trabalho do Registro K280 durante o processamento do **Bloco K**. Devido ao ponto de entrada dar acesso direto ao arquivo de trabalho, não são realizadas validações das informações gravadas.

*[Clique aqui e veja mais informações sobre o Ponto de Entrada REGK280](https://tdn.totvs.com/display/public/PROT/PEST07670+REGK280+Registros+K280+Bloco+K)*

**Estrutura do Registro K280:**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K280" | C | 4 | - | O |
| 02 | DT\_EST | Data do estoque final escriturado que está sendo corrigido | N | 8 | - | O |
| 03 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | C | 60 | - | O |
| 04 | QTD\_COR\_P | Quantidade de correção positiva de apontamento ocorrido em período de apuração anterior | N | - | 3 | OC |
| 05 | QTD\_COR\_N | Quantidade de correção negativa de apontamento ocorrido em período de apuração anterior | N | - | 3 | OC |
| 06 | IND\_EST | Indicador do tipo de estoque: 0 = Estoque de propriedade do informante e em seu poder; 1 = Estoque de propriedade do informante e em posse de terceiros; 2 = Estoque de propriedade de terceiros e em posse do informante. | C | 1 | - | O |
| 07 | COD\_PART | Código do participante (campo 02 do Registros 0150): Proprietário/Possuidor que não seja o informante do arquivo. | C | 60 | - | OC |

**Saiba mais:**

*[Mais informações sobre Registro K280 e fluxo de correção de apontamento gerado na prática](https://tdn.totvs.com/pages/releaseview.action?pageId=259560569)*

*[Informações sobre as movimentações que são consideradas no Registro K270](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=259560564)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
