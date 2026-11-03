---
content_hash: 602f9f5d3641b1679efdba4ee0fea99c715d51fd9cc0d25f9097f378bcaa7063
fetched_at: '2026-06-29T00:09:35.949035+00:00'
page_id: '425459448'
product: rm
source: tdn-rm
title: Correspondência - Auto-Incremento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459448
version: 2
---

**Correspondência - Auto-Incremento**

---

A operação Auto Incremento retorna o valor de incremento do campo. Esses campos são buscados em uma tabela que contém as informações sobre os valores de incremento de cada um deles.  
 Os parâmetros para configurar a operação são:

**Identificação**

* **Nome:** Campo somente leitura, tem como valor o tipo da operação.
* **Nome:** Nome da operação.

**Parâmetros**

* **Código do sistema:** Informe de qual sistema será buscada a informação. Sendo que deve ser informado a letra do sistema.
* **Coluna:** Informe qual o campo será utilizado para realizar o auto incremento.
* **Driver Name:** Informe se o driver é Sql ou Oracle.
* **Nome do Auto Incremento:** Informe a coligada**.**

**Exemplo de operação Auto Incremento:**

Código do Sistema: G  
 Coluna: IDCONCEITO  
 Driver Name: SqlServer  
 Nome do Auto Incremento: 1  
 *observação: o valor que consta no campo é 0.*  
    
 O resultado é igual a 1 (Valor que estava no campo, somado +1)
