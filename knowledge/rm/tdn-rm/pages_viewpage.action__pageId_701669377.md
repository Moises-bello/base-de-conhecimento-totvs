---
content_hash: 4d2c0e502bb176cc7908a02b10d1bdc1c0bd5711ccaa9dfca3ff9efcf75eac5a
fetched_at: '2026-06-29T00:11:22.335967+00:00'
page_id: '701669377'
product: rm
source: tdn-rm
title: Funções de fórmulas (TOTVS Gestão de Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=701669377
version: 48
---

#### Existe no RM a possibilidade de cadastrar **fórmulas** que podem ser utilizadas em diversas ocasiões.

#### As fórmulas facilitam a utilização do sistema **garantindo** maior **agilidade**.

#### Abaixo estão descritas as **funções** de fórmula disponíveis no módulo TOTVS Gestão de estoque, compras e faturamento.

0solidNOVIDADE 12.1.2602 - GRAVARCACHE e LERCACHE

## GRAVARCACHE e LERCACHE

A criação das funções **GRAVARCACHE** e **LERCACHE** tem um objetivo principal: **otimizar a performance do sistema RM**.

Em muitas situações, fórmulas realizam cálculos complexos ou consultas repetidas ao banco de dados (SQL) que consomem muito tempo, processamento e memória. Com o uso destas funções, você pode calcular ou consultar um dado apenas uma vez, "guardar" (gravar) esse resultado na memória temporária do sistema e "resgatar" (ler) esse valor sempre que precisar novamente.

**Vantagens:**

* Redução drástica no número de consultas SQL repetidas.
* Menor consumo de processador e memória.
* Fórmulas e processos muito mais rápidos.

---

### GRAVARCACHE

A função `GRAVARCACHE` tem o objetivo de armazenar um valor na memória para que possa ser acessado posteriormente por outras fórmulas ou em etapas seguintes do mesmo processo.

#### Parâmetros da Função

| **Parâmetro** | **Descrição** |
| --- | --- |
| **chaveCache** | É o "ID" ou o "Nome" exclusivo que você dará ao valor guardado. É através dessa chave que o sistema saberá qual informação buscar depois. *(Veja mais sobre como criar boas chaves na seção de Atenção abaixo)*. |
| **valor** | O dado em si que será armazenado na memória. Pode ser um número (inteiro ou decimal) ou um texto (string). |

---

### LERCACHE

A função `LERCACHE` é utilizada para resgatar o valor que foi previamente guardado na memória pela função `GRAVARCACHE`.

#### Parâmetros da Função

| **Parâmetro** | **Descrição** |
| --- | --- |
| **chaveCache** | O exato "ID" que foi utilizado no momento da gravação. Se a chave não for idêntica à gravada, a função não encontrará o valor e retornará 0. |

---

### ⚠️ ATENÇÃO: A Importância da "Chave do Cache" e Seus Riscos

A definição da **chaveCache** é a parte mais crítica ao usar essas funções. Como o cache é um espaço de memória compartilhado durante a execução, uma chave mal definida pode causar sérios problemas de consistência nos dados.

> **O Risco da Chave Fraca:**
>
> Se você usar uma chave genérica, como `"VALOR_TOTAL"`, e dois processos ou movimentos diferentes executarem a fórmula ao mesmo tempo, o segundo movimento irá sobrescrever o valor do primeiro. Ao tentar ler o cache, o primeiro movimento pegará o valor do segundo, resultando em cálculos completamente errados (misturando valores).

**Como criar uma Chave Forte:**

Uma chave segura deve ser **única** para o contexto que você está trabalhando. Combine identificadores exclusivos do registro para garantir que nenhum outro processo acesse aquele "endereço" de memória por engano.

* **Exemplo para um Movimento:** Junte o Código da Coligada e o ID do Movimento.

  + *Chave Ideal:* `CODCOLIGADA_IDMOV` (Exemplo: `"1_1598"`)
* **Exemplo para um Item de Movimento:** Junte a Coligada, o ID do Movimento e o ID do Item.

  + *Chave Ideal:* `CODCOLIGADA_IDMOV_IDITEM` (Exemplo: `"1_1598_1"`)

---

### 📌 Regras Importantes de Uso

1. **Tempo de Vida (Validade):** O cache é temporário. Os valores gravados permanecem na memória por **exatos 5 minutos**. Após esse período, a informação é apagada automaticamente. Se a fórmula for executada novamente após esse tempo, o valor precisará ser recalculado e gravado de novo.
2. **Responsabilidade:** É de inteira responsabilidade do criador da fórmula garantir a unicidade da chave (tanto na hora de usar o `GRAVARCACHE` quanto o `LERCACHE`) para evitar o cruzamento indevido de dados.

Exemplo:

SE LERCACHE('1-100456-PROCESSADO') <> 1  
    ENTAO  
        GRAVARCACHE('1-100456-PROCESSADO', 1);  
        EXECSQL('CONSULTASQL');  
            SE EXECSQL('RVR.EVC08699') = 1  
                ENTAO  
                    GRAVARCACHE('1-100456-SQLEXECUTADA',1);  
                    GRAVARCACHE('1-100456-VALORORIGINAL', RESULTSQL('RVR.EVC08699','VALORORIGINAL'));  
                    GRAVARCACHE('1-100456-VALORDESCONTO', RESULTSQL('RVR.EVC08699','VALORDESCONTO'));  
            FIMSE  
    FIMSE  
FIMSE;

SE LERCACHE('1-100456-SERV\_MATRICULA') = 'T' OU  
    LERCACHE('1-100456-SERV\_MATRICULA\_ING') = 'T'  
    ENTAO   
        SE TABITM('NUMEROSEQUENCIAL','I') = 1  
            ENTAO LERCACHE('1-100456-VALORORIGINAL') - LERCACHE('1-100456-VALORDESCONTO');  
        SENAO   
            LERCACHE('1-100456-VALORORIGINAL');  
        FIMSE  
    SENAO 0  
FIMSE

---

---

TABMOV

| Função | **TABMOV** |
| --- | --- |
| Descrição | Valor de um campo do movimento |
| Sintaxe | TABMOV('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo do movimento * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABMOV('CODCFO','S' ) |
| Retorno | C00001 |

TABMOVCOMPL

| Função | **TABMOVCOMPL** |
| --- | --- |
| Descrição | Valor de um campo complementar do movimento |
| Sintaxe | TABMOVCOMPL('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABMOVCOMPL('Data aquisição','D' ) |
| Retorno | 03/08/2021 |

TABITMMOVCOMPL

| Função | TABITMMOVCOMPL |
| --- | --- |
| Descrição | Valor de um campo complementar de um item do movimento |
| Sintaxe | TABITMMOVCOMPL('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABITMMOVCOMPL('Data aquisição','D' ) |
| Retorno | 03/08/2021 |

TABITMCNT

| Função | **TABITMCNT** |
| --- | --- |
| Descrição | Valor de um campo do item de contrato que esta vinculado a um movimento. Não retorna campos de itens de contrato que  não possuam vinculo com o movimento. Deve ser utilizado contexto de movimento para utilização da função de fórmula. |
| Sintaxe | TABITMCNT('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABITMCNT('CAMPOLIVRE1','S' ) |
| Retorno | Conteúdo do campo "CAMPOLIVRE1" do item de contrato vinculado ao item de movimento. |

TABTCNT

| Função | **TABTCNT** |
| --- | --- |
| Descrição | Valor de um campo do contrato. |
| Sintaxe | TABTCNT('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABTCNT('CAMPOLIVRE1','S' ) |
| Retorno | Conteúdo do campo "CAMPOLIVRE1" do contrato. |

TABTITMCNT

| Função | **TABTITMCNT** |
| --- | --- |
| Descrição | Valor de um campo do item de contrato. |
| Sintaxe | TABTITMCNT('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABTITMCNT('CAMPOLIVRE1','S' ) |
| Retorno | Conteúdo do campo "CAMPOLIVRE1" do item de contrato. |

TABCNTCOMPL

| Função | TABCNTCOMPL |
| --- | --- |
| Descrição | Valor de um campo complementar do contrato. |
| Sintaxe | * TABCNTCOMPL('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABCNTCOMPL('CAMPOLIVRE1','S' ) |
| Retorno | Conteúdo do campo "CAMPOLIVRE1" do campo complementar do contrato. |

TABITMCNTCOMPL

| Função | TABITMCNTCOMPL |
| --- | --- |
| Descrição | Valor de um campo complementar do item do contrato. |
| Sintaxe | * TABITMCNTCOMPL('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABITMCNTCOMPL('CAMPOLIVRE1','S' ) |
| Retorno | Conteúdo do campo "CAMPOLIVRE1" do campo complementar do item do contrato. |

TABPRDLOC

| Função | **TABPRDLOC** |
| --- | --- |
| Descrição | Valor de um campo de saldos/custos de um ITEM DO MOVIMENTO. Necessita do contexto de um movimento, uma vez que,  precisa de dados do item. |
| Sintaxe | TABPRDLOC('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABPRDLOC('CUSTOUNITARIO','V' ) |
| Retorno | Conteúdo do campo "CUSTOUNITARIO" de um item de movimento. |

TABPRDLOCGERAL

| Função | **TABPRDLOCGERAL** |
| --- | --- |
| Descrição | Valor de um campo de saldos/custos. A diferença para a da TABPRDLOC é que ela deve ser usada em movimentos  (pois precisa de dados do item) , já a TABPRDLOCGERAL pode ser executa de outros lugares, como: Produtos,  Movimentos e Reajuste de Preço) |
| Sintaxe | TABPRDLOCGERAL('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABPRDLOCGERAL('CUSTOUNITARIO','V' ) |
| Retorno | Conteúdo do campo "CUSTOUNITARIO" da tabela TPRDLOC. |

TABPRDMOV

| Função | **TABPRDMOV** |
| --- | --- |
| Descrição | Valor de um campo de produto do primeiro item do movimento. |
| Sintaxe | TABPRDMOV('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABPRDMOV('COMPRIMENTO','V' ) |
| Retorno | Conteúdo do campo "COMPRIMENTO" da tabela TPRODUTO. |

TABITM

| Função | TABITM |
| --- | --- |
| Descrição | Valor de um campo do item do movimento |
| Sintaxe | TABITM('CAMPO','TIPO' ) |
| Parâmetros | * CAMPO → Nome do campo do item do movimento * TIPO → Tipo de retorno   + V = valor   + I = inteiro   + D = data   + S = string |
| Exemplo | TABITM('PRECOUNITARIO','V') |
| Retorno | 100,00 |

Funções destinadas a itens não são compatíveis com fórmulas de movimento. Elas retornam apenas informações do primeiro item e não realizam somatórios ou cálculos considerando todos os itens do movimento

TABITM('RATEIO  ')

A função TABITM('RATEIO  ') correspondente ao valor do rateio para cada valor do movimento que são possíveis de serem rateados:

Para utilizar estas funções, os tipos de movimentos devem ser alterados, habilitando o parâmetro Rateio Valor Financeiro para os valores que se deseja ratear para os itens. Com esta funcionalidade, o cálculo do rateio será executado ao salvar o movimento. Com isto os valores rateados já estarão gravados na TITMMOV, ganhando assim, na performance de relatórios, cálculo do custo médio, contabilização, etc.. Rateios extras de 3 a 10 disponíveis a partir da versão 12.1.2606.

|  |
| --- |
| **Função** |
| TABITM ('RATEIODEDMAT','V') |
| TABITM ('RATEIODEDOUT','V') |
| TABITM 'RATEIODEDSUB','V') |
| TABITM ('RATEIODESC','V') |
| TABITM ('RATEIODESP','V') |
| TABITM ('RATEIOEXTRA1','V') |
| TABITM ('RATEIOEXTRA2','V') |
| TABITM ('RATEIOFRETE','V') |
| TABITM ('RATEIOFRETECTRC','V') |
| TABITM ('RATEIOSEGURO','V') |
| TABITM ('RATEIOEXTRA3','V') |
| TABITM ('RATEIOEXTRA4','V') |
| TABITM ('RATEIOEXTRA5','V') |
| TABITM ('RATEIOEXTRA6','V') |
| TABITM ('RATEIOEXTRA7','V') |
| TABITM ('RATEIOEXTRA8','V') |
| TABITM ('RATEIOEXTRA9','V') |
| TABITM ('RATEIOEXTRA10','V') |

MVB

| Função | **MVB** |
| --- | --- |
| Descrição | Valor bruto do movimento |
| Sintaxe | MVB |
| Parâmetros | * N/A |
| Exemplo | MVB |
| Retorno | 80,00 |

MVL

| Função | **MVL** |
| --- | --- |
| Descrição | Valor líquido do movimento |
| Sintaxe | MVL |
| Parâmetros | * N/A |
| Exemplo | MVL |
| Retorno | 720,00 |

MDZ

| Função | **MDZ** |
| --- | --- |
| Descrição | Valor despesa do movimento |
| Sintaxe | MDZ |
| Parâmetros | * N/A |
| Exemplo | MDZ |
| Retorno | 20,00 |

MZP

| Função | **MZP** |
| --- | --- |
| Descrição | Percentual de despesa do movimento |
| Sintaxe | MZP |
| Parâmetros | * N/A |
| Exemplo | MZP |
| Retorno | 10,00 |

MDT

| Função | **MDT** |
| --- | --- |
| Descrição | Valor do desconto do movimento |
| Sintaxe | MDT |
| Parâmetros | * N/A |
| Exemplo | MDT |
| Retorno | 20,00 |

MEP

| Função | **MEP** |
| --- | --- |
| Descrição | Percentual de desconto do movimento |
| Sintaxe | MEP |
| Parâmetros | * N/A |
| Exemplo | MEP |
| Retorno | 10,00 |

ME1

| Função | **ME1** |
| --- | --- |
| Descrição | Valor extra 1 do movimento |
| Sintaxe | ME1 |
| Parâmetros | * N/A |
| Exemplo | ME1 |
| Retorno | 20,00 |

M1P

| Função | **M1P** |
| --- | --- |
| Descrição | Percentual extra 1 do movimento |
| Sintaxe | M1P |
| Parâmetros | * N/A |
| Exemplo | M1P |
| Retorno | 10,00 |

ME2

| Função | **ME2** |
| --- | --- |
| Descrição | Valor extra 2 do movimento |
| Sintaxe | ME2 |
| Parâmetros | * N/A |
| Exemplo | ME2 |
| Retorno | 20,00 |

M2P

| Função | **M2P** |
| --- | --- |
| Descrição | Percentual extra 2 do movimento |
| Sintaxe | M2P |
| Parâmetros | * N/A |
| Exemplo | M2P |
| Retorno | 10,00 |

ME3

| Função | **ME3** |
| --- | --- |
| Descrição | Valor extra 3 do movimento |
| Sintaxe | ME3 |
| Parâmetros | * N/A |
| Exemplo | ME3 |
| Retorno | 20,00 |

M3P

| Função | **M3P** |
| --- | --- |
| Descrição | Percentual extra 3 do movimento |
| Sintaxe | M3P |
| Parâmetros | * N/A |
| Exemplo | M3P |
| Retorno | 10,00 |

ME4

| Função | **ME4** |
| --- | --- |
| Descrição | Valor extra 4 do movimento |
| Sintaxe | ME4 |
| Parâmetros | * N/A |
| Exemplo | ME4 |
| Retorno | 20,00 |

M4P

| Função | **M4P** |
| --- | --- |
| Descrição | Percentual extra 4 do movimento |
| Sintaxe | M4P |
| Parâmetros | * N/A |
| Exemplo | M4P |
| Retorno | 10,00 |

ME5

| Função | **ME5** |
| --- | --- |
| Descrição | Valor extra 5 do movimento |
| Sintaxe | ME5 |
| Parâmetros | * N/A |
| Exemplo | ME5 |
| Retorno | 20,00 |

M5P

| Função | **M5P** |
| --- | --- |
| Descrição | Percentual extra 5 do movimento |
| Sintaxe | M5P |
| Parâmetros | * N/A |
| Exemplo | M5P |
| Retorno | 10,00 |

ME6

| Função | **ME6** |
| --- | --- |
| Descrição | Valor extra 6 do movimento |
| Sintaxe | ME6 |
| Parâmetros | * N/A |
| Exemplo | ME6 |
| Retorno | 20,00 |

M6P

| Função | **M6P** |
| --- | --- |
| Descrição | Percentual extra 6 do movimento |
| Sintaxe | M6P |
| Parâmetros | * N/A |
| Exemplo | M6P |
| Retorno | 10,00 |

ME7

| Função | **ME7** |
| --- | --- |
| Descrição | Valor extra 7 do movimento |
| Sintaxe | ME7 |
| Parâmetros | * N/A |
| Exemplo | ME7 |
| Retorno | 20,00 |

M7P

| Função | **M7P** |
| --- | --- |
| Descrição | Percentual extra 7 do movimento |
| Sintaxe | M7P |
| Parâmetros | * N/A |
| Exemplo | M7P |
| Retorno | 10,00 |

ME8

| Função | **ME8** |
| --- | --- |
| Descrição | Valor extra 8 do movimento |
| Sintaxe | ME8 |
| Parâmetros | * N/A |
| Exemplo | ME8 |
| Retorno | 20,00 |

M8P

| Função | **M8P** |
| --- | --- |
| Descrição | Percentual extra 8 do movimento |
| Sintaxe | M8P |
| Parâmetros | * N/A |
| Exemplo | M8P |
| Retorno | 10,00 |

ME9

| Função | **ME9** |
| --- | --- |
| Descrição | Valor extra 9 do movimento |
| Sintaxe | ME9 |
| Parâmetros | * N/A |
| Exemplo | ME9 |
| Retorno | 20,00 |

M9P

| Função | **M9P** |
| --- | --- |
| Descrição | Percentual extra 9 do movimento |
| Sintaxe | M9P |
| Parâmetros | * N/A |
| Exemplo | M9P |
| Retorno | 10,00 |

ME10

| Função | **ME10** |
| --- | --- |
| Descrição | Valor extra 10 do movimento |
| Sintaxe | ME10 |
| Parâmetros | * N/A |
| Exemplo | ME10 |
| Retorno | 20,00 |

M10P

| Função | **M10P** |
| --- | --- |
| Descrição | Percentual extra 10 do movimento |
| Sintaxe | M10P |
| Parâmetros | * N/A |
| Exemplo | M10P |
| Retorno | 10,00 |

MSG

| Função | **MSG** |
| --- | --- |
| Descrição | Valor do seguro do movimento |
| Sintaxe | MSG |
| Parâmetros | * N/A |
| Exemplo | MSG |
| Retorno | 20,00 |

MSP

| Função | **MSP** |
| --- | --- |
| Descrição | Percentual seguro do movimento |
| Sintaxe | MSP |
| Parâmetros | * N/A |
| Exemplo | MSP |
| Retorno | 10,00 |

MFR

| Função | **MFR** |
| --- | --- |
| Descrição | Valor do frete do movimento |
| Sintaxe | MFR |
| Parâmetros | * N/A |
| Exemplo | MFR |
| Retorno | 20,00 |

MFP

| Função | **MFP** |
| --- | --- |
| Descrição | Percentual frete do movimento |
| Sintaxe | MFP |
| Parâmetros | * N/A |
| Exemplo | MFP |
| Retorno | 10,00 |

MOU

| Função | **MOU** |
| --- | --- |
| Descrição | Valor outros (Subtotal) do movimento |
| Sintaxe | MOU |
| Parâmetros | * N/A |
| Exemplo | MOU |
| Retorno | 20,00 |

DEM

| Função | **DEM** |
| --- | --- |
| Descrição | Data de emissão do movimento |
| Sintaxe | DEM |
| Parâmetros | * N/A |
| Exemplo | DEM |
| Retorno | 02/01/2022 |

DES

| Função | **DES** |
| --- | --- |
| Descrição | Data de saída do movimento |
| Sintaxe | DEM |
| Parâmetros | * N/A |
| Exemplo | DES |
| Retorno | 10/02/2022 |

DA1

| Função | **DA1** |
| --- | --- |
| Descrição | Data 1 do movimento |
| Sintaxe | DA1 |
| Parâmetros | * N/A |
| Exemplo | DA1 |
| Retorno | 11/04/2022 |

DA2

| Função | **DA2** |
| --- | --- |
| Descrição | Data 2 do movimento |
| Sintaxe | DA2 |
| Parâmetros | * N/A |
| Exemplo | DA2 |
| Retorno | 11/04/2022 |

DOM

| Função | **DOM** |
| --- | --- |
| Descrição | Data do movimento |
| Sintaxe | DOM |
| Parâmetros | * N/A |
| Exemplo | DOM |
| Retorno | 11/04/2022 |

DOC

| Função | **DOC** |
| --- | --- |
| Descrição | Data de cancelamento do movimento |
| Sintaxe | DOC |
| Parâmetros | * N/A |
| Exemplo | DOC |
| Retorno | 11/04/2022 |

KQT

| Função | KQT |
| --- | --- |
| Descrição | Quantidade do item do movimento |
| Retorno | Quantidade |

KPU

| Função | KPU |
| --- | --- |
| Descrição | Preço Unitário do Item do Movimento |
| Retorno | Preço Unitário |

Dicas

* Se na construção de uma fórmula for necessário validar se um campo do tipo data está NULL é usar a função de fórmula global [DATANULA](https://tdn.totvs.com/pages/viewpage.action?pageId=381051703#Fun%C3%A7%C3%B5esGlobais-DATANULA)

**Exemplo**:

SE TABMOVCOMPL('Data aquisição','D' ) = DATANULA

ENTAO 'Data não está preenchida'

SENÃO TABMOVCOMPL('Data aquisição','D' )

FIMSE

* Valores extras e percentuais de 3 a 10 disponíveis a partir da versão 12.1.2606.
560px

**CONTEUDO COMPLEMENTAR**

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
