---
content_hash: 51727ee0e14d1f9be7bce8fade70aed1f1f850220f42726b11fa28fa84b69620
fetched_at: '2026-06-29T00:08:57.716762+00:00'
page_id: '354469739'
product: rm
source: tdn-rm
title: DT Customização do Percentual / Valor da bolsa por fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354469739
version: 14
---

# Customização do percentual ou valor da bolsa por fórmula

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro de Bolsa | Cadastro de Bolsa | |  |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Geração de Lançamento | Geração de Lançamento | |  |  | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [DEDUINTEGRACOES-2286](http://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-2286) |
| **País(es):** | N/A |
| **Banco(s) de Dados:** | N/A |
| **Tabelas Utilizadas:** | SBolsa |
| **Sistema(s) Operacional(is):** | N/A |

## **Descrição**

O objetivo do recurso de **customização do percentual ou valor** da bolsa por fórmula permite vincular uma fórmula no cadastro da bolsa que tem **regras específicas programadas pelo cliente** para determinar o valor do desconto do **tipo percentual ou do tipo valor** da bolsa de forma customizada durante a **geração do lançamento financeiro**.

**Exemplo**:

Na matrícula o aluno ganha uma bolsa de 5% com um desconto progressivo, e em que a cada mês será acrescido a bolsa do aluno 1%.

Como será?

- Cadastra uma bolsa “Bolsa desconto progressivo" do tipo de desconto igual a percentual com valor percentual de desconto de 5%.

- Para essa bolsa iremos associar uma fórmula que tem como função acrescentar o 1% conforme o mês da parcela.

Este recurso estará disponível oficialmente a parti da versão 12.1.21, porém o mesmo poderá ser antecipado juntamente com o recurso do desconto por antecipação a partir da versão 12.1.19, neste caso será necessário executar scripts específicos.

## **Cadastro de Bolsa**

No cadastro de bolsa foram adicionados dois novos campos para que seja possível vincular as fórmulas que serão responsáveis em customizar o percentual ou valor.

Informação

Deverá ser associada as fórmulas de forma separada, ou seja, uma formula para percentual e outra para valor.

O campo de fórmula não será bloqueado conforme o tipo de desconto da bolsa, pois a bolsa poderá ser cadastrada com o tipo de desconto “Percentual”. E essa mesma bolsa poderá estar a associada ao contrato do aluno com o tipo de desconto igual a “Valor”.

Para este cenário se houver necessidade de customizar os dois tipos de descontos será necessário preencher os dois campos de fórmula.

## **Fórmula**

Foram disponibilizadas funções de fórmula específicas para serem utilizadas na criação das formulas que serão associadas a bolsa.

* **CAMPOSBOLSAALUNO:** Retorna a informação de qualquer campo da tabela SBOLSAALUNO durante a geração de lançamento financeiro.

Esta função de fórmula possibilita ter acesso também aos campos abaixo:

SBOLSA.CODCFO,

SBOLSA.CODCOLCFO,

SBOLSA.NOME,

SBOLSA.CODTIPOCURSO,

SBOLSA.VALIDADELIMITADA,

SBOLSA.TIPOSAC, SBOLSA.FIES,

SCLASSIFICACAOBOLSA.CODCLASSIFICACAO,

SCLASSIFICACAOBOLSA.TIPOBOLSA,

ORDEMBOLSACLASSIFICACAO campo ORDEMBOLSA da SCLASSIFICACAOBOLSA

Essa fórmula pode ser utiliza fora da geração de lançamento financeiro, porém o contexto deve ser em cima do cadastro de bolsa do contrato (SBOLSAALUNO)

**Exemplo:**

CAMPOSBOLSAALUNO('CODSERVICO','S')

CAMPOSBOLSAALUNO('NOME','S')

* **VLRDESCONTOANT:** Retorna o valor do desconto por antecipação considerado para a parcela durante a geração de lançamento financeiro.

O valor retornado é o valor calculado do desconto por antecipação durante a geração do lançamento. Desta forma, será necessário o sistema está configurado para calcular o . E observar se no cadastro da bolsa do contrato do aluno o campo "**Aplicar desconto por antecipação"** tem o valor "**Depois do cálculo da bolsa**" isso indica que o desconto por antecipação será calculado depois do valor da bolsa.

ATENÇÃO

Caso tiver com a utilização dessa fórmula para calcular o valor da bolsa com as configurações citadas anteriormente o valor do desconto por antecipação **será zero**, pois na bolsa está configurada para aplicar o desconto por antecipação **depois do cálculo da bolsa**.

**Exemplo:**

VLRDESCONTOANT

* **PERCENTUALDESCANT:** Retorna o percentual do desconto por antecipação considerado para a parcela durante a geração de lançamento financeiro.

O valor retornado é o valor calculado do desconto por antecipação durante a geração do lançamento. Desta forma, será necessário o sistema está configurado para calcular o . E observar se no cadastro da bolsa do contrato do aluno o campo "**Aplicar desconto por antecipação"** tem o valor "**Depois do cálculo da bolsa**" isso indica que o desconto por antecipação será calculado depois do valor da bolsa. 

ATENÇÃO

Caso tiver com a utilização dessa fórmula para calcular o valor da bolsa com as configurações citadas anteriormente o valor do desconto por antecipação **será zero**, pois na bolsa está configurada para aplicar o desconto por antecipação **depois do cálculo da bolsa**.

**Exemplo:**

PERCENTUALDESCANT

* **VALORPARCELA:** Retorna o valor da parcela durante a geração de lançamento financeiro.

O valor retornado é o valor calculado para parcela na geração de lançamento. Se a parcela estiver configurada para valor calculado pelo número de créditos, o sistema deverá está configurado corretamente para realizar o cálculo da parcela.

**Exemplo:**

VALORPARCELA

* **MODIFICAPERCENTUALDESCANT ou MODIFICAVALORDESCANT:** Permite modificar em memória o valor ou percentual do desconto por antecipação durante a geração de lançamento financeiro.

Vale ressaltar, O valor modificado vai refletir na formula VLRDESCONTOANT e PERCENTUALDESCANT, ou seja se estas formulas forem executadas durante o processamento das bolsas para o mesmo aluno o sistema vai retorna o valor modificado.

ATENÇÃO

A utilização das fórmulas **MODIFICAPERCENTUALDESCANT ou MODIFICAVALORDESCANT** devem ser utilizadas dentro do contexto de geração de lançamento, mas o controle dos valores devem ser realizados exclusivamente na fórmula criada.

**Exemplo:**

MODIFICAVALORDESCANT(100), modifica o valor do desconto por antecipação para R$100,00. Vale ressaltar, que com a modificação do desconto por antecipação o seu percentual será ajustado.

MODIFICAPERCENTUALDESCANT(23), modifica o percentual do desconto por antecipação para 23%. Vale ressaltar, que com a modificação do desconto por antecipação o seu valor será ajustado.

* **IDHABILITACAOFILIAL**: Retorna o IDHABILITACAOFILIAL do contrato do aluno vinculada à bolsa durante a geração de lançamento financeiro.

Essa fórmula pode ser utiliza fora da geração de lançamento financeiro, porém o contexto deve ser em cima do cadastro de bolsa do contrato (SBOLSAALUNO)

**Exemplo**:

IDHABILITACAOFILIAL

* **MOCK:** Simula um valor para as funções de fórmula "**VLRDESCONTOANT**" ou "**VALORPARCELA**".

Para utilizar a função MOCK, é necessário utilizar a função "**VLRDESCONTOANT**" ou "**VALORPARCELA**" para obter o valor simulado gerado pela função MOCK. Em seguida, essa fórmula deve ser chamada para obter o valor simulado gerado pela função MOCK.

Após o término dos testes, a função MOCK deve ser removida para garantir a precisão dos resultados.

**Exemplos**:

Para simular o valor da parcela durante a execução dos testes, utiliza-se a fórmula MOCK('VALORPARCELA', 1000);

Para obter o valor simulado da parcela, utiliza-se a fórmula VALORPARCELA() que retorna o valor 1000;

Para simular o valor do desconto durante a execução dos testes, utiliza-se a fórmula MOCK('VLRDESCONTOANT', 1500);

Para obter o valor simulado do desconto, utiliza-se a fórmula VLRDESCONTOANT() que retorna o valor 1500.

sql

**Geração de Lançamento**

Durante a geração do lançamento financeiro o sistema realiza o cálculos das bolsas vinculadas para o aluno considerando as parametrizações (ordem da bolsa, cascata, somar bolsa, e etc ).

Antes do cálculo das bolsas, o sistema vai identificar as bolsas que possuem fórmula associada e executá-las. O resultado desta fórmula será considerado para “percentual” ou “valor” a ser considerado no cálculo da bolsa.

A identificação será feita pelo tipo de desconto da bolsa no contrato do aluno. Isso é:

* Para o cálculo do valor da bolsa via fórmula. No cadastro de bolsa do contrato deve ser do tipo de desconto igual a valor. Assim o sistema vai identificar se no cadastro da bolsa tem uma fórmula informada no campo "Fórmula para valor".
* Para o cálculo do percentual da bolsa via fórmula. No cadastro de bolsa do contrato deve ter o tipo de desconto igual a percentual. Assim o sistema vai identificar se no cadastro da bolsa tem uma fórmula informada no campo "Fórmula para percentual"

ATENÇÃO

Se no cadastro da bolsa no contrato do aluno o tipo de desconto for valor e no cadastro da bolsa não tiver uma fórmula cadastrada no campo "Fórmula para valor". O sistema não irá calcular o valor da bolsa por fórmula, mesmo que tenha uma fórmula cadastrada no campo "Fórmula para percentual".

Se no cadastro da bolsa no contrato do aluno o tipo de desconto for percentual e no cadastro da bolsa não tiver uma fórmula cadastrada no campo "Fórmula para percentual". O sistema não irá calcular o valor da bolsa por fórmula, mesmo que tenha uma fórmula cadastrada no campo "Fórmula para valor".

**Exemplo 1:**

A Bolsa “X” de 20% está vinculada para o aluno, porém nesta bolsa temos a fórmula “XPTO” que acrescenta 1%.

A fórmula XPTO retornará o percentual de 21%, logo o sistema considerará para o cálculo da bolsa os 21%.

**Exemplo 2:**

O valor da bolsa será 20% do valor do desconto por antecipação. No cadastro da bolsa no contrato o campo "**Aplicar desconto por antecipação"** tem o valor "**Antes do cálculo da bolsa**".

O valor da parcela é de R$ 1000,00 com data de vencimento para 15/09/2024

O percentual do desconto por antecipação é de 30% até o dia 14/09/2024

Desta forma teremos os seguintes valores:

Valor da parcela: R$ 1000,00

Valor do desconto por antecipação até o dia 14/09/2024 é de 20%: R$ 1000,00 \* 0,20 = R$ 200,00

A fórmula XPTO1 é: VLRDESCONTOANT \* 0,30 = R$ 200,00 \* 0,30 = R$ 60,00

Informações

Com objetivo de ter o histórico da informação para saber se o cálculo do percentual ou valor foi processado por uma fórmula serão gravados dois campos na tabela SBOLSALAN.

Campo “**EXECUTOUFORMULA**”:

0 - Não executou

1 – Executou fórmula para customizar o percentual

2 – Executou fórmula para customizar o valor

Campo ”**PERCENTCALCFORMULA**”:

Identifica o percentual retornado pela fórmula.
