---
content_hash: a0e8ea7d7c2065250f950c3ba88066e7f5988a84b4d2f5820db522f229485d38
fetched_at: '2026-06-29T00:11:53.794424+00:00'
page_id: '851306722'
product: rm
source: tdn-rm
title: Funções de Fórmula - Gestão Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=851306722
version: 42
---

As funções de fórmula tem por objetivo permitir aos clientes customizar o cálculo dos valores a serem gerados nos lançamentos/partidas e seus respectivos rateios para efeitos de contabilização das operações patrimoniais (aquisição, depreciação, baixa, transferência de controle, entre outras).

O contexto de execução das fórmulas é determinado pelo tipo de contabilização: Aquisição, Depreciação, Ocorrência ou Transferência de Controle. As funções devem ser aplicadas de acordo com o contexto, ou seja, algumas só podem ser utilizadas em um contexto específico e outras em qualquer situação. Consulte a documentação para entender as particularidades de cada função.

ACRESCIMO

* **Descrição**:
  + A função retorna o valor que representa o tipo de **ocorrência de Acréscimo** no patrimônio (70).
* **Parâmetros**:

  + Não possui.
* **Exemplo:**
  + ACRESCIMO() - O resultado será 70
BAIXAPARCIAL

* **Descrição**:
  + A função retorna o valor que representa o tipo de **ocorrência de Baixa Parcial** no patrimônio (90).
* **Parâmetros**:

  + Não possui.
* **Exemplo:**
  + BAIXAPARCIAL() - O resultado será 90
BAIXAPERIODOANTERIOR

* **Descrição**:
  + A função retorna o valor que representa o tipo de **ocorrência para Baixa de Período Anterior** no patrimônio (100).
* **Parâmetros**:
  + Não possui.
* **Exemplo:**
  + BAIXAPERIODOANTERIOR() - O resultado será 100
BAIXATOTAL

* **Descrição**:
  + A função retorna o valor que representa o tipo de **ocorrência de Baixa Total** no patrimônio (99).
* **Parâmetros**:
  + Não possui.
* **Exemplo:** 
  + BAIXATOTAL() - O resultado será 99
CAMPOBEM

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da **IBEM (Bem)**. Caso não haja dados, busca-se os valores compatíveis na tabela **IPATRIMONIO (Patrimônio)**. Se o campo não existir, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela **IBEM** ou **IPATRIMONIO**
* **Exemplo:** 
  + CAMPOBEM("DESCRICAO") - O resultado será o valor do campo "Descrição".
CAMPOBEMCOMPL

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **IPATRIMONIOCOMPL (Complemento do Patrimônio)**. Se o campo não existir na tabela, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela **IPATRIMONIOCOMPL**
* **Exemplo:** 
  + CAMPOBEMCOMPL("PLACA") - O resultado será o valor do campo "Placa".
CAMPOBEMTRANSFERENCIA

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **IPATRIMONIOTRANSFERENCIA (Transferência de Patrimônio)**. Se o campo não existir na tabela, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela **IPATRIMONIOTRANSFERENCIA**.
* **Exemplo:** 
  + CAMPOBEMTRANSFERENCIA("CODFILIALORIGEM") - O resultado será o valor do campo "CodFilialOrigem".
CAMPOCALCULORAZAO

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **ICALCULORAZAO (Cálculo Razão)**, convertido para o tipo indicado. Se o campo não existir na tabela ou o tipo indicado for incorreto, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela **ICALCULORAZAO**.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.
* **Exemplo:** 
  + CAMPOCALCULORAZAO("TAXADEPRECIACAOPERIODO", "V") - O resultado será o valor do campo "TaxaDepreciacaoPeriodo" convertido para um valor numérico.
CAMPOOCORRENCIA

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **IOCORRENCIA (Ocorrência)**. Se o campo não existir na tabela, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela **IOCORRENCIA**.
* **Exemplo:** 
  + CAMPOOCORRENCIA("VALORVENDA") - O resultado será o valor do campo "ValorVenda".
CAMPOPATRIMONIO

* **Descrição**: A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **IPATRIMONIO (Patrimônio)**, convertido para o tipo indicado. Se o campo não existir na tabela ou o tipo indicado for incorreto, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela **IPATRIMONIO**.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.
* **Exemplo:** 
  + CAMPOPATRIMONIO("DESCRICAO", "S") - O resultado será o valor do campo "Descrição" convertido para um texto.
CAMPOPATRIMONIOCOMPL

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela de **IPATRIMONIOCOMPL (Complemento do Patrimônio)**, convertido para o tipo indicado. Se o campo não existir na tabela ou o tipo indicado for incorreto, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela **IPATRIMONIOCOMPL**.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.
* **Exemplo:** 
  + CAMPOPATRIMONIOCOMPL("COR", "S") - O resultado será o valor do campo "Cor" convertido para um texto.
CAMPOPATRIMONIOTRANSFERENCIA

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **IPATRIMONIOTRANSFERENCIA (Transferência de Patrimônio),** convertido para o tipo indicado. Se o campo não existir na tabela ou o tipo indicado for incorreto, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela IPATRIMONIOTRANSFERENCIA.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.
* **Exemplo:**
  + CAMPOPATRIMONIOTRANSFERENCIA("CODCENTROCUSTODESTINO", "S") - O resultado será o valor do campo "Código de Centro de Custo do Destino" convertido para um texto.
CAMPORAZAO

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **ICALCULORAZAO** (**Cálculo Razão)**, convertido para texto. Se o campo não existir na tabela, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela ICALCULORAZAO.
* **Exemplo:**
  + CAMPORAZAO("INDICE") - O resultado será o valor do campo "Índice" convertido para um texto.

OBSERVAÇÃO

Caso deseje utilizar outros tipos de conversão, é possível utilizar a função de fórmula "**CAMPOCALCULORAZAO**".

CAMPOTRANSFERENCIA

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **ITRANSFERENCIACONTROLE (****Transferência de Patrimônio)**, convertido para texto. Se o campo não existir na tabela, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela ITRANSFERENCIACONTROLE.
* **Exemplo:**
  + CAMPOTRANSFERENCIA("OBSERVACAO") - O resultado será o valor do campo "Observação" convertido para um texto.

OBSERVAÇÃO

Caso deseje utilizar outros tipos de conversão, é possível utilizar a função de fórmula "**CAMPOTRANSFERENCIACONTROLE**".

CAMPOTRANSFERENCIACONTROLE

* **Descrição**:
  + A função recebe um campo como parâmetro e retorna o valor correspondente da tabela **ITRANSFERENCIACONTROLE (****Transferência de Patrimônio)**, convertido para o tipo indicado. Se o campo não possuir valor ou o tipo indicado for incorreto, uma exceção será lançada.
* **Parâmetros**:
  + Campo (string): O nome do campo desejado. Possíveis valores: Todos os campos da tabela ITRANSFERENCIACONTROLE.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.
* **Exemplo:**
  + CAMPOTRANSFERENCIACONTROLE("OBSERVACAO", "S") - O resultado será o valor do campo "Observação" convertido para um texto.
DATAAQUISICAO

* **Descrição**:
  + A função retorna o valor que representa a **Data de Aquisição**da tabela **IPATRIMONIO (****Patrimônio)**,convertido para o tipo indicado. Se o campo não possuir valor ou o tipo indicado for incorreto, uma exceção será lançada.
* **Parâmetros**:  
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.
* **Exemplo:**
  + DATAAQUISICAO("D") - O resultado será o valor do campo "Data de Aquisição" convertida para uma data.
DATABASE

* **Descrição**:
  + A função retorna o valor que representa a **Data de Base** do Patrimônio, convertida para o tipo indicado.  Se o campo não possuir valor ou o tipo indicado for incorreto, uma exceção será lançada.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a Data de Base do Patrimônio. O sistema busca valor em uma das três tabelas diferentes, retornando valor da primeira encontrada e seguindo a respectiva ordem citada logo a frente:
    - **ISALDOCALCULOPATRIMONIOMOEDA (Saldo do Cálculo do Patrimônio Moeda)  -** Campo: **DATABASEPATRIMONIO**.
    - **ICALCULOPATRIMONIO (Cálculo do Patrimônio)** - Campo: **DATAINICIOVIGENCIA**.
    - **IPATRIMONIO (Patrimônio)** - Campo: **DATAAQUISICAO**.

* **Parâmetros**:
  + Identificador de Cálculo do Patrimônio (int): Relativo ao Identificador de Cálculo do Patrimônio das tabelas citadas no funcionamento.
  + Identificador de Moeda do Patrimônio (int): Relativo ao Identificador da Moeda utilizada no Cálculo do Patrimônio.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.

* **Exemplo:**
  + DATABASE(1, 1, "D") - O resultado será o valor do campo "Data Base Patrimônio", "Data Início Vigência" ou "Data de Aquisição", retornando sempre o primeiro a ser encontrado e convertido para uma data.
DEPRECIACAOACUMULADACORRIGIDA

* **Descrição**:
  + Retorna o valor que representa a **Depreciação Acumulada Corrigida** do Patrimônio.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornado o valor de acordo com a regra descrita abaixo:  
      
    Busca o valor primeiro na tabela **ICALCULORAZAO** - Campo: **DEPRECIACAOACUMULADACORRIGIDA**.  
    Se o valor retornado for zero, busca o valor na tabela **ISALDOCALCULOPATRIMONIOMOEDA** - Campo: **DEPRECIACAOACUMULADACORRIGIDA**  
    Se o valor retornado for zero, busca o valor na tabela **IPATRIMONIOMOEDA**- Campo: **DEPRECIACAOAQUISICAOCORRIGIDA**
  + **OBS:** Filtra os dados onde a data seja menor ou igual a data informada.
* **Parâmetros**
  + Data:  Indica qual a data será levada em consideração para buscar o valor base. Ex:18/07/2024
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V":  Para valores numéricos de ponto flutuante.
    2. "I":   Para valores inteiros.
    3. "D": Para datas.
    4. "S":  Para string.
* **Exemplo: DEPRECIACAOACUMULADACORRIGIDA**("18/07/2024","V") - Retorna o valor convertido no formato definido pelo **Tipo**.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

DEPRECIACAOACUMULADACORRIGIDAMESCALCULOATUAL

* **Descrição**:
  + Retorna o valor decimal que representa a **Depreciação Acumulada Corrigida** do Patrimônio referente ao **período de cálculo atual**.
* **Funcionamento:** 
  + A Fórmula tem o mesmo comportamento da função **DEPRECIACAOACUMULADACORRIGIDA**, usando a data igual ao período de cálculo atual do sistema e o tipo de retorno como decimal.
* **Exemplo:** 
  + DEPRECIACAOACUMULADACORRIGIDA() - O resultado será a Depreciação Acumulada Corrigida referente ao período de cálculo atual convertida para decimal.
DEPRECIACAOMENSAL

* **Descrição**:
  + A função retorna o valor que representa a **Depreciação Mensal** do Patrimônio da tabela **ICALCULORAZAO (Cálculo Razão)** , convertido para o tipo indicado. Se o campo não possuir valor ou o tipo indicado for incorreto, uma exceção será lançada.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornado o Valor de Depreciação Mensal do Patrimônio. O resultado será o somatório do campo DEPRECIACAOAJUSTADA, buscando o Valor do ano e mês de cálculo atual.
* **Parâmetros**:  
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.
* **Exemplo:**
  + DEPRECIACAOMENSAL("S") - O resultado será a Soma dos valores do campo "Depreciação Ajustada", no Período de Cálculo atual, convertido em formato de texto.
DTAQUISICAO

* **Descrição**:
  + A função retorna o valor que representa a **Data de Aquisição**no Patrimônio. Se o campo não possuir valor, uma exceção será lançada.
* **Parâmetros**:

  + Não possui.

* **Exemplo:**
  + DTAQUISICAO() - O resultado será o valor do campo "Data de Aquisição" convertida para um texto.

DTBASE

* **Descrição**:
  + A função retorna o valor que representa a **Data de Base** do Patrimônio, convertida para o tipo indicado.  Se o campo não possuir valor ou o tipo indicado for incorreto, uma exceção será lançada.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a Data de Base do Patrimônio. O sistema busca valor em uma das três tabelas diferentes, retornando valor da primeira encontrada e seguindo a respectiva ordem citada logo a frente:
    - **ISALDOCALCULOPATRIMONIOMOEDA (Saldo do Cálculo do Patrimônio Moeda)  -** Campo: **DATABASEPATRIMONIO**.
    - **ICALCULOPATRIMONIO (Cálculo do Patrimônio)** - Campo: **DATAINICIOVIGENCIA**.
    - **IPATRIMONIO (Patrimônio)** - Campo: **DATAAQUISICAO.**
* **Parâmetros**:

  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.

* **Exemplo:**
  + DTBASE("D") O resultado será o valor do campo **"Data Base Patrimônio"** (**DATABASEPATRIMONIO** da tabela: **ISALDOCALCULOPATRIMONIOMOEDA**), **"Data Início Vigência"** (**DATAINICIOVIGENCIA** da tabela: **ICALCULOPATRIMONIO**) ou **"Data de Aquisição"** (**DATAAQUISICAO** da tabela: **IPATRIMONIO**), retornando sempre o primeiro a ser encontrado e convertido para uma data.
NOMEOCORRENCIA

* **Descrição**:
  + Retorna o nome do Tipo de Ocorrência.
* **Funcionalidade:**
  + Para cada tipo de ocorrência o sistema tem um tratamento especifico, o valor esperado deve ser um entre os citados abaixo.
* **Parâmetros**:

  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "0"     Sem Ocorrência: Não há quaisquer ocorrências para o bem.
    2. "1"     Transferência De Controle: Transferência física.
    3. "2"     Transferência monetária.
    4. "3"     Impairment: Redução por perdas (Impairment).
    5. "4"     Recuperação Impairment: Recuperação de perdas (Reversão Impairment).
    6. "60"    Avaliação.
    7. "70"    Acréscimo.
    8. "90"    Baixa Parcial: Baixa parcial do bem.
    9. "99"    Baixa Total: Baixa total do bem.
    10. "100"  Baixa Período Anterior: Baixa em período anterior.

* **Exemplo:**
  + NOMEOCORRENCIA("4") A formula irá buscar o Tipo de Ocorrência correspondente.
RESIDUALREAL

* **Descrição**:
  + Retorna o valor de saldo residual do patrimônio, convertido para texto.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada o Valor Residual do Patrimônio. O sistema buscará o somatório do valor em uma das duas tabelas, retornando valor da primeira encontrada e seguindo a respectiva ordem citada logo a frente:
    - **ICALCULORAZAO(Cálculo Razão)** - Campo: **SALDORESIDUALINDICE.**
    - **ISALDOCALCULOPATRIMONIOMOEDA(Saldo do Cálculo do Patrimônio Moeda)** - Campo: **SALDORESIDUALINDICE.**
* **Parâmetros**:

  + Data (string): Relativa a Data até onde será buscada a Depreciação do Patrimônio das tabelas citadas no funcionamento.

* **Exemplo:**  
  + **RESIDUALREAL**("01/01/2020") - O resultado será a **Soma** dos valores do campo **"Saldo Residual",** até a Data de **"01/01/2020",** convertido em formato de texto.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

RESIDUALUFIR

* **Descrição**:
  + Retorna o valor de saldo residual UFIR do patrimônio, convertido para texto.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada o Valor Residual do Patrimônio. O sistema buscará o somatório do valor em uma das duas tabelas, retornando valor da primeira encontrada e seguindo a respectiva ordem citada logo a frente:
    - **ICALCULORAZAO(Cálculo Razão)** - Campo: **SALDORESIDUALINDICE.**
    - **ISALDOCALCULOPATRIMONIOMOEDA(Saldo do Cálculo do Patrimônio Moeda)** - Campo: **SALDORESIDUALINDICE.**
* **Parâmetros**:

  + Data (string): Relativa a Data até onde será buscada a Depreciação do Patrimônio das tabelas citadas no funcionamento.

* **Exemplo:**  
  + **RESIDUALUFIR**("01/01/2020") - O resultado será a **Soma** dos valores do campo **"Saldo Residual" (UFIR),** até a Data de **"01/01/2020",** convertido em formato de texto.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

SALDORESIDUAL

* **Descrição**:
  + Retorna o valor de saldo residual do patrimônio.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada o Valor Residual do Patrimônio. O sistema buscará o somatório do valor em uma das duas tabelas, retornando valor da primeira encontrada e seguindo a respectiva ordem citada logo a frente:
    - **ICALCULORAZAO(Cálculo Razão)** - Campo: **SALDORESIDUALINDICE.**
    - **ISALDOCALCULOPATRIMONIOMOEDA(Saldo do Cálculo do Patrimônio Moeda)** - Campo: **SALDORESIDUALINDICE.**
* **Parâmetros**:

  + Data (string): Relativa a Data até onde será buscada a Depreciação do Patrimônio das tabelas citadas no funcionamento.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.

* **Exemplo:**  
  + **SALDORESIDUAL**("01/01/2020", "S") - O resultado será a **Soma** dos valores do campo **"Saldo Residual",** até a Data de **"01/01/2020",** convertido em formato de texto.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

SALDORESIDUALMESCALCULOATUAL

* **Descrição**:
  + Retorna o valor decimal que representa o **Saldo Residual** do Patrimônio referente ao **período de cálculo atual**.
* **Funcionamento:** 
  + A Fórmula tem o mesmo comportamento da função **SALDORESIDUAL**, usando a data igual ao período de cálculo atual do sistema e o tipo de retorno como decimal.
* **Exemplo:** 
  + SALDORESIDUALMESCALCULOATUAL() - O resultado será o Saldo Residual referente ao período de cálculo atual convertido para decimal.
SALDORESIDUALINDICE

* **Descrição**:
  + Retorna o valor de saldo residual UFIR do patrimônio.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada o Valor Residual do Patrimônio. O sistema buscará o somatório do valor em uma das duas tabelas, retornando valor da primeira encontrada e seguindo a respectiva ordem citada logo a frente:
    - **ICALCULORAZAO(Cálculo Razão)** - Campo: **SALDORESIDUALINDICE.**
    - **ISALDOCALCULOPATRIMONIOMOEDA(Saldo do Cálculo do Patrimônio Moeda)** - Campo: **SALDORESIDUALINDICE.**
    - A conversão do campo **Valor** é definida de acordo com o **Tipo** passado.
* **Parâmetros**:

  + Data (string): Relativa a Data até onde será buscada a Depreciação do Patrimônio das tabelas citadas no funcionamento.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V": Para valores numéricos de ponto flutuante.
    2. "I": Para valores inteiros.
    3. "D": Para datas.
    4. "S": Para strings.

* **Exemplo:**  
  + **SALDORESIDUALINDICE**("01/01/2020", "Tipo") - O resultado será a **Soma** dos valores do campo **"Saldo Residual" (UFIR),** até a Data de **"01/01/2020",** convertido em formato definido pelo **Tipo**.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

SALDORESIDUALINDICEMESCALCULOATUAL 

* **Descrição**:
  + Retorna o valor decimal que representa o **Saldo Residual UFIR** do Patrimônio referente ao **período de cálculo atual**.
* **Funcionamento:** 
  + A Fórmula tem o mesmo comportamento da função **SALDORESIDUALINDICE**, usando a data igual ao período de cálculo atual do sistema e o tipo de retorno como decimal.
* **Exemplo:** 
  + SALDORESIDUALINDICEMESCALCULOATUAL () - O resultado será o Saldo Residual UFIR referente ao período de cálculo atual convertido para decimal.
TAXADEPRECIACAO

* **Descrição**:
  + Retorna a taxa de depreciação de um patrimônio no mês.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a **Taxa de Depreciação** do Patrimônio no mês. O sistema buscará o ultimo valor de taxa de acordo com o parâmetro **Mês** na tabela:
    - **ITAXADEPRECIACAO** - Campo: **VALOR.**
* **Parâmetros**:

  + Mês (string): Indica qual o **Mês** será levado em consideração para busca da taxa de depreciação.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V":  Para valores numéricos de ponto flutuante.
    2. "I":   Para valores inteiros.
    3. "D": Para datas.
    4. "S":  Para strings.

* **Exemplo:**  
  + **TAXADEPRECIACAO**("Mês", "Tipo") - Filtra de acordo com o **Mês** definido e busca a **Taxa de Depreciação,** convertendo o em formato definido pelo **Tipo**.
TAXADEPRECIACAOSEGUNDAMOEDA

* **Descrição**:
  + Retorna a taxa de depreciação de um patrimônio no mês
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a **Taxa de Depreciação** do Patrimônio no mês. O sistema buscará o ultimo valor de taxa onde a moeda e diferente da moeda índice, de acordo com o parâmetro **Mês** na tabela:
    - **ITAXADEPRECIACAO** - Campo: **VALOR.**
    - **OBS:** Esta formula procura a **Taxa de Depreciação** onde amoeda **diferente** da **moeda índice.**
* **Parâmetros**:

  + Mês (string): Indica qual o **Mês** será levado em consideração para busca da taxa de depreciação.
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V":  Para valores numéricos de ponto flutuante.
    2. "I":   Para valores inteiros.
    3. "D": Para datas.
    4. "S":  Para strings.

* **Exemplo:**  
  + **TAXADEPRECIACAOSEGUNDAMOEDA**("Mês", "Tipo") - Filtra de acordo com o **Mês** definido e busca a **Taxa de Depreciação** da moeda diferente da moeda índice, convertendo o em formato definido pelo **Tipo**.
TRANSFERENCIA

* **Descrição**:
  + Retorna o código de ocorrência do tipo transferência
* **Parâmetros**:

  + Não possui.

* **Exemplo:**
  + **TRANSFERENCIA()** - O resultado será o  código de ocorrência do tipo transferência.
TXDEPREC

* **Descrição**:
  + Retorna a taxa de depreciação de um patrimônio no mês.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a última **Taxa de Depreciação** do Patrimônio no mês informado por parâmetro.
    - **ITAXADEPRECIACAO** - Campo: **VALOR.**
    - **OBS:** Esta formula procura a **Taxa de Depreciação** em que amoeda índice é **igual** a **moeda corrente**e que não seja reavaliado.
* **Parâmetros**:

  + Mês (string): Indica qual o **Mês** será utilizado buscar a taxa de depreciação.

* **Exemplo:**  
  + **TXDEPREC**("5") - Retorna em formato string.
TXDEPREC2

* **Descrição**:
  + Retorna a taxa de depreciação de um patrimônio no mês na segunda moeda.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a última **Taxa de Depreciação** do patrimônio no mês informado por parâmetro.
    - **ITAXADEPRECIACAO** - Campo: **VALOR.**
    - **OBS:** Esta formula procura a **Taxa de Depreciação** em que amoeda índice é **diferente** da **moeda corrente**e que não seja reavaliado.
* **Parâmetros**:

  + Mês (string): Indica qual o **Mês** será utilizado buscar a taxa de depreciação.

* **Exemplo:**  
  + **TXDEPREC**("4") - Retorna em formato string.
VALORAQUISICAO

* **Descrição**:
  + Retorna o valor de aquisição do patrimônio.
* **Funcionamento:**   
  + - **IPATRIMONIO**- Campo: **AQUISICAO.**
* **Parâmetros**:

  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V":  Para valores numéricos de ponto flutuante.
    2. "I":   Para valores inteiros.
    3. "D": Para datas.
    4. "S":  Para string.

* **Exemplo:**  
  + **VALORAQUISICAO**("Tipo") - Retorna o valor convertido no formato definido pelo **Tipo**.
VALORBASECORRIGIDO

* **Descrição**:
  + Retorna o valor base corrigido do patrimônio.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornado o valor base corrigido do patrimônio de acordo com a regra descrita abaixo:  
      
    Busca o valor primeiro na tabela **ICALCULORAZAO** - Campo: **VALORBASECORRIGIDO**.  
    Se o valor retornado for zero, busca o valor na tabela **ISALDOCALCULOPATRIMONIOMOEDA** - Campo: **VALORBASECORRIGIDO**  
    Se o valor retornado for zero, busca o valor na tabela **IPATRIMONIOMOEDA**- Campo: **AQUISICAO**
  + **OBS:** Filtra os dados onde a data seja menor ou igual a data informada.
* **Parâmetros**
  + Data:  Indica qual a data será levada em consideração para buscar o valor base. Ex:18/07/2024
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V":  Para valores numéricos de ponto flutuante.
    2. "I":   Para valores inteiros.
    3. "D": Para datas.
    4. "S":  Para string.
* **Exemplo:**

* + **VALORBASECORRIGIDO**("18/07/2024","V") - Retorna o valor convertido no formato definido pelo **Tipo**.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

VALORBASECORRIGIDOMESCALCULOATUAL

* **Descrição**:
  + Retorna o valor decimal que representa o **Valor Base Corrigido** do Patrimônio referente ao **período de cálculo atual**.
* **Funcionamento:** 
  + A Fórmula tem o mesmo comportamento da função **VALORBASECORRIGIDO**, usando a data igual ao período de cálculo atual do sistema e o tipo de retorno como decimal.
* **Exemplo:** 
  + VALORBASECORRIGIDOMESCALCULOATUAL() - O resultado será o Valor Base Corrigido referente ao período de cálculo atual convertido para decimal.
VALORBASEDEPREC

* **Descrição**:
  + Retorna o valor de base de depreciação do patrimônio.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornado o valor de base de depreciação do patrimônio.
    - **IPATRIMONIO**- Campo: **VALORBASE.**

* **Parâmetros**
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V":  Para valores numéricos de ponto flutuante.
    2. "I":   Para valores inteiros.
    3. "D": Para datas.
    4. "S":  Para string.

* **Exemplo:**  
  + **VALORBASEDEPREC**("Tipo") - Retorna o valor convertido no formato definido pelo **Tipo**.
VALORDEDUCAO

* **Descrição**:
  + Retorna o valor de dedução (Valor de aquisição - Valor base depreciação).
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornado o valor da dedução com base na subtração dos campos abaixo.
    - **IPATRIMONIO**- Campo: **AQUISICAO**
    - **IPATRIMONIO -** Campo: **VALORBASE**
* **Parâmetros**
  + Tipo (string): Indica o tipo de dado esperado para o retorno. Os possíveis valores são:
    1. "V":  Para valores numéricos de ponto flutuante.
    2. "I":   Para valores inteiros.
    3. "D": Para datas.
    4. "S":  Para string.

* **Exemplo:**  
  + **VALORDEDUCAO**("Tipo") - Retorna o valor convertido no formato definido pelo **Tipo**.
VLB

* **Descrição**:
  + Retorna o valor base corrigido do patrimônio.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a soma do valor base corrigido do patrimônio de acordo com a regra descrita abaixo:
    - Busca o valor primeiro na tabela **ICALCULORAZAO** - Campo: **VALORBASECORRIGIDO**.
    - Se o valor retornado for zero, busca o valor na tabela **ISALDOCALCULOPATRIMONIOMOEDA** - Campo: **VALORBASECORRIGIDO**
    - Se o valor retornado for zero, busca o valor retornado seja zero, busca o valor na tabela **IPATRIMONIOMOEDA**- Campo: **AQUISICAO**
    - **OBS:** Filtra os dados onde a moeda índice seja a moeda corrente, o cenário de cálculo seja o primeiro (código 1) e a data seja menor ou igual a data informada

* **Parâmetros**

  + Data:  Indica qual a data será levada em consideração para busca do valor base. Ex:18/07/2024

* **Exemplo:**  
  + **VLB**("18/07/2024") - Retorna o valor convertido no formato string.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

VLD

* **Descrição**:
  + Retorna o valor base corrigido do patrimônio.
* **Funcionamento:** 
  + Ao utilizar a Fórmula, será retornada a soma do valor base corrigido do patrimônio de acordo com a regra descrita abaixo:
    - Busca o valor primeiro na tabela **ICALCULORAZAO** - Campo: **DEPRECIACAOACUMULADACORRIGIDA**.
    - Se o valor retornado for zero, busca o valor na tabela **ISALDOCALCULOPATRIMONIOMOEDA** - Campo: **DEPRECIACAOACUMULADACORRIGIDA**
    - Se o valor retornado for zero, busca o valor retornado seja zero, busca o valor na tabela **IPATRIMONIOMOEDA** - Campo: **DEPRECIACAOAQUISICAOCORRIGIDA**
    - ****OBS:**** Filtra os dados onde a moeda índice seja a moeda corrente, o cenário de cálculo seja o primeiro (código 1) e a data seja menor ou igual a data informada.
* ****Parâmetros****
  + Data**:** Indica qual a data será levada em consideração para busca do valor base. Ex:18/07/2024

* **Exemplo:**  
  + **VLD**("18/07/2024") - Retorna o valor convertido no formato string.

OBSERVAÇÃO

Caso não consiga executar a função, utilize o formato dd-mm-aa para o parâmetro de data. Por exemplo "18-07-204"

VLQ

* **Descrição**:
  + Retorna o valor de aquisição do patrimônio.
* **Funcionamento:**   
  + - **IPATRIMONIO**- Campo: **AQUISICAO.**

* **Exemplo:**  
  + **VLQ**() - Retorna o valor convertido no formato string.
OBSERVAÇÃO

As funções listadas que trazem dados de tabelas devem ser utilizadas preferencialmente por fórmulas que trabalhem com determinados contextos para o correto funcionamento das mesmas.
