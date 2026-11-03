---
content_hash: d2698e227c5f1a2c60594649d6200b0cb130d776bd1af56e548b90cb3be6597d
fetched_at: '2026-06-29T00:10:57.946753+00:00'
page_id: '601695426'
product: rm
source: tdn-rm
title: Extração de dados do Inventário, Estoque e Movimentações - Ernst & Young
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=601695426
version: 60
---

Essa documentação tem como intuito orientar o usuário para a correta utilização dos objetos gerenciais referentes à extração de dados nos formatos esperados pela consultoria Ernst & Young.

falsedeckCompletotrueHistórico de Compra (Purchase History)slide

Através desse layout é possível extrair dados consolidados do Histórico de Compras, Vendas e Movimentações, de duas ou mais empresas, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **MOVLAY0039 - Exportacao de Movimentação - ErnstYoung.TotvsGen.**

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

Data Final: data final do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

#### Estáticos (definidos internamente e não variam)

Classificação do(s) Movimento(s): serão listados apenas movimentos cuja classificação seja 'Recebimento de Materiais', "Importação" ou 'Aquisição de Serviços'.

Exemplo

Status do(s) Movimento(s): serão listados apenas movimentos cujo status seja diferente de 'Cancelado'.

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Descrição |
| --- | --- |
| Product code | Código do Produto |
| Quantity purchase | Quantidade total comprada do produto no período, considerando a unidade de medida de controle do produto |
| Unit of measure | Unidade de medida de controle de estoque |
| Purchase amount | Valor total da compra do produto no período |
| Latest purchase price | Preço unitário do ultimo movimento de compra do produto no período, considerando a unidade de controle do produto |
| Last purchase date | Data do ultimo movimento de compra do produto no período (se tiver mais de um movimento no mesmo dia, considerar a ordenação por IDMOV) |
| Last purchase invoice code | Dados do último movimento de compra do produto no período no formato: Série, Número da Nota Fiscal, Emitente, Natureza de Operação e Sequencial do Item na Nota (todas as informações separadas por underline)  \*Retorna a natureza do Item, se estiver vazia retorna a natureza do Movimento |
| Business unit | Coligada do movimento |

Importante!

Os campos **Quantity,****Latest price** e **Amount**(sales e purchase) tem sua quantidade de casas decimais pré-definidas de acordo com o esperado pelo Relatório base Ernst & Young, sendo 5 para os dois primeiros e 2 para o último.

Outro detalhe a se destacar é que esses campos sempre serão arredondados, tomando como base a informação citada acima.

Histórico de Venda (Sales History)slide

Através desse layout é possível extrair dados consolidados do Histórico de Compras, Vendas e Movimentações, de duas ou mais empresas, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **MOVLAY0039 - Exportacao de Movimentação - ErnstYoung.TotvsGen.**

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

Data Final: data final do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

#### Estáticos (definidos internamente e não variam)

Classificação do(s) Movimento(s): serão listados apenas movimentos cuja classificação seja 'Faturamento' ou 'Exportação'.

Exemplo

Status do(s) Movimento(s): serão listados apenas movimentos cujo status seja diferente de 'Cancelado'.

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Observações |
| --- | --- |
| Product code | Código do produto |
| Quantity sold | Quantidade total vendida do produto no período, considerando a unidade de medida de controle do produto |
| Unit of measure | Unidade de medida de controle de estoque |
| Sales amount | Valor total da venda do produto no período |
| Latest sales price | Preço unitário do ultimo movimento de venda do produto no período, considerando a unidade de controle do produto |
| Last sales date | Data do ultimo movimento de venda do produto no período (se tiver mais de um movimento no mesmo dia, considerar a ordenação por IDMOV) |
| Last sales invoice code | Dados do último movimento de venda do produto no período no formato: Série, Número da Nota Fiscal e Sequencial do Item na Nota (todas as informações separadas por underline) |
| Business unit | Coligada do Movimento |

Importante!

Os campos **Quantity,****Latest price** e **Amount**(sales e purchase) tem sua quantidade de casas decimais pré-definidas de acordo com o esperado pelo Relatório base Ernst & Young, sendo 5 para os dois primeiros e 2 para o último.

Outro detalhe a se destacar é que esses campos sempre serão arredondados, tomando como base a informação citada acima.

Histórico de Movimento (Movement History)slide

Através desse layout é possível extrair dados consolidados do Histórico de Compras, Vendas e Movimentações, de duas ou mais empresas, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **MOVLAY0039 - Exportacao de Movimentação - ErnstYoung.TotvsGen.**

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

Data Final: data final do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

#### Estáticos (definidos internamente e não variam)

Classificação do(s) Movimento(s): serão listados apenas movimentos cuja classificação seja 'Faturamento' ou 'Exportação' (Venda) e 'Recebimento de Materiais', "Importação" ou 'Aquisição de Serviços' (Compra).

Exemplo

Status do(s) Movimento(s): serão listados apenas movimentos cujo status seja diferente de 'Cancelado'.

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Observações |
| --- | --- |
| Product code | Código do produto |
| Last sales date | Data do último movimento de venda do produto no período |
| Last purchase date | Data do último movimento de compra do produto no período |
| Last sales invoice code | Dados do último movimento de venda do produto no período no formato: Série, Número da Nota Fiscal e Sequencial do Item na Nota (todas as informações separadas por underline)  \*se tiver mais de um movimento no mesmo dia, considerar a ordenação por IDMOV |
| Last purchase invoice code | Dados do último movimento de compra do produto no período no formato: Série, Número da Nota Fiscal, Emitente, Natureza de Operação e Sequencial do Item na Nota (todas as informações separadas por underline)  \*Retorna a natureza do Item, se estiver vazia retorna a natureza do Movimento \*\*se tiver mais de um movimento no mesmo dia, considerar a ordenação por IDMOV |
| Business unit | Coligada do Movimento |

Contagem Permanente de Inventário (Perpetual Inventory Count)slide

Através desse layout é possível extrair dados consolidados do Estoque, de duas ou mais empresas, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **ESTLAY0020 - Exportacao de Estoque - ErnstYoung.TotvsGen.**

DadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

Data Final: data final do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Observações |
| --- | --- |
| Product code | Código do produto |
| Last counted date | Data da última contagem de estoque (Inventário) |
| Adjustment made | Identificador (por exemplo, S / N) para determinar se a contagem perpétua identificou diferenças entre o livro e as quantidades físicas disponíveis. |
| Adjustment quantity | Valor da diferença |
| Location | Código da Filial + Código do Local de Estoque |
| Business unit | Coligada |

Lista do Inventário (Inventory Valuation Listing)slide

Através desse layout é possível extrair dados consolidados do Inventário, de duas ou mais empresas, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **ESTLAY0019 - Exportacao de Inventário - ErnstYoung.TotvsGen.**

DadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

Data Final: data final do intervalo para busca do(s) movimento(s) (serão filtrados considerando TMOV.DATAEMISSAO).

#### Estáticos (definidos internamente e não variam)

Serão exibidos somente dados do Saldo Físico (Saldo 2)

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Observações |
| --- | --- |
| Business unit | Código da Coligada |
| Product code | Código do produto |
| Quantity | Quantidade do produto disponível no final do período, após a ultima movimentação para o Produto. |
| Unit of measure | Unidade de medida de controle de estoque |
| Material cost per unit | Custo Médio, após a ultima movimentação para o Produto. |
| Total cost per unit | Custo Médio, após a ultima movimentação para o Produto. |
| Material cost | Total da Movimentação após a ultima movimentação para o Produto |
| Amount | Total da Movimentação após a ultima movimentação para o Produto |
| Location | Filial + Local de Estoque |
| Subledger Name | Conta contábil vinculada no produto com classificação contábil EY |

Produto (Product Master File)slide

Foi disponibilizada uma consulta que será responsável por retornar determinadas informações sobre produtos, respeitando os parâmetros (filtros) de entrada.

DadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Observações |
| --- | --- |
| Product code | Código do produto |
| Product description | Nome fantasia do produto |
| Product group | Grupo de produtos usado para organizar produtos. Primeiro nível da máscara do produto |
| Product type | Situação da mercadoria (Dados fiscais do produto) |
| Valuation method | Tipo de custo (Médio, PEPS, UEPS, etc) |

Unidade de Medida (Unit of Measure)slide

Foi disponibilizada uma consulta que será responsável por retornar determinadas informações sobre as Unidades de Medida.

DadosParâmetros

(Nenhum parâmetro se aplica a esse relatório)

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Observações |
| --- | --- |
| Unit of measure code | Código da Unidade de medida |
| Unit of measure description | Descrição da Unidade de Medida |

Unidade de Negócio (Business Unit)slide

Foi disponibilizada uma consulta que será responsável por retornar determinadas informações sobre as Unidades de Negócio

DadosParâmetros

(Nenhum parâmetro se aplica a esse relatório)

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| Campo | Observações |
| --- | --- |
| Business unit code | Código da Coligada |
| Business unit description | Nome da Coligada |
