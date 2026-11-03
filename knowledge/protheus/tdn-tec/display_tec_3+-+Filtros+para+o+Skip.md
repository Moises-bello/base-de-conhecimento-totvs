---
content_hash: e7e5dd15cdb002d3ffc16c44e9f4baf2173aa6ecf9a78a51f0ecaa964086db42
fetched_at: '2026-07-02T19:24:29.423201+00:00'
page_id: '868234163'
product: protheus
source: tdn-tec
title: 3 - Filtros para o Skip
type: documentation
url: https://tdn.totvs.com/display/tec/3+-+Filtros+para+o+Skip
version: 7
---

Utilizando filtros para o Skip

O recurso de salto possui a possibilidade de informar algumas circunstâncias que o teste deve ser "pulado", seguem:

* Sistema Operacional;
* Versão tlppCore;
* Versão AppServer;
* Nome AppServer;
* Banco de Dados;
* Função customizada.

O recurso funciona tanto para a annotation `@Skip()` como para o comando `SKIPASSERT`.

Vejamos os exemplos:

---

## Sistema Operacional

Pula o teste quando o AppServer for executado em um determinado Sistema Operacional, veja os exemplos:

* **Microsoft Windows**

cppcpp

```

```

* **Linux**

cppcpp

---

## Versão tlppCore

Pula o teste quando o AppServer for executado utilizando determinada versão do tlppCore, veja os exemplos:

* **Somente a versão 01.02.10**

cppcpp

```

```

* **Todas as versões abaixo de 01.02.12**

cppcpp

```

```

* **Todas as versões acima e igual de 01.02.12**

cpp= 01.02.12" )]]>cpp= 01.02.12"]]>

---

## Versão AppServer

Pula o teste quando o AppServer for executado determinada versão do binário, veja os exemplos:

* **Somente a versão 19.3.1.5**

cppcpp

```

```

* **Todas as versões abaixo de 19.3.1.7**

cppcpp

```

```

* **Todas as versões acima e igual de 19.3.1.7**

cpp= 19.3.1.7" )]]>cpp= 19.3.1.7"]]>

---

## Nome AppServer

Pula o teste quando o AppServer for executado determinado nome do binário, veja os exemplos:

* **Somente AppServer LOBO-GUARA**

cppcpp

```

```

* **Somente AppServer HARPIA**

cppcpp

```

```

---

## Banco de Dados

Pula o teste quando houver uma conexão ativa com determinado Banco de Dados.

Disponível somente a partir da versão 01.04.10

**Exemplo com Microsoft SQL Server**

cppcpp

```

```

---

## Função customizada

Pula o teste conforme retorno de uma função customizada do usuário / desenvolvedor.

Disponível somente a partir da versão 01.04.10

**Exemplo:**

cppcpp

```
Implementação função:
```

A função a ser implementada pode ser em AdvPL ou TLPP, User Function ou Function, que o **PROBAT** será capaz de executá-la.

Ela receberá alguns dados como parâmetros, portanto mesmo que não for usá-los é importante seguir a assinatura conforme exemplo:

cpptrue

O retorno da função determinará se o teste será ou não pulado, sendo:

* True (.T.) = Pula;
* False (.F.) = Não Pula.

---

## IMPORTANTE

É possível juntar mais de uma opção no mesmo SKIP.

Exemplos:

cppcpp

* Pode juntar as 6 (seis) opções de filtro.
* Toda vez que tiver mais de uma opção, o operador utilizado é o "AND", ou seja, todas as opções precisam ser válidas para entrar no filtro, caso contrário o teste não será "pulado".
