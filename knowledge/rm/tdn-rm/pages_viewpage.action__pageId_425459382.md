---
content_hash: b8dc076275d3c7765dcc6a8474ea40af8219b9b538ca7ceeea97c0da1567f213
fetched_at: '2026-06-29T00:09:35.529749+00:00'
page_id: '425459382'
product: rm
source: tdn-rm
title: Correspondência - Arredondamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459382
version: 4
---

**Correspondência - Arredondamento**

---

A operação Arredondamento recebe um valor como entrada que é convertido para um decimal (Double) e então são aplicadas as operações definidas no parâmetro de "Tipo de Arredondamento".

Os parâmetros para configurar a operação são:

*Alimentação*

* **Entrada:** Ponto de entrada da operação ou campo.

*Identificação*

* **Nome:** Nome da operação criada.
* **Nome:** Campo somente leitura, tem como valor o tipo da operação.

*Parâmetros*

* **Tipo:** Qual arredondamento. Este parâmetro pode ter como valor:
* **Arredondar:** Arredonda um valor para o inteiro mais próximo. No caso do número 5, arredonda para o número par mais próximo. Exemplos:

Entrada: 0.6  
 Tipo: Arredondar  
 *O resultado será igual a 1.*  
 Entrada: 10.5  
 Tipo: Arredondar  
 *O resultado será igual a 10.*

* + **ParaCima:** Arredonda o número decimal para o inteiro mais alto. Exemplo:

Entrada: 10.25  
 Tipo: ParaCima  
 *O resultado será igual a 11.*

* + **ParaBaixo:** Arredonda o número decimal para o inteiro mais baixo. Exemplo:

Entrada: 1.9  
 Tipo: ParaBaixo  
 *O resultado será igual a 1.*

* + **TruncarDecimais:** Remove a parte decimal do número. Exemplo:

Entrada: 10.25  
 Tipo: TruncarDecimais  
 *O resultado será igual a 10.*

---

---

**Recursos Adicionais**

Acesse o boletim técnico abaixo para ver um exemplo desta operação:

[Conceito utilizando Operação Arredondamento](http://totvsconnect.blogspot.com/2011/05/como-fazer-conceito-utilizando-operacao)
