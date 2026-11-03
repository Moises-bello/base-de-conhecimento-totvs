---
content_hash: a6fffbfe313ef12a225beaa118895c7e311f8f36431c22a4fa08b70ec31727bc
fetched_at: '2026-06-29T00:11:06.133299+00:00'
page_id: '63276243'
product: rm
source: tdn-rm
title: Processo de Industrialização (Retorno em 1 NF) - Remetente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63276243
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão de Estoque Compras e Faturamento                       **Versão:** 11.52 e posteriores |
| **Processo** | **:** | Estoque DE/COM Terceiros |
| **Subprocesso** | **:** | Processo de Industrialização (Retorno em 1 NF) - Remetente |
| **Data da publicação** | **:** | 18/06/2013 |

Neste processo, consideramos que somente a **Empresa Remetente** possui o ERP RM e esta não exerce atividades industriais. Esta empresa também, **NAO podera controlar estoque de servicos no sistema**.

A empresa remetente da operação de industrialização irá incluir um movimento de saída **‘Remessa para Industrialização’** para controle do estoque COM Terceiros e regularização fiscal e contábil da operação. Este movimento irá **aumentar** o estoque **COM Terceiros**, sem interferir no estoque total de propriedade da empresa (Saldo Atual). Consideramos que o estoque COM Terceiros é um estoque indisponível para movimentações de saídas, até que seja lançado o retorno do insumo. O valor financeiro do estoque COM Terceiros será calculado com base no custo médio dos insumos já registrados no sistema.

A empresa que efetuar a industrialização poderá enviar o produto industrializado (PI), cobrar o serviço de industrialização e devolver simbolicamente a matéria prima utilizada no processo de industrialização em uma única nota fiscal (1 NF) ou em duas notas fiscais (2 NF). Descreveremos a seguir o processo com o retorno da industrialização em uma única nota fiscal (1 NF).

Ao receber a nota fiscal de industrialização efetuada por outra empresa (que conterá o retorno simbólico da matéria prima e a cobrança do serviço), a empresa remetente irá incluir um movimento de entrada **‘Industrialização Efetuada por Terceiros’** através de um processo específico para este tipo de operação – Retorno Industrialização Efetuada por Terceiros – Em uma única NF. Neste processo serão selecionadas as notas fiscais de remessa para industrialização emitidas pela empresa cujos insumos ainda não retornaram, seja parcial ou total. Em seguida será solicitado alguns dados referente ao produto industrializado pelo terceiro, para que seu estoque seja atualizado. Após confirmar essas opções, será aberta a edição do movimento de **‘Industrialização Efetuada por Terceiros’** com os insumos selecionados anteriormente e as respectivas quantidades pendentes de retorno. Neste momento o usuário poderá alterar a quantidade retornada e preencher os dados fiscais da operação se estes não estiverem parametrizados no tipo de movimento. Deverá incluir o serviço referente a cobrança da industrialização com respectivo CFOP. Ao finalizar a inclusão desse movimento, o estoque COM Terceiros dos insumos enviados para o processo de industrialização será afetado (diminuir), conforme parametrizado no tipo de movimento. Consequentemente o estoque de propriedade da empresa (Saldo Atual) dos insumos também serão afetados (diminuir), conforme parametrizado no tipo de movimento.

### Parametrização do tipo de movimento:

#### --> Movimento de Remessa para Industrialização.

Etapa:  “Estoque/Estoque 2/3”

Contabilidade e Fiscal parametrizar de acordo com as obrigações legais e contábeis da empresa.

#### --> Movimento de Entrada do Produto Industrializado por Terceiros.

Etapa:  “Estoque/Estoque 1/3”

Etapa:  “Estoque/Estoque 2/3”

Observação:  Informar a fórmula de acordo com o critério de cálculo de custo médio adotado pela empresa.

Contabilidade: Parametrizar de acordo com as obrigações contábeis da empresa.

#### --> Movimento de Industrialização Efetuada por Terceiros.

Etapa:  “Item – Identificação 1/2”

Observação: O tipo de itens tem que ser “Ambos” para aceitar os produtos retornados e o serviço de industrialização.

Etapa:  “Item – Identificação 2/2”

Observação: Permitir item repetido é necessário porque a mercadoria devolvida simbolicamente pode ter saído em mais de uma NF, nesse caso, irá criar um item relacionado para cada Nota Fiscal.

Etapa:  “Estoque – Estoque 1/3”

Etapa:  “Estoque – Estoque 2/3”

Observação: Informar o tipo de movimento parametrizado anteriormente para a entrada do produto industrializado.

Contabilidade: Parametrizar de acordo com a obrigação contábil da empresa.

Integração Fiscal: Parametrizar de acordo com a obrigação legal da empresa.

Integração Financeira: Parametrizar se a NF de retorno for conjugada e possuir a cobrança do serviço.

#### --> Movimento de Retorno da Mercadoria não Aplicada na Industrialização.

Etapa:  “Mov – Outros Dados”

Observação: Usar cópia por referencia motivo 11.

Etapa:  “Item – Identificação 1/2”

Etapa:  “Item – Identificação 2/2”

Observação: Permitir item repetido é necessário porque a mercadoria devolvida que não foi industrializada pode ter saído em mais de uma NF, nesse caso, irá criar um item relacionado para cada Nota Fiscal.

Etapa:  “Estoque - Estoque 1/3”

Etapa:  “Estoque - Estoque 2/3”

Integração Contábil: Parametrizar de acordo com as obrigações contábeis da empresa.

Integração Fiscal: Parametrizar de acordo com as obrigações legais da empresa.

##### Para o detalhamento do processo acesse o link:  Demonstração do processo de Industrialização (Retorno em 1 NF) - Remetente
