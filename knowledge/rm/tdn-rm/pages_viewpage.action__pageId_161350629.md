---
content_hash: 8e4d5b58acd1485d1cd73e7b8e903835b019d77742f0be81dbf515fa9ec8a456
fetched_at: '2026-06-29T00:05:56.995507+00:00'
page_id: '161350629'
product: rm
source: tdn-rm
title: COMO FAZER - Geração CAGED Portaria 1.129
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=161350629
version: 16
---

Produto

**RMLabore**

**Processo:** **Geração CAGED de acordo com Portaria 1.129**

Versão: 11.5X ou superior

**1 – Criar o campo complementar para funcionário conforme abaixo:**

Nome da Coluna: CAGED

Descrição: CAGED

Tipo: Alfanumérico

Tipo de Texto: Texto

Tamanho: 3

Clique para visualizar a imagem.

**2– Dentro do sistema, a partir do menu**  **Utilitários -> Consultas SQL (Delphi) ou Ambiente -> Visões de Dados (.Net). Criar as seguintes sentenças de acordo com seu banco de dados (SQL ou Oracle)**

**a. Primeira (SQL)**

Código: CAGED

Título: CAGED

Texto:

###### *SELECT            A.CHAPA*

###### *FROM        PFCOMPL A (NOLOCK), PFUNC B (NOLOCK)*

###### *WHERE*

###### *A.CODCOLIGADA = B.CODCOLIGADA*

###### *AND               A.CHAPA = B.CHAPA*

###### *AND         (YEAR(B.DATAADMISSAO) = YEAR(GETDATE())*

###### *AND               MONTH(B.DATAADMISSAO) = MONTH(GETDATE())*

###### *AND               DAY(B.DATAADMISSAO) =  DAY(GETDATE()))*

###### *AND               A.CAGED = 'SIM'*

***a. Primeira (Oracle)***

Código: CAGED

Título: CAGED

Texto:

###### *SELECT  A.CHAPA*

###### *FROM    PFCOMPL A*

###### *JOIN PFUNC B ON (A.CODCOLIGADA = B.CODCOLIGADA AND A.CHAPA = B.CHAPA)*

###### *WHERE TO\_NUMBER(TO\_CHAR(B.DATAADMISSAO, 'yy')) = TO\_NUMBER(TO\_CHAR(SYSDATE, 'yy'))*

###### *AND   TO\_NUMBER(TO\_CHAR(B.DATAADMISSAO, 'MM')) = TO\_NUMBER(TO\_CHAR(SYSDATE, 'MM'))*

###### *AND   TO\_NUMBER(TO\_CHAR(B.DATAADMISSAO, 'DD')) = TO\_NUMBER(TO\_CHAR(SYSDATE, 'DD'))*

###### *AND   A.CAGED = 'SIM'*

Clique para visualizar a imagem.

**b. Segunda (SQL)**

Código: CAGED2

Título: CAGED2

Texto:

###### *SELECT PFCOMPL.CHAPA FROM PFCOMPL, PFUNC*

###### *WHERE (PFUNC.CHAPA = PFCOMPL.CHAPA*

###### *AND PFUNC.CODCOLIGADA = PFCOMPL.CODCOLIGADA)*

###### *AND ((( CAGED <>'SIM' ) OR CAGED IS NULL)*

###### *OR (PFUNC.CODSITUACAO = 'D'  AND PFCOMPL.CAGED = 'SIM' ))*

***b. Segunda (Oracle)***

Código: CAGED2

Título: CAGED2

Texto:

###### *SELECT  PFCOMPL.CHAPA*

###### *FROM PFCOMPL*

###### *JOIN PFUNC ON (PFUNC.CHAPA = PFCOMPL.CHAPA AND PFUNC.CODCOLIGADA = PFCOMPL.CODCOLIGADA)*

###### *WHERE  ((( CAGED <>'SIM' ) OR CAGED IS NULL)*

###### *OR (PFUNC.CODSITUACAO = 'D'  AND PFCOMPL.CAGED = 'SIM' ))*

Clique para visualizar a imagem.

***3 – Criar os seguintes filtros no Sistema***

**a. Primeiro**

Nome: Caged com Seguro Desemprego

Campo: Chapa

1ª OP: IN

1º Valor: CAGED

Tela Delphi (Clique para visualizar imagem)Tela .Net (Clique para visualizar imagem)

**b. Segundo**

Nome: Caged sem Seguro Desemprego

Campo: Chapa

1ª OP: IN

1º Valor: CAGED2

Tela Delphi (Clique aqui para visualizar imagem)Tela .Net (Clique aqui para visualizar imagem)

**4 – Na admissão do funcionário, na aba campos complementares, deverá ser preenchido com “Sim” apenas funcionários que estavam recebendo seguro desemprego.**

Para os demais funcionário preencher com “Não”.

Funcionários que já estão admitidos na base de dados não há necessidade de preenchimento.

Tela Delphi (Clique para visualizar imagem)Tela .Net (Clique para visualizar imagem)

**5 – Executando o Caged utilizando o filtro “Caged com Seguro Desemprego” será gerado Caged para funcionários admitidos no mês, que recebiam seguro desemprego e que tenha sido admitido na data atual**

Exemplos

**EX1:** Competência do sistema = 09

Admissão do funcionário = 10/09/2014

Campo complementar = sim

Data Atual = 10/09/2014

55
incomplete
 Neste caso funcionário **SERÁ** levado para caged.

**EX2:** Competência do sistema = 09

Admissão do funcionário = 10/09/2014

Campo complementar = sim

Data Atual = 11/09/2014

56
incomplete
 Neste caso funcionário **NÃO SERÁ** levado para caged

**EX3:** Competência do sistema = 09

Admissão do funcionário = 10/09/2014

Campo complementar = não

Data Atual = 10/09/2014

57
incomplete
 Neste caso funcionário **NÃO SERÁ** levado para caged

**6 – Executando Caged utilizando o filtro “Caged sem Seguro Desemprego” será gerado Caged para funcionários admitidos no mês, que não recebiam seguro desemprego e funcionários demitidos no mês.**

Exemplos

**EX1:** Competência do sistema = 09

Admissão do funcionário = 10/09/2014

Campo complementar = não

Data Atual = 10/09/2014

58
incomplete
Neste caso funcionário será levado para caged.

**EX2:** Competência do sistema = 09

Admissão do funcionário = 10/09/2014

Campo complementar = sim

Data Atual = 10/09/2014

59
incomplete
Neste caso funcionário não será levado para caged.

**EX3:** Competência do sistema = 09

Admissão do funcionário = 11/09/2014

Campo complementar = sim

Data Atual = 10/09/2014

60
incomplete
Neste caso funcionário não será levado para caged.

**EX4:** Competência do sistema = 09

Demissão do funcionário = 10/09/2014

Campo complementar = null ‘sem preenchimento’

Data Atual = 10/09/2014

61
incomplete
Neste caso funcionário será levado para caged.

**EX5:** Competência do sistema = 11

Admissão do funcionário = 11/09/2014

Demissão do funcionário = 10/11/2014

Campo complementar = sim

Data Atual = 20/11/2014

62
incomplete
Neste caso funcionário será levado para caged.

**EX6:** Competência do sistema = 11

Admissão do funcionário = 11/09/2014

Demissão do funcionário = 10/11/2014

Campo complementar = não

Data Atual = 20/11/2014

63
incomplete
Neste caso funcionário será levado para caged.
