---
content_hash: 4dab83660ff53759e16c46890c2185f00c9aa16ca360eadb97b8e2b6e2b3a4ac
fetched_at: '2026-06-29T00:08:25.103375+00:00'
page_id: '270912662'
product: rm
source: tdn-rm
title: RPT00013.1.1 - TO_DATE (Oracle)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270912662
version: 38
---

# Índice:

---

.\*ndice:

# Introdução

---

Na versão **11.80**, o provedor de dados é o **Microsoft OLE DB Provider for Oracle**, disponibilizado pela própria **Microsoft,** enquanto que na versão **12**

o provedor de dados é o **Devart ADO .Net Provider**, disponibilizado pela empresa **Devart**.

Mais Informações

Para saber mais sobre:

* **Microsoft** veja [Microsoft WebPage](https://www.microsoft.com/pt-br/) **(PT-br)**
* **Microsoft and Oracle Technologies** veja [Microsoft and Oracle Technologies WebPage](http://www.oracle.com/us/technologies/microsoft/overview/index.html) **(EN-en)**
* **Microsoft OLE DB Provider for Oracle** veja [Microsoft OLE DB Provider for Oracle WebPage](https://msdn.microsoft.com/pt-br/library/office/jj249674.aspx) **(PT-br)**
* **Devart** [Devart WebPage](http://www.devart.com/) veja **(En-en)**
* **Devart ADO .Net Provider** veja [Devart ADO .Net Provider WebPage](http://tdn.totvs.com/www.devart.com/dotconnect) **(EN-en)**
* **Oracle Database** veja [Oracle Database](https://www.oracle.com/br/database/index.html) **(PT-br)**

# Função TO\_DATE()

---

falseSintaxe

```
TO_DATE( string1 [, format_mask] [, nls_language] )
```

**Descrição dos Parâmetros:**

| Nº | Nome | Descrição | Obrigatoriedade | Outras Informações |
| --- | --- | --- | --- | --- |
| **1** | string1 | Cadeia de caracteres que será convertida em uma data válida. |  |  |
| **2** | format\_mask | Máscara que será utilizada para a correta formatação da data.  !Importante! O formato (segundo parâmetro) sempre deve corresponder ao formato da string (primeiro parâmetro), assim o interpretador vai identificar qual formato esta entrando para poder converter a string em data. |  |  |
| **3** | nls\_language | Linguagem utilizada na conversão da cadeia de caracteres em uma data válida |  |  |

**Alguns dos formatos disponíveis (format\_mask):**

| N° | Nome | Descrição |
| --- | --- | --- |
| **1** | YEAR | Ano, soletrado |
| **2** | YYYY | Ano (4 dígitos) |
| **3** | YYY YY Y | Últimos 3, 2, ou 1 digito(s) do ano. |
| **4** | IYY IY I | Últimos 3, 2, ou 1 digito(s) do ano (Padrão ISO). |
| **5** | IYYY | Ano (4 dígitos baseados no padrão ISO) |
| **6** | RRRR | Recebe um ano (2 dígitos) e retorna um ano (4 dígitos) Um valor entre 0-49 irá retornar um ano (20xx). Um valor entre 50-99 irá retornar um ano (19xx). |
| **7** | Q | 1/4 de um ano (1, 2, 3, 4; JAN-MAR = 1). |
| **8** | MM | Mês (01-12; JAN = 01). |
| **9** | MON | Nome abreviado do mês. |
| **10** | MONTH | Nome do mês preenchido com espaços em branco para completar 9 caracteres. |
| **11** | RM | Numeral romano referente ao mês (I-XII; JAN = I). |
| **12** | WW | Semana do ano (1-53) onde a semana 1 começa no primeiro dia do ano e continua ao sétimo dia do ano. |
| **13** | W | Semana do mês (1-5) onde a semana 1 começa no primeiro dia do mês e termina ao sétimo. |
| **14** | IW | Semana do ano (1-52 ou 1-53) baseado no padrão ISO. |
| **15** | D | Dia da semana (1-7). |
| **16** | DAY | Nome do dia. |
| **17** | DD | Dia do mês (1-31). |
| **18** | DDD | Dia do ano (1-366). |
| **19** | DY | Nome abreviado do dia. |
| **20** | J | Dia juliano; O número de dias desde 1 de janeiro de 4712 A.C. |
| **21** | HH | Hora do dia (1-12). |
| **22** | HH12 | Hora do dia (1-12). |
| **23** | HH24 | Hora do dia (0-23). |
| **24** | MI | Minutos (0-59). |
| **25** | SS | Segundos (0-59). |
| **26** | SSSSS | Segundos após a meia-noite (0-86399). |
| **27** | AM, A.M., PM, ou P.M. | Indicador Meridiano. |
| **28** | AD ou A.D | Indicador AD. |
| **29** | BC ou B.C. | Indicador BC. |
| **30** | TZD | Informações do Horário de Verão. |
| **31** | TZH | Hora do fuso horário. |
| **32** | TZM | Minutos do fuso horário. |
| **33** | TZR | Região do fuso horário. |

A função **TO\_DATE()** pode ser usada nas seguintes versões do **Oracle/PLSQL**:

| Nº | Versão |
| --- | --- |
| **1** | Oracle 12c |
| **2** | Oracle 11g |
| **3** | Oracle 10g |
| **4** | Oracle 9i |
| **5** | Oracle 8i |

**Exemplo:**

Vamos observar alguns exemplos do uso da função **TO\_DATE():**

falseExemplo 1

**TO\_DATE(**'09/07/2003', 'dd/mm/yyyy'**) *Resultado:*** valor de data referente à 9 de julho de 2003

falseExemplo 2

**TO\_DATE(**'090703', 'DDMMYY'**) *Resultado:***valor de data referente à 9 de julho de 2003

falseExemplo 3

**TO\_DATE(**'15032002', 'ddmmyyyy'**) *Resultado:***valor de data referente à 15 de março de 2002

# Microsoft Provider x Devart Provider - TO\_DATE()

---

Existem diversas diferenças entre esses dois provedores de dados, mas vamos focar apenas na função **TO\_DATE()**.

|  | **Microsoft OLE DB Provider** | | **Devart ADO .Net Provider** | |
| --- | --- | --- | --- | --- |
|  | Sim/Não | Descrição | Sim/Não | Descrição |
| Conversões Internas |  | O padrão da função **TO\_DATE()** é receber um **campo do tipo string como****parâmetro**, porém com as conversões internas do provedor, mesmo passando um **campo do tipo datetime como****parâmetro**, a função será executada sem levantar exceções. |  | Funciona conforme o **driver nativo do oracle**, ou seja, suporta apenas **um campo do tipo string como parâmetro**, qualquer outro tipo, uma exceção é levantada. |
| Formatações Internas |  | O padrão da função **TO\_DATE()** é receber uma **máscara de formato idêntica** ao valor passado como parâmetro, porém com as formatações internas, mesmo passando uma **máscara diferente** do valor passado como parâmetro, a função será executada sem levantar exceções. |  | Funciona conforme o **driver nativo do oracle**, ou seja, a **máscara do formato** têm que ser **idêntica** ao valor passado como parâmetro. |

# Exceções Mais Comuns

---

| N° | Código Exceção | Descrição | Solução |
| --- | --- | --- | --- |
| **1** | ORA-01830 | **A imagem do formato da data termina antes de converter a string de entrada inteira.**   * **Formato utilizado (2 parâmetro)** não se encaixa de forma precisa ao valor passado no **primeiro parâmetro** da função. Ex: TO\_DATE('02022000', 'dd/mm/yyyy') | **Informar uma máscara de data que condiz com o valor passado como parâmetro.**   * Ex: TO\_DATE('02022000', 'ddmmyyyy') |
| **2** | ORA-01843 | **Valor do mês inválido.**   * Valores negativos (x < 0); * 0 (x = 0); * Maiores que os valores já convencionados para mês (x > 12) | **Informar um mês válido.**   * Valores positivos maiores que 0 e menores ou iguais a 12 (x > 0 e x <= 12) |
| **3** | ORA-01847 | **Valor do dia inválido.**   * Valores negativos (x < 0); * 0 (x = 0); * Maiores que os valores já convencionados para dia: Jan, Mar, Mai, Jul, Ago, Out, Dez (x > 31) Fev (x > 28 ou X > 29 se bissexto),  Abr, Jun, Set, Nov (x > 30) | I**nformar um dia válido.**   * Valores positivos maiores que 0 e menores ou iguais a: Jan, Mar, Mai, Jul, Ago, Out, Dez (x > 0 e x <= 31) Fev (x > 0 e (x <= 28 ou X <= 29 se bissexto)),  Abr, Jun, Set, Nov (x > 0 e x <= 30) |
|  | | | |

# RM, Consultas SQL, Oracle e ORA-01830

---

A Solução geral dada acima, para a exceção de código **ORA-01830,** logicamente serve também para o produto **RM**, porém existem algumas peculiaridades que devem ser tratadas de forma isolada.

A principal peculiaridade que trataremos aqui são os **parâmetros da Consulta SQL.**

Para que a exceção de código **ORA-01830** não aconteça, devemos ter certeza de que os **parâmetros da consulta SQL** utilizados na função **TO\_DATE()****:**

* Não referenciem campos da base, parâmetros do relatório, campos do relatório, que sejam nativamente do tipo **datetime**.

  OBSERVACAO

  Caso referenciem, devem estar acompanhados do sufixo **\_S; é de extrema importância** que esse sufixo esteja presente nesses parâmetros, pois como definimos um **tipo prévio para o parâmetro**, o processo de execução da **Consulta SQL** não tem que detectar o tipo, fazendo com que o retorno da consulta seja mais rápido, além disso, como o tipo do **parâmetro** foi definido como **string (cadeia de caracteres), a exceção não deverá ocorrer,** lembrando que a **máscara do formato** deverá ser **idêntica** ao valor do **parâmetro**.

# Substituindo TO\_DATE para TO\_CHAR

---

Uma ótima alternativa é substituir o **TO\_DATE** para **TO\_CHAR,** quando os campos utilizados na **Consulta SQL** sejam nativamente **datetime**.

O uso do **TO\_CHAR** é mais simples, já que **não é necessário** que **a máscara do formato** seja idêntica ao valor passado como primeiro parâmetro (teoricamente **data** ou **number**) dessa função.

Ex: TO\_CHAR('2003-01-01','dd/MM/yyyy')

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** TO\_DATE (Oracle)

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
