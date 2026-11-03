---
article_id: 360014702032
category: SIGAEST - LEGAIS
content_hash: 5fab1b5134facd4554227a8efb925179b277d95d85b5437857845746c992ff1a
fetched_at: '2026-06-28T22:38:51.471415+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Registro
  K220: Outras Movimentações Internas entre Mercadorias'
type: support-article
updated_at: '2026-04-23T18:15:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014702032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Registro-K220-Outras-Movimenta%C3%A7%C3%B5es-Internas-entre-Mercadorias
---

O Registro K220 no SPED registra movimentações internas entre mercadorias que não se enquadram nos demais registros do Bloco K, considerando transferências feitas pelas rotinas MATA260 e MATA261 com produtos de origem e destino diferentes. Inclui campos como data, código dos itens e quantidades movimentadas. É usado no Protheus a partir da versão 11.80 e envolve a tabela SD3.

**Dúvida**  
O que é e como gerar o Registro K220 no SPED?  
  
**Ambiente**  
Protheus – Estoque – A partir da versão 11.80  
  
**Solução**

O Registro K220 (Outras Movimentações Internas entre Mercadorias) contém as informações de movimentações internas entre mercadorias que não se enquadram nos demais registros do Bloco K.

Para a montagem deste registro, são consideradas todas as transferências realizadas através das rotinas MATA260 e MATA261, cujos os produtos de Origem e Destino sejam diferentes.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K220" | C | 4 | - | O |
| 02 | DT\_MOV | Data da movimentação interna | N | 8 | - | O |
| 03 | COD\_ITEM\_ORI | Código do item de origem (campo 02 do Registro 0200) | C | 60 | - | O |
| 04 | COD\_ITEM\_DEST | Código do item de origem (campo 02 do Registro 0200) | C | 60 | - | O |
| 05 | QTD\_ORI | Quantidade movimentada do item de Origem | N | - | 3 | O |
| 06 | QTD\_DEST | Quantidade movimentada do item de destino | N | - | 3 | O |

**Tipos de Produtos considerados no registro K200**:

00, 01, 02, 03, 04, 05 e 10.

**Rotinas envolvidas**

MATA260 – Transferência de Produtos  
MATA261 – Transferência de Produtos Modelo II

**Tabelas envolvidas**

SD3 – Movimentações Internas

**Exemplo prático:**

Temos os produtos PA007 e PA007TR01. Iremos transferir 2 itens do PA007 para o PA007TR01. Veja como será:

1 - Execução da Transferência de Produtos - MATA260

![image2018-10-30_21-23-50.png](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-23-50.png?version=1&modificationDate=1540949030953&api=v2)

2 - Geração do SPED com a pergunta "Gera Bloco K?" = Sim

![image2018-10-30_21-27-6.png](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-27-6.png?version=1&modificationDate=1540949226433&api=v2)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
