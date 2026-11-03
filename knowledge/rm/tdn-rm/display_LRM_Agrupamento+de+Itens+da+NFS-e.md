---
content_hash: 173e7041d9255dedca291996aed457a098bcf6df4ce6b23e90d53d0a6c2f4cee
fetched_at: '2026-06-29T00:12:01.342520+00:00'
page_id: '893431156'
product: rm
source: tdn-rm
title: Agrupamento de Itens da NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Agrupamento+de+Itens+da+NFS-e
version: 17
---

# Conteúdo

2Conteúdo

# 1. Introdução

O processo de emissão de Nota Fiscal de Serviço Eletrônica (NFS-e) no Backoffice RM foi desenvolvido para atender às diversas exigências legais e práticas gerenciais. Uma das principais demandas é a capacidade de agrupar itens com o mesmo código de serviço, permitindo que a NFS-e seja emitida conforme as especificações dos municípios, enquanto oferece maior flexibilidade para o gerenciamento interno.

Essa funcionalidade é especialmente relevante, pois muitos municípios exigem que as NFS-e apresentem apenas um item consolidado, independentemente da quantidade de itens descritos no movimento de venda ou prestação de serviços. Por exemplo, em uma escola que fornece disciplinas diferentes como Matemática, História e Inglês, essas informações podem ser detalhadas internamente, mas serão agrupadas sob o código de serviço genérico definido pela prefeitura, como *"8.01 – Ensino regular pré-escolar, fundamental, médio e superior."*

Neste documento, serão apresentadas as instruções necessárias para parametrizar o agrupamento de itens, bem como as boas práticas e riscos envolvidos.

# 2. Parametrização

A configuração do agrupamento de itens na NFS-e é controlada por meio do campo **"Não Agrupar Itens"**, disponível nos dados fiscais do município. Essa parametrização define se os itens do movimento serão consolidados ou enviados individualmente no XML da NFS-e. Para mais informações sobre este campo, consulte a documentação especifica:

# 3. Como Funciona o Agrupamento?

O agrupamento de itens na NFS-e é um recurso que otimiza a geração do XML, consolidando serviços com o mesmo código de serviço. No entanto, ele traz nuances específicas no cálculo dos tributos, especialmente no que diz respeito ao ISS. A seguir, detalharemos como esse processo ocorre no movimento e no XML da NFS-e, além dos ajustes automáticos realizados pelo sistema para garantir a conformidade fiscal.

## 3.1 Movimento

O agrupamento é aplicado apenas no momento da geração do XML da NFS-e, enquanto no movimento os itens permanecem individualizados. Essa abordagem pode ocasionar diferenças no cálculo do ISS entre os valores calculados por item e o valor consolidado na nota. Veja o exemplo abaixo:

Exemplo:

|  |  |
| --- | --- |
| **Movimento com 2 Itens**   1. **Item 1:**    * Valor bruto R$ 355,79    * ISS = R$ 355,79 x 2% = **R$ 7,12** 2. **Item 2:**    * Valor bruto R$ 14,28    * ISS = R$ 14,28 x 2% = **R$ 0,29**   Soma do ISS nos dois itens:**R$ 7,41** | **Itens Agrupados na NFS-e**   * Valor bruto R$ 355,79 + R$ 14,28 = **R$ 370,07** * ISS = R$ 370,04 x 2% = **R$ 7,40** |

Essa diferença de **R$ 0,01** pode causar rejeição da nota em alguns municípios, dependendo das regras de validação aplicadas.

**Ajuste Automático no Movimento**

Para evitar problemas de rejeição, o sistema realiza automaticamente o ajuste no cálculo do ISS considerando o item agrupado, redistribuindo a diferença nos itens originais. Essa redistribuição é feita salvando a diferença no **primeiro item**, que será identificado como **editado** (campo "Manter Valor" configurado como **Editado**).

Exemplo:

|  |  |
| --- | --- |
| **Movimento com 2 Itens**   1. **Item 1:**    * Valor bruto R$ 355,79    * ISS = R$ 355,79 x 2% = **R$ 7,11** 2. **Item 2:**    * Valor bruto R$ 14,28    * ISS = R$ 14,28 x 2% = **R$ 0,29**   Soma do ISS nos dois itens: **R$ 7,40** | **Itens Agrupados na NFS-e**   * Valor bruto R$ 355,79 + R$ 14,28 = **R$ 370,07** * ISS = R$ 370,04 x 2% = **R$ 7,40** |

**Condições para Aplicação do Ajuste**

O ajuste será aplicado automaticamente quando:

1. O movimento estiver parametrizado para envio de NFS-e (Etapa **67 - Fis - NF-e: Envia Manualmente ou Envia Automaticamente**).
2. O movimento estiver parametrizado para aceitar produtos repetidos, nos parâmetros do Tipo de Movimento -  **Etapa 27 - Item - Identificação 2/2**
3. O movimento contiver mais de um item com o mesmo **ID PRD** (produto/serviço).
4. O município da filial estiver o campo **"Não Agrupar Itens"** desmarcado.

Importante

Caso o ajuste seja aplicado e seja necessário recalcular o movimento, itens cuja tributação esteja configurada como **Manter Valor = Editado** não terão os valores recalculados automaticamente. Para forçar o recalculo, siga os passos abaixo:

1. Acesse o movimento em questão.
2. Altere o campo **Manter Valor** de **Editado** para **Calculado**.
3. Realize o recalculo do movimento, conforme o objetivo desejado.

## 3.2 XML da NFS-e

xmlEclipse1XML NFse Itens Agrupadostrue
7.40
0.00
0.00
0.00
0.00
0.00
0.00
0.00
2.0000
0.0000
0.0000
0.0000
0.0000
0.0000
370.07
0
0
0




]]>
