---
content_hash: 15ed862cd68aa9a1bec93322b5282e9c43c483bde049326b559ee9f7d13c2dc8
fetched_at: '2026-06-29T00:10:07.846357+00:00'
page_id: '452719451'
product: rm
source: tdn-rm
title: Fórmulas / Funções - C
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719451
version: 2
---

**Fórmulas / Funções - C**

* **Função CHAPA:** Retorna o número da chapa do funcionário.

**Sintaxe:** CHAPA

**Tipo de Retorno:** Valor

* **Função CHAPAIMP:** Retorna o número da chapa de importação de importação do funcionário.

**Sintaxe:** CHAPAIMP

**Tipo de Retorno:** Valor

**Exemplo:** Esta função será utilizada apenas no momento da importação das batidas do funcionário pelo módulo Movimento | Importação de Batidas para a fórmula de formatação de chapa. Suponha que as chapas dos funcionários tenham o seguinte padrão: XXXXX-XX Suponha, agora, que os crachás dos funcionários foram confeccionados desconsiderando o hífen: XXXXXXX Utilizando a fórmula de formatação, é possível transformar a seqüência XXXXXXX em XXXXX-XX A seguinte fórmula efetua a formatação: CONCAT (CONCAT (SUBSTR (CHAPAIMP, 1, 5), ''), SUBSTR (CHAPAIMP, 6,2)). Ao importar o arquivo de batidas, o Sistema transforma as chapas, reconhecendo o funcionário correspondente.

* **Função CHR:** Retorna um caracter a partir de um código ASCII.

**Sintaxe:** CHR(VALOR) **Tipo de Retorno:** String

* **Função COMPLEM:** Retorna o conteúdo de um campo da tabela de campos complementares.

**Sintaxe:** COMPLEM ( DA TABELA', DE VER O RETORNO )

**Tipo de Retorno:** Indefinido

**Exemplos:** Funcionário X 1) Quando o tipo de retorno for S ( string ): COMPLEM ('SANGUE','S') Retorna o valor cadastrado no Campo Complementar 'do funcionário. Resultado = A+. 2) Quando o tipo de retorno for D ( data ): COMPLEM (',') Retorna o valor cadastrado no Campo Complementar 'do funcionário. Resultado = 15/06/1999 3) Quando o tipo de retorno for I ( inteiro ) COMPLEM (',') Retorna o valor cadastrado no Campo Complementar 'do funcionário. Resultado = 41 4) Quando o tipo de retorno for V (valor ) COMPLEM (',') Retorna no valor cadastrado no Campo Complementar 'do funcionário. Resultado = 1,15

**Observação:** O modo de ver o retorno do campo complementar é para que o sistema retorne o campo de acordo com que foi gravado no banco de dados. No exemplo a cima o campo sangue que está cadastrado na tabela de campo complementar, foi gravado no banco de dados como uma String. Quando criamos a fórmula COMPLEM ('SANGUE','S') o tipo de retorno é S pelo fato do campo SANGUE ser do tipo string.

**Dica:** Para montar uma fórmula buscando dados do campo complementar temos que ver no módulo Cadastros| Funcionários | Campos Complementares, como é o tipo do campo complementar ( Alfanumérico, Data, Inteiro ou Real ). Quando o campo for Alfanumérico, o tipo de retorno será S, pois é gravado no banco de dados como uma String. Quando o campo for Data, o tipo de retorno será D, pois é gravado no banco de dados como uma Data. Quando o campo for Inteiro, o tipo de retorno será I, pois é gravado no banco de dados como Inteiro. Quando o campo for Real, o tipo de retorno será V, pois é gravado no banco de dados como um valor.

* **Função CONCAT:** Retorna o cosseno de um valor.

**Sintaxe:** COS ( VALOR )

**Tipo de Retorno:** Valor

* **Função COTAN:** Retorna cotangente de um valor.

**Sintaxe:** COTAN ( VALOR )

**Tipo de Retorno:** Valor

|  |  |
| --- | --- |
|  | Informações Complementares |

[  
Funções Específicas do TOTVS Automação de Ponto|Fórmulas - PTO]
