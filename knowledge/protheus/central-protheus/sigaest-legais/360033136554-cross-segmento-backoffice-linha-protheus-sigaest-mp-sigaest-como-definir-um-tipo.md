---
article_id: 360033136554
category: SIGAEST - LEGAIS
content_hash: c70d4d2bc672b76f9ed4b4dfc03707ae6e64b80633fa59fc69db98f189f0e327
fetched_at: '2026-06-28T22:38:51.809128+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MP - SIGAEST- Como
  definir um tipo de produto que não seja padrão do sistema para que seja considerado
  no Bloco K?
type: support-article
updated_at: '2025-03-12T11:42:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MP-SIGAEST-Como-definir-um-tipo-de-produto-que-n%C3%A3o-seja-padr%C3%A3o-do-sistema-para-que-seja-considerado-no-Bloco-K
---

**Dúvida**  
Quais os tipos de produtos são considerados no Bloco K e como definir um **tipo** de produto que não seja padrão do sistema para que seja considerado no **Bloco K**?  
  
**Ambiente**  
Microsiga Protheus – Estoque – A partir da versão 12.1.17  
  
**Solução**  
Em algumas situações é necessário a utilização de outros tipos de produtos, conforme a regra de negócio da empresa. Por este motivo foi criado o parâmetro **MV\_BLKTP\*\*** que, conforme tipo do produto poderá informar o conteúdo e assim ele poderá ser considerado no Bloco K, para o registro **K200**.

**Definições de Tipo de Produto para o Bloco K**

No **Bloco K** são tratados os tipos de produto 00, 01, 02, 03, 04, 05, 06 e 10. Conforme definição da Receita Federal, temos os seguintes conceitos para estes tipos de produtos:

|  |  |  |
| --- | --- | --- |
| **Tipo** | **Descrição** | **Definição** |
| 00 | Mercadoria para Revenda | Produto adquirido para comercialização. |
| 01 | Matéria-Prima | A mercadoria que componha, física e/ou quimicamente, um produto em processo ou produto acabado e que não seja oriunda do processo produtivo. A mercadoria recebida para industrialização é classificada como Tipo 01, pois não decorre do processo produtivo, mesmo que no processo de produção se produza mercadoria similar classificada como Tipo 03. |
| 02 | Embalagem | - |
| 03 | Produto em Processo | O produto que possua as seguintes características, cumulativamente: oriundo do processo produtivo; e, preponderantemente, consumido no processo produtivo. Dentre os produtos em processo está incluído o produto resultante caracterizado como retorno de produção. Um produto em processo é caracterizado como retorno de produção quando é resultante de uma fase de produção e é destinado, rotineira e exclusivamente, a uma fase de produção anterior à qual o mesmo foi gerado. No "retorno de produção", o produto retorna (é consumido) a uma fase de produção anterior à qual ele foi gerado. Isso é uma excepcionalidade, pois o normal é o produto em processo ser consumido em uma fase de produção posterior à qual ele foi gerado, e acontece, portanto, em poucos processos produtivos. |
| 04 | Produto Acabado | O produto que possua as seguintes características, cumulativamente:   * Oriundo do processo produtivo; * Produto final resultante do objeto da atividade econômica do contribuinte; * Pronto para ser comercializado. |
| 05 | Subproduto | O produto que possua as seguintes características, cumulativamente: oriundo do processo produtivo e não é objeto da produção principal do estabelecimento; tem aproveitamento econômico; não se enquadre no conceito de produto em processo (Tipo 03) ou de produto acabado (Tipo 04). |
| 06 | Produto Intermediário | Aquele que, embora não se integrando ao novo produto, for consumido no processo de industrialização. |
| 10 | Outros Insumos | - |

**Observações:**

1 - Note que pela definição da Receita Federal o tipo de produto **03 (Produto em Processo)**, **equivale ao tipo de produto PI (Produto Intermediário) do Protheus.**

2 - **O tipo de produto 06 (Produto Intermediário)** tem um conceito diferente do que conhecemos no Protheus. De acordo com a definição acima, podemos entender que é um produto consumido no processo de industrialização, porém, não faz parte do produto resultante, como por exemplo uma lixa utilizada no processo produtivo.

3 - O Protheus possui seus tipos de produtos padronizados, como por exemplo: PA, para definir o Produto Acabado. Porém, o cliente pode ter sua própria definição para os tipos de produto. Com o objetivo de flexibilizar a "amarração" entre os tipos de produto do SPED e os tipos de produtos do Protheus, disponibilizamos um parâmetro para cada tipo de produto, onde é possível que a empresa realize sua própria "amarração". Ao informar um Tipo de Produto no parâmetro, o sistema desconsidera a amarração padrão e assume o conteúdo informado. Se os parâmetros não forem preenchidos, o sistema considera os valores padrões.

OBS: Utilizar sempre com aspas simples:

OBS 2: Ao acessar estes parâmetros no Configurador, perceberá que o "Tipo Padrão"  vem com seu conteúdo vazio (porém o tipo padrão vem cadastrado de forma implícita).

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Tipo de produto** | **Tipo Padrão** |
| MV\_BLKTP00 | Mercadoria para Revenda | 'ME' |
| MV\_BLKTP01 | Matéria-Prima | 'MP' |
| MV\_BLKTP02 | Embalagem | 'EM' |
| MV\_BLKTP03 | Produto em Processo | 'PP' |
| MV\_BLKTP04 | Produto Acabado | 'PA' |
| MV\_BLKTP05 | Subproduto | 'SP' |
| MV\_BLKTP06 | Produto Intermediário | 'PI' |
| MV\_BLKTP10 | Outros Insumos | 'OI' |

Para preenchimento dos tipos de produtos, é necessária a utilização do apóstrofo e vírgula para seleção de dois ou mais tipos.

**Exemplo Correto**:

MV\_BLKTP00 = **'ME', 'XX', 'YY'**.

**Exemplo****s Errados:**

MV\_BLKTP00 = **ME**

MV\_BLKTP00 = **"ME"**

MV\_BLKTP00 = **"ME",'XX'**

MV\_BLKTP00 = **" 'ME', 'XX' "**

O processamento do **Bloco K** disponibiliza também o do ponto de entrada **SPDFIS001.** para que seja possível alterar a amarração entre os tipos de produto do SPED e do Sistema. Porém, ao utilizar o ponto de entrada, os valores definidos nos parâmetros MV\_BLKTP\*\* serão sobrepostos.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Fiscais/Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
