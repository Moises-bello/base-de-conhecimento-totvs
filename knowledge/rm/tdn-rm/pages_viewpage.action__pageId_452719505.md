---
content_hash: 51ccf47a005bcca062ba6a470b874bfef0dd7847efa394891bb10cb8d2da064b
fetched_at: '2026-06-29T00:10:08.068087+00:00'
page_id: '452719505'
product: rm
source: tdn-rm
title: Fórmulas / Funções - T
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719505
version: 4
---

**Fórmulas / Funções - T**

* **Função TABAAFHTFUN:** Retorna valores da tabela aafhtfun.

**Sintaxe:** TABAAFHTFUN(STRING,DATA) 1 - Atraso, Falta, HTrab, ExtraExecutado, ExtraAutorizado, Adicional ou Base. 2 - Data

**Tipo de Retorno:** Valor

**Exemplo:** TABAAFHTFUN ('HTrab','01/06/2006) Retorna o número de horas trabalhadas no dia 01/06/2006.

* **Função TABABANCOHORFUN:** Retorna valores da tabela abancohorfun.

**Sintaxe:** TABABANCOHORFUN(STRING,DATA) 1 - ExtraFaixa1, ExtraFaixa2, ExtraFaixa3, ExtraFaixa4, ExtraFaixa5, ExtraDesc1, Extradesc2, ExtraFer1, ExtraFer2, ExtraComp1, ExtraComp2, Falta, Atraso ou CalcPorFormula 2 - Data

**Tipo de Retorno:** Valor

**Exemplo:**

TABABANCOHORFUN('ExtraFaixa2','13/06/2006') Retorna o número de horas extras faixa 2 do dia 13/06/2006.

* **Função TABAHORARIO:** Esta variável retorna o conteúdo de um campo da tabela de horário (AHORARIO).

**Sintaxe:** TABHORARIO (DA TABELA ', 'DATA')

**Tipo de Retorno:** Indeterminado

**Exemplo:** TABAHORARIO('CONSFERIADO', '01/09/2007'). Retornará o valor do parâmetro "Não considera feriados no cálculo" do funcionário no dia 01/09/2007. Se o parâmetro estiver marcado irá retornar 1, senão, irá retornar 0.

* **Função TABCARGO:** Esta variável retorna o conteúdo de um campo na tabela de cargo.

**Sintaxe:** TABCARGO ('Código do Cargo','Campo da Tabela de Cargo')

**Tipo de Retorno:** Indefinido

**Exemplo:**

TABCARGO ('01' , 'DESCRICAO') Retorna a descrição que está cadastrada no Cargo "01".

* **Função TABCOLIG:** Esta variável retorna o conteúdo de um campo na tabela coligada.

**Sintaxe:** TABCOLIG ('Campo da Coligada')

**Tipo de Retorno:** Valor

**Exemplo:**

TABCOLIG ('CIDADE') Retorna o nome da cidade cadastrada na Coligada.

* **Função TABEXTRAAUTO:** Esta variável retorna o conteúdo de um campo na tabela de extra autorizado.

**Sintaxe:** TABEXTRAAUTO ('Nome do campo','Tipo de retorno', da informação')

**Tipo de Retorno:** Indefinido

**Exemplo:**

1) TABEXTRAAUTO ('AUTORIZADO' , 'V' , '05/04/2001') Irá retornar o número de horas extras autorizadas ( em minutos ) no dia 05/04/2001.

2) TABEXTRAAUTO ('MOTIVO' , 'S' , '05/04/2001') Irá retornar o motivo da autorização das extras no dia 05/04/2001.

**Observação:** O tipo de retorno varia de acordo com que cada campo é gravado no banco de dados. Segue abaixo os campos da tabela de extra autorizado e o tipo de retorno de cada campo:

Nome do campo      Tipo de retorno

AUTORIZADO                   V (Valor)

CHAPA                              I (Inteiro)

CODCOLIGADA                I (Inteiro)

DATA                                   D (Data)

MOTIVO                            S (String)

* **Função TABFUNC:** Esta variável retorna o conteúdo de um campo na tabela funcionário.

**Sintaxe:** TABFUNC (DO FUNCIONÁRIO', DE RETORNO')

**Tipo de Retorno:** Indeterminado

**Exemplo:**

TABFUNC ( ', ') Retorna o nome do funcionário

* **Função TABFUNCAO:** Esta variável retorna o conteúdo de um campo da tabela função.

**Sintaxe:** TABFUNCAO (DA TABELA ', 'MODO DE RETORNO')

**Tipo de Retorno:** Indeterminado

**Exemplo:**

TABFUNCAO(TABFUNC('CODFUNCAO','S') , 'NUMPONTOS')

Retorna o número de pontos de determinada função cadastrada em Função. Onde a fórmula TABFUNC('CODFUNCAO','S') retorna o código da função do funcionário.

* **Função TABPARFUN:** Esta variável retorna o conteúdo de um campo da tabela de parâmetro do funcionário.

**Sintaxe:** TABPARFUN (DA TABELA ', 'MODO DE RETORNO')

**Tipo de Retorno:** Indeterminado

**Exemplo:**

TABPARFUN ('CODPARCOL' , 'S')

Retorna o código do parâmetro Sindicato RM Chronus do funcionário.

* **Função TAMSTR:** Retorna o tamanho de uma string.

**Sintaxe:** TAMSTR (')

**Tipo de Retorno:** Valor

* **Função TAN:** Retorna a tangente de um número.

**Sintaxe:** TAN (VALOR)

**Tipo de Retorno:** Valor

* **Função TETO:** Arredonda um valor para cima.

**Sintaxe:** TETO (VALOR)

**Tipo de Retorno:** Valor

**Exemplo:**

TETO (751.20) = 752.00

* **Função TIPOATRASO:** Retorna os minutos de atraso efetuado pelo funcionário por chegar atrasado, ou durante o horário de serviço, ou se o funcionário saiu mais cedo.

**Sintaxe:** TIPOATRASO(DATA, DATA, STRING)

**Tipo de Retorno:** Valor

**Exemplo:**

Horário do funcionário 08:00 12:00 14:00 18:00

Batidas do funcionário 16/02/2006 –10:15 12:00 15:00 16:30

Fórmula:

TIPOATRASO('/02/2006', '/02/2006', ') = 135 Referente ao intervalo de 08:00 às 10:15

TIPOATRASO('/02/2006', '/02/2006', ') = 60 Referente ao intervalo de 14:00 às 15:00

TIPOATRASO('/02/2006', '/02/2006', ') = 90 Referente ao intervalo de 16:30 às 18:00

* **Função TIPOEXTRA:** Retorna os minutos de extra efetuado pelo funcionário por trabalhar um tempo maior que sua jornada de trabalho de acordo com o tipo de extra.

**Sintaxe:** TIPOEXTRA(DATA, STRING, STRING)

1ª Sintaxe: Data = dd/mm/aaaa

2ª Sintaxe: Tipo da Extra = O parâmetro deve ser 'E' (Extras normais ou extras em dia de refeição) ou 'R' (Extras em dia de feriado) ou 'D' (Extras em dia de descanso) ou 'C' (Extras em dia compensado).

3ª Sintaxe: Diurna ou Noturna = O tipo dever ser 'D' (Extras executadas no período diurno) ou 'N' (Extras executadas no período de adicional noturno)

**Tipo de Retorno:** Valor

**Exemplo:**

Horário do funcionário 08:00 12:00 14:00 18:00

Batidas do funcionário 22/05/2024 – 08:00 12:00 14:00 20:30

Fórmula:

TIPOEXTRA('22/05/2024', 'E', 'D') = 150 Referente ao intervalo de 18:00 às 20:30

TIPOEXTRA('22/05/2024', 'E', 'N') =  0 Não existe extra normal executado em período noturno na data de 22/05/2024

* **Função TQUEBRA:** Esta variável testa o código de quebra.

**Sintaxe:** TQUEBRA (', DE QUEBRA')

**Tipo de Retorno:** Valor

**Exemplo:**

SE TQUEBRA (', '.01') = VERDADE

ENTAO VERDADE

SENAO FALSO

FIMSE

O sistema irá selecionar apenas os funcionários da seção 01.01

* **Função TRABINIFER:** Esta função verifica se o funcionário trabalhou em um dia de feriado.

**Sintaxe:** TRABINIFER('DATA')

**Tipo de Retorno:** Valor

**Exemplo:**

Se o funcionário iniciar a jornada em um dia de feriado o sistema retorna 1 (verdade) se não iniciar a jornada em dia do feriado o sistema retorna 0 (falso).

Horário do funcionário: 31/12 - 22:00E 23:30S 01/01 - 01:00E 06:00S 22:00E 23:30S 02/02 - 01:00E 06:00S 22:00E 23:30S Feriado: 01/01 de 00:00 às 24:00

Batidas do funcionário 00001: 31/12 - 22:00E 23:30S 01/01 - 01:00E 06:00S 22:00E 23:30S 02/02 - 01:00E 06:00S

Batidas do funcionário 00002: 31/12 - 22:00E 23:30S 01/01 - 01:00E 06:00S

Fórmula: TRABINIFER('01/01/2003')

Resultado da fórmula: Funcionário de chapa 00001 = 1 ( Pois o funcionário iniciou uma jornada no dia do feriado. Batida considerada para o cálculo da fórmula 22:00E do dia 01/01. ) Funcionário de chapa 00002 = 0 ( Pois o funcionário não iniciou jornada no dia do feriado. As batidas do dia 01/01 são referentes a jornada do dia 31/12.)

**Observação:**

Esta fórmula só poderá ser utilizada pelos funcionários que possuem intervalo de refeição cadastrado no horário.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
