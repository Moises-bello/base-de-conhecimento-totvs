---
content_hash: 578fd03cb16c5fd70eba84d05e5754194aca0da288a396be8086fbad1735fd79
fetched_at: '2026-06-29T00:08:12.559454+00:00'
page_id: '243643471'
product: rm
source: tdn-rm
title: TVBWZB_DT_Conceito_E_Aplicacao_De_Bolsas
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBWZB_DT_Conceito_E_Aplicacao_De_Bolsas
version: 9
---

# CONCEITOS E APLICAÇÃO DE BOLSAS - CONDICIONAIS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de lançamentos* | **Geração de lançamentos financeiros** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de lançamentos* | **Geração de lançamentos financeiros** | | ***Baixa de lançamentos*** | *Baixa de lançamentos* | | *Parâmetros de Sistema* | *Parâmetros de Sistema* | | *Cadastro de Bolsas* | *Cadastro de Bolsas* | | *Contabilização por competência* | *Contabilização por competência* | | *Simulação de valores de parcelas* | *Simulação de valores de parcelas* | |
| **Cadastros Iniciais:** | *1. Cadastro de bolsas do contrato  *2. Cadastro de parcelas do contrato** |
| **Parâmetro(s):** | *Criação do parâmetro "Manter fórmula default para valor opcional de bolsas condicionais"* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados relacionados** | *TVEBGW* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas utilizadas:** | *N/A* |
| **Sistema(s) operacional(is):** | *Todos.* |
| **Versões/Release:** | *12.1.12* |

## Descrição

O Totvs Educacional trabalha com dois conceitos de bolsas (Incondicionais e Condicionais).

As bolsas **INCONDICIONAIS** são aquelas que sempre manterão o mesmo valor original de bolsas da geração.

As bolsas **CONDICIONAIS** são aquelas que, dependendo de alguma condição (pagamento em atraso, coeficiente de rendimento ruim do aluno, notas, frequência, etc...), terão o seu valor alterado.

Foram feitas as seguintes alterações:

1) Ajuste Labels

    1.1) Parâmetros do Educacional (De - Para)

* (De) Utilizar escalonamento de bolsas - (Para) Utilizar bolsas condicionais. A utilização da bolsa condicional não necessariamente tem que ter um escalonamento.
* (De) Bolsas válidas APÓS o vencimento - (Para) Bolsas incondicionais. A aplicação do parâmetro não relação nenhuma com a data de vencimento, independentemente de qualquer variável a bolsa não será perdida.
* (De) Bolsas válidas ATÉ o vencimento - (Para) Bolsas condicionais. A regra para perda de valores da bolsa não está necessariamente ligada a data de vencimento, ela pode servir para pagamento antecipado, para análise de rendimento do aluno, ou qualquer outra campanha que a instituição trabalhe.

    1.2) Cadastro de Bolsas

* (De)Válida após o vencimento da parcela - (Para) Bolsa incondicional – A regra para perda de valores da bolsa não está necessariamente ligada a data de vencimento, ela pode servir para pagamento antecipado, para análise de rendimento do aluno, ou qualquer outra campanha que a instituição trabalhe.

    1.3) Simulação de valores de parcelas

* (De)Vlr. bolsa válida após vencimento - (Para) Bolsa incondicional
* (De)Vlr. bolsa válida até vencimento - (Para) Bolsa condicional

 2) Geração de lançamentos com bolsas **CONDICIONAIS**: Foi criado o parâmetro "Manter fórmula default para valor opcional de bolsas condicionais" que, ao ser marcado, mantém a fórmula default associada ao valor opcional de bolsas condicionais na geração de lançamentos. Essa fórmula que será responsável por setar os valores de bolsas condicionais. Para que seja considerado o valor de bolsas do lançamento, poderá ser utilizada a função de fórmula **VALORBOLSALAN()**. Exemplo: VALORBOLSALAN(0,0,'-1'). Caso o parâmetro esteja desmarcado, a geração de lançamentos calculará e atribuirá o valor das bolsas condicionais ao valor opcional parametrizado para Bolsas condicionais do lançamento anulando a fórmula vinculada a esse campo.

3) Simulação de valores de parcelas: Os valores mostrados para bolsas condicionais serão os valores de bolsas condicionais calculados para o contrato (Independente de fórmula e data de cálculo).

4) Baixa de lançamentos com bolsas **CONDICIONAIS**: Ao cadastrar uma bolsa no sistema com o campo "Bolsas incondicionais" **DESMARCADO**, é habilitado o campo "**Ordem de perda**" que indicará a ordem em que as bolsas perderão valor na baixa. A ordem de baixa das bolsas será o inverso da ordem de perda, ou seja, o menor número de Ordem de perda terá a menor prioridade de baixa. Os valores gerados de cada bolsa serão registrados no campo **VALOR** da tabela **SBOLSALAN**. Os valores baixados de cada bolsa serão registrados no campo **VALORBAIXA** da tabela **SBOLSALAN**.

Bolsas com a mesma Ordem de perda, terão os seus valores proporcionalizados com relação ao valor original total gerado para cada ordem de perda.

Seguem abaixo algumas situações exemplificando as ordens de perda:

O contrato do aluno possuirá três bolsas (A, B e C) com valores originais de bolsa nos valores de 100.00, 100.00 e 100.00 totalizando 300.00

**Exemplo 1 - Valores de bolsas condicionais iguais aos valores originais de bolsas gerados e mesma ordem de perda** **(1):**

Se não houver diferença entre os valores gerados e os valores baixados, ao baixar o lançamento com as bolsas, o sistema atribuirá ao valor baixado o valor original gerado para bolsa (SBOLSALAN.VALORBAIXADO = SBOLSALAN.VALOR)

**Exemplo 2 - Valores de bolsas condicionais diferentes dos valores originais de bolsas gerados e mesma ordem de perda** **(1):**

Caso haja diferença entre os valores gerados e os valores baixados, o sistema ordenará as bolsas **CONDICIONAIS** por ordem **DECRESCENTE**  de ordem de perda para que, o maior número de ordem de perda seja a primeira bolsa a ser baixada.

Consideraremos que o valor calculado para as bolsas condicionais na baixa seja de 250.00 (Calculado através da fórmula associada ao valor opcional vinculado a bolsas condicionais)

Como todas as bolsas possuem a mesma ordem de perda, sistema processará os registros de SBOLSALAN na sequência:

* Bolsa (A) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 100
* Bolsa (B) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 100
* Bolsa (C) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 50

**Exemplo 3 - Valores de bolsas condicionais diferentes dos valores originais de bolsas gerados e diferentes ordens de perda:**

Caso haja diferença entre os valores gerados e os valores baixados, o sistema ordenará as bolsas **CONDICIONAIS** por ordem **DECRESCENTE**  de ordem de perda para que, o maior número de ordem de perda seja a primeira bolsa a ser baixada.

Consideraremos que o valor calculado para as bolsas condicionais na baixa seja de 250.00 (Calculado através da fórmula associada ao valor opcional vinculado a bolsas condicionais) com as seguintes ordens de perda por bolsa:

* Bolsa (A) - ORDEMDEPERDA = 1
* Bolsa (B) - ORDEMDEPERDA = 2
* Bolsa (C) - ORDEMDEPERDA = 3

Como as bolsas possuem ordens de perda diferentes, sistema processará os registros de SBOLSALAN na sequência:

* Bolsa (C) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 100
* Bolsa (B) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 100
* Bolsa (A) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 50

**Exemplo 4 - Valores de bolsas condicionais diferentes dos valores originais de bolsas gerados e diferentes ordens de perda:**

Caso haja diferença entre os valores gerados e os valores baixados, o sistema ordenará as bolsas **CONDICIONAIS** por ordem **DECRESCENTE**  de ordem de perda para que, o maior número de ordem de perda seja a primeira bolsa a ser baixada.

Consideraremos que o valor calculado para as bolsas condicionais na baixa seja de 100.00 (Calculado através da fórmula associada ao valor opcional vinculado a bolsas condicionais) com as seguintes ordens de perda por bolsa:

* Bolsa (A) - ORDEMDEPERDA = 1
* Bolsa (B) - ORDEMDEPERDA = 2
* Bolsa (C) - ORDEMDEPERDA = 2

Como a bolsa (A) possui ordem de perda diferente e as bolsas (B) e (C) possuem mesmos valores de ordens de perda, o sistema processará os registros de SBOLSALAN conforme abaixo:

* Bolsa (C) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 50 (<VALOR ORIGINAL DA BOLSA> / <VALOR TOTAL DE BOLSAS POR ORDEM DE PERDA>) \* <VALOR DISPONIVEL PARA BAIXA ANTES DE PROCESSAR A ORDEM DE PERDA> = (100 / 200) \* 100 = 50
* Bolsa (B) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 50 (<VALOR ORIGINAL DA BOLSA> / <VALOR TOTAL DE BOLSAS POR ORDEM DE PERDA>) \* <VALOR DISPONIVEL PARA BAIXA ANTES DEPROCESSAR A ORDEM DE PERDA> = (100 / 200) \* 100 = 50
* Bolsa (A) - SBOLSALAN.VALOR = 100, SBOLSALAN.VALORBAIXADO = 0

**OBSERVAÇÃO**:

As bolsas **INCONDICIONAIS** terão sempre o mesmo valor nos campos **SBOLSALAN.VALOR** e **SBOLSALAN.VALORBAIXA**

## Procedimento para Implantação

1. Configuração dos respectivos valores opcionais para bolsas condicionais e incondicionais
2. Marcação do parâmetro para manter fórmula default associada a valores de bolsas condicionais.

## Procedimento para Configuração

N/A

## Procedimento para Utilização

1. Instalação do release 12.1.12 ou posterior
2. Configuração dos valores opcionais para bolsas condicionais e incondicionais
3. Geração de lançamentos para parcelas com esses tipos de bolsas
4. Baixa de lançamentos com os tipos de bolsas acima citados.
