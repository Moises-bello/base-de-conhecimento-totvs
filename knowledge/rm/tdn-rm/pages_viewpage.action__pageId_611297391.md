---
content_hash: ec9bd687ee2dd1f73b3c8e12ec9f6e332d9bf9e5b86586918d7e6f9128f0f9b1
fetched_at: '2026-06-29T00:10:59.097053+00:00'
page_id: '611297391'
product: rm
source: tdn-rm
title: Extração de dados do Ativo Imobilizado - Ernst & Young
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611297391
version: 2
---

Essa documentação tem como intuito orientar o usuário para a correta utilização dos objetos gerenciais referentes à extração de dados nos formatos esperados pela consultoria Ernst & Young.

falsedeckCompletotruePP&E register (Registro de Ativos)slide

Através desse layout é possível extrair os dados detalhados do ativo imobilizado assim como informações sobre adições, alienações e depreciação, para apoio nas auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **PATLAY0002 - Exportacao Patrimônios - ErnstYoung**. 

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Cenário Patrimônio: Cenário de cálculo a ser utilizado.

Data Inicial: data inicial do cálculo.

Data Final: data final do cálculo.

Filtro para Seleção de Patrimônios: Caso queira restringir os Patrimônios a serem exportados pode-se criar um filtro específico.

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do arquivo.

| ID | Formato | Tamanho | Dec | Descrição | Origem dos Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico |  |  | Número do ativo | Código do patrimônio presente no cadastro. |  |
| 2 | Alfanumérico |  |  | Descrição do ativo | Descrição do patrimônio. |  |
| 3 | Alfanumérico |  |  | Localização do Ativo | Nome do local em que o ativo está. |  |
| 4 | Alfanumérico |  |  | Posse do Ativo | Campo não aderente ao layout. |  |
| 5 | Alfanumérico |  |  | Categoria de ativo | Descrição do grupo ao qual o patrimônio foi associado. |  |
| 6 | Alfanumérico |  |  | Tipo de ativo | Título (grau superior) ao qual o patrimônio está vinculado. |  |
| 7 | Alfanumérico |  |  | Depreciação de ativos | Valor fixo 'Y'. |  |
| 8 | Alfanumérico |  |  | Método de depreciação | Valor fixo 'SL'. |  |
| 9 | Decimal |  | 2 | Custo de compra | Valor da aquisição presente no cadastro do patrimônio. |  |
| 10 | Decimal |  | 2 | Saldo residual | Corresponde ao valor residual ao final da vida útil existente em alguns processos como Avaliação Patrimonial e Revisão de Vida Útil. |  |
| 11 | Decimal |  | 2 | Percentual do saldo redutor | Não será gerado |  |
| 12 | Decimal |  | 0 | Vida útil (anos) | Vida útil do patrimônio em anos. | O cálculo é feito pela divisão de 100 pela taxa de depreciação corrente. |
| 13 | Decimal |  | 0 | Vida útil restante no início do Período | Campo opcional. Não está sendo calculado. |  |
| 14 | Decimal |  | 0 | Vida útil restante no Encerramento do Período | Campo opcional. Não está sendo calculado. |  |
| 15 | Data |  |  | Data capitalizada | Data da primeira depreciação do patrimônio. |  |
| 16 | Data |  |  | Data de alienação | Data da baixa mais recente existente dentro do período que está sendo auditado. |  |
| 17 | Data |  |  | Data de transferência | Data da transferência mais recente existente dentro do período que está sendo auditado. |  |
| 18 | Decimal |  | 2 | Custo no início do Período | Valor base corrigido do patrimônio no início do período que está sendo auditado. |  |
| 19 | Decimal |  | 2 | Custo de Adição | Soma dos acréscimos e avaliações que incidiram no patrimônio durante o período selecionado. |  |
| 20 | Decimal |  | 2 | Custo de Transferência | Soma das transferências realizadas pelos patrimônios de origem durante o período que está sendo auditado. |  |
| 21 | Decimal |  | 2 | Custo de Alienação | Soma das baixas realizadas pelo patrimônio durante o período que está sendo auditado. |  |
| 22 | Decimal |  | 2 | Custo no fechamento do Período | Valor base corrigido no fechamento do período que está sendo auditado. |  |
| 22 | Decimal |  | 2 | Depreciação no início do Período | Depreciação acumulada corrigida existente na última linha de cálculo anterior a data de início da auditoria. Caso o patrimônio seja avaliado será somada a depreciação acumulada, da linha de cálculo principal, com a depreciação acumulada da avaliação. |  |
| 24 | Decimal |  | 2 | Depreciação cobrada durante o período | Soma da depreciação ajustada das linhas de cálculo existentes no período que está sendo auditado. |  |
| 25 | Decimal |  | 2 | Depreciação transferida | Soma do ajuste da depreciação acumulada corrigida, existente no cálculo de depreciação, gerado pelas ocorrências de transferência monetária. |  |
| 26 | Decimal |  | 2 | Depreciação Alienada | Soma do ajuste da depreciação acumulada corrigida, existente no cálculo de depreciação, gerado pelas ocorrências de baixa. |  |
| 27 | Decimal |  | 2 | Depreciação de Fechamento | Depreciação acumulada corrigida existente na última linha de cálculo do período que está sendo auditado. Caso o patrimônio seja avaliado será somada a depreciação acumulada, da linha de cálculo principal, com a depreciação acumulada da avaliação. |  |
| 28 | Decimal |  | 2 | Valor Líquido na abertura | Valor contábil do patrimônio no início do período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo no Início do Período e a Depreciação no Início do Período existentes no layout. |
| 29 | Decimal |  | 2 | Valor Líquido no fechamento | Valor contábil do patrimônio no final do período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo no Fechamento do Período e a Depreciação de Fechamento existentes no layout. |
| 30 | Decimal |  | 2 | Valor Líquido de alienações | Valor líquido de custo e depreciação acumulada dos patrimônios que foi baixado durante o período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo de Alienação e a Depreciação Alienada existentes no layout. |
| 31 | Decimal |  | 2 | Valor Líquido de transferências | Valor líquido de custo e depreciação acumulada dos patrimônios de origem que realizaram transferências durante o período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo de Transferência e a Depreciação Transferida existentes no layout. |
