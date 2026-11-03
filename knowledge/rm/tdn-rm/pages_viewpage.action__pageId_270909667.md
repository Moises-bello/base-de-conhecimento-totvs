---
content_hash: 3fa15ca1e1ed89d7673728d4f6cd23932adf7a141b229e673a0f65a14ff7b3b2
fetched_at: '2026-06-29T00:08:25.008317+00:00'
page_id: '270909667'
product: rm
source: tdn-rm
title: RPT00021.1 - Expressão (Geral)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270909667
version: 45
---

# Índice:

---

.\*ndice:

# Expressão (Entendendo as Propriedades)

---

O componente expressão tem várias propriedades, e o entendimento das mesmas é necessário para uma correta configuração do componente.

# Propriedades Presentes na Smart Tag

---

Ao adicionar um componente Expressão, o usuário observará uma pequena seta do lado direito superior do componente. A clicar na seta, uma pequena janela será mostrada com algumas propriedades, essas propriedades são muito importantes para a correta configuração do componente.

Essas propriedades são:

| N° | Nome | Versão | Descrição |
| --- | --- | --- | --- |
| **1** | Expressão | 12.1.x | Define a expressão que será validada e executada pelo "motor" do relatório, afim de apresentar um valor. |
| **2** | Formato | 12.1.x | Formata o valor final gerado pelo componente expressão. |
| **3** | Arredondar Valor | 12.1.15 (ou superiores) | Arredondamento facultativo do valor após a aplicação da formatação. (Valor Padrão: Campo Marcado) |

# Propriedade Expressão

---

Ao clicar no botão [...] do lado direito da caixa de texto, vinculados a propriedade Expressão, uma tela será apresentada:

Nela temos duas funcionalidades:

| N° | Nome | Versão | Descrição |
| --- | --- | --- | --- |
| **1** | Funções | 12.1.x | Dispõe de diversas funções, que varia de Lógicas a Estatísticas, para facilitar a construção de uma expressão. |
| **2** | Parâmetros | 12.1.x | Dispõe de componentes do relatório, campos da base e campos de consultas SQL, para tornar a expressão mais dinâmica. |

# Funcionalidade Funções

---

**As funções disponíveis são:**

falseILógico

* Comandos lógicos;
* Apresentação de resultado conforme condições.

**Funções Disponíveis:**

**operadorcondicionalif**

| N° | Nome | Parâmetros | Descrição |
| --- | --- | --- | --- |
| **1** | If | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Teste | * Boolean | | **2** | Verdadeiro | * DateTime * Decimal * Enum * Integer * Object * String | | **3** | Falso | * DateTime * Decimal * Enum * Integer * Object * String | | Promove resultado condicional, ou seja, pode ser apresentado um resultado definido como verdadeiro, ou pode ser apresentado um resultado definido como falso.  **Assinaturas Possíveis:**   * **DateTime If(Boolean** Teste, **DateTime** Verdadeiro, **DateTime** Falso**)** * **Decimal If(Boolean** Teste, **Decimal** Verdadeiro, **Decimal** Falso**)** * **Enum If(Boolean** Teste, **Enum** Verdadeiro, **Enum** Falso**)** * **Integer If(Boolean** Teste, **Integer** Verdadeiro, **Integer** Falso**)** * **Object If(Boolean** Teste, **Object** Verdadeiro, **Object** Falso**)** * **String If(Boolean** Teste, **String** Verdadeiro, **String** Falso**)** |

Conversão

* Comandos de conversão;
* Realiza a conversão de tipos;
* Necessário para o bom funcionamento caso se utilize como parâmetro de outras funções.

**Funções Disponíveis:**

| N° | Nome | Parâmetros | Descrição |
| --- | --- | --- | --- |
| **1** | Boolean | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Boolean * DateTime * Decimal * Enum * Integer * Object * String | | Converte um objeto em um valor lógico.  **Assinaturas Possíveis:**   * **Boolean Boolean(Boolean** Valor**)** * **Boolean Boolean(DateTime** Valor**)** * **Boolean Boolean(Decimal** Valor**)** * **Boolean Boolean(Enum** Valor**)** * **Boolean Boolean(Integer** Valor**)** * **Boolean Boolean(Object** Valor**)** * **Boolean Boolean(String** Valor**)** |
| **2** | DateTime | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Boolean * DateTime * Decimal * Enum * Integer * Object * String | | Converte um objeto em um valor Data/Hora.  **Assinaturas Possíveis:**   * **DateTime DateTime(Boolean** Valor**)** * **DateTime DateTime(DateTime** Valor**)** * **DateTime DateTime(Decimal** Valor**)** * **DateTime DateTime(Enum** Valor**)** * **DateTime DateTime(Integer** Valor**)** * **DateTime DateTime(Object** Valor**)** * **DateTime DateTime(String** Valor**)** |
| **3** | Decimal | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Boolean * DateTime * Decimal * Enum * Integer * Object * String | | Converte um objeto em um valor numérico decimal (fracionário ou não).  **Assinaturas Possíveis:**   * **Decimal Decimal(Boolean** Valor**)** * **Decimal Decimal(DateTime** Valor**)** * **Decimal Decimal(Decimal** Valor**)** * **Decimal Decimal(Enum** Valor**)** * **Decimal Decimal(Integer** Valor**)** * **Decimal Decimal(Object** Valor**)** * **Decimal Decimal(String** Valor**)** |
| **4** | Enum | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Boolean * DateTime * Decimal * Enum * Integer * Object * String | | Converte um objeto em um valor Enumerado .  **Assinaturas Possíveis:**   * **Enum Enum(Boolean** Valor**)** * **Enum Enum(DateTime** Valor**)** * **Enum Enum(Decimal** Valor**)** * **Enum Enum(Enum** Valor**)** * **Enum Enum(Integer** Valor**)** * **Enum Enum(Object** Valor**)** * **Enum Enum(String** Valor**)** |
| **5** | Integer | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Boolean * DateTime * Decimal * Enum * Integer * Object * String | | Converte um objeto em um valor inteiro.  **Assinaturas Possíveis:**   * **Integer Integer(Boolean** Valor**)** * **Integer Integer(DateTime** Valor**)** * **Integer Integer(Decimal** Valor**)** * **Integer Integer(Enum** Valor**)** * **Integer Integer(Integer** Valor**)** * **Integer Integer(Object** Valor**)** * **Integer Integer(String** Valor**)** |
| **6** | Object | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Boolean * DateTime * Decimal * Enum * Integer * Object * String | | Converte qualquer outro tipo em um objeto.  **Assinaturas Possíveis:**   * **Object Object(Boolean** Valor**)** * **Object Object(DateTime** Valor**)** * **Object Object(Decimal** Valor**)** * **Object Object(Enum** Valor**)** * **Object Object(Integer** Valor**)** * **Object Object(Object** Valor**)** * **Object Object(String** Valor**)** |
| **7** | String | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Boolean * DateTime * Decimal * Enum * Integer * Object * String | | Converte um objeto em um valor alfanumérico .  **Assinaturas Possíveis:**   * **String String(Boolean** Valor**)** * **String String(DateTime** Valor**)** * **String String(Decimal** Valor**)** * **String String(Enum** Valor**)** * **String String(Integer** Valor**)** * **String String(Object** Valor**)** * **String String(String** Valor**)** |

Matemática

* Comandos matemáticos;
* Permite arredondamentos, truncamentos, calculo com ângulos, etc...

**Funções Disponíveis:**

| Nº | Nome | Parâmetro | Descrição |
| --- | --- | --- | --- |
| **1** | Trunc | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna o numero informado truncado, ou seja, retorna a parte inteira de um numero, a parte fracionária é descartada.  **Assinaturas Possíveis:**   * **Integer Trunc(Decimal** Valor**)** |
| **2** | Round | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna o valor informado arredondado.  **Assinaturas Possíveis:**   * **Integer Round(Decimal** Valor**)** |
| **3** | ArcTan | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Tangente | * Decimal | | Retorna o valor do ângulo para o valor da tangente informado.  **Assinaturas Possíveis:**   * **Decimal ArcTan(Decimal** Tangente**)** |
| **4** | Cos | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Ângulo | * Decimal | | Retorna o cosseno do ângulo informado.  **Assinaturas Possíveis:**   * **Decimal Cos(Decimal** Ângulo**)** |
| **5** | Exp | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Potência | * Decimal | | Retorna o valor de e elevado a potência informada.  **Assinaturas Possíveis:**   * **Decimal Exp(Decimal** Potência**)** |
| **6** | Frac | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna a parte fracionária de um numero informado.  **Assinaturas Possíveis:**   * **Decimal Frac(Decimal** Valor**)** |
| **7** | Int | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna a parte inteira de um numero informado.  **Assinaturas Possíveis:**   * **Decimal Int(Decimal** Valor**)** |
| **8** | Log | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna o logaritmo do número informado.  **Assinaturas Possíveis:**   * **Decimal Log(Decimal** Valor**)** |
| **9** | Sin | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Ângulo | * Decimal | | Retorna o seno do ângulo informado.  **Assinaturas Possíveis:**   * **Decimal Sin(Decimal** Ângulo**)** |
| **10** | Sqr | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna o número informado elevado ao quadrado.  **Assinaturas Possíveis:**   * **Decimal Sqr(Decimal** Valor**)** |
| **11** | Sqrt | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna a raiz quadrada do numero informado  **Assinaturas Possíveis:**   * **Decimal Sqrt(Decimal** Valor**)** |
| **12** | Abs | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal | | Retorna o valor absoluto do número informado.  **Assinaturas Possíveis:**   * **Decimal Abs(Decimal** Valor**)** |
| **13** | Power | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | 1 | Valor | * Decimal | | 2 | Potência | * Decimal | | Retorna um valor elevado a potência informada.  **Assinaturas Possíveis:**   * **Decimal Power(Decimal** Valor, **Decimal** Potência**)** |
| **14** | Random | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Máximo | * Integer | | Retorna um valor aleatório.  **Assinaturas Possíveis:**   * **Decimal Random()** * **Decimal Random(****Integer** Máximo**)** |

Texto

* Comandos de Texto;
* Permite transformar os caracteres de uma cadeia de caracteres em maiúsculo, minusculo;
* Permite remover os espaços em branco tanto na frente quanto atrás da cadeia de caracteres;
* Permite remover caracteres da cadeia de caracteres, etc...

**Funções Disponíveis:**

| N° | Nome | Parâmetros | Descrição |
| --- | --- | --- | --- |
| **1** | Upper | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | Transforma o texto informado em maiúsculo.  **Assinaturas Possíveis:**   * **String Upper(String** Texto**)** |
| **2** | Lower | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | Transforma o texto informado em minusculo.  **Assinaturas Possíveis:**   * **String Lower(String** Texto**)** |
| **3** | Length | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | Retorna o tamanho do texto informado.  **Assinaturas Possíveis:**   * **Integer Length(String** Texto**)** |
| **4** | Trim | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | Retira os espaços em branco do inicio e fim do texto informado.  **Assinaturas Possíveis:**   * **String Trim(String** Texto**)** |
| **5** | TrimEnd | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | Retira os espaços em branco do fim do texto informado.  **Assinaturas Possíveis:**   * **String TrimEnd(String** Texto**)** |
| **6** | TrimStart | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | Retira os espaços em branco do inicio do texto informado.  **Assinaturas Possíveis:**   * **String TrimStart(String** Texto**)** |
| **7** | IndexOf | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto1 | * String | | **2** | Texto2 | * String | | **3** | Posição | * Integer | | **4** | Inicio | * Integer | | **5** | Fim | * Integer | | Retorna a primeira posição do texto 2 dentro do texto 1.  **Assinaturas Possíveis:**   * **Integer IndexOf(String** Texto1, **String** Texto2**)** * **Integer IndexOf(String** Texto1, **String** Texto2, **Integer** Posição**)** * **Integer IndexOf(String** Texto1, **String** Texto2, **Integer** Inicio, **Integer** Fim**)** * **Integer IndexOf(String** Texto1, **String** Texto2, **Integer** Posição**)** * **Integer IndexOf(String** Texto1, **String** Texto2, **Integer** Inicio, **Integer** Fim**)** |
| **8** | LastIndexOf | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto1 | * String | | **2** | Texto2 | * String | | Retorna a ultima posição do texto 2 dentro do texto 1.  **Assinaturas Possíveis:**   * **Integer LastIndexOf(String** Texto1, **String** Texto2**)** |
| **9** | PadLeft | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | **2** | Tamanho | * Integer | | **3** | Caractere | * String | | Alinha o texto informado a esquerda de acordo com o tamanho informado.  **Assinaturas Possíveis:**   * **String PadLeft(String** Texto, **Integer** Tamanho**)** * **String PadLeft(String** Texto, **Integer** Tamanho, **String** Caractere**)** |
| **10** | PadRight | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | **2** | Tamanho | * Integer | | **3** | Caractere | * String | | Alinha o texto informado a direita de acordo com o tamanho informado.  **Assinaturas Possíveis:**   * **String PadRight(String** Texto, **Integer** Tamanho**)** * **String PadRight(String** Texto, **Integer** Tamanho, **String** Caractere**)** |
| **11** | Remove | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | **2** | Posição | * Integer | | **3** | Tamanho | * Integer | | Remove os caracteres do texto informado a partir da posição informada.  **Assinaturas Possíveis:**   * **String Remove**(String**** Texto, **Integer** Posição**)** * **String Remove**(String**** Texto, **Integer** Posição, **Integer**Tamanho**)** |
| **12** | SubString | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | **2** | Posição | * Integer | | **3** | Tamanho | * Integer | | Retorna o sub-texto do texto informado a partir da posição informada.  **Assinaturas Possíveis:**   * **String SubString(String** Texto, **Integer** Posição**)** * **String SubString(String** Texto, **Integer** Posição, **Integer** Tamanho**)** |
| **13** | Replace | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | **2** | Procurar | * String | | **3** | NovoValor | * String | | Substitui a ocorrência de um texto por outro, dentro do texto informado.  **Assinaturas Possíveis:**   * **String Replace(String** Texto, **String** Procurar, **String** NovoValor**)** |
| **14** | ReplaceAll | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | **2** | Procurar | * String | | **3** | NovoValor | * String | | Substitui todas as ocorrências de um texto por outro, dentro do texto informado.  **Assinaturas Possíveis:**   * **String ReplaceAll(String** Texto, **String**Procurar, **String** NovoValor**)** |
| **15** | StringBetween | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Texto | * String | | **2** | Procurar | * String | | **3** | Inicio | * Integer | | **4** | Final | * Integer | | Retorna o texto que está após o valor informado.  **Assinaturas Possíveis:**   * **String StringBetween(String** Texto, **String** Procurar**)** * **String StringBetween(String** Texto, **Integer** Inicio, **Integer** Final**)** |
| **16** | Format | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * Decimal * Integer * DateTime * String | | **2** | Máscara | * String | | Aplica a máscara de formatação em um objeto.  **Assinaturas Possíveis:**   * **String Format(Decimal** Valor**)** * **String Format(Integer** Valor**)** * **String Format(DateTime** Valor**)** * **String Format(String** Valor**)** |
| **17** | Split | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Valor | * String | | **2** | Separador | * String | | **3** | Delimitador | * String | | **4** | Índice | * Integer | | Quebra um texto separado pelo separador informado e retorna um item do índice.  **Assinaturas Possíveis:**   * **String Split(String** Valor, **String** Separador, **Integer** Indice**)** * **String Split(String** Valor, **String** Separador, **String** Delimitador, **Integer** Indice**)** |
| **18** | Join | | N° | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Separador | * String | | **2** | Texto1 | * String | | **3** | Texto2 | * String | | Faz a união de dois valores usando o separador informado.  **Assinaturas Possíveis:**   * **String Join(String** Separador, **String** Texto1, **String** Texto2**)** |

Data/Hora

* Comandos de Data/Hora;
* Retorna data e hora de hoje, retorna dia da semana entre outros...

**Funções Disponíveis:**

| N° | Nome | Parâmetros | Descrição |
| --- | --- | --- | --- |
| **1** | Today | Nenhum | Data do Sistema  **Assinaturas Possíveis:**   * **DateTime Today(****)** |
| **2** | Now | Nenhum | Data/Hora do Sistema  **Assinaturas Possíveis:**   * **DateTime Now(****)** |
| **3** | Day | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna o dia da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer Day(DateTime** Data**)** |
| **4** | Month | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna o mês da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer Month(DateTime** Data**)** |
| **5** | Year | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna o ano da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer Year(DateTime** Data**)** |
| **6** | Hour | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna a hora da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer Hour(DateTime** Data**)** |
| **7** | Minute | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna os minutos da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer Minute(DateTime** Data**)** |
| **8** | Second | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna os segundos da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer Second(DateTime** Data**)** |
| **9** | Millisecond | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna os milissegundos da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer Millisecond(DateTime** Data**)** |
| **10** | DayOfWeek | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna o dia da semana da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer DayOfWeek(DateTime** Data**)** |
| **11** | DayOfYear | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | Retorna o dia do ano da Data/Hora informada.  **Assinaturas Possíveis:**   * **Integer DayOfYear(DateTime** Data**)** |
| **12** | DaysBetween | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | DataInicial | * DateTime | | **2** | DataFinal | * DateTime | | Retorna o número de dias entre as duas datas informadas.  **Assinaturas Possíveis:**   * **Integer DaysBetween(DateTime** DataInicial, **DateTime** DataFinal**)** |
| **13** | MonthsBetween | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | DataInicial | * DateTime | | **2** | DataFinal | * DateTime | | Retorna o número de meses entre as duas datas informadas.  **Assinaturas Possíveis:**   * **Integer DaysBetween(**DateTime**** DataInicial, **DateTime** DataFinal**)** |
| **14** | AddDays | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | **2** | Valor | * Decimal | | Adiciona o número de dias especificados na data informada.  **Assinaturas Possíveis:**   * ****DateTime** AddDays(**DateTime**** Data, **Decimal** Valor**)** |
| **15** | AddMonths | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | **2** | Valor | * Integer | | Adiciona o número de meses especificados na data informada.  **Assinaturas Possíveis:**   * ****DateTime** AddMonths(**DateTime**** Data, **Integer** Valor**)** |
| **16** | AddYears | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | **2** | Valor | * Integer | | Adiciona o número de anos especificados na data informada.  **Assinaturas Possíveis:**   * ****DateTime** AddYears(**DateTime**** Data, **Integer** Valor**)** |
| **17** | AddHours | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | **2** | Valor | * Decimal | | Adiciona o número de horas especificados na data informada.  **Assinaturas Possíveis:**   * ****DateTime** AddHours(**DateTime**** Data, **Decimal** Valor**)** |
| **18** | AddMinutes | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | **2** | Valor | * Decimal | | Adiciona o número de minutos especificados na data informada.  **Assinaturas Possíveis:**   * ****DateTime** AddMinutes(**DateTime**** Data, **Decimal** Valor**)** |
| **19** | AddSeconds | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | **2** | Valor | * Decimal | | Adiciona o número de segundos especificados na data informada.  **Assinaturas Possíveis:**   * ****DateTime** AddSeconds(**DateTime**** Data, **Decimal** Valor**)** |
| **20** | AddMilliseconds | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Data | * DateTime | | **2** | Valor | * Decimal | | Adiciona o número de milisegundos especificados na data informada.  **Assinaturas Possíveis:**   * **DateTime AddMilliseconds(**DateTime**** Data, **Decimal** Valor**)** |

Financeira

* Comandos Financeiros;
* Retorna Períodos de uma Anuidade, bem como valores futuros e juros incidentes sobre a mesma.
* Retorna Taxa de Retorno, VPL e Tempo de Payback de Lançamentos, entre outros...

**Funções Disponíveis:**

| N° | Nome | Parâmetros | Descrição |
| --- | --- | --- | --- |
| **1** | FV | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Taxa | * Decimal | | **2** | Períodos | * Decimal | | **3** | Pagamento | * Decimal | | **4** | ValorPresente | * Decimal | | **5** | ModoDePagamento | * Integer | | Retorna o valor futuro de uma anuidade com pagamentos periódicos fixos.  **Assinaturas Possíveis:**   * **Decimal FV(Decimal** Taxa, **Decimal** Periodos, **Decimal** Pagamento, **Decimal** ValorPresente, **Integer** ModoDePagamento**)** |
| **2** | IPmt | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Taxa | * Decimal | | **2** | Período | * Decimal | | **3** | Períodos | * Decimal | | **4** | ValorPresente | * Decimal | | **5** | ValorFuturo | * Decimal | | **6** | ModoDePagamento | * Integer | | Retorna os juros pagos em uma anuidade com pagamentos periódicos fixos.  **Assinaturas Possíveis:**   * **Decimal IPmt(Decimal** Taxa, **Decimal** Periodo, **Decimal** Periodos, **Decimal** ValorPresente, **Decimal** ValorFuturo, **Integer** ModoDePagamento**)** |
| **3** | NPer | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Taxa | * Decimal | | **2** | Pagamento | * Decimal | | **3** | ValorPresente | * Decimal | | **4** | ValorFuturo | * Decimal | | **5** | ModoDePagamento | * Integer | | Retorna o número de períodos de uma anuidade com pagamentos periódicos fixos.  **Assinaturas Possíveis:**   * **Decimal NPer(Decimal** Taxa, **Decimal** Pagamento, **Decimal** ValorPresente, **Decimal** ValorFuturo, **Integer** ModoDePagamento**)** |
| **4** | Pmt | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Taxa | * Decimal | | **2** | Periodos | * Decimal | | **3** | ValorPresente | * Decimal | | **4** | ValorFuturo | * Decimal | | **5** | ModoDePagamento | * Integer | | Retorna o valor do pagamento por período de uma anuidade com pagamentos periódicos fixos.  **Assinaturas Possíveis:**   * **Decimal Pmt(Decimal** Taxa, **Decimal** Periodos, **Decimal** ValorPresente, **Decimal** ValorFuturo, **Integer** ModoDePagamento**)** |
| **5** | PPmt | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Taxa | * Decimal | | **2** | Periodo | * Decimal | | **3** | Periodos | * Decimal | | **4** | ValorPresente | * Decimal | | **5** | ValorFuturo | * Decimal | | **6** | ModoDePagamento | * Integer | | Retorna o valor do pagamento principal de uma anuidade com pagamentos periódicos fixos.  **Assinaturas Possíveis:**   * **Decimal PPmt(Decimal** Taxa, **Decimal** Periodo, **Decimal** Periodos, **Decimal** ValorPresente, **Decimal** ValorFuturo, **Integer** ModoDePagamento**)** |
| **6** | PV | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Taxa | * Decimal | | **2** | Periodos | * Decimal | | **3** | Pagamento | * Decimal | | **4** | ValorFuturo | * Decimal | | **5** | ModoDePagamento | * Integer | | Retorna o valor presente de uma anuidade com pagamentos periódicos fixos a ser paga no futuro.  **Assinaturas Possíveis:**   * **Decimal PV(Decimal** Taxa, **Decimal** Periodos, **Decimal** Pagamento, **Decimal** ValorFuturo, **Integer** ModoDePagamento**)** |
| **7** | Rate | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Periodos | * Decimal | | **2** | Pagamento | * Decimal | | **3** | ValorPresente | * Decimal | | **4** | ValorFuturo | * Decimal | | **5** | ModoDePagamento | * Integer | | Retorna a taxa de juros de uma anuidade com pagamentos periódicos fixos.  **Assinaturas Possíveis:**   * **Decimal Rate(Decimal** Periodos, **Decimal** Pagamento, **Decimal** ValorPresente, **Decimal** ValorFuturo, **Integer** ModoDePagamento**)** |
| **8** | ConvertRate | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Taxa | * Decimal | | **2** | Origem | * Integer | | **3** | Destino | * Integer | | Retorna a taxa de juros anual convertida para mensal.  **Assinaturas Possíveis:**   * **Decimal ConvertRate(Decimal** Taxa, **Integer** Origem, **Integer** Destino**)** * **Decimal ConvertRate(Decimal** Taxa**)** |
| **9** | IRR | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Tabela | * Object | | **2** | Periodo | * String | | **3** | Valor | * String | | **4** | TaxaValorFuturo | * Decimal | | Retorna a taxa interna de retorno para uma série de lançamentos.  **Assinaturas Possíveis:**   * **Decimal IRR(Object** Tabela, **String** Periodo, **String** Valor, **Decimal**  TaxaValorFuturo**)** |
| **10** | MIRR | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Tabela | * Object | | **2** | Período | * String | | **3** | Valor | * String | | **4** | TaxaDesconto | * Decimal | | **5** | TaxaInvestimento | * Decimal | | Retorna a taxa interna de retorno modificada para uma série de lançamentos.  **Assinaturas Possíveis:**   * **Decimal MIRR(Object** Tabela, **String** Periodo, **String** Valor, **Decimal**  TaxaDesconto, **Decimal** TaxaInvestimento**)** |
| **11** | NPV | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Tabela | * Object | | **2** | Periodo | * String | | **3** | Valor | * String | | **4** | TaxaDesconto | * Decimal | | Retorna o VPL para uma série de lançamentos.  **Assinaturas Possíveis:**   * **Decimal NPV(Object** Tabela, **String** Periodo, **String** Valor, **Decimal**  TaxaDesconto**)** |
| **12** | Payback | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | 1 | Tabela | * Object | | 2 | Periodo | * String | | 3 | Valor | * String | | 4 | TaxaDesconto | * Decimal | | Calcula o tempo de payback para uma série de lançamentos.  **Assinaturas Possíveis:**   * **Decimal Payback(Object** Tabela, **String** Periodo, **String** Valor, **Decimal**  TaxaDesconto**)** |

Ligação de dados

* Comandos Estatísticos;
* A partir de uma lista de objetos os comandos estatísticos retornam a quantidade de itens, a soma, a média, o mínimo e o máximo, entre outras operações com listas.

**Funções Disponíveis:**

| N° | Nome | Parâmetros | Descrição |
| --- | --- | --- | --- |
| **1** | Sum | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Lista | * Object | | **2** | Campo | * String | | Soma os valores de uma lista.  **Assinaturas Possíveis:**   * **Decimal Sum(Object** Lista, **String** Campo**)** |
| **2** | Min | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Lista | * Object | | **2** | Campo | * String | | Retorna o menor valor de um campo da lista.  **Assinaturas Possíveis:**   * **Decimal Min(Object** Lista, **String** Campo**)** |
| **3** | Max | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Lista | * Object | | **2** | Campo | * String | | Retorna o maior valor de um campo da lista.  **Assinaturas Possíveis:**   * **Decimal Max(Object** Lista, **String** Campo**)** |
| **4** | Select | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Lista | * Object | | **2** | Filtro | * String | | **3** | Campos | * String | | **4** | Valores | * String | | Retorna um subconjunto filtrado dos dados de uma lista.  **Assinaturas Possíveis:**   * **Object Select(Object** Lista, **String** Filtro**)** * **Object Select(Object** Lista, **String** Campos, **String** Valores**)** |
| **5** | Lookup | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Lista | * Object | | **2** | ColunaResultado | * String | | **3** | ColunaValor | * String | | **4** | Valor | * Object | | **5** | Linha | * Integer | | Retorna o valor de uma coluna da lista baseado no valor de outra.  **Assinaturas Possíveis:**   * **Object Lookup(Object** Lista, **String** ColunaResultado, **String** ColunaValor, **Object** Valor**)** * **Object Lookup(Object** Lista, **String** ColunaResultado, **Integer** Linha**)** |
| **6** | isEmpty | | Nº | Parâmetro | Tipos possíveis | | --- | --- | --- | | **1** | Lista | * Object | | Retorna se a lista está vazia.  **Assinaturas Possíveis:**   * **Boolean isEmpty(Object** Lista**)** |

Os tipos de parâmetros possíveis não devem ser colocados entre os parênteses. Informe apenas o valor desejado conforme o exemplo:

---

# Funcionalidade Parâmetros

Os parâmetros disponíveis são:

| N° | Nome | Descrição | Imagem |
| --- | --- | --- | --- |
| **1** | Base | Os parâmetros **Base (Campos da Base)**, poderão ser:   * Campos da base (Separados pelo nome da Tabela do banco) * Campos de consultas SQL (Separados pelo nome da consulta SQL) |  |
| **2** | Relatório | Os parâmetros **Relatório (Campos do Relatório)**, poderão ser:   * Os variados controles disponíveis na caixa de ferramentas do Relatório. * Parâmetros do Relatório |  |

# Propriedades Formato e Arredondar Valor

---

* Para melhor compreender a propriedade Formato, veja [Formatação (Passo a Passo)](http://tdn.totvs.com/x/NNaFDg).
* Para melhor compreender a propriedade Arredondar Valor, veja [Propriedade Arredondar Valor](http://tdn.totvs.com/x/XMElE).

# Como Utilizar a Expressão em um Relatório.

---

**PASSO 1** - Verifique se o **detalhe,** onde a **expressão será adicionada,** contém um **membro de dados.**

OBSERVACAO

O **membro de dados** pode ser tanto uma **tabela do banco** como uma **consulta SQL**.

Se uma expressão é adicionada em um detalhe cujo **membro de dados** não foi definido, o **valor** da expressão poderá aparecer **zerado**.

**PASSO 2** - Arraste o componente expressão para dentro do relatório:

**PASSO 3** - Preencha as propriedades da Expressão:

**PASSO 3 - A)** Escreve a expressão utilizando toda a funcionalidade explicada acima. **(OBRIGATORIO)**

**PASSO 3 - B)** Escolha a formatação para o resultado da expressão. **(FACULTATIVO)**

**PASSO 3 - C)** Escolha se quer que o resultado seja arredondado ou não. **(FACULTATIVO)**

OBSERVACAO

Caso queira configurar mais propriedades do **componente Expressão** aperte **F4** para que o menu **Grade de** **Propriedades** seja apresentado.

# Formatação de Dados - XLSX

---

É possível formatar os dados de uma expressão para a exportação de relatórios nos formatos **"XSLX" e "XLS",** utilizando o parâmetro "**XLSX Formato String"** no RM Reports:

**Exemplos:**

Abaixo está demonstrado um exemplo de formatação com unidades de milhar e decimais, utilizando a máscara **0,000.00**:

* **Quando o campo** **"XLSX Formato String" NÃO é preenchido:**

Ao realizar a geração de um relatório, onde contem uma expressão, perceba que o relatório gerado apresenta a unidade de milhar

* Quando realizado a exportação do relatório para um arquivo **"XSLX" e "XLS",** perceba que o campo perde a formatação ao abrir

* **Quando o campo** **"XSLX" e "XLS" é preenchido CORRETAMENTE:**
  + Na grade de propriedades da expressão, Aba "Dados", perceba que existe um campo com o nome "**XLSX Formato String**". Para impedir que a formatação da expressão não seja perdida ao exportar para **XLSX/XLS**, iremos adicionar a máscara citada no campo:

* Agora, ao gerar o relatório e exportar para para um arquivo **"XSLX" e "XLS",** perceba que o formato não foi perdido, é o mesmo de quando o relatório foi gerado.

# Considerações Importantes acerca da Formatação de Dados - XLSX

A formatação de dados segue o padrão utilizado nativamente pelo Microsoft Excel. Dessa forma, para alcançar o resultado desejado, deve se atentar à máscara tal qual o Excel utiliza.

Decimais e Milhares

É importante frisar que a ferramenta de exportação para **XLSX/XLS** determina que a **vírgula/comma** ( , ) deve ser utilizada para separar unidades de milhar e o **ponto/period** ( . ) deve ser utilizado para separar unidades decimais, o que pode ocasionar resultados indesejados caso não seja seguido a risca:

**Dado (Deve seguir o formato padrão, com vírgula para separar decimais):**

**Formatação do campo (Seguindo as determinações corretas):**

**Resultado:**

Abaixo estão as principais máscaras, no padrão do Excel. Para mais informações, consulte a documentação do Microsoft Excel: [Criar um formato de número personalizado](https://support.microsoft.com/pt-br/office/criar-um-formato-de-n%C3%BAmero-personalizado-78f2a361-936b-4c03-8772-09fab54be7f4)

* 0
* 0.00
* 0,000.00
* #,##0
* #,##0.00
* 0%
* 0.00%
* 0.00E+00
* ##0.0E+0
* # ?/?
* # ??/??
* m/d/yyyy
* d-mmm-yy
* d-mmm
* mmm-yy
* h:mm AM/PM
* h:mm:ss AM/PM
* h:mm
* h:mm:ss
* m/d/yyyy h:mm
* mm:ss
* mm:ss.0

# Exceções Mais Comuns

---

Algumas exceções são bastante comuns de ocorrer, quando se executa um relatório contendo expressões, são elas:

| N° | Nome | Descrição | Solução |
| --- | --- | --- | --- |
| **1** | Operador Multiplicação | O operador **Mult** é incompatível com o tipo **String**. | A solução é simples:   * Basta envolver o campo com a função Decimal();   **Exemplo:**   * **DE:** Relatório.Text1 * **PARA:** Decimal(Relatório.Text1)   Caso haja a possibilidade do campo ser **nulo** ou **branco**, utilizar o para **retornar um valor numérico.**  **Exemplo:**   * **DE:** Decimal(Relatório.Text1) * **PARA:** Decimal(If(Relatório.Text1 = '', '0', Relatório.Text)) |
| **2** | Operador Divisão | O operador **Div** é incompatível com o tipo **String**. |
| **3** | Operador Soma | O operador **Plus** é incompatível com o tipo **String**. |
| **4** | Operador Subtração | O operador **Minus** é incompatível com o tipo **String**. |
| ... | | | |

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Expressão (Geral)

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
