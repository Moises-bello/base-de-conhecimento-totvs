---
content_hash: 9d24fdb5ca7227d7c1285ef8841f4212bcc32939e8d576d9eed9d7537b2b83b8
fetched_at: '2026-06-29T00:09:35.851619+00:00'
page_id: '425459394'
product: rm
source: tdn-rm
title: Correspondência - Concatenação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459394
version: 3
---

**Correspondência - Concatenação**

---

A operação Concatenação recebe duas entradas e resulta em uma saída com os dados concatenados.

Os parâmetros para configurar a operação são:

*Alimentação*

* **Entrada:** Ponto de entrada da operação ou campo.
* **Entrada Secundária:** Valor a ser concatenado à entrada principal.

*Identificação*

* **Nome:** Nome da operação.
* **Nome:** Campo somente leitura, tem como valor o tipo da operação.

*Parâmetros*

* **Concatenador:** Caracteres que serão incluídos entre as entradas principal e secundária, funcionando como um separador de dados.
* **Tipo de Dados:** Tipo de dados resultante da operação, que pode ser Texto, Inteiro, Decimal, Data.

Se o campo "Tipo de Dados" estiver definido como texto os dados serão concatenados. Mas essa operação também pode executar funções de soma de valores do tipo Inteiro e Decimal.   
 Caso esse campo esteja definido como inteiro as entradas serão convertidas para inteiro e então será realizada a soma dos valores (o mesmo vale para o tipo decimal). Neste caso, o campo Concatenador deve ser deixado em branco ou preenchido com um valor numérico que será acrescentado ao total da soma das duas entradas.

**Exemplo:**

Entrada: 2   
 Entrada Secundária: 3   
 Concatenador: 5   
 Tipo de Dado: Inteiro   
    
 Resultado: a operação irá retornar como resultado o número 10.

---

**Recursos Adicionais**

Acesse o boletim técnico abaixo para ver um exemplo desta operação:

[Conceito utilizando Operação Concatenação](http://totvsconnect.blogspot.com/2011/05/como-fazer-conceito-utilizando-operacao_31)
